# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import re
import typing as tp

from .._parser import YamlParser
from .._proto_namespace import _ProtoNamespace
from ._17_docker import DockerMixin


class CiMixin(DockerMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("ci", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.ci.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(ci=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("jobs",)

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        deps = self.auxcon.dependencies.dev
        deps.append(self.versions.requests)
        deps.append(self.versions.types_requests)
        data = self.auxcon.ci
        vslug = self.python_version_slug
        data.jobs = [f"python-deps-{vslug}      ;default=true"]
        if self.is_enabled("pre-commit"):
            data.jobs += [
                f"pre-commit-{vslug}       ;default=true",
                f"pre-commit-all-{vslug}   ;default=true",
            ]
        if self.is_enabled("pytest"):
            data.jobs += [f"pytest-{vslug}           ;default=true"]
        if self.is_enabled("coverage"):
            data.jobs += [f"pycov-{vslug}            ;default=true"]
        if self.is_enabled("docs"):
            data.jobs += [f"docs-{vslug}                 ;default=true"]
        if self.is_enabled("gitlab"):
            data.jobs += [
                "check-release-notes",
                "gitlab-release",
                "pkg-gitlab",
            ]

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        super().update_to_template(tpl)

        data = self.auxcon.ci
        old = list(map(self._job_name, data.jobs))
        for job in tpl.ci.jobs:
            name = self._job_name(job)
            if name not in old:
                data.jobs.append(job)
                self._print(f"ci.jobs: added {name}", fg="green")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.ci.runner = "dind-cached"
        self.auxcon.ci.mechanism = "mixed"
        self.auxcon.ci.jobs[3] += ";run=true;service=postgres"

    @contextlib.contextmanager
    def extra(  # pylint: disable=too-many-branches
        self, stage1: bool = False
    ) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            data = auxcone.ci
            if stage1:
                data.jobs = self.list2nsl(data.jobs)
                for x in data.jobs:
                    self._boolify(x, "default")
                yield auxcone
                return
            data.jobs = self.list2ns(data.jobs)

            valid_opts_keys = [
                "default",
                "build",
                "build-deps",
                "build-stage",
                "build-rules",
                "images",
                "run",
                "run-deps",
                "run-stage",
                "run-rules",
                "services",
                "overwrite",
                "rules",
                "files",
                "function",
                "target",  # for develop/release-tag
                "always-build",  # for image
                "deps",
            ]

            for job, val in data.jobs.items():
                if "default" in val and isinstance(val.default, str):
                    val.default = val.default in ["true", "True"]

                self._set_default(job, val)

                val.setdefault("function", "docker")
                self._handle_special(job, val)

                for key in ["build", "run"]:
                    val.setdefault(key, True)
                    if isinstance(val[key], str):
                        val[key] = val[key] in ["true", "True"]

                for key in ["build-stage", "run-stage"]:
                    val.setdefault(key, None)

                for key in [
                    "build-deps",
                    "run-deps",
                    "deps",  # points to non build
                    "rules",
                    "build-rules",
                    "run-rules",
                    "services",
                    "images",
                    "overwrite",
                    "files",
                ]:
                    val.setdefault(key, [])
                    if isinstance(val[key], str):
                        val[key] = val[key].split(",")

                # infuse shorthands
                shorthand = dict(push=["push-no-mr", "mr"])
                default_rules: tp.Dict[str, tp.List[str]] = {
                    "rules": shorthand["push"] + ["web", "pipeline"],
                }
                for key in ["rules", "build-rules", "run-rules"]:
                    res = []
                    for rule in val[key]:
                        if rule in shorthand:
                            val[key].remove(rule)
                            res += shorthand[rule]
                        else:
                            res += [rule]
                    if not val["rules"]:
                        res = res or default_rules[key]
                    val[key] = res

                diff = set(val.keys()) - set(valid_opts_keys)
                if diff:
                    raise RuntimeError(f"invalid options: {diff}")

            data.setdefault("mechanism", "monolith")
            data.setdefault("runner", "normal")
            data.setdefault("docker_image", self.versions.ci_docker_image)
            assert data.mechanism in ["monolith", "gitlab", "mixed"]
            assert data.runner in ["dind-cached", "normal"]
            yield auxcone

    @classmethod
    def _set_default(cls, job: str, opts: _ProtoNamespace) -> None:
        if not opts.get("default", False):
            return

        default_trigger = ["web", "pipeline"]
        version = job.rsplit("-", 1)[1]
        if "pre-commit-all" in job:
            opts.setdefault("build", False)
            opts.setdefault("run-deps", f"pre-commit-{version}")
            opts.setdefault("rules", ["mr"] + default_trigger)
        elif "pre-commit" in job:
            opts.setdefault("files", ["devops/pre-commit/config.yaml"])
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("run-rules", ["push-no-mr"] + default_trigger)
            opts.setdefault("build-rules", ["push-no-mr", "mr"] + default_trigger)
        elif "python-deps" in job:
            opts.setdefault("build-stage", "pre-build")
            opts.setdefault("run", False)
            opts.setdefault("rules", ["push"] + default_trigger)
        elif "pytest-standalone" in job:
            opts.setdefault("rules", ["vip-mr"] + default_trigger)
        elif "image-pytest" in job:
            opts.setdefault("always-build", True)
            opts.setdefault("build-deps", [f"pytest-{version}"])
            opts.setdefault("build-stage", "build")
            opts.setdefault("rules", ["release-mr"] + default_trigger)
        elif "ansible-deploy" in job:
            opts.setdefault("build-stage", "pre-build")
            opts.setdefault("run-stage", "deploy")
            opts.setdefault("deps", "release-tag")
            opts.setdefault("rules", ["release-push"] + default_trigger)
        elif "pytest" in job:
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("run-rules", ["push"] + default_trigger)
        elif "pycov" in job:
            opts.setdefault("build", False)
            opts.setdefault("run-deps", [f"pytest-{version}"])
            opts.setdefault("run-rules", ["mr", "vip-push"] + default_trigger)
        elif "docs" in job:
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("run-rules", ["push"] + default_trigger)
            # opts.setdefault("run-rules", ["release-mr"] + default_trigger)
        elif "image" in job:
            opts.setdefault("always-build", True)
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("build-stage", "build")
            opts.setdefault("run", False)
            opts.setdefault("rules", ["release-push"] + default_trigger)
        else:
            raise NotImplementedError(f"no default available for {job}!")

    @classmethod
    def _handle_special(cls, job: str, opts: _ProtoNamespace) -> None:
        if job == "check-release-notes":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-mr")
            opts.function = "spez"
        elif job == "gitlab-release":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
            opts.function = "spez"
        elif job == "pkg-gitlab":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
        elif job == "pkg-pypi":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
        elif job in ["release-tag", "develop-tag"]:
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            if job == "release-tag":
                opts.setdefault("rules", "release-push")
            elif job == "develop-tag":
                opts.setdefault("rules", "develop-push")
            if "target" not in opts:
                raise RuntimeError(f"{job} must specify the option 'target'")
            opts.function = "spez"

    def bake(self) -> None:  # pylint: disable=too-many-branches,too-many-locals
        super().bake()
        dest_dir = self.target / "CI"
        data = self.auxcon.ci
        base_files = ["00-main.yml", "01-rules.yml"]
        job_files = []
        if data.mechanism in ["monolith", "mixed"]:
            job_files += ["python_ci.py"]
            self.bake_file("../_aux_ci.py", "CI/_aux_ci.py")

        if data.mechanism in ["mixed", "gitlab"]:
            base_files += ["02-template.yml"]
            job_files += ["03-build.yml", "04-run.yml"]

        for filename in base_files:
            self.bake_file(f"CI/{filename}")

        valid_rules = []

        config = YamlParser.read(dest_dir / "01-rules.yml")
        valid_rules += list(x.replace(".r-", "") for x in config)
        ci_rules = self._generate_python_rules(valid_rules, config)

        # validate jobs
        valid_build_deps: tp.List[str] = []
        valid_run_deps: tp.List[str] = []

        def invalid_option_error(key: str, k: str, valid: tp.Sequence[str]) -> None:
            if k not in valid:
                raise RuntimeError(f"{k} is not in valid {key} ({valid})")

        for job, opts in list(data.jobs.items()):
            for key, valid in [
                ("build-deps", valid_build_deps),
                ("run-deps", valid_run_deps),
                ("build-rules", valid_rules),
                ("run-rules", valid_rules),
                ("rules", valid_rules),
            ]:
                if key in opts:
                    for k in opts[key]:
                        invalid_option_error(key, k, valid)

            for key, valid in [
                ("target", valid_build_deps),
            ]:
                if key in opts:
                    invalid_option_error(key, opts[key], valid)

            if opts.build:
                docker_job = self.auxcon.docker.services[job]
                opts.branch_match = docker_job.get("branch_match", [])
                if docker_job.base and docker_job.base not in opts.images:
                    opts.images.append(docker_job.base)
                valid_build_deps.append(job)
            if opts.run:
                base = [job] if opts.build else []
                opts["run-deps"] = base + opts["run-deps"]
                # develop/release-tag special addition
                target = opts.get("target")
                if target:
                    opts["run-deps"].append(target)

                opts["services"] = [job] + opts["services"]
                for service_name in opts["services"]:
                    service = data.jobs.get(service_name)
                    if not service:
                        continue
                    if (
                        service.function == "docker" or service_name == "gitlab-release"
                    ) and service_name not in self.auxcon.docker.services:
                        raise RuntimeError(
                            f"{service_name} is listed in CI but not in docker.services, please fix!"
                        )
                valid_run_deps.append(job)

        for filename in job_files:
            self.bake_file(f"CI/{filename}", ci_rules=ci_rules)

        if "python_ci.py" in job_files:
            self.chmod(dest_dir / "python_ci.py", 0o755)

    def _generate_python_rules(
        self, valid_rules: tp.List[str], config: _ProtoNamespace
    ) -> tp.List[tp.Tuple[str, str]]:
        initial = [(rule, config[".r-" + rule]["if"]) for rule in valid_rules]
        res = []
        for name, form in initial:
            python_form = self._rule_to_python(form)
            res.append((name, python_form))
        return res

    @classmethod
    def _rule_to_python(cls, form: str) -> str:
        x = re.sub(r"\$([A-Z0-9_]+)", r'env("\1")', form)
        x = re.sub(r"\|\|", "or", x)
        x = re.sub(r"\&\&", "and", x)
        x = re.sub("null", '""', x)
        return x
