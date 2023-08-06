# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import copy
import subprocess
import sys
import typing as tp

from .._parser import ConfigParser
from .._proto_namespace import _ProtoNamespace
from ._05_dependency import DependencyMixin


class PylintMixin(DependencyMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("pylint", _ProtoNamespace())
        self.auxcon.setdefault("pylint_test", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.pylint.setdefault(key, [])
            self.auxcon.pylint_test.setdefault(key, [])

        if not self.is_enabled("docs"):
            self.auxcon.pylint.setdefault(
                "disable",
                [
                    "missing-class-docstring",
                    "missing-module-docstring",
                    "missing-function-docstring",
                ],
            )

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(pylint=self.__keys(), pylint_test=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("disable", "good_names")

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.dev.append(self.versions.pylint)

        if not self.is_enabled("docs"):
            self.auxcon.pylint.disable = [
                "missing-class-docstring",
                "missing-module-docstring",
                "missing-function-docstring",
            ]

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.pylint
        data.disable += ["too-few-public-methods", "no-self-use"]
        data.good_names += ["t", "dt"]

    def bake(self) -> None:
        super().bake()
        # ensure python version
        found_version = ".".join(map(str, sys.version_info[:2]))
        if found_version != self.auxcon.project.minimal_version:
            raise RuntimeError(
                f"you are using python {found_version}, please use python {self.auxcon.project.minimal_version} (minimal version)."
            )

        x = subprocess.run(
            ["pylint", "--generate-rcfile"], capture_output=True, check=True
        )
        text = x.stdout.decode()

        hooks = self.auxcon.pre_commit.hooks
        configs = [ConfigParser.read_string(text)]
        keys = ["pylint"]
        writeout = ["pylint" in hooks]

        writeout.append("pylint-test" in hooks)
        if writeout[-1]:
            keys.append("pylint-test")

        for i, key in enumerate(keys):
            config = configs[-1]
            if i > 0:
                config = copy.deepcopy(config)
                configs.append(config)

            key = key.replace("-", "_")
            for key1, key2, key3 in [
                ("MESSAGES CONTROL", "disable", "disable"),
                ("BASIC", "good-names", "good_names"),
                ("SIMILARITIES", "min-similarity-lines", "min_similarity_lines"),
                ("BASIC", "variable-rgx", "variable_rgx"),
                ("BASIC", "const-rgx", "const_rgx"),
                ("BASIC", "function-rgx", "function_rgx"),
                ("BASIC", "argument-rgx", "argument_rgx"),
                ("BASIC", "class-rgx", "class_rgx"),
                ("BASIC", "method-rgx", "method_rgx"),
                ("BASIC", "attr-rgx", "attr_rgx"),
                ("BASIC", "class-attribute-rgx", "class_attr_rgx"),
            ]:
                subconfig = config[key1]
                data = self.auxcon[key]
                if key2 in ["good-names", "disable"]:
                    proplist = copy.copy(subconfig[key2])
                    for x in data[key3]:
                        proplist[-1] += ","
                        if x in proplist:
                            raise RuntimeError(f"{x} is already marked {key3}")
                        proplist.append(x)
                    subconfig[key2] = proplist
                else:
                    if key3 in data:
                        subconfig[key2] = data[key3]

            config["SIMILARITIES"]["ignore-imports"] = "yes"

        for key, config, wout in zip(keys, configs, writeout):
            if not wout:
                continue
            dest = self.target / f"pre-commit/{key}rc"
            written = ConfigParser.write(config, dest)
            if written:
                self._print(f"baked {dest}", fg="green")
