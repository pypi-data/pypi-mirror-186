# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import typing as tp

from .._parser import Jinja2Parser
from .._parser import YamlParser
from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin
from ._05_dependency import DependencyMixin


class PrecommitMixin(DependencyMixin, ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("pre_commit", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.pre_commit.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(pre_commit=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("hooks", "rev_overwrite")

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.dependencies
        data.dev.append(self.versions.pre_commit)
        data.dev_apt.append("git-core")

        data = self.auxcon.pre_commit
        data.hooks = [
            "check-yaml;exclude=devops/CI",
            "check-toml",
            "check-json",
            "end-of-file-fixer",
            "add-copy-right",
            "trailing-whitespace",
            "black;exclude=devops/CI",
            "blacken-docs",
            "pyupgrade",
            "pycln",
            "reorder-python-imports",
        ]
        if self.is_enabled("mypy"):
            data.hooks.append("mypy")

        if self.is_enabled("pylint"):
            data.hooks.append("pylint")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.pre_commit
        data.hooks = list(data.hooks[0:12:5])
        data.hooks += ["pylint-test;files=tests/"]
        data.rev_overwrite = ["black==21.9b0"]

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            data = auxcone.pre_commit
            if stage1:
                data.hooks = self.list2nsl(data.hooks)
                yield auxcone
                return
            data.hooks = self.list2ns(data.hooks)
            data.rev_overwrite = {x.split("==", 1)[0]: x for x in data.rev_overwrite}

            # add custom extensions
            custom_config = self.target_custom / "pre-commit" / "config.yaml"
            data.custom = ""
            if custom_config.exists():
                with open(custom_config, encoding="utf-8") as f:
                    data.custom = f.read()

            yield auxcone

    def bake(self) -> None:  # pylint: disable=too-many-branches
        super().bake()

        data = self.auxcon.pre_commit
        # overwrite revs
        self.auxcon.versions.update(data.rev_overwrite)

        srcj = self.root / "pre-commit/config.yaml.jinja2"
        with Jinja2Parser.render_to_tmp(srcj, aux=self.auxcon) as src:
            config = YamlParser.read(src)

        requested_hooks = list(data.hooks.keys())

        self._raise_if_unsupported_hooks(config, requested_hooks)

        multi_hook_repo = ""
        # remove the ones not selected
        for repo in reversed(config.repos):

            def keep_selected(hook: _ProtoNamespace) -> bool:
                return hook.id in requested_hooks

            if len(repo.hooks) > 1:
                multi_hook_repo = repo.repo
            repo.hooks = list(filter(keep_selected, repo.hooks))
            if not repo.hooks:  # remove repo if empty
                config.repos.remove(repo)

            # integrate options
            for hook in repo.hooks:
                for key, val in data.hooks[hook.id].items():
                    if key in ["coverage"]:
                        continue
                    if key not in ["files", "exclude"]:
                        raise NotImplementedError(
                            f"support for option '{key}' of {hook.id} not implemented yet"
                        )
                    if key in hook:
                        hook[key] += "|" + val
                    else:
                        hook[key] = val

        # check if local python files are required from the hook
        for repo in config.repos:
            for hook in repo.hooks:
                entry = hook.get("entry")
                if entry and entry.startswith("devops/") and "custom" not in entry:
                    self.bake_file(entry.replace("devops/", ""), chmod=0o755)

        # order the config according to the requested_hooks
        if multi_hook_repo != "":
            self._print(
                f"pre-commit: cannot sort repos: '{multi_hook_repo}' has multiple hooks",
                fg="red",
            )
        config.repos = sorted(
            config.repos, key=lambda x: requested_hooks.index(x.hooks[0].id)
        )

        dest = self.target / "pre-commit/config.yaml"
        written = YamlParser.write(config, dest)
        if written:
            self._print(f"baked {dest}", fg="green")

    @classmethod
    def _raise_if_unsupported_hooks(
        cls, config: _ProtoNamespace, requested_hooks: tp.Iterable[str]
    ) -> None:
        available_hooks: tp.List[str] = sum(
            ([hook.id for hook in repo.hooks] for repo in config.repos), []
        )
        unknown_hooks = set(requested_hooks) - set(available_hooks)
        if unknown_hooks:
            raise RuntimeError(
                f"pre-commit hooks are not supported by aux: {unknown_hooks}.\n"
                "       Hint: You could add them in the custom directory."
            )
