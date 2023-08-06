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
from picsellia.types.schemas import ArtifactSchema
from picsellia.utils import filter_payload

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Artifact(Dao):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    def __str__(self):
        return f"{Colors.GREEN}Artifact {self.name}{Colors.ENDC} (id: {self.id})"

    @property
    def filename(self) -> str:
        """Filename of this (Artifact)"""
        return self._filename

    @property
    def large(self) -> bool:
        """If true, this (Artifact) has a large size"""
        return self._large

    @property
    def name(self) -> str:
        """(Artifact) name"""
        return self._name

    @property
    def object_name(self) -> str:
        """(Artifact) object name stored in storage"""
        return self._object_name

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> ArtifactSchema:
        schema = ArtifactSchema(**data)
        self._name = schema.name
        self._object_name = schema.object_name
        self._large = schema.large
        self._filename = schema.filename
        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/artifact/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(
        self,
        name: Optional[str] = None,
        filename: Optional[str] = None,
        object_name: Optional[str] = None,
        large: Optional[bool] = None,
    ) -> None:
        """Update this artifact.

        Examples:
            ```python
            this_artifact.update(object_name="another-path-to-artifact")
            ```
        """
        payload = {
            "name": name,
            "filename": filename,
            "object_name": object_name,
            "large": large,
        }
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            f"/sdk/artifact/{self.id}", data=orjson.dumps(filtered_payload)
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
        self.connexion.delete(f"/sdk/artifact/{self.id}")

    @exception_handler
    @beartype
    def download(
        self, target_path: Union[str, Path] = "./", force_replace: bool = False
    ) -> None:
        """Download an experiment's artifact to a given target_path.

        Examples:
            ```python
            this_artifact.download("myDir")
            file_list = os.path.listdir("myDir")
            print(file_list)
            >>> ["saved_model.zip"]
            ```
        Arguments:
            target_path (str or Path, optional): Path to download the file to, default to cwd. Defaults to './'.
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.

        """
        self.sync()
        path = os.path.join(target_path, self.filename)
        if self.connexion.download_file(
            self.object_name, path, self.large, force_replace=force_replace
        ):
            logger.info(f"{self.filename} downloaded successfully")
        else:  # pragma: no cover
            logger.error(f"Did not download file '{self.name}' ({self.filename})")
