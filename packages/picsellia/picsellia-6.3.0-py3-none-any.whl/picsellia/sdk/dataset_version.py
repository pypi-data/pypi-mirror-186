import logging
import os
import random
import warnings
from functools import partial
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from uuid import UUID

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from picsellia_annotations.coco import COCOFile
from picsellia_annotations.exceptions import FileError, ParsingError
from picsellia_annotations.utils import read_coco_file, read_pascal_voc_file
from picsellia_annotations.voc import Object, PascalVOCFile

import picsellia.pxl_multithreading as mlt
from picsellia import exceptions
from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.exceptions import (
    DownloadError,
    FileNotFoundException,
    NoDataError,
    PicselliaError,
    ResourceNotFoundError,
    UnparsableAnnotationFileException,
)
from picsellia.sdk.annotation import Annotation, MultiAnnotation
from picsellia.sdk.asset import Asset, MultiAsset
from picsellia.sdk.classification import Classification
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.data import Data, MultiData
from picsellia.sdk.label import Label
from picsellia.sdk.polygon import Polygon
from picsellia.sdk.rectangle import Rectangle
from picsellia.sdk.tag import Tag, TagTarget
from picsellia.sdk.taggable import Taggable
from picsellia.sdk.worker import Worker
from picsellia.types.enums import (
    AnnotationFileType,
    AnnotationStatus,
    ImportAnnotationMode,
    InferenceType,
)
from picsellia.types.schemas import DatasetVersionSchema
from picsellia.utils import (
    combine_two_ql,
    convert_tag_list_to_query_language,
    filter_payload,
)

from .job import Job

warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)
logger = logging.getLogger("picsellia")


