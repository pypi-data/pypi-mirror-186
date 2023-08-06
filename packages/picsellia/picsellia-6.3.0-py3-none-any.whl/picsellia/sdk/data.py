import logging
import os
import warnings
from functools import partial
from operator import countOf
from pathlib import Path
from typing import List, Optional, Union
from uuid import UUID

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from picsellia import exceptions as exceptions
from picsellia import pxl_multithreading as mlt
from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.multi_object import MultiObject
from picsellia.sdk.tag import Tag, TagTarget
from picsellia.sdk.taggable import Taggable
from picsellia.types.enums import DataType
from picsellia.types.schemas import DataSchema, ImageSchema, VideoSchema

from .datasource import DataSource

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Data(Dao, Taggable):
    def __init__(self, connexion: Connexion, datalake_id: UUID, data: dict):
        Dao.__init__(self, connexion, data)
        Taggable.__init__(self, TagTarget.DATA)
        self._datalake_id = datalake_id

    def __str__(self):
        return f"{Colors.GREEN}Data{Colors.ENDC} object (id: {self.id})"

    @property
    def datalake_id(self) -> UUID:
        """UUID of (Datalake) where this (Data) is"""
        return self._datalake_id

    @property
    def object_name(self) -> str:
        """Object name of this (Data)"""
        return self._object_name

    @property
    def filename(self) -> str:
        """Filename of this (Data)"""
        return self._filename

    @property
    def type(self) -> DataType:
        """Type of this (Data)"""
        return self._type

    @property
    def width(self) -> int:
        """Width of this (Data)"""
        if self.type == DataType.IMAGE:
            return self._width
        else:
            return 0

    @property
    def height(self) -> int:
        """Height of this (Data) if this is an Image."""
        if self.type == DataType.IMAGE:
            return self._height
        else:
            return 0

    @property
    def duration(self) -> int:
        """Duration of this (Data) if this is a Video."""
        if self.type == DataType.VIDEO:
            return self._duration
        else:
            return 0

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        if data["type"] == DataType.IMAGE.value:
            schema = ImageSchema(**data)
        elif data["type"] == DataType.VIDEO.value:
            schema = VideoSchema(**data)
        else:
            schema = DataSchema(**data)

        self._object_name = schema.object_name
        self._filename = schema.filename
        self._type = schema.type

        if schema.type == DataType.IMAGE:
            self._height = schema.meta.height
            self._width = schema.meta.width
        elif schema.type == DataType.VIDEO:
            self._duration = schema.meta.duration

        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/data/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def get_tags(self) -> List[Tag]:
        """Retrieve the tags of your data.

        Examples:
            ```python
            tags = data.get_tags()
            assert tags[0].name == "bicycle"
            ```

        Returns:
            List of tags as Tag
        """
        r = self.sync()
        return list(map(partial(Tag, self.connexion), r["tags"]))

    @exception_handler
    @beartype
    def get_datasource(self) -> Optional[DataSource]:
        r = self.sync()
        if "data_source" not in r or r["data_source"] is None:
            return None

        return DataSource(self.connexion, r["data_source"])

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete data and remove it from datalake.

        :warning: **DANGER ZONE**: Be very careful here!

        Remove this data from datalake, and all assets linked to this data.

        Examples:
            ```python
            data.delete()
            ```
        """
        response = self.connexion.delete(f"/sdk/data/{self.id}")
        assert response.status_code == 204
        logger.info(f"1 data (id: {self.id}) deleted from datalake {self.datalake_id}.")

    @exception_handler
    @beartype
    def download(
        self, target_path: Union[str, Path] = "./", force_replace: bool = False
    ) -> None:
        """Download this data file into given target_path

        Examples:
            ```python
            data = clt.get_datalake().fetch_data(1)
            data.download('./data/')
            ```

        Arguments:
            target_path (str, optional): Target path where data will be downloaded. Defaults to './'.
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.
        """
        data = self.sync()
        path = os.path.join(target_path, self.filename)
        if self.connexion.do_download_file(
            path, data["presigned_url"], is_large=True, force_replace=force_replace
        ):
            logger.info(f"{self.filename} downloaded successfully")
        else:
            logger.error(f"Did not download file '{self.filename}'")


class MultiData(MultiObject[Data], Taggable):
    @beartype
    def __init__(self, connexion: Connexion, datalake_id: UUID, items: List[Data]):
        MultiObject.__init__(self, connexion, items)
        Taggable.__init__(self, TagTarget.DATA)
        self.datalake_id = datalake_id

    def __str__(self) -> str:
        return f"{Colors.GREEN}MultiData for datalake {self.datalake_id} {Colors.ENDC}, size: {len(self)}"

    def __getitem__(self, key) -> Union[Data, "MultiData"]:
        if isinstance(key, slice):
            indices = range(*key.indices(len(self.items)))
            data = [self.items[i] for i in indices]
            return MultiData(self.connexion, self.datalake_id, data)
        return self.items[key]

    @beartype
    def __add__(self, other) -> "MultiData":
        self.assert_same_connexion(other)
        items = self.items.copy()
        if isinstance(other, MultiData):
            items.extend(other.items.copy())
        elif isinstance(other, Data):
            items.append(other)
        else:
            raise exceptions.BadRequestError("You can't add these two objects")

        return MultiData(self.connexion, self.datalake_id, items)

    @beartype
    def __iadd__(self, other) -> "MultiData":
        self.assert_same_connexion(other)

        if isinstance(other, MultiData):
            self.extend(other.items.copy())
        elif isinstance(other, Data):
            self.append(other)
        else:
            raise exceptions.BadRequestError("You can't add these two objects")

        return self

    def copy(self) -> "MultiData":
        return MultiData(self.connexion, self.datalake_id, self.items.copy())

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete a bunch of data and remove them from datalake.

        :warning: **DANGER ZONE**: Be very careful here!

        Remove a bunch of data from datalake, and all assets linked to each data.

        Examples:
            ```python
            whole_data = datalake.fetch_data(quantity=3)
            whole_data.delete()
            ```
        """
        payload = self.ids
        self.connexion.delete(
            f"/sdk/datalake/{self.datalake_id}/datas",
            data=orjson.dumps(payload),
        )
        logger.info(f"{len(self.items)} data deleted from datalake {self.datalake_id}.")

    @exception_handler
    @beartype
    def download(
        self,
        target_path: Union[Path, str] = "./",
        force_replace: bool = False,
        max_workers: int = 20,
    ) -> None:
        """Download this multi data in given target path


        Examples:
            ```python
            bunch_of_data = client.get_datalake().fetch_data(25)
            bunch_of_data.download('./downloads/')
            ```
        Arguments:
            target_path (str or Path, optional): Target path where to download. Defaults to './'.
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.
            max_workers (int, optional): Number of threads used to download. Defaults to 20.
        """

        def download_one_data(item: Data):
            data = item.sync()
            path = os.path.join(target_path, item.filename)
            return self.connexion.do_download_file(
                path, data["presigned_url"], is_large=True, force_replace=force_replace
            )

        results = mlt.do_mlt_function(
            self.items, download_one_data, lambda item: item.id, max_workers=max_workers
        )
        downloaded = countOf(results.values(), True)

        logger.info(
            f"{downloaded} data downloaded (over {len(results)}) in directory {target_path}"
        )
