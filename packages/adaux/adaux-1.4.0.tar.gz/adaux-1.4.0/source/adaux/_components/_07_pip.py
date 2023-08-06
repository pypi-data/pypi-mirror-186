# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import collections
import contextlib
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._05_dependency import DependencyMixin


class PipMixin(DependencyMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("pip", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.pip.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(pip=self.__keys()[1:], **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("extra_index_url", "branch_match")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.pip
        data.extra_index_url = dict(
            demo="https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.x.y/api/v4/projects/118/packages/pypi/simple"
        )
        data.branch_match = dict(
            demo="https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.x.y/user/demo.git"
        )

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            data = auxcone.pip
            for key in self.__keys():
                if data[key] == "":
                    data[key] = []
            if stage1:
                yield auxcone
                return
            try:
                data.extra_index_url = collections.OrderedDict(
                    tuple(val.split("=", 1)) for val in data.extra_index_url or []  # type: ignore
                )
            except ValueError:
                data.extra_index_url = collections.OrderedDict(data.extra_index_url)

            try:
                data.branch_match = collections.OrderedDict(
                    tuple(val.split("=", 1)) for val in data.branch_match  # type: ignore
                )
            except ValueError:
                data.branch_match = collections.OrderedDict(data.branch_match)

            wo_creds = collections.OrderedDict()
            creds = collections.OrderedDict()

            for key, url in data.extra_index_url.items():
                if "@" in url:
                    pre, url = url.split("@", 1)
                    proto, cred = pre.split("//", 1)
                    url = f"{proto}//{url}"
                    token, var_cred = cred.split(":", 1)
                    assert "$" == var_cred[0]
                    creds[key] = var_cred[1:]
                    assert "$" not in token

                wo_creds[key] = url

            data.extra_index_url_wo_creds = wo_creds
            data.creds = creds
            yield auxcone

    def bake(self) -> None:
        super().bake()

        # we rely on .netrc for the credentials
        name = "pip/pip.conf"
        self.bake_file(name)

    def branch_match_and_cred_passing(self, opts: _ProtoNamespace) -> None:
        opts.pip_extra_url = self._collect_extra_url(opts.pip_req)
        opts.pip_cred_vars = self._collect_cred_vars(opts.pip_req)
        for i, dep in enumerate(opts.pip_req):
            pkg, _ = self.parse_dep(dep)
            match = self.auxcon.pip.branch_match.get(pkg)
            if match is None:
                continue
            # skip matching these branches
            skip = [self.auxcon.gitlab.release_branch]
            var = f'{pkg.upper().replace(".", "_").replace("-", "_")}_MATCHING_REPO'
            opts.pip_req[i] = f"${{{var}:-{dep}}}"
            opts.pip_cred_vars.append(var)
            opts.setdefault("branch_match", [])
            opts.branch_match.append((pkg, var, match, skip))  # variable used by CI

    def _collect_extra_url(self, deps: tp.List[str]) -> tp.List[str]:
        extra_url = set()

        for dep in deps:
            pkg, _ = self.parse_dep(dep)
            url = self.auxcon.pip.extra_index_url.get(pkg)
            if url is not None:
                extra_url.add(url)

        return list(sorted(extra_url))

    def _collect_cred_vars(self, deps: tp.List[str]) -> tp.List[str]:
        cred_vars = set()

        for dep in deps:
            pkg, _ = self.parse_dep(dep)
            cred = self.auxcon.pip.creds.get(pkg)
            if cred is not None:
                cred_vars.add(cred)

        return list(sorted(cred_vars))
