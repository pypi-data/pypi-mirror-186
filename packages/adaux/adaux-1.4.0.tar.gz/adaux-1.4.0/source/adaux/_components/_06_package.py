# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import copy
import typing as tp

from .._parser import ConfigParser
from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin


class PackageMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("package", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.package.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(package=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("include", "exclude")

    def bake(self) -> None:
        super().bake()
        config = self.auxcon.project.config
        data = self.auxcon.package
        name = self.auxcon.project.name

        for dkey, ckey in [
            ("include", "options.package_data"),
            ("exclude", "options.exclude_package_data"),
        ]:
            if not data[dkey]:
                continue
            config.setdefault(ckey, _ProtoNamespace())
            config[ckey][name] = data[dkey]

        config = copy.copy(config)

        def not_devops(x: str) -> bool:
            return "devops" not in x

        config.options = copy.copy(config.options)
        config.options.scripts = list(filter(not_devops, config.options.scripts))
        if not config.options.scripts:
            del config.options.scripts

        extra = copy.copy(config["options.extras_require"])
        del extra["dev"]
        config["options.extras_require"] = extra
        data.config = config

    def writeout(self) -> None:
        super().writeout()
        dest = self.target / "package/setup-dist.cfg"
        written = ConfigParser.write(self.auxcon.package.pop("config"), dest)
        if written:
            self._print(f"baked {dest}", fg="green")
