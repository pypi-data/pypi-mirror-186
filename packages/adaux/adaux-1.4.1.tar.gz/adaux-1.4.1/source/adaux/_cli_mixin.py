# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import io
import subprocess
import typing as tp
from pathlib import Path

from ._components import AllComponents
from ._components._02_base import BaseComponent
from ._gitlab import GitlabSetter
from ._tick import TickSetter


class LazyVersionStr:
    def __str__(self) -> str:
        # pylint: disable=import-outside-toplevel,cyclic-import
        import adaux

        return adaux.__version__


class CliMixin(BaseComponent):  # pylint: disable=too-many-ancestors
    def __init__(self, target: Path, silent: bool = False) -> None:
        super().__init__()
        self.verbose = not silent
        self.target = Path(target or "devops").resolve()

        if str(Path.cwd()) in str(self.target):
            self.target = self.target.relative_to(Path.cwd())

        valid_suffix = [".yml", ".yaml", ".cfg"]
        candidates = [
            (self.target.parent / "auxilium").with_suffix(sfx) for sfx in valid_suffix
        ]
        self.auxcon_file = candidates[0]

        # fuzzy finder via git root
        if not any(cand.exists() for cand in candidates) and target is None:
            resp = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                capture_output=True,
                check=False,
            )
            if resp.returncode == 0:
                git_root = Path(resp.stdout.decode().strip())
                self.target = git_root / "devops"
                candidates = [
                    (git_root / "auxilium").with_suffix(sfx) for sfx in valid_suffix
                ]

        for cand in candidates:
            if cand.exists():
                self.auxcon_file = cand
                self.load_auxcon()
                break
        self._print(f"adaux {LazyVersionStr()} at your service", fg="blue")

    @property
    def target_custom(self) -> Path:
        return self.target / "custom"

    def demo(self: "CliMixin") -> None:
        self.clear_to_demo()
        out = io.StringIO()
        self.save_auxcon_to_stream(out)
        self._print(out.getvalue())

    def show(self: "CliMixin", full: bool = False) -> None:
        out = io.StringIO()
        self.save_auxcon_to_stream(out, stage1=not full)
        self._print(out.getvalue())

    def init(
        self: "CliMixin",
        project_name: str,
        project_slug: str,
        python_version: str,
        author: str,
        force: bool = False,
    ) -> None:

        self.clear_to_template(
            project_name=project_name,
            project_slug=project_slug,
            python_version=python_version,
            author=author,
        )

        self.target.mkdir(parents=True, exist_ok=True)
        self.save_auxcon_and_print(force)

    def save_auxcon_and_print(self, force: bool = False, stage1: bool = True) -> None:
        dest = self.auxcon_file
        over, fg_col = "", "green"
        if dest.exists():
            if not force:
                raise RuntimeError(f"{dest} exists, use -f or --force to overwrite.")
            over, fg_col = "over", "yellow"

        with self.extra(stage1=stage1):
            self.save_auxcon()

        # pylint: disable=protected-access
        self._print(f"{over}written template to {dest}", fg=fg_col)

    def sync(self: "CliMixin") -> None:
        proj = self.auxcon.project
        clean = self.type_wo_disabled(discard_before="SentinelMixin")()

        clean.clear_to_template(
            project_name=proj.name,
            project_slug=proj.slug,
            python_version=proj.minimal_version,
            author=proj.author,
        )
        self.update_to_template(clean.auxcon)
        with self.extra(stage1=True):
            self.save_auxcon()

    def bake(self: "CliMixin") -> None:
        if not self.auxcon_file.exists():
            raise RuntimeError(f"{self.auxcon_file} does not exists! use 'aux init'")
        super().bake()

    def gitlab(self: "CliMixin", token: str) -> None:
        gls = GitlabSetter(self, token)
        with self.extra():
            gls.bake()

    def pipeline(
        self: "CliMixin", token: str, show_success: bool
    ) -> tp.Tuple[bool, bool]:
        gls = GitlabSetter(self, token)
        with self.extra():
            return gls.pipeline(show_success)

    def tick(
        self: "CliMixin",
        release_message: str,
        major: bool = False,
        minor: bool = False,
        commit: bool = False,
    ) -> None:
        if major and minor:
            raise RuntimeError("cannot set major and minor tick at the same time!")
        if len(release_message) < 16:
            raise RuntimeError("message cannot be shorter than 16 char")
        ticker = TickSetter(self, release_message, major, minor)
        with self.extra():
            ticker.bake()
            if commit:
                ticker.commit()

    def release(self: "CliMixin", token: str) -> tp.Tuple[bool, bool]:
        gls = GitlabSetter(self, token)
        with self.extra():
            return gls.release()

    def convert(self: "CliMixin", src: Path, dest: Path, force: bool = False) -> None:
        self.auxcon_file = src
        self.load_auxcon()
        self.auxcon_file = dest
        self.save_auxcon_and_print(force)


class CliRenderer(CliMixin, AllComponents):  # pylint: disable=too-many-ancestors
    pass
