# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import typing as tp
from pathlib import Path


class FileOpsConvenience:
    @classmethod
    def ensure_parent(cls, dest: Path) -> None:
        target = dest.resolve().parent
        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)


class BaseParser(FileOpsConvenience):
    @classmethod
    def rec_walk(cls, obj: tp.Any, mods: tp.Any) -> tp.Any:
        for ident, modify in mods:
            if ident(obj):
                obj = modify(obj)
        if hasattr(obj, "items"):
            for key, val in obj.items():
                obj[key] = cls.rec_walk(val, mods)
        elif isinstance(obj, list):
            obj = [cls.rec_walk(val, mods) for val in obj]
        return obj

    @classmethod
    def read(cls, filename: Path) -> tp.Any:
        raise NotImplementedError()

    @classmethod
    def write(cls, data: tp.Any, dest: Path) -> bool:
        raise NotImplementedError()
