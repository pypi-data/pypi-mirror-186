# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
# type: ignore
import ruamel.yaml

__all__ = ["yaml", "CommentedMap", "CommentedSeq"]

CommentedMap = ruamel.yaml.comments.CommentedMap
CommentedSeq = ruamel.yaml.comments.CommentedSeq

yaml = ruamel.yaml.YAML()
yaml.indent = 4
yaml.width = 3000
yaml.preserve_quotes = True
