"""
Primary interface class
"""

from pathlib import Path
from typing import Any, Callable
from pyeio.builder import IO


class EIO:
    def __init__(self) -> None:
        self.io = IO()

    def load(self, path: str | Path, astype: Callable | None = None) -> Any:
        """
        Description

        Args:
            path (str | Path): _description_
            form (str, optional): _description_. Defaults to "auto".

        Returns:
            Any: _description_
        """
        file_format = self.io.query.file_format(path)
        assert file_format in self.io.formats, "unsupported file format"
        data = self.io._id[file_format]["load"](path)
        if astype is None:
            return data
        else:
            return astype(data)

    def save(self, data: Any, path: str | Path) -> None:
        """
        Description

        Args:
            data (Any): _description_
            path (str | Path): _description_

        Notes:
            - Auto detects save type based on file extension.
        """
        target = self.io.query.file_format(path)
        assert target in self.io.formats, "unsupported file format"
        kind = self.io.query.data_type(data)
        assert self.io.transform.valid(target, kind), "invalid target format"
        data = self.io.transform._td[target][kind](data)
        self.io._id[target]["save"](data, path)
