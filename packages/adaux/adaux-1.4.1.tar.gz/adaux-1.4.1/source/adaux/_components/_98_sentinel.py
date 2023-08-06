# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._02_base import BaseComponent


class SentinelMixin(BaseComponent):
    def bake(self) -> None:
        with self.extra():
            super().bake()
            self.writeout()

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            tmp, self.auxcon = self.auxcon, auxcone
            yield auxcone
            self.auxcon = tmp
