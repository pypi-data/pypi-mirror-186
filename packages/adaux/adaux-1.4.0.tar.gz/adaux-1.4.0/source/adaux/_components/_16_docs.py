# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import contextlib
import typing as tp

from .._proto_namespace import _ProtoNamespace
from ._04_project import ProjectMixin


class DocsMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("docs", _ProtoNamespace())

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.docs = [
            self.versions.sphinx,
            self.versions.sphinx_rtd_theme,
            self.versions.sphinx_click,
            self.versions.jupyter_sphinx,
            self.versions.bash_kernel,
        ]

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(docs=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return tuple()

    @contextlib.contextmanager
    def extra(self, stage1: bool = False) -> tp.Iterator[_ProtoNamespace]:
        with super().extra(stage1) as auxcone:
            data = auxcone.docs
            self._boolify(data, "strict")
            if stage1:
                yield auxcone
                return
            data.setdefault(
                "root", f"{auxcone.project.source_dir}/docs"
            )  # pylint: disable=pointless-statement

            gitlab = auxcone.gitlab
            if "url" not in data:
                pages_url = gitlab.remote_url.replace("gitlab", "pages")
                remote_name = gitlab.get("remote_name", auxcone.project.second_name)
                data.setdefault(
                    "url",
                    f"https://{gitlab.remote_user}.{pages_url}/{remote_name}",
                )

            auxcone.project.project_urls.Documentation = data.url
            yield auxcone

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.docs
        data.root = "source/docs"

    def bake(self) -> None:
        super().bake()
        data = self.auxcon.docs

        # user docs dir
        dest_rel = f"../{data.root}"
        self.bake_file(
            "docs/user/conf.py", f"{dest_rel}/conf.py", only_if_inexistent=True
        )
        self.bake_file(
            "docs/user/index.rst", f"{dest_rel}/index.rst", only_if_inexistent=True
        )
        self.bake_file("docs/user/gitignore", f"{dest_rel}/.gitignore")

        for name in ["static"]:
            path = self.target / f"{dest_rel}/{name}"
            path.mkdir(parents=True, exist_ok=True)

        # devops docs dir
        dest_rel = "docs"
        for name in ["static", "templates"]:
            path = self.target / f"{dest_rel}/{name}"
            path.mkdir(parents=True, exist_ok=True)

        self.bake_file("docs/default_conf.py")
        self.bake_file("docs/postprocess_html.py")
        self.bake_file("docs/static/git-link-color.css")
