import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class DevelopmentStorage:
    
    _path: str = f"/Users/georgekibe/Desktop/Projects/Dowell/legalzard_backend/vol/web"
    #_path: str = f"/home/george/Dowell/legalzard-backend/vol/web"

    def __str__(self) -> str:
        return f"{self._path}"

    @classmethod
    def get_path(cls):
        return f"{cls._path}"


class ProductionStorage:
    _path: str = f"/home/100080/100080-dowelllegalzard/vol/web"

    def __str__(self) -> str:
        return f"{self._path}"

    @classmethod
    def get_path(cls):
        return f"{cls._path}"


def get_storage_path(debug) -> str:
    return DevelopmentStorage.get_path() if debug else ProductionStorage.get_path()
