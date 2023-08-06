import logging
import os
from pathlib import Path
from typing import Union

from beartype import beartype

from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import ModelFileSchema

logger = logging.getLogger("picsellia")


class ModelFile(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    @property
    def name(self) -> str:
        """Name of this (ModelFile)"""
        return self._name

    @property
    def object_name(self) -> str:
        """Object name of this (ModelFile)"""
        return self._object_name

    @property
    def filename(self) -> str:
        """Filename of this (ModelFile)"""
        return self._filename

    @property
    def large(self) -> bool:
        """If True, this (ModelFile) is considered having a large size"""
        return self._large

    def __str__(self):
        return (
            f"{Colors.BLUE}Model file named '{self.name}'{Colors.ENDC} (id: {self.id})"
        )

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/model/file/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ModelFileSchema:
        schema = ModelFileSchema(**data)
        self._name = schema.name
        self._object_name = schema.object_name
        self._filename = schema.filename
        self._large = schema.large
        return schema

    @exception_handler
    @beartype
    def download(
        self, target_path: Union[str, Path] = "./", force_replace: bool = False
    ) -> None:
        """Download file stored.

        Examples:
            ```python
            latest_cp = model.get_file("model-latest")
            latest_cp.download("./files/")
            ```
        Arguments:
            target_path (str or Path, optional): Directory path where file will be downloaded
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.
        """
        self.sync()
        path = os.path.join(target_path, self.filename)
        if self.connexion.download_file(
            self.object_name, path, self.large, force_replace=force_replace
        ):
            logger.info(f"{self.filename} downloaded successfully")
        else:  # pragma: no cover
            logger.warning(f"Did not download file '{self.filename}'")

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this file

        Examples:
            ```python
            model_file.delete()
            ```
        """
        self.connexion.delete(f"/sdk/model/file/{self.id}")
        logger.info(f"{self} deleted from platform.")
