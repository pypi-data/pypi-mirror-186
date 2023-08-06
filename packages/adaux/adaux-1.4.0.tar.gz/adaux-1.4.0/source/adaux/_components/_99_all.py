# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
from ._03_meta import MetaMixin
from ._04_project import ProjectMixin
from ._05_dependency import DependencyMixin
from ._06_package import PackageMixin
from ._07_pip import PipMixin
from ._08_gitignore import GitIgnoreMixin
from ._09_gitlab import GitlabMixin
from ._10_precommit import PrecommitMixin
from ._11_pylint import PylintMixin
from ._12_executable import ExecutablesMixin
from ._13_mypy import MypyMixin
from ._14_pytest import PytestMixin
from ._15_coverage import CoverageMixin
from ._16_docs import DocsMixin
from ._17_docker import DockerMixin
from ._18_ci import CiMixin
from ._98_sentinel import SentinelMixin

__all__ = ["AllComponents"]


class AllComponents(  # pylint: disable=too-many-ancestors
    SentinelMixin,
    PipMixin,
    DocsMixin,
    CiMixin,
    DockerMixin,
    PackageMixin,
    ExecutablesMixin,
    PylintMixin,
    MypyMixin,
    PrecommitMixin,
    CoverageMixin,
    PytestMixin,
    DependencyMixin,
    GitlabMixin,
    GitIgnoreMixin,
    ProjectMixin,
    MetaMixin,
):
    pass
