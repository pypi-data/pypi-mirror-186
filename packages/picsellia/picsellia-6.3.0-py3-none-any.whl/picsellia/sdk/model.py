import logging
from functools import partial
from typing import List, Optional, Union

import orjson
from beartype import beartype

import picsellia.utils as utils
from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.model_version import ModelVersion
from picsellia.sdk.tag import Tag, TagTarget
from picsellia.sdk.taggable import Taggable
from picsellia.types.enums import Framework, InferenceType
from picsellia.types.schemas import ModelSchema

logger = logging.getLogger("picsellia")


class Model(Dao, Taggable):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)
        Taggable.__init__(self, TagTarget.MODEL)

    @property
    def name(self) -> str:
        """Name of this (Model)"""
        return self._name

    @property
    def type(self) -> InferenceType:
        """Type of this (Model)"""
        return self._type

    @property
    def framework(self) -> Framework:
        """Framework of this (Model)"""
        return self._framework

    @property
    def private(self) -> bool:
        """Privacy of this (Model)"""
        return self._private

    def __str__(self):
        is_private = "" if self._private else "[PUBLIC]"
        return f"{Colors.BLUE}{is_private} Model '{self.name}' with type {self.type.name} and framework {self.framework.name}  {Colors.ENDC} (id: {self.id})"

    @exception_handler
    @beartype
    def get_resource_url_on_platform(self) -> str:
        """Get platform url of this resource.

        Examples:
            ```python
            print(foo_dataset.get_resource_url_on_platform())
            >>> "https://app.picsellia.com/model/62cffb84-b92c-450c-bc37-8c4dd4d0f590"
            ```

        Returns:
            Url on Platform for this resource
        """

        return f"{self.connexion.host}/model/{self.id}"

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/model/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        schema = ModelSchema(**data)
        self._name = schema.name
        self._type = schema.type
        self._framework = schema.framework
        self._private = schema.private
        return schema

    @exception_handler
    @beartype
    def update(
        self,
        name: Optional[str] = None,
        framework: Union[str, Framework, None] = None,
        private: Optional[bool] = None,
        description: Optional[str] = None,
        type: Union[str, InferenceType, None] = None,
    ) -> None:
        """Update a model with a new name, framework, privacy, description or type

        Examples:
            ```python
            model.update(description="Very cool model")
            ```
        """
        if framework:
            framework = Framework.validate(framework)

        if type:
            type = InferenceType.validate(type)

        if type and type not in [
            InferenceType.CLASSIFICATION,
            InferenceType.OBJECT_DETECTION,
            InferenceType.SEGMENTATION,
        ]:
            raise TypeError(f"Type '{type}' not supported yet for model")

        payload = {
            "name": name,
            "type": type,
            "framework": framework,
            "private": private,
            "description": description,
        }
        filtered_payload = utils.filter_payload(payload)
        r = self.connexion.patch(
            f"/sdk/model/{self.id}", data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)
        logger.info(f"{self} updated.")

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete model.

        Delete the model in Picsellia database

        Examples:
            ```python
            model.delete()
            ```
        """
        self.connexion.delete(f"/sdk/model/{self.id}")
        logger.info(f"{self} deleted.")

    @exception_handler
    @beartype
    def get_tags(self) -> List[Tag]:
        """Retrieve the tags of your model.

        Examples:
            ```python
            tags = my_model.get_tags()
            assert tags[0].name == "my-model-1"
            ```

        Returns:
            List of tags as Tag
        """
        r = self.sync()
        return list(map(partial(Tag, self.connexion), r["tags"]))

    @exception_handler
    @beartype
    def create_version(
        self,
        docker_image_name: Optional[str] = None,
        docker_flags: Optional[List[str]] = None,
        thumb_object_name: Optional[str] = None,
        notebook_link: Optional[str] = None,
        labels: Optional[dict] = None,
        base_parameters: Optional[dict] = None,
        docker_env_variables: Optional[dict] = None,
    ) -> ModelVersion:
        """Create a version of a model.

        The version number of this model will be defined by the platform. It is incremented automatically.

        Examples:
            ```python
            model_v0 = model.create_version()
            ```

        Returns:
            A (ModelVersion) object
        """
        payload = {
            "docker_image_name": docker_image_name,
            "docker_flags": docker_flags,
            "thumb_object_name": thumb_object_name,
            "notebook_link": notebook_link,
            "labels": labels,
            "base_parameters": base_parameters,
            "docker_env_variables": docker_env_variables,
        }
        filtered_payload = utils.filter_payload(payload)
        r = self.connexion.post(
            f"/sdk/model/{self.id}/versions",
            data=orjson.dumps(filtered_payload),
        ).json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def get_version(self, version: int) -> ModelVersion:
        """Retrieve a version of a model

        Examples:
            ```python
            version = model.get_version(0)
            ```

        Returns:
            A (ModelVersion) object
        """
        params = {"version": version}
        r = self.connexion.get(
            f"/sdk/model/{self.id}/versions/find", params=params
        ).json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def list_versions(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
    ) -> List[ModelVersion]:
        """List versions of a model

        Examples:
            ```python
            versions = model.list_versions()
            ```

        Returns:
            A list of (ModelVersion) object of this model
        """
        params = {"limit": limit, "offset": offset, "order_by": order_by}
        params = utils.filter_payload(params)
        r = self.connexion.get(f"/sdk/model/{self.id}/versions", params=params).json()
        return list(map(partial(ModelVersion, self.connexion), r["items"]))
