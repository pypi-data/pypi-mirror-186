"""
Primary interface class
"""

from pathlib import Path
from typing import Any, Callable
from pyeio.builder import IO, Utility


class EIO:
    def __init__(self) -> None:
        self.io = IO()
        self.util = Utility()

    def load(self, path: str | Path, astype: Callable | None = None) -> Any:
        """
        Description

        Args:
            path (str | Path): _description_
            form (str, optional): _description_. Defaults to "auto".

        Returns:
            Any: _description_
        """
        file_format = self.util.get_file_format(path)
        assert file_format in self.io.formats, "unsupported file format"
        data = self.io.interface[file_format]["load"](path)
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
        target_format = self.util.get_file_format(path)
        assert target_format in self.io.formats, "unsupported file format"
