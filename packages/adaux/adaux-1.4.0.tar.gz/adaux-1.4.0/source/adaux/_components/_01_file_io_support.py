# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import filecmp
import os
import shutil
import typing as tp
from pathlib import Path

from .._base_parser import FileOpsConvenience
from .._parser import BaseParser
from .._parser import ConfigParser
from .._parser import Jinja2Parser
from .._parser import YamlParser
from .._proto_namespace import _ProtoNamespace


class FileIOSupport(FileOpsConvenience, _ProtoNamespace):
    def __init__(self) -> None:
        super().__init__()
        self.root = Path(__file__).resolve().parent.parent / "src"
        self.verbose = True

    def _print(
        self, msg: str, **kwgs: tp.Any  # pylint: disable=unused-argument
    ) -> None:
        if self.verbose:
            print(msg)

    def load_auxcon(self) -> None:
        # pylint: disable=attribute-defined-outside-init
        self.auxcon = self.get_parser().read(self.auxcon_file)
        self.set_defaults()

    def save_auxcon(self) -> None:
        self.cleanup()
        self.get_parser().write(self.auxcon, self.auxcon_file)

    def get_parser(self) -> tp.Type[BaseParser]:
        suffix = self.auxcon_file.suffix
        if suffix in [".ini", ".cfg"]:
            return ConfigParser
        elif suffix in [".yaml", ".yml"]:
            return YamlParser
        else:
            raise NotImplementedError(f"filetype {suffix} not supported!")

    def save_auxcon_to_stream(self, ost: tp.TextIO, stage1: bool = True) -> None:
        with self.extra(stage1=stage1) as auxcone:
            YamlParser.write_stream(auxcone, ost)

    @classmethod
    def list2ns(cls, list_w_opt: tp.List[str]) -> _ProtoNamespace:
        res = _ProtoNamespace()
        for item in list_w_opt:
            if isinstance(item, str):
                parts = item.split(";")
                id_ = parts[0].strip()
                res[id_] = _ProtoNamespace()
                for opt in parts[1:]:
                    key, val = opt.split("=", 1)
                    res[id_][key.strip()] = val.strip()
            else:  # yaml dict
                id_ = item.pop("id")
                res[id_] = _ProtoNamespace(**item)

        return res

    @classmethod
    def list2nsl(
        cls, list_w_opt: tp.List[str]
    ) -> tp.List[tp.Union[str, _ProtoNamespace]]:
        res: tp.List[tp.Union[str, _ProtoNamespace]] = []
        for key, val in cls.list2ns(list_w_opt).items():
            if val:
                add = _ProtoNamespace(id=key)
                add.update(val)
                res.append(add)
            else:
                res.append(key)
        return res

    @classmethod
    def _boolify(cls, data: tp.Union[_ProtoNamespace, str], key: str) -> None:
        if isinstance(data, str):
            return
        assert isinstance(data, _ProtoNamespace)
        try:
            data[key] = data[key] in ["true", "True", True]
        except (KeyError, AttributeError):
            pass

    def copy_file(
        self,
        name: tp.Union[str, Path],
        dest_name: tp.Union[str, Path] = "",
        chmod: tp.Optional[int] = None,
        custom: bool = False,
    ) -> None:
        if isinstance(name, str):
            if custom:
                src = self.target_custom / name
            else:
                src = self.root / name
        else:
            src = name
            assert dest_name != ""

        dest_name = dest_name or name
        if isinstance(name, str):
            dest = self.target / dest_name
        else:
            dest = dest_name

        self.ensure_parent(dest)

        if dest.exists() and filecmp.cmp(src, dest):
            return

        shutil.copyfile(src, dest)
        if chmod:
            self.chmod(dest, chmod)
        self._print(f"copied {dest}", fg="blue")

    def bake_file(  # pylint: disable=too-many-arguments
        self,
        name: str,
        dest_name: str = "",
        chmod: tp.Optional[int] = None,
        only_if_inexistent: bool = False,
        custom: bool = False,
        ignore_absent: bool = False,
        **kwgs: tp.Any,
    ) -> None:
        dest_name = dest_name or name
        src_dir = self.target_custom if custom else self.root
        dest = self.target / dest_name
        if only_if_inexistent and dest.exists():
            return

        src = src_dir / name
        if src.exists():
            self.copy_file(name, dest_name, chmod=chmod, custom=custom)
            return

        jinja_src = src_dir / (name + ".jinja2")
        if not jinja_src.exists() and ignore_absent:
            return
        written = Jinja2Parser.render_to_dest(jinja_src, dest, aux=self.auxcon, **kwgs)
        if written:
            if chmod:
                self.chmod(dest, chmod)
            self._print(f"baked {dest}", fg="green")

    def combine_files(self, *names: str, dest_name: str) -> None:
        tmp_combo = self.root / "temp-combination"
        if tmp_combo.exists():
            tmp_combo.unlink()
        with open(tmp_combo, "a", encoding="utf-8") as tmp:
            for name in names:
                src = self.root / name
                with open(src, encoding="utf-8") as in_:
                    tmp.writelines(in_.readlines())
                    if name != names[-1]:
                        tmp.write("\n")

        self.copy_file(tmp_combo.name, dest_name)
        tmp_combo.unlink()

    @classmethod
    def chmod(cls, dest: Path, chmod: int) -> None:
        os.chmod(dest, chmod)

    def copy_many_files(self, *names: str) -> None:
        for name in names:
            self.copy_file(name)
