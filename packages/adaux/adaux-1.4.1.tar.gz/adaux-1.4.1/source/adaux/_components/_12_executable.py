# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin
from ._05_dependency import DependencyMixin


class ExecutablesMixin(DependencyMixin, ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("executables", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.executables.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(executables=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("console_scripts", "scripts")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.executables.scripts += ["scripts/say_hello"]

    def bake(self) -> None:
        super().bake()
        config = self.auxcon.project.config
        data = self.auxcon.executables

        default_scripts = [
            ("mypy", "mp"),
            ("pylint", "pl"),
            ("coverage", "cov"),
            ("docker", "dcp"),
            ("ci", "ci"),
            ("pre-commit", "pra2"),
            ("project", "pipi"),
            ("package", "sdist"),
            ("docs", "docs"),
        ]

        for key, val in default_scripts:
            if self.is_enabled(key):
                self.bake_file(f"scripts/{val}")
                data.scripts += [f"devops/scripts/{val}"]

        config.options.scripts = data.scripts
        cscr = data.console_scripts
        for i, val in enumerate(cscr):
            if "=" in val:
                continue
            name = val.rsplit(":", 1)[1]
            cscr[i] = f"{name} = {val}"

        config["options.entry_points"].console_scripts = cscr
