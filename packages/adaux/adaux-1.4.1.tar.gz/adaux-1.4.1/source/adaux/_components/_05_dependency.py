# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import re
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin


class DependencyMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("dependencies", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.dependencies.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(dependencies=self.__keys()[1:], **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return (
            "default",
            "test",
            "dev",
            "docs",
            "default_apt",
            "test_apt",
            "dev_apt",
            "docs_apt",
        )

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.dependencies
        data.default_apt = ["postgres"]
        data.default = ["numpy"]
        data.dev.pop(-1)

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        super().update_to_template(tpl)
        data = self.auxcon.dependencies
        # add inexisting deps
        for mod in tpl.dependencies:
            if mod not in data:
                data[mod] = tpl.dependencies[mod]
                self._print(f"dependencies.{mod}: added {data[mod]}", fg="green")

        for mod in tpl.dependencies:
            if mod not in ["test", "doc", "dev"]:
                continue
            newer = {}
            for dep in tpl.dependencies[mod]:
                pkg, version = self.parse_dep(dep)
                if version is not None:
                    newer[pkg] = version

            dep_list = data.get(mod, [])
            for i, dep in enumerate(dep_list):
                pkg, version = self.parse_dep(dep)
                if version is not None:
                    if pkg in newer and newer[pkg] != version:
                        self._print(
                            f"dependencies.{mod}: updated {pkg} {version}->{newer[pkg]}",
                            fg="green",
                        )
                        dep_list[i] = dep.replace(version, newer[pkg])

    @classmethod
    def parse_dep(cls, dep: str) -> tp.Tuple[str, tp.Optional[str]]:
        if "=" in dep:
            pkg, version = re.split("[=><~]{2}", dep, 1)
        else:
            pkg = dep
            version = None
        return pkg, version

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            if stage1:
                yield auxcone
                return
            data = auxcone.dependencies
            for key in self.__keys():  # config loading artefact
                if data[key] == "":
                    data[key] = []
            yield auxcone

    def bake(self) -> None:
        super().bake()
        config = self.auxcon.project.config

        for key, deps in self.auxcon.dependencies.items():
            if key.endswith("_apt") or key.endswith("_script"):
                continue
            if key == "default":
                # my config writer will mess up dependencies with environment markers
                # if ' are present, but I need ' in auxilium.cfg for the docker files
                # as some are "${VAR}" and '${VAR}' does not work
                config.options.install_requires = [x.replace("'", '"') for x in deps]
            elif self.is_enabled(key):
                config["options.extras_require"][key] = deps
