# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import dataclasses as dc
import datetime
import functools
import subprocess
import time
import typing as tp
import urllib.parse

from ._proto_namespace import _ProtoNamespace
from ._util import ApiRequestCommunicator

# graphql queries for image tags
# query = '{project(fullPath: "'+self.repo_name+'") { containerRepositories(name: "'+"adaux-pre-commit"+'") { nodes {id} }}}'
# resp = self.graphql_request(query=query)
# res = resp["data"]["project"]["containerRepositories"]["nodes"][0]["id"]
# query = '{containerRepository(id: "'+res+'"){tags{nodes{name}}}}'
# resp = self.graphql_request(query=query)
# print([x["name"] for x in resp["data"]["containerRepository"]["tags"]["nodes"]])


@dc.dataclass
class GitlabSetter(ApiRequestCommunicator):
    ns: _ProtoNamespace
    token: str
    repo_name: str = dc.field(init=False)

    def __post_init__(self) -> None:
        out = subprocess.run(["git", "remote", "-v"], capture_output=True, check=True)
        (line,) = (x.strip() for x in out.stdout.decode().split("\n") if "fetch" in x)
        line = line.rsplit(" ", 1)[0]
        host, repo = line.split("git@")[1].split(":")
        base_url = "https://" + host
        is_name = repo.replace(".git", "")
        should_name = self.ns.auxcon.project.name.replace(".", "/")
        if is_name != should_name:
            RuntimeError(f"names dont match {is_name} != {should_name}")

        self.repo_name = is_name
        self.base_url = base_url
        # self.headers = {"Authorization": f"Bearer {self.token}"}
        self.headers = {"PRIVATE-TOKEN": self.token}
        self._print(
            f"working on project {self.repo_name} and instance {self.base_url}",
            fg="white",
        )

    def _print(self, msg: str, **kwgs: tp.Any) -> None:
        # pylint: disable=protected-access
        self.ns._print(msg, **kwgs)

    @functools.cached_property
    def project_id(self) -> str:
        # old impl
        # query = '{project(fullPath: "' + self.repo_name + '") {id}}'
        # resp = self.graphql_request(query=query)
        # return resp["data"]["project"]["id"].split("/")[-1]  # type: ignore
        return urllib.parse.quote_plus(self.repo_name)

    def sync_settings(self) -> None:
        resp = self.api_request("projects", self.project_id)

        settings = dict(
            ci_config_path="devops/CI/00-main.yml",
            ci_default_git_depth=2,
            container_expiration_policy=dict(
                enabled=True,
                cadence="1d",
                keep_n=1,
                older_than="7d",
                name_regex_keep=None,
                name_regex="aux-.*",
            ),
            default_branch=self.ns.auxcon.gitlab.default_branch,
        )

        for key, val in settings.items():
            added = ""
            outdated = self._check_outdated(val, resp[key])
            if isinstance(val, dict):
                added += "_attributes"
            if outdated:
                resp = self.api_request(
                    "projects", self.project_id, mode="put", **{key + added: val}
                )
                self._print(f"set {key} to {resp[key]}", fg="yellow")
            else:
                self._print(f"ok: {key}", fg="green")

    def sync_badges(self) -> None:
        resp = self.api_request("projects", self.project_id, "badges")
        names = [y["name"] for y in resp]

        settings = dict(
            Pipeline=dict(
                link_url=self.url(
                    "%{project_path}/-/pipelines/%{default_branch}/latest"
                ),
                image_url=self.url(
                    "%{project_path}/badges/%{default_branch}/pipeline.svg"
                ),
            ),
            Coverage=dict(
                link_url=self.url("%{project_path}/-/commits/%{default_branch}"),
                image_url=self.url(
                    "%{project_path}/badges/%{default_branch}/coverage.svg"
                ),
            ),
        )
        resp_dict = {x["name"]: x for x in resp}
        for badge_name, setting in settings.items():
            if badge_name not in names:
                msg = "installed"
                resp = self.api_request(
                    "projects",
                    self.project_id,
                    "badges",
                    mode="post",
                    **setting,
                    name=badge_name,
                )
            else:
                outdated = self._check_outdated(setting, resp_dict[badge_name])
                if outdated:
                    msg = "updated"
                    resp = self.api_request(
                        "projects",
                        self.project_id,
                        "badges",
                        resp_dict[badge_name]["id"],
                        mode="put",
                        **setting,
                    )
                else:
                    self._print(f"ok badge: {badge_name}", fg="green")
                    continue

            self._print(f"{msg} badge: {resp['name']}", fg="yellow")

    def _check_outdated(self, setting: tp.Any, resp: tp.Any) -> bool:
        if isinstance(setting, dict):
            for key, val in setting.items():
                val2 = self._special_key_resolution(resp, key)
                if self._check_outdated(val, val2):
                    self._print(f"{key}: {val}!={val2}", fg="magenta")
                    return True
        else:
            if str(setting) != str(resp):
                return True

        return False

    @classmethod
    def _special_key_resolution(cls, resp: tp.Any, key: str) -> tp.Any:
        if key in ["push_access_level", "merge_access_level"]:
            lvls = resp[f"{key}s"]
            assert len(lvls) == 1
            return lvls[0]["access_level"]
        return resp[key]

    def sync_protection(self) -> None:
        vip_branches = self.ns.auxcon.gitlab.vip_branches
        resp = self.api_request("projects", self.project_id, "protected_branches")
        on_remote = [x["name"] for x in resp]
        to_remove = set(on_remote) - set(vip_branches)

        resp_dict = {x["name"]: x for x in resp}
        for branch, setting in vip_branches.items():
            if branch not in on_remote:
                msg = "installed"
            else:
                outdated = self._check_outdated(setting, resp_dict[branch])
                if outdated:
                    resp = self.api_request(
                        "projects",
                        self.project_id,
                        "protected_branches",
                        branch,
                        mode="delete",
                    )
                    msg = "updated"
                else:
                    self._print(f"ok protection: {branch}", fg="green")
                    continue

            resp = self.api_request(
                "projects",
                self.project_id,
                "protected_branches",
                **setting,
                name=branch,
                mode="post",
            )
            self._print(f"{msg} protection: {resp['name']}", fg="yellow")

        for branch in to_remove:
            resp = self.api_request(
                "projects", self.project_id, "protected_branches", branch, mode="delete"
            )
            self._print(f"removed protection for: {branch}", fg="red")

    def bake(self) -> None:

        self.sync_settings()
        self.sync_badges()
        self.sync_protection()

    @staticmethod
    def _col(x: tp.Any) -> str:
        status = x["status"]
        if status == "success":
            return "green"
        if status == "failed":
            return "red"
        if status == "pending":
            return "blue"
        if status == "created":
            return "cyan"
        if status == "canceled":
            return "magenta"
        return "yellow"

    def pipeline(self, show_success: bool = False) -> tp.Tuple[bool, bool]:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            check=True,
            capture_output=True,
        )
        branch = out.stdout.decode().strip()
        resp = self.api_request("projects", self.project_id, "pipelines")
        for pipeline in resp:
            self.pretty_pipeline(pipeline)
            if branch not in pipeline["ref"]:
                continue
            self.display_pipeline(pipeline, show_success)

            done = bool(pipeline["status"] in ["success", "failed"])
            success = bool(pipeline["status"] in ["success"])
            return done, success
        return True, False

    def pretty_pipeline(self, pipeline: tp.Any) -> None:
        if "refs/merge-requests" in pipeline["ref"]:
            mr_id = int(pipeline["ref"].split("/")[2])
            mr_resp = self.api_request(
                "projects", self.project_id, "merge_requests", mr_id
            )
            pipeline["ref"] = "{source_branch}->{target_branch}".format_map(mr_resp)
        ddt = datetime.datetime
        start = ddt.strptime(pipeline["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if pipeline["status"] != "running":
            last_update = ddt.strptime(pipeline["updated_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            last_update = datetime.datetime.utcnow()
        delta = last_update - start
        pipeline["duration"] = str(delta).rsplit(".", 1)[0].split(":", 1)[1]
        pipeline["source"] = pipeline["source"][:2]

    def display_pipeline(self, pipeline: tp.Any, show_success: bool = False) -> None:
        self._print(
            "[{source}|{status[0]}|{duration}]{ref:<36} {web_url}".format_map(pipeline),
            fg=self._col(pipeline),
        )
        jobs = self.api_request(
            "projects", self.project_id, "pipelines", pipeline["id"], "jobs"
        )

        for job in reversed(jobs):
            if not show_success and job["status"] == "success":
                continue
            job["name"] = "{stage}:{name}".format_map(job)
            if job["duration"] is None:
                job["duration"] = "--:--"
            else:
                job["duration"] = (
                    str(datetime.timedelta(seconds=job["duration"]))
                    .split(".", 1)[0]
                    .split(":", 1)[1]
                )
            self._print(
                "   [{status[0]}|{duration}]{name:<36} {web_url}".format_map(job),
                fg=self._col(job),
            )

    def release(self) -> tp.Tuple[bool, bool]:
        current_version, _ = self.ns.get_current_version_and_lines()
        mr_message = f"release {current_version}"
        coord = ["projects", self.project_id, "merge_requests"]
        settings = dict(source_branch="develop", target_branch="release")
        release_notes = self.ns.get_release_notes()

        self._print(f"{mr_message} [{release_notes[current_version]}]", fg="green")
        resp = self.api_request(*coord)
        show = [  # order is important
            settings["target_branch"],
            "{source_branch}->{target_branch}".format_map(settings),
        ]
        n_success = len(show)
        error = 0
        success = 0
        for mr in resp:  # pylint: disable=invalid-name
            # check that there isnt a mr to release already
            if (
                mr["source_branch"] == settings["source_branch"]
                and mr["target_branch"] == settings["target_branch"]
                and mr["title"] == mr_message
            ):
                # if the pipeline fails, we set the merge again
                if (
                    not mr["merge_when_pipeline_succeeds"]
                    and mr["state"] == "opened"
                    and mr["merge_status"] == "can_be_merged"
                ):
                    resp = self.api_request(
                        *coord,
                        mr["iid"],
                        "merge",
                        mode="put",
                        merge_when_pipeline_succeeds=True,
                    )
                resp = self.api_request("projects", self.project_id, "pipelines")
                for pipeline in resp:
                    self.pretty_pipeline(pipeline)
                    if pipeline["ref"] in show:
                        i = show.index(pipeline["ref"])
                        show = show[i + 1 :]  # we dont want to see the old tag pipeline
                        if pipeline["status"] != "success":
                            error += 1
                            self.display_pipeline(pipeline)
                        else:
                            success += 1

                if success == n_success and not error:
                    self._print("fully released, congrats :)", fg="green")
                    return True, True
                elif not error:
                    self._print(f"release ongoing {success}/{n_success}", fg="yellow")
                return False, False

        # create new mr
        mr = self.api_request(  # pylint: disable=invalid-name
            *coord,
            mode="post",
            **settings,
            title=mr_message,
        )
        for _ in range(6):
            if mr["merge_status"] == "can_be_merged":
                resp = self.api_request(
                    *coord,
                    mr["iid"],
                    "merge",
                    mode="put",
                    merge_when_pipeline_succeeds=True,
                )
                mwps_msg = " and set mwps"
                break
            time.sleep(0.3)
            mr = self.api_request(*coord, mr["iid"])  # pylint: disable=invalid-name
        else:
            mwps_msg = " and was NOT able to set mwps"

        self._print(
            "created release-mr ({source_branch}->{target_branch})".format_map(settings)
            + mwps_msg,
            fg="yellow",
        )
        return False, False
