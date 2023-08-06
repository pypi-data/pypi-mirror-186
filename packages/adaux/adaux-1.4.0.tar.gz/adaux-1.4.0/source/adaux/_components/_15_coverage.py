# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
from ._14_pytest import PytestMixin


class CoverageMixin(PytestMixin):
    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.test.append(self.versions.pytest_cov)
