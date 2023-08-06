# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import contextlib
import copy
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._01_file_io_support import FileIOSupport


class BaseComponent(FileIOSupport):
    def __init__(self) -> None:
        super().__init__()
        self.versions = _ProtoNamespace(
            pytest="pytest>=7.2",
            pytest_cov="pytest-cov~=4.0",
            pre_commit="pre-commit>=2.20",
            mypy="mypy==0.991",
            pylint="pylint==2.15.5",
            black="black==22.12.0",
            sphinx="sphinx>=5.3.0",
            sphinx_rtd_theme="sphinx-rtd-theme>=1.0.0",
            sphinx_click="sphinx-click>=4.3",
            jupyter_sphinx="jupyter-sphinx>=0.4",
            bash_kernel="bash_kernel>=0.8",
            ci_docker_image="docker:20.10.17",
            blacken_docs="blacken-docs==v1.12.1",
            pre_commit_hooks="pre-commit-hooks==v4.4.0",
            pyupgrade="pyupgrade==v3.3.1",
            pycln="pycln==v2.1.2",
            reorder_python_imports="reorder_python_imports==v3.9.0",
            encryption_check="encryption_check==v1.0.0",
            docstr_coverage="docstr-coverage==v2.2.0",
            requests="requests==2.28.1",
            types_requests="types-requests",
        )
        self.set_defaults()

    def set_defaults(self) -> None:
        self.setdefault("auxcon", _ProtoNamespace())

    def clear_to_demo(self, **kwgs: tp.Any) -> None:
        self.clear_to_template(**kwgs)

    def cleanup(self, **kwgs: tp.Any) -> None:
        for component, keys in kwgs.items():
            for key in keys:
                if not self.auxcon[component][key]:
                    del self.auxcon[component][key]

        for key in copy.copy(self.auxcon):
            if not self.auxcon[key]:
                del self.auxcon[key]

    def clear_to_template(self, **kwgs: str) -> None:
        assert not kwgs
        self.auxcon.clear()
        self.set_defaults()

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        pass

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        auxcone = copy.deepcopy(self.auxcon)
        if not stage1:
            auxcone.versions = copy.copy(self.versions)
        yield auxcone

    def bake(self) -> None:
        pass

    def writeout(self) -> None:
        pass

    @classmethod
    def compose(cls, *types: type) -> "BaseComponent":
        if cls not in types:
            types = (cls,) + types
        bases = tuple(reversed(types))
        return type("DynComponent", bases, {})  # type: ignore
