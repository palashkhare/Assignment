import os
from pathlib import Path

from werkzeug.datastructures import FileStorage

from app.core.interfaces import FilestorageInterface


class FilestorageAdapter(FilestorageInterface):

    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        if not self.base_dir.exists():
            os.mkdir(self.base_dir)

    def list_all(self, ):
        return os.listdir(self.base_dir)

    def read_text(self, ):
        return self.base_dir.read_text(encoding="utf-8")

    def save(self, file: FileStorage, path: str, overwrite: bool = False):
        path = self.base_dir.joinpath(path)
        if path.exists() and not overwrite:
            raise FileExistsError
        file.save(path)

    def write_text(self, content: str, path: str, ):
        path: Path = self.base_dir.joinpath(path)
        path.write_text(data=content, encoding="utf-8")
