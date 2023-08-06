# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin


class GitlabMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("gitlab", _ProtoNamespace())

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.gitlab
        data.vip_branches = [
            "develop;push_access_level=40;allow_force_push=True",
            "release",
        ]

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.gitlab.default_branch = "develop"
        self.auxcon.gitlab.release_branch = "release"
        self.auxcon.gitlab.remote_user = "administratum"
        self.auxcon.gitlab.remote_name = "auxilium"
        self.auxcon.gitlab.remote_url = "gitlab.x.y"

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            data = auxcone.gitlab
            if stage1:
                if "vip_branches" in data:
                    data.vip_branches = self.list2nsl(data.vip_branches)
                    for x in data.vip_branches:
                        self._boolify(x, "allow_force_push")
                yield auxcone
                return
            data.vip_branches = self.list2ns(data.vip_branches)
            vip_branch_name = list(data.vip_branches)
            data.setdefault("default_branch", vip_branch_name[0])
            data.setdefault("release_branch", vip_branch_name[-1])

            if "remote_user" in data and "remote_url" in data:
                remote_name = data.get("remote_name", auxcone.project.second_name)
                auxcone.project.project_urls.Source = (
                    f"https://{data.remote_url}/{data.remote_user}/{remote_name}"
                )

            # https://docs.gitlab.com/ee/api/protected_branches.html
            default = {
                (False, False): dict(
                    allow_force_push=True, push_access_level=30, merge_access_level=30
                ),
                (True, False): dict(push_access_level=0, merge_access_level=30),
                (False, True): dict(push_access_level=0, merge_access_level=40),
            }
            for key, val in data.vip_branches.items():
                mark = (key == data.default_branch, key == data.release_branch)
                for skey, sval in default[mark].items():
                    val.setdefault(skey, sval)

            yield auxcone
