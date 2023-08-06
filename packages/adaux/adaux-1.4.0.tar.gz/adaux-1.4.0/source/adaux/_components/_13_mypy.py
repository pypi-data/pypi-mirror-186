# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import typing as tp
from pathlib import Path

from .._parser import ConfigParser
from .._proto_namespace import _ProtoNamespace
from ._05_dependency import DependencyMixin


class MypyMixin(DependencyMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("mypy", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.mypy.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(mypy=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("ignore",)

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.dev.append(self.versions.mypy)

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.mypy.ignore += ["click_help_colors"]

    def bake(self) -> None:
        super().bake()
        src = self.root / "pre-commit/mypy.ini"
        dest = self.target / "pre-commit/mypy.ini"
        config = ConfigParser.read(src)

        # namespace compat
        if "." in self.auxcon.project.name:
            config["mypy"]["namespace_packages"] = True
            config["mypy"]["explicit_package_bases"] = True
            config["mypy"][
                "mypy_path"
            ] = f"$MYPY_CONFIG_FILE_DIR/../../{self.auxcon.project.source_dir}"

        for x in self.auxcon.mypy.ignore:
            config[f"mypy-{x}.*"] = _ProtoNamespace(ignore_missing_imports="True")

        # special django stubs case
        for dep in self.auxcon.dependencies["dev"]:
            if (
                "django-stubs" in dep
                and (Path(self.auxcon.project.source_dir) / "settings.py").exists()
            ):
                config["mypy"]["plugins"] = ["mypy_django_plugin.main"]
                config["mypy.plugins.django-stubs"] = dict(
                    django_settings_module=f"{self.auxcon.project.name}.settings"
                )

        written = ConfigParser.write(config, dest)
        if written:
            self._print(f"baked {dest}", fg="green")
