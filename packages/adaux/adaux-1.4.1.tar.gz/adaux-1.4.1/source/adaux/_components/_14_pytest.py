# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._05_dependency import DependencyMixin


class PytestMixin(DependencyMixin):
    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.dependencies
        data.test.append(self.versions.pytest)

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.setdefault("pytest", _ProtoNamespace())
        data = self.auxcon.pytest
        data.asyncio_mode = "strict"

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            if stage1:
                yield auxcone
                return
            auxcone.setdefault("pytest", _ProtoNamespace())
            yield auxcone