class DatasetVersion(Dao, Taggable):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)
        Taggable.__init__(self, TagTarget.DATASET_VERSION)

    @property
    def origin_id(self) -> UUID:
        """UUID of the (Dataset) origin"""
        return self._origin_id

    @property
    def name(self) -> str:
        """Name of the (Dataset) origin"""
        return self._name

    @property
    def version(self) -> str:
        """Version of this (DatasetVersion)"""
        return self._version

    @property
    def type(self) -> InferenceType:
        """Type of this (DatasetVersion)"""
        return self._type

    def __str__(self):
        return f"{Colors.YELLOW}Version '{self.version}' of dataset {self.name} {Colors.ENDC} (id: {self.id})"

    @exception_handler
    @beartype
    def get_resource_url_on_platform(self) -> str:
        """Get platform url of this resource.

        Examples:
            ```python
            print(foo_dataset.get_resource_url_on_platform())
            >>> "https://app.picsellia.com/dataset/62cffb84-b92c-450c-bc37-8c4dd4d0f590"
            ```

        Returns:
            Url on Platform for this resource
        """

        return f"{self.connexion.host}/dataset/version/{self.id}"

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        schema = DatasetVersionSchema(**data)
        self._name = schema.name
        self._version = schema.version
        self._type = schema.type
        self._origin_id = schema.origin_id
        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/dataset/version/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def get_tags(self) -> List[Tag]:
        """Retrieve tags of your dataset version.

        Examples:
            ```python
            tags = foo_dataset_version.get_tags()
            assert tags[0].name == "training-dataset"
            ```

        Returns:
            List of (Tag) objects
        """
        r = self.sync()
        return list(map(partial(Tag, self.connexion), r["tags"]))

    @exception_handler
    @beartype
    def add_data(
        self,
        data: Union[Data, List[Data], MultiData],
        tags: Optional[List[Union[str, Tag]]] = None,
    ) -> Job:
        """Feed this version with data coming from a datalake.

        A versioned dataset (DatasetVersion) takes (Data) from (Datalake) and transform it as annotable (Asset).
        You can give tags that will be added as asset tags to every created asset.

        Examples:
            ```python
            foo_dataset = client.create_dataset('foo_dataset')
            foo_dataset_version_1 = foo_dataset.create_version('first')
            some_data = client.get_datalake().list_data(limit=1000)
            foo_dataset_version_1.add_data(some_data)
            ```

        Arguments:
            data ((Data), List[(Data)] or (MultiData)): data to add to dataset
            tags (List of str or Tag) : tags to add to every asset created
        """
        if isinstance(data, Data):
            payload = {"data_ids": [data.id]}
        else:
            payload = {"data_ids": [data.id for data in data]}

        assert payload["data_ids"] != [], "Please specify the assets to add to dataset"

        asset_tag_ids = set()
        asset_tag_names = set()
        if tags:
            for tag in tags:
                tag_name = tag.name if isinstance(tag, Tag) else tag
                tag_created = self.get_or_create_asset_tag(tag_name)
                asset_tag_ids.add(tag_created.id)
                asset_tag_names.add(tag_created.name)

        payload["asset_tag_ids"] = list(asset_tag_ids)

        r = self.connexion.post(
            f"/sdk/dataset/version/{self.id}/assets", data=orjson.dumps(payload)
        ).json()
        self.refresh(r["dataset_version"])
        logger.info(
            f"Data are being added as assets to {self}.\n"
            "This operation can take some time (depending on how much asset you're adding)."
        )
        if asset_tag_names:
            tag_names = ", ".join(asset_tag_names)
            logger.info(f"Each asset created will have tags: {tag_names}")
        return Job(self.connexion, r["job"])

    @exception_handler
    @beartype
    def fork(
        self,
        version: str,
        description: Optional[str] = None,
        assets: Union[List[Asset], MultiAsset, Asset, None] = None,
        type: Union[InferenceType, str] = InferenceType.NOT_CONFIGURED,
        with_tags: bool = False,
    ) -> Tuple["DatasetVersion", Job]:
        """Fork this dataset version into another dataset version, with the same origin.

        Will create a new dataset version, with the same origin and the given version.
        You can give a description and a default type.
        You can give a list of asset coming from this dataset version to add into the new dataset version.
        Only these assets will be added to the new dataset.
        If with_tags is True, tags of each asset will be transferred to the new dataset version.

        Examples:
            ```python
            foo_dataset_version = client.get_dataset('my_datatest').get_version('first')
            assets = foo_dataset_version.list_assets(limit=100)
            bar_dataset_version = foo_dataset_version.fork('second', assets)
            ```

        Arguments:
            version (str): new version name
            description (str): description, defaults to "Forked from version '<version_name>'"
            assets ((MultiAsset) or (Asset)): assets to add to the new dataset version, defaults will be all assets
            type (InferenceType): inference type of the new dataset version, defaults to NOT_CONFIGURED
            with_tags (bool): if true tags of assets will be added to the new dataset version, defaults to false

        Returns:
            A (DatasetVersion) with given assets
        """
        type = InferenceType.validate(type)

        if version == "":
            raise ValueError("Version name can't be empty")

        if description is None:
            description = f"Fork from {self.version}"

        payload = {
            "parent_id": self.id,
            "version": version,
            "description": description,
            "type": type,
            "with_tags": with_tags,
        }

        if assets is not None:
            if isinstance(assets, Asset):
                assets: List[Asset] = [assets]
            payload["asset_ids"] = [asset.id for asset in assets]

        r = self.connexion.post(
            f"/sdk/dataset/{self.origin_id}/fork", data=orjson.dumps(payload)
        ).json()
        logger.info(
            f"{self} forked with {len(assets) if assets is not None else 'all'} assets"
        )
        return DatasetVersion(self.connexion, r["dataset_version"]), Job(
            self.connexion, r["job"]
        )

    @exception_handler
    @beartype
    def find_asset(
        self,
        data: Optional[Data] = None,
        filename: Optional[str] = None,
        object_name: Optional[str] = None,
    ) -> Asset:
        """Find an asset into this dataset version

        You can find it by giving its supposed Data object, its filename or its object name

        Examples:
            ```python
            my_asset = my_dataset_version.find_asset(filename="test.png")
            ```
        Arguments:
            data (Data, optional): data linked to asset. Defaults to None.
            filename (str, optional): filename of the asset. Defaults to None.
            object_name (str, optional): object name in the storage S3. Defaults to None.

        Raises:
            If no asset match the query, it will raise a NotFoundError.
            In some case, it can raise an InvalidQueryError,
                it might be because platform stores 2 assets matching this query (for example if filename is duplicated)

        Returns:
            The (Asset) found
        """
        assert not (
            data is None and filename is None and object_name is None
        ), "Select at least one criteria to find an asset"

        params = {}
        if data is not None:
            params["data_id"] = data.id

        if filename is not None:
            params["filename"] = filename

        if object_name is not None:
            params["object_name"] = object_name

        r = self.connexion.get(
            f"/sdk/dataset/version/{self.id}/assets/find", params=params
        ).json()
        return Asset(self.connexion, self.id, r)

    @exception_handler
    @beartype
    def find_all_assets(
        self,
        filenames: Optional[List[str]] = None,
        object_names: Optional[List[str]] = None,
    ) -> MultiAsset:
        """Find some assets of this dataset version from their filenames

        Examples:
            ```python
            my_asset = my_dataset_version.find_all_assets(filenames=["test.png", "image2.jpg"])
            ```
        Arguments:
            filenames (List[str]): filenames of the assets you're looking for. Defaults to None.
            object_names (List[str]): object names of the assets you're looking for. Defaults to None.

        Returns:
            A list of (Asset) found
        """
        payload = {}
        if filenames is not None:
            payload["filenames"] = filenames

        if object_names is not None:
            payload["object_names"] = object_names

        assert payload != {}, "Can't search with nothing"

        r = self.connexion.xget(
            f"/sdk/dataset/version/{self.id}/assets", data=orjson.dumps(payload)
        ).json()
        assets = list(map(partial(Asset, self.connexion, self.id), r["items"]))

        if len(assets) == 0:
            raise NoDataError("No asset found")

        return MultiAsset(self.connexion, self.id, assets)

    @exception_handler
    @beartype
    def list_assets(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        tags: Union[Tag, List[Tag], str, List[str], None] = None,
        data_tags: Union[Tag, List[Tag], str, List[str], None] = None,
        intersect_tags: bool = False,
        intersect_data_tags: bool = False,
    ) -> MultiAsset:
        """List assets of this dataset version

        It will retrieve all assets object of this dataset.
        You will then be able to manipulate them or add them to another dataset.

        Examples:
            ```python
            assets = foo_dataset_version.list_assets()
            ```

        Arguments:
            limit (int): limit to a certain number of assets
            offset (int): offset to access some new objects, if 0 will retrieve starting from the beginning
            page_size (int): page size when paginating.
            order_by (str): a list of string to use for sorting data, if None will not sort
            tags (str, (Tag), list[(Tag) or str], optional): if given, will return assets that have one of given tags
                                                            by default. if `intersect_tags` is True,
                                                            it will return assets that have all the given tags
            intersect_tags (bool, optional): if True, and a list of tags is given, will return assets that have
                                             all the given tags. Defaults to False.
            data_tags (str, (Tag), list[(Tag) or str], optional): if given, will return assets that have one of given
                                                            data tags by default. if `intersect_data_tags` is True,
                                                            it will return assets that have all the given data tags
            intersect_data_tags (bool, optional): if True, and a list of data tags is given, will return assets that have
                                             all the given data tags. Defaults to False.
        Returns:
            A (MultiAsset) object that wraps some (Asset) that you can manipulate.
        """
        qt = convert_tag_list_to_query_language(tags, intersect_tags)
        qd = convert_tag_list_to_query_language(
            data_tags, intersect_data_tags, prefix="data."
        )
        q = combine_two_ql(qt, qd)

        assets = mlt.do_paginate(
            limit, offset, page_size, partial(self._do_list_assets, q, order_by)
        )

        if len(assets) == 0:
            raise NoDataError("No asset retrieved")

        return MultiAsset(self.connexion, self.id, assets)

    @exception_handler
    @beartype
    def _do_list_assets(
        self, q: Optional[str], order_by: Optional[List[str]], limit: int, offset: int
    ) -> Tuple[List[Asset], int]:
        params = {"limit": limit, "offset": offset}
        if order_by is not None:
            params["order_by"] = order_by
        if q is not None:
            params["q"] = q

        r = self.connexion.get(
            f"/sdk/dataset/version/{self.id}/assets", params=params
        ).json()
        return (
            list(map(partial(Asset, self.connexion, self.id), r["items"])),
            r["count"],
        )

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete a dataset version.

        :warning: **DANGER ZONE**: Be very careful here!

        It will remove this dataset version from our database, all of its assets and annotations will be removed.

        Examples:
            ```python
            foo_dataset_version.delete()
            ```
        """
        self.connexion.delete(f"/sdk/dataset/version/{self.id}")
        logger.info(f"{self} deleted")

    @exception_handler
    @beartype
    def set_type(self, type: Union[str, InferenceType]) -> None:
        """Set type of Dataset.

        Examples:
            ```python
            dataset.set_type('detection')
            ```
        """
        payload = {"type": InferenceType.validate(type)}
        r = self.connexion.patch(
            f"/sdk/dataset/version/{self.id}", data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info(f"{self} is now of type {type.name}")

    @exception_handler
    @beartype
    def update(
        self,
        version: Optional[str] = None,
        description: Optional[str] = None,
        type: Union[str, InferenceType, None] = None,
    ) -> None:
        """Update version, description and type of a Dataset.

        Examples:
            ```python
            dataset.update(description='My favourite dataset')
            ```
        """
        payload = {"version": version, "description": description}
        if type:
            payload["type"] = InferenceType.validate(type)
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            f"/sdk/dataset/version/{self.id}",
            data=orjson.dumps(filtered_payload),
        ).json()
        self.refresh(r)
        logger.info(f"{self} updated")

    @exception_handler
    @beartype
    def download(
        self,
        target_path: Union[str, Path, None] = None,
        force_replace: bool = False,
        max_workers: int = 20,
    ) -> None:
        """Downloads assets of a dataset.

        It will download all assets from a dataset into specified folder.
        If target_path is None, it will download into ./<dataset_name>/<dataset_version>
        You can precise a number of threads to use while downloading.

        Examples:
            ```python
            foo_dataset.download('~/Downloads/dataset_pics')
            ```
        Arguments:
            target_path (str or Path, optional): Target folder. Defaults to None.
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.
            max_workers (int, optional): Number of threads to use. Defaults to 20.
        """
        if target_path is not None:
            path = target_path
        else:
            path = os.path.join("./", self.name, self.version)

        Path(path).mkdir(parents=True, exist_ok=True)

        logger.debug(f"Retrieving assets of {self}...")
        multi_data = self.list_assets().as_multidata()

        logger.debug("Downloading assets...")
        multi_data.download(path, force_replace, max_workers)

        logger.info(f"Assets of {self} downloaded into {path}")

    @exception_handler
    @beartype
    def list_labels(self) -> List[Label]:
        """Get all labels of a dataset

        It will retrieve a list of label objects.

        Examples:
            ```python
            foo_dataset.create_label("today")
            labels = foo_dataset.get_labels()
            assert labels[0].name == "today"
            ```

        Returns:
            List of (Label)
        """
        r = self.connexion.get(f"/sdk/dataset/version/{self.id}/labels").json()
        return list(map(partial(Label, self.connexion), r["items"]))

    @exception_handler
    @beartype
    def create_label(self, name: str) -> Label:
        """Add label to a dataset version.

        You have to give a name to the label.

        Examples:
            ```python
            foo_dataset.create_label("today")
            ```
        Arguments:
            name (str): label name to add

        Returns:
            A (Label) object
        """

        payload = {"name": name}
        r = self.connexion.post(
            f"/sdk/dataset/version/{self.id}/labels", data=orjson.dumps(payload)
        ).json()
        label = Label(self.connexion, r)
        logger.info(f"{label} has been added to {self}")
        return label

    @exception_handler
    @beartype
    def get_label(self, name: str) -> Label:
        """Find label in a dataset version.

        Examples:
            ```python
            label = foo_dataset.get_label("today")
            ```
        Arguments:
            name (str): label name to find

        Returns:
            A (Label) object
        """

        params = {"name": name}
        r = self.connexion.get(
            f"/sdk/dataset/version/{self.id}/labels/find", params=params
        ).json()
        return Label(self.connexion, r)

    @exception_handler
    @beartype
    def get_or_create_label(self, name: str) -> Label:
        """Retrieve a label used in this dataset by its name.
        If label does not exist, create it and return it.

        Examples:
            ```python
            label = self.get_or_create_label("new_label")
            ```
        Arguments:
            name (str): label to retrieve or create

        Returns:
            A (label) object
        """
        try:
            return self.get_label(name)
        except ResourceNotFoundError:
            return self.create_label(name)

    @exception_handler
    @beartype
    def list_annotations(
        self,
        worker: Optional[Worker] = None,
        status: Union[AnnotationStatus, str, None] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        page_size: Optional[int] = None,
    ) -> MultiAnnotation:
        """Retrieve annotations of a dataset.

        Examples:
            ```python
            annotations = foo_dataset.list_annotations()
            ```
        Arguments:
            limit (Optional[int], optional): Limit number of annotations to retrieve.
                Defaults to None, all annotations will be retrieved.
            offset (Optional[int], optional): Offset to begin with when listing annotations.
                Defaults to None, starting at 0.
            page_size (Optional[int], optional): Size of each page when retrieving .
                Defaults to None, page will be equals to default pagination.
            order_by (Optional[List[str]], optional): Order annotation by some criteria.
                Defaults to None.
            worker (Optional[Worker], optional): Worker filter.
                Defaults to None.
            status (Optional[AnnotationStatus], optional): Status of annotations to retrieve.
                Defaults to None.

        Raises:
            NoDataError: When no annotations retrieved

        Returns:
            A (MultiAnnotation) object
        """
        if status:
            status = AnnotationStatus.validate(status)

        annotations = mlt.do_paginate(
            limit,
            offset,
            page_size,
            partial(self._do_list_annotations, status, worker, order_by),
        )

        if len(annotations) == 0:
            raise NoDataError("No annotation retrieved")

        return MultiAnnotation(self.connexion, self.id, annotations)

    def _do_list_annotations(
        self,
        status: Optional[AnnotationStatus],
        worker: Optional[Worker],
        order_by: Optional[List[str]],
        limit: int,
        offset: int,
    ) -> Tuple[List[Annotation], int]:
        params = {"limit": limit, "offset": offset}
        if order_by is not None:
            params["order_by"] = order_by
        if worker is not None:
            params["worker_id"] = worker.id
        if status is not None:
            params["status"] = status.value

        r = self.connexion.get(
            f"/sdk/dataset/version/{self.id}/annotations", params=params
        ).json()
        return (
            list(
                map(
                    lambda item: Annotation(
                        self.connexion, self.id, UUID(item["asset_id"]), item
                    ),
                    r["items"],
                )
            ),
            r["count"],
        )

    @exception_handler
    @beartype
    def load_annotations(
        self,
        worker: Optional[Worker] = None,
        status: Optional[AnnotationStatus] = None,
        chunk_size: int = 1000,
        max_workers: Optional[int] = None,
        skip_error: bool = False,
    ) -> dict:
        """Load these annotation by retrieving shapes with labels, asset_id and worker_id

        Examples:
            ```python
            dict_annotations = foo_dataset.load_annotations()
            ```
        Arguments:
            worker (Optional[Worker], optional): Worker filter. Defaults to None.
            status (Optional[AnnotationStatus], optional): Status of annotations to retrieve. Defaults to None.
            chunk_size (int, optional): Size of chunk of annotations to load by request. Defaults to 1000.
            max_workers (int, optional): max workers to use when multithreading. Defaults to cpu_count() + 4.
            skip_error (bool, optional): skip error of a chunk and return partial annotations. Default to False
        """
        if chunk_size < 1 or chunk_size > 10000:
            raise exceptions.BadRequestError(
                "Impossible to load less than 1 or more than 10000 annotations by chunk. Please give another chunk_size"
            )

        params = {}
        if worker is not None:
            params["worker_id"] = worker.id
        if status is not None:
            params["status"] = status.value

        ids = self.connexion.get(
            f"/sdk/dataset/version/{self.id}/annotations/ids", params=params
        ).json()

        return MultiAnnotation.load_annotations_from_ids(
            self.connexion, self.id, ids, chunk_size, max_workers, skip_error
        )

    @exception_handler
    @beartype
    def export_annotation_file(
        self,
        annotation_file_type: Union[AnnotationFileType, str],
        target_path: Union[str, Path] = "./",
        assets: Union[MultiAsset, List[Asset], None] = None,
        worker: Optional[Worker] = None,
        status: Union[AnnotationStatus, str, None] = None,
        force_replace: bool = True,
    ) -> str:
        """Export annotations of this dataset version into a file, and download it.

        Giving 'worker' argument, you will retrieve only annotations of this worker if they exist.
        If you don't give 'worker', it will only export the last created annotation and its shapes.

        Examples:
            ```python
            dataset_v0.export_annotation_file(AnnotationFileType.COCO, "./")
            ```
        Arguments:
            annotation_file_type (AnnotationFileType): choose to export in Pascal VOC format or COCO format.
            target_path (str or Path, optional): directory path where file is downloaded. Defaults to current directory.
            assets (Union[(MultiAsset), List[(Asset)], None], optional): a list of assets of this dataset version.
                Only these assets will be concerned by this export. Defaults to None.
            worker ((Worker), optional): worker of annotations. Defaults to None.
            status (AnnotationStatus, optional): status of annotations. Defaults to None.
            force_replace (bool, optional): if true, will replace an existing file annotation. Defaults to True.

        Returns:
            Path of downloaded file.
        """
        payload = {"type": AnnotationFileType.validate(annotation_file_type)}
        if assets is not None:
            payload["asset_ids"] = [asset.id for asset in assets]

        if worker is not None:
            payload["worker_id"] = worker.id

        if status is not None:
            payload["status"] = AnnotationStatus.validate(status)

        r = self.connexion.post(
            f"/sdk/dataset/version/{self.id}/annotations/export",
            data=orjson.dumps(payload),
        ).json()

        path = os.path.join(target_path, r["object_name"])

        if self.connexion.do_download_file(
            path=path,
            presigned_url=r["presigned_url"],
            is_large=False,
            force_replace=force_replace,
        ):
            return path
        else:  # pragma: no cover
            object_name = r["object_name"]
            url = r["url"]
            raise DownloadError(
                f"Could not download annotation file {object_name} at {url}"
            )

    @exception_handler
    @beartype
    def import_annotation_voc_file(
        self,
        file_path: Union[str, Path],
        worker: Optional[Worker] = None,
        mode: Union[ImportAnnotationMode, str] = ImportAnnotationMode.REPLACE,
        force_create_label: bool = True,
    ) -> Tuple[
        Tuple[Asset, Annotation], List[Rectangle], List[Polygon], List[Classification]
    ]:
        """Read a Pascal VOC file, parse it and create some annotations and shape for one given asset

        Examples:
            ```python
            dataset_v0.import_annotation_voc_file(file_path="voc.xml")
            ```

        Arguments:
            file_path (str or Path): Path of file to import
            worker (Worker, optional): Worker to use. Defaults to current user.
            mode (ImportAnnotationMode, optional): Mode used to import.
                    REPLACE will delete worker annotation if exists and replace it.
                    CONCATENATE will create shapes on existing annotation.
                    SKIP will do nothing on existing annotation.
                    Defaults to ImportAnnotationMode.REPLACE.
            force_create_label (bool): Ensures labels are created if they don't exist. Defaults to True.

        Raises:
            FileNotFoundException: if file is not found
        """
        mode = ImportAnnotationMode.validate(mode)

        try:
            vocfile: PascalVOCFile = read_pascal_voc_file(file_path=file_path)
        except FileError:
            raise FileNotFoundException(f"{file_path} not found")
        except ParsingError as e:
            raise UnparsableAnnotationFileException(
                f"Could not parse VOC file {file_path} because : {e}"
            )

        logger.info("Reading labels")

        if isinstance(vocfile.annotation.object, Object):
            objects = [vocfile.annotation.object]
        else:
            objects = vocfile.annotation.object

        labels: Dict[str, Label] = {}
        for obj in objects:
            if obj.name in labels:
                continue

            # Can raise label NotFound
            try:
                labels[obj.name] = self.get_label(name=obj.name)
            except ResourceNotFoundError as e:
                if force_create_label:
                    logger.error(f"Label {obj.name} not found, creating it")
                    labels[obj.name] = self.create_label(name=obj.name)
                else:
                    raise e

        logger.info("Retrieving asset")

        asset = self.find_asset(filename=vocfile.annotation.filename)
        try:
            asset_annotation = asset.get_annotation(worker)
        except PicselliaError:
            asset_annotation = None

        # In Replace mode, delete old annotation
        if asset_annotation is not None and mode == ImportAnnotationMode.REPLACE:
            asset_annotation.delete()
            asset_annotation = None

        # If asset_annotation is None, it means there is actually no annotation on this asset
        if asset_annotation is None:
            asset_annotation = asset.create_annotation(duration=0.0, worker=worker)
        else:
            # Else, already an annotation (Replace mode already handled, so Skip mode is the only edge case here)
            if mode == ImportAnnotationMode.SKIP:
                logger.info(
                    f"This file {file_path} is skipped because an annotation already exists."
                )
                return (asset, asset_annotation), [], [], []

        logger.info("Creating shapes and importing them")

        rectangles: List[Tuple[int, int, int, int, Label]] = []
        polygons: List[Tuple[List, Label]] = []
        classifications: List[Label] = []
        for obj in objects:
            label = labels[obj.name]

            if obj.is_rle():  # pragma: no cover
                logger.error("RLE not implemented yet")
                continue
            elif obj.is_polygon():
                coords = obj.polygon_to_list_coordinates()
                polygons.append((coords, label))
            elif obj.bndbox is not None:
                rectangles.append(
                    (
                        int(obj.bndbox.xmin),
                        int(obj.bndbox.ymin),
                        int(obj.bndbox.xmax) - int(obj.bndbox.xmin),
                        int(obj.bndbox.ymax) - int(obj.bndbox.ymin),
                        label,
                    )
                )
            else:
                classifications.append(label)

        created_rectangles = []
        try:
            if len(rectangles) > 0:
                created_rectangles = asset_annotation.create_multiple_rectangles(
                    rectangles
                )
        except Exception as e:  # pragma: no cover
            logger.error(
                f"Could not create rectangle annotations for file {asset.filename}  because {e}"
            )

        created_polygons = []
        try:
            if len(polygons) > 0:
                created_polygons = asset_annotation.create_multiple_polygons(polygons)
        except Exception as e:  # pragma: no cover
            logger.error(
                f"Could not create polygon annotations for file {asset.filename} because {e}"
            )

        created_classifications = []
        try:
            if len(classifications) > 0:
                created_classifications = (
                    asset_annotation.create_multiple_classifications(classifications)
                )
        except Exception as e:  # pragma: no cover
            logger.error(
                f"Could not create classification annotations for file {asset.filename} because {e}"
            )

        nb_created_rectangles = len(created_rectangles)
        nb_created_polygons = len(created_polygons)
        nb_created_classifications = len(created_classifications)

        if nb_created_rectangles + nb_created_polygons + nb_created_classifications > 0:
            logger.info(f"Done! Pascal VOC file {file_path} imported on asset {asset}")
            if nb_created_rectangles > 0:
                logger.info(f"{nb_created_rectangles} rectangles created")

            if nb_created_polygons > 0:
                logger.info(f"{nb_created_polygons} polygons created")

            if nb_created_classifications > 0:
                logger.info(f"{nb_created_classifications} classifications created")
        else:  # pragma: no cover
            logger.warning(
                f"VOC file {file_path} was imported, but no shape was created"
            )

        return (
            (asset, asset_annotation),
            created_rectangles,
            created_polygons,
            created_classifications,
        )

    @exception_handler
    @beartype
    def import_annotations_coco_file(
        self,
        file_path: Union[Path, str],
        worker: Optional[Worker] = None,
        mode: Union[ImportAnnotationMode, str] = ImportAnnotationMode.REPLACE,
        force_create_label: bool = True,
        fail_on_asset_not_found: bool = True,
    ) -> Tuple[
        Dict[int, Tuple[Asset, Optional[Annotation]]],
        List[Rectangle],
        List[Polygon],
        List[Classification],
    ]:
        """Read a COCO file, parse it and create some annotations and shape for given assets

        Examples:
            ```python
            dataset_v0.import_annotations_coco_file(file_path="coco.json")
            ```

        Arguments:
            file_path (str): Path of file to import
            worker (Worker, optional): Worker to use. Defaults to current user.
            mode (ImportAnnotationMode, optional): Mode used to import.
                    REPLACE will delete worker annotation if exists and replace it.
                    CONCATENATE will create shapes on existing annotation.
                    SKIP will do nothing on existing annotation.
                    Defaults to ImportAnnotationMode.REPLACE.
            force_create_label (bool): Ensure labels are created if they don't exist. Defaults to True
            fail_on_asset_not_found (bool): Raise an error if asset is not found. Default to True

        Raises:
            FileNotFoundException: if file is not found

        Returns:
            (List[Tuple[Asset, Optional[Annotation]]]): A list with tuples of Asset with non-skipped Annotation
        """
        mode = ImportAnnotationMode.validate(mode)

        try:
            cocofile: COCOFile = read_coco_file(file_path=file_path)
        except FileError:
            raise FileNotFoundException(f"{file_path} not found")
        except ParsingError as e:
            raise UnparsableAnnotationFileException(
                f"Could not parse COCO file {file_path} because : {e}"
            )

        logger.info("Reading categories as labels..")

        labels: Dict[int, Label] = {}
        for category in cocofile.categories:
            if category.id in labels:
                raise UnparsableAnnotationFileException(
                    f"Category id {category.id} already defined"
                )

            # Can raise label NotFound
            try:
                labels[category.id] = self.get_label(name=category.name)
            except ResourceNotFoundError as e:
                if force_create_label:
                    logger.error(f"Label {category.name} not found, creating it")
                    labels[category.id] = self.create_label(name=category.name)
                else:
                    raise e

        logger.info("Reading images as assets...")
        filenames = {image.file_name: image.id for image in cocofile.images}
        multi_assets = self.find_all_assets(filenames=list(filenames.keys()))

        if fail_on_asset_not_found and len(multi_assets) != len(filenames):
            raise ResourceNotFoundError(
                "Some filenames were not found in this dataset version."
            )

        logger.info("Retrieving annotations...")
        assets: Dict[int, Tuple[Asset, Optional[Annotation]]] = {}
        for asset in multi_assets:
            try:
                asset_annotation = asset.get_annotation(worker)
            except PicselliaError:
                asset_annotation = None

            # In Replace mode, delete old annotation
            if asset_annotation is not None and mode == ImportAnnotationMode.REPLACE:
                asset_annotation.delete()
                asset_annotation = None

            # If asset_annotation is None, it means there is actually no annotation on this asset
            if asset_annotation is None:
                asset_annotation = asset.create_annotation(duration=0.0, worker=worker)
            else:
                # Else, there is already an annotation (Replace mode already handled, so Skip mode is edge case here)
                if mode == ImportAnnotationMode.SKIP:
                    asset_annotation = None

            assets[filenames[asset.filename]] = (asset, asset_annotation)

        logger.info("Reading shapes..")

        rectangles: Dict[int, List[Tuple[int, int, int, int, Label]]] = {}
        polygons: Dict[int, List[Tuple[List, Label]]] = {}
        classifications: Dict[int, List[Label]] = {}
        for annotation in cocofile.annotations:

            try:
                label = labels[annotation.category_id]
            except KeyError:  # pragma: no cover
                logger.error(
                    f"category_id {annotation.category_id} not found into retrieved labels"
                )
                continue

            try:
                asset, asset_annotation = assets[annotation.image_id]
            except KeyError:
                logger.error(
                    f"image_id {annotation.image_id} not found into retrieved assets"
                )
                continue

            if asset_annotation is None:
                logger.info(
                    f"Skipped annotation {annotation.image_id} because already exists"
                )
                continue

            if annotation.is_rle():  # pragma: no cover
                logger.error("RLE not implemented yet")
                continue
            elif annotation.is_polygon():
                if annotation.image_id not in polygons:
                    polygons[annotation.image_id] = []
                polygon_coords = annotation.polygon_to_list_coordinates()
                for polygon_coord in polygon_coords:
                    polygons[annotation.image_id].append((polygon_coord, label))
            elif annotation.bbox is not None and annotation.bbox != []:
                if annotation.image_id not in rectangles:
                    rectangles[annotation.image_id] = []
                rectangles[annotation.image_id].append(
                    (
                        int(annotation.bbox[0]),
                        int(annotation.bbox[1]),
                        int(annotation.bbox[2]),
                        int(annotation.bbox[3]),
                        label,
                    )
                )
            else:
                if annotation.image_id not in classifications:
                    classifications[annotation.image_id] = []
                classifications[annotation.image_id].append(label)

        logger.info("Creating shapes..")

        created_rectangles = []
        for image_id, objects in rectangles.items():
            asset, asset_annotation = assets[image_id]
            try:
                created_rectangles.extend(
                    asset_annotation.create_multiple_rectangles(objects)
                )
            except Exception as e:  # pragma: no cover
                logger.error(
                    f"Could not create rectangle annotations of image {asset.filename} ({image_id}) because {e}"
                )
                continue

        created_polygons = []
        for image_id, objects in polygons.items():
            asset, asset_annotation = assets[image_id]
            try:
                created_polygons.extend(
                    asset_annotation.create_multiple_polygons(objects)
                )
            except Exception as e:  # pragma: no cover
                logger.error(
                    f"Could not create polygon annotations of image {asset.filename} ({image_id}) because {e}"
                )
                continue

        created_classifications = []
        for image_id, objects in classifications.items():
            asset, asset_annotation = assets[image_id]
            try:
                created_classifications.extend(
                    asset_annotation.create_multiple_classifications(objects)
                )
            except Exception as e:  # pragma: no cover
                logger.error(
                    f"Could not create classification annotations of image {asset.filename} ({image_id}) because {e}"
                )
                continue

        nb_created_rectangles = len(created_rectangles)
        nb_created_polygons = len(created_polygons)
        nb_created_classifications = len(created_classifications)

        if nb_created_rectangles + nb_created_polygons + nb_created_classifications > 0:
            logger.info(
                f"Done! COCO file {file_path} imported, on {len(assets.values())} assets"
            )
            if nb_created_rectangles > 0:
                logger.info(f"{nb_created_rectangles} rectangles created")

            if nb_created_polygons > 0:
                logger.info(f"{nb_created_polygons} polygons created")

            if nb_created_classifications > 0:
                logger.info(f"{nb_created_classifications} classifications created")
        else:
            logger.info(f"COCO file {file_path} was imported, but no shape was created")

        return assets, created_rectangles, created_polygons, created_classifications

    @exception_handler
    @beartype
    def delete_all_annotations(self, workers: Optional[List[Worker]] = None) -> None:
        """Delete all annotations of this dataset

        :warning: **DANGER ZONE**: Be very careful here!

        It will remove all annotation of every asset of this dataset
        You can give workers on which it will be effectively erased.

        Examples:
            ```python
            foo_dataset.delete_all_annotations()
            ```
        """
        payload = {"asset_ids": ["__all__"]}
        if workers is not None:
            payload["worker_ids"] = [worker.id for worker in workers]

        self.connexion.delete(
            f"/sdk/dataset/version/{self.id}/annotations",
            data=orjson.dumps(payload),
        )
        logger.info(f"All annotations in {self} were removed.")

    @exception_handler
    @beartype
    def synchronize(
        self, target_dir: str, do_download: bool = False
    ) -> Optional[MultiAsset]:
        """Synchronize this dataset with target dir by comparing assets in target dir with assets uploaded in dataset.

        Examples:
            ```python
            foo_dataset.synchronize('./foo_dataset/first')
            ```
        Arguments:
            target_dir (str): directory to synchronize against
            do_download (bool): do download files when they are not in local directory
        """
        assert os.path.isdir(target_dir), "Please select a valid directory path"
        logger.info("⌛️ Scanning Dataset Assets..")
        assets: MultiAsset = self.list_assets()
        filenames = set(map(lambda asset: asset.filename, assets))
        logger.info("🔍 Scanning Local Dataset Folder ..")
        local_filenames = set(
            [
                e
                for e in os.listdir(target_dir)
                if os.path.isfile(os.path.join(target_dir, e))
            ]
        )

        not_uploaded = local_filenames - filenames
        if len(not_uploaded) > 0:
            logger.info(
                f"📚 {len(not_uploaded)} assets not uploaded. You need to add data to the datalake first with :"
            )
            filepaths = list(
                map(
                    lambda filename: str(os.path.join(target_dir, filename)),
                    not_uploaded,
                )
            )
            logger.info(f"filepaths = {filepaths}")
            logger.info("list_data = client.get_datalake().upload_data(filepaths)")
            logger.info(
                f'client.get_dataset_by_id({self.origin_id}).get_version("{self.version}").add_data(list_data)'
            )

        not_downloaded = filenames - local_filenames
        if len(not_downloaded) > 0:
            assets_to_download = list(
                filter(
                    lambda asset: asset.filename in not_downloaded,
                    assets.items,
                )
            )
            multi_assets = MultiAsset(self.connexion, self.id, assets_to_download)
            logger.info(f"📚 {len(not_downloaded)} assets not downloaded")
            if do_download:
                logger.info(f"📚 Downloading {len(not_downloaded)} assets")
                multi_assets.download(target_dir)
            else:
                logger.info(
                    "📚 Call this method again with do_download=True if you want to download these assets"
                )
            return multi_assets
        else:
            logger.info("✅ Dataset is up-to-date.")
            return None

    @exception_handler
    @beartype
    def get_or_create_asset_tag(self, name: str) -> Tag:
        """Retrieve an asset tag used in this dataset version by its name.
        If tag does not exist, create it and return it.

        Examples:
            ```python
            tag = self.get_or_create_asset_tag("new_tag")
            ```
        Arguments:
            name (str): Tag to retrieve or create

        Returns:
            A (Tag) object
        """
        try:
            return self.get_asset_tag(name)
        except exceptions.ResourceNotFoundError:
            return self.create_asset_tag(name)

    @exception_handler
    @beartype
    def create_asset_tag(self, name: str) -> Tag:
        """Create asset tag only available in this dataset version.

        Examples:
            ```python
            tag_dog = dataset_v0.create_asset_tag("dog")
            ```
        Arguments:
            name (str): name of tag

        Returns:
            A (Tag) object
        """
        payload = {"name": name}
        r = self.connexion.post(
            f"/sdk/dataset/version/{self.id}/tags", data=orjson.dumps(payload)
        ).json()
        return Tag(self.connexion, r)

    @exception_handler
    @beartype
    def get_asset_tag(self, name: str) -> Tag:
        """Retrieve an asset tag used in this dataset version.

        Examples:
            ```python
            tag_dog = dataset_v0.get_asset_tag("dog")
            ```
        Arguments:
            name (str): Name of the tag you're looking for

        Returns:
            A (Tag) object
        """
        params = {"name": name}
        r = self.connexion.get(
            f"/sdk/dataset/version/{self.id}/tags/find", params=params
        ).json()
        return Tag(self.connexion, r)

    @exception_handler
    @beartype
    def convert_tags_to_classification(
        self, tag_type: TagTarget, tags: List[Tag]
    ) -> Job:
        assert (
            self.type == InferenceType.CLASSIFICATION
        ), "You cannot convert tags on this dataset."
        assert (
            tag_type == TagTarget.ASSET or tag_type == TagTarget.DATA
        ), "You can only convert asset tags or data tags"

        tag_ids = []
        for tag in tags:
            if tag.target_type != tag_type:
                raise TypeError(f"{tag} is not a {tag_type} type of tag.")

            tag_ids.append(tag.id)

        payload = {"tag_ids": tag_ids, "tag_type": tag_type}

        r = self.connexion.post(
            f"/sdk/dataset/version/{self.id}/tags/convert", data=orjson.dumps(payload)
        ).json()
        logger.info(
            f"Tags (of type {tag_type}) are being converted into classifications."
            "This operation can take some time, please wait for returned job to end."
        )

        return Job(self.connexion, r)

    @exception_handler
    @beartype
    def list_asset_tags(self) -> List[Tag]:
        """List asset tags created in this dataset version

        Examples:
            ```python
            tags = dataset_v0.list_asset_tags()
                assert tag_dog in tags
            ```

        Returns:
            A list of (Tag)
        """
        r = self.connexion.get(f"/sdk/dataset/version/{self.id}/tags").json()
        return list(map(partial(Tag, self.connexion), r["items"]))

    @beartype
    def train_test_split(
        self, prop: float = 0.8, random_seed: Optional[Any] = None
    ) -> Tuple[MultiAsset, MultiAsset, Dict[str, list], Dict[str, list], List[Label]]:
        """Train test split

        Examples:
            ```python
            train_assets, eval_assets, count_train, count_eval, labels = dataset.train_test_split()
            ```
        Arguments:
            prop (float, optional): Percentage of data for training set. Defaults to 0.8.
            random_seed (Any, optional): Use a seed to ensures same result if run multiple times.

        Returns:
            A tuple with all of this information (
                list of train assets,
                list of test assets,
                dict of repartition of classes for train assets,
                dict of repartition of classes for test assets,
                list of labels
            )
        """
        r = self.connexion.get(f"/sdk/dataset/version/{self.id}/assets/extended").json()
        if r["count"] == 0:
            raise NoDataError("No asset with annotation found in this dataset")

        count = 0
        items = []
        for item in r["items"]:
            if not item["annotations"]:
                logger.debug(f"No annotation for asset {item['data']['filename']}")
                continue

            count += 1
            items.append(item)

        if random_seed is not None:
            random.seed(random_seed)

        nb_assets_train = int(count * prop)
        train_eval_rep = [1] * nb_assets_train + [0] * (count - nb_assets_train)
        random.shuffle(train_eval_rep)

        labels = self.list_labels()
        label_names = {str(label.id): label.name for label in labels}

        k = 0

        train_assets = []
        eval_assets = []

        train_label_count = {}
        eval_label_count = {}
        for item in items:
            annotations = item["annotations"]

            # TODO: Get only from worker or status
            annotation = annotations[0]

            asset = Asset(self.connexion, dataset_version_id=self.id, data=item)

            if train_eval_rep[k] == 0:
                eval_assets.append(asset)
                label_count_ref = eval_label_count
            else:
                train_assets.append(asset)
                label_count_ref = train_label_count

            k += 1

            label_ids = []
            for shape in annotation["rectangles"]:
                label_ids.append(shape["label_id"])

            for shape in annotation["classifications"]:
                label_ids.append(shape["label_id"])

            for shape in annotation["points"]:
                label_ids.append(shape["label_id"])

            for shape in annotation["polygons"]:
                label_ids.append(shape["label_id"])

            for shape in annotation["lines"]:
                label_ids.append(shape["label_id"])

            for label_id in label_ids:
                try:
                    label_name = label_names[label_id]
                    if label_name not in label_count_ref:
                        label_count_ref[label_name] = 1
                    else:
                        label_count_ref[label_name] += 1
                except KeyError:  # pragma: no cover
                    logger.warning(f"A shape has an unknown label ({label_id}).")

        train_repartition = {
            "x": list(train_label_count.keys()),
            "y": list(train_label_count.values()),
        }

        eval_repartition = {
            "x": list(eval_label_count.keys()),
            "y": list(eval_label_count.values()),
        }

        return (
            MultiAsset(self.connexion, self.id, train_assets),
            MultiAsset(self.connexion, self.id, eval_assets),
            train_repartition,
            eval_repartition,
            labels,
        )
