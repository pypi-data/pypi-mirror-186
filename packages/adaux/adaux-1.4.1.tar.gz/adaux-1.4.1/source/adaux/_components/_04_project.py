# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import datetime
import os
import sys
import typing as tp
from pathlib import Path

from .._parser import ConfigParser
from .._parser import Jinja2Parser
from .._proto_namespace import _ProtoNamespace
from ._02_base import BaseComponent


class ProjectMixin(BaseComponent):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("project", _ProtoNamespace())

    def clear_to_template(self, *, project_name: str, project_slug: str, python_version: str, author: str, **kwgs: str) -> None:  # type: ignore # pylint: disable=arguments-differ
        super().clear_to_template(**kwgs)
        data = self.auxcon.project
        data.name = project_name
        data.slug = project_slug
        data.minimal_version = python_version
        data.supported_versions = [python_version]
        data.author = author
        data.creation_year = self.get_current_year()

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(
            project_name="hallo.world",
            project_slug="hlw",
            python_version=self.deduce_python_version(),
            author="anonymous",
            **kwgs,
        )
        data = self.auxcon.project
        data.license = "MIT"

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            if stage1:
                yield auxcone
                return
            data = auxcone.project
            data.minimal_version_slug = data.minimal_version.replace(".", "")
            data.setdefault("source_dir", "source")  # stay sync with aux_ci!
            data.setdefault("license", "Proprietary")
            data.module_dir = data.source_dir + "/" + data.name.replace(".", "/")
            data.namespace_name, data.second_name = "", data.name
            if "." in data.name:
                data.namespace_name, data.second_name = data.name.split(".", 1)
            data.active_years = self.get_active_years()
            data.setdefault("project_urls", _ProtoNamespace())
            data.setup_fields = [
                "name",
                "author",
                "license",
                "description",
                "long_description",
                "project_urls",
            ]
            yield auxcone

    def bake(self) -> None:
        super().bake()
        data = self.auxcon.project
        self.bake_file("install-dev.sh", chmod=0o755)
        self.bake_file("root/_setup.py", "../setup.py")

        srcj = self.root / "root/setup.cfg.jinja2"
        with Jinja2Parser.render_to_tmp(srcj, aux=self.auxcon) as src:
            data.config = ConfigParser.read(src)
            for key in data.setup_fields:
                if key not in data:
                    continue
                val = data[key]
                if val:
                    data.config.metadata[key] = val

        # license
        if data.license != "Proprietary":
            self.bake_file(
                f"license/{data.license}.txt",
                (self.target / ".." / "LICENSE.txt").resolve(),
            )

    def writeout(self) -> None:
        super().writeout()
        dest = self.target / "../setup.cfg"
        written = ConfigParser.write(self.auxcon.project.pop("config"), dest)
        if written:
            self._print(f"baked {dest}", fg="green")

    @classmethod
    def deduce_project_name(cls, path: tp.Optional[Path] = None) -> str:
        path = path or (Path.cwd())

        # level 1
        for obj in path.glob("*/__init__.py"):
            if "__version__" in obj.open("r", encoding="utf-8").read():
                lvl1 = obj.parent.stem
                return lvl1
        # level 2
        for obj in path.glob("*/*/__init__.py"):
            if "__version__" in obj.open("r", encoding="utf-8").read():
                lvl1 = obj.parent.stem
                lvl2 = obj.parent.parent.stem
                if lvl2 in ["source"]:
                    return lvl1
                return f"{lvl2}.{lvl1}"
        return "not-found"

    @classmethod
    def deduce_project_slug(cls) -> str:
        proj_name = cls.deduce_project_name()
        if proj_name.count(".") == 1:
            ns, sub = proj_name.split(".")
            return ns[:2] + sub[:3]
        return proj_name[:3]

    @classmethod
    def deduce_python_version(cls) -> str:
        return ".".join(map(str, sys.version_info[:2]))

    @classmethod
    def deduce_user(cls) -> str:
        return os.environ.get("USER", os.environ.get("USERNAME", "unknown"))

    @property
    def python_version_slug(self) -> str:
        return str(self.auxcon.project.minimal_version.replace(".", ""))

    def get_active_years(self) -> str:
        current_year = self.get_current_year()
        creation_year = self.auxcon.project.creation_year
        if creation_year == current_year:
            return f"{creation_year}"

        return f"{creation_year}-{current_year}"

    @classmethod
    def get_current_year(cls) -> str:
        return str(datetime.date.today().year)

    def get_current_version_and_lines(self) -> tp.Tuple[str, tp.List[str]]:
        data = self.auxcon.project
        init = self.auxcon_file.parent / data.module_dir / "__init__.py"

        with init.open("r", encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                if "__version__" in line:
                    version = line.strip().split('"', 2)[1]
                    break
            else:
                raise RuntimeError(f"version not found in {init}")

        return version, lines

    def get_release_notes(self) -> tp.Dict[str, str]:
        data = self.auxcon.project
        notes = self.auxcon_file.parent / data.source_dir / "release-notes.txt"
        release_note: tp.Dict[str, str] = {}
        with notes.open("r", encoding="utf8") as f:
            for line in f.readlines():
                version, note = line.strip().split(" ", 1)
                release_note[version] = note

        return release_note
