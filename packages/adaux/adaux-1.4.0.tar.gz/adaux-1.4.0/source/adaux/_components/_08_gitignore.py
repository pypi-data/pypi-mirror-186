# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import typing as tp

from .._parser import Jinja2Parser
from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin


class GitIgnoreMixin(ProjectMixin):
    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            if stage1:
                yield auxcone
                return
            auxcone.setdefault("git_ignore", _ProtoNamespace())
            auxcone.git_ignore.setdefault("root", [])
            auxcone.git_ignore.setdefault("source", [])
            yield auxcone

    def bake(self) -> None:
        super().bake()
        self.bake_file("gitignore", ".gitignore")

        data = self.auxcon.project

        name1 = "root/gitignore_root"
        name2 = "root/gitignore_source"
        src1 = self.root / f"{name1}.jinja2"
        src2 = self.root / f"{name2}.jinja2"
        dest = self.target / ".." / ".gitignore"
        if data.source_dir != ".":
            self.bake_file(name1, "../.gitignore")
            self.bake_file(name2, f"../{data.source_dir}/.gitignore")

            flip = False
            for key in list(self.auxcon.project.config):
                if flip:
                    self.auxcon.project.config.move_to_end(key)
                if key == "options":
                    flip = True
                    self.auxcon.project.config["options.packages.find"] = dict(
                        where=data.source_dir
                    )

        else:
            tpl1 = Jinja2Parser.read(src1)
            tpl2 = Jinja2Parser.read(src2)
            tpl = f"{tpl1.render(aux=self.auxcon)}\n{tpl2.render(aux=self.auxcon)}"
            written = Jinja2Parser.write(tpl, dest)
            if written:
                self._print(f"baked {dest}", fg="green")
