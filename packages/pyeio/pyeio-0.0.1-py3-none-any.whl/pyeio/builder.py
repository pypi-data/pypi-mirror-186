"""
Data format IO builder classes
"""

from pathlib import Path
import json
from typing import Any


class Query:
    @staticmethod
    def file_name(path: str | Path) -> str:
        "get file name from path"
        return str(path).split("/")[-1]

    @staticmethod
    def file_format(path: str | Path) -> str:
        "get file format from path"
        return Query.file_name(path).split(".")[-1]

    @staticmethod
    def file_size(path: str | Path) -> int:
        "get file size in bytes from path"
        raise NotImplementedError()

    @staticmethod
    def data_type(obj: Any) -> str:
        "get object type as string"
        return str(type(obj)).split("'")[-2]


class Transform:
    def __init__(self) -> None:
        self.__init_transform_dict()

    def __init_transform_dict(self) -> None:
        self._td = {
            "json": {
                "list": list,
                "dict": dict,
                "pandas.core.series.Series": list,
                "pandas.core.frame.DataFrame": lambda x: x.to_dict(orient="list"),
            }
        }

    def valid(self, target_format: str, data_type: str) -> bool:
        return data_type in self._td[target_format]


class IO:
    def __init__(self):
        self.__init_utility_subclasses()
        self.__init_interface_subclasses()
        self.__init_interface_dict()

    def __init_utility_subclasses(self) -> None:
        self.query = Query()
        self.transform = Transform()

    def __init_interface_subclasses(self) -> None:
        self.json = JSON()
        self.csv = CSV()
        self.xlsx = XLSX()
        self.yaml = YAML()
        self.toml = TOML()

    def __init_interface_dict(self) -> None:
        self._id = {"json": {"save": self.json.save, "load": self.json.load}}

    @property
    def formats(self) -> set[str]:
        return set(self._id.keys())


class JSON:
    @staticmethod
    def load(path: str | Path) -> dict | list:
        with open(path, "r") as file:
            data = json.load(file)
        file.close()
        return data

    @staticmethod
    def save(data: dict | list, path: str | Path) -> None:
        with open(path, "w") as file:
            file.write(json.dumps(data, indent=4))
        file.close()


class CSV:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class XLSX:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class YAML:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class TOML:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class ZIP:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class BIN:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class NULL:
    "no extension, assumed binary or text file"

    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class PY:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class JS:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class GRAPHML:
    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass


class SZ:
    "7 zip, can't start class name with number"

    @staticmethod
    def load(path: str | Path) -> Any:
        pass

    @staticmethod
    def save(data: Any, path: str | Path) -> None:
        pass
