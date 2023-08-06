import logging
import os
import warnings
from pathlib import Path
from typing import Optional, Union

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.types.schemas import LoggingFileSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class LoggingFile(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)
        self.text = ""

    def __str__(self):
        return f"{Colors.GREEN}Logging file {self.object_name}{Colors.ENDC} (id: {self.id})"

    @property
    def object_name(self) -> str:
        """Object name of this (LoggingFile)"""
        return self._object_name

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> LoggingFileSchema:
        schema = LoggingFileSchema(**data)
        self._object_name = schema.object_name
        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/logging/file/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(
        self,
        object_name: Optional[str] = None,
    ) -> None:
        """Update this artifact.

        Examples:
            ```python
            this_artifact.update(object_name="another-path-to-artifact")
            ```
        """
        payload = {
            "object_name": object_name,
        }
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            f"/sdk/logging/file/{self.id}", data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this artifact

        Examples:
            ```python
            this_artifact.delete()
            ```
        """
        self.connexion.delete(f"/sdk/logging/file/{self.id}")

    @exception_handler
    @beartype
    def download(
        self, target_path: Union[str, Path] = "./", force_replace: bool = False
    ) -> None:
        """Download an experiment logging file to a given target_path.

        Examples:
            ```python
            logging_file.download("myDir")
            file_list = os.path.listdir("myDir")
            print(file_list)
            >>> ["saved_model.zip"]
            ```
        Arguments:
            force_replace: (bool, optional): If true, force replacement of existing disk file. Defaults to false.
            target_path (str or Path, optional): Path to download the file to, default to cwd. Defaults to './'.

        """
        self.sync()
        filename = self.object_name.split("/")[-1]
        path = os.path.join(target_path, filename)
        if self.connexion.download_file(
            self.object_name, path, False, force_replace=force_replace
        ):
            logger.info(f"{filename} downloaded successfully")
        else:  # pragma: no cover
            logger.error(f"Did not download logging file of {self}")
