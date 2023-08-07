from __future__ import annotations

import abc
import os
import uuid
from abc import abstractmethod
from typing import Any
from typing import List
from typing import Tuple

from .enums import ApplicationType
from .utils import save_json, load_json, ensure_path_exists
from ..core.compression import get_compressor


class SerializerMixin(metaclass=abc.ABCMeta):
    @staticmethod
    def get_serialized(obj, meta_list: List[SerializerMixin.__class__]) -> dict:
        ser_list = [meta.serialize(obj) for meta in meta_list]
        result = dict()
        for s in ser_list:
            result.update(s)
        return result

    def deserialize(self, obj: dict) -> Any:
        for key, val in obj.items():
            setattr(self, key, val)
        return self

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class DescriptionMixin(SerializerMixin):
    _description: str = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    def serialize(self):
        return {"description": self.description}


class AttrDatasetMixin(SerializerMixin):
    _dataset: str = None

    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, val):
        self._dataset = val

    def serialize(self):
        return {"dataset": self.dataset}


class AttrProjectMixin(SerializerMixin):
    _project: str = None

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, val):
        self._project = val

    def serialize(self):
        return {"project": self.project}


class AttrFrameworkMixin(SerializerMixin):
    _framework: str = None

    @property
    def framework(self):
        return self._framework

    @framework.setter
    def framework(self, val):
        self._framework = val

    def serialize(self):
        return {"framework": self.framework}


class AttrMetadataMixin(SerializerMixin):
    _metadata: dict = None

    @property
    def metadata(self) -> dict:
        """
        Object metadata which may not be saved by framework used must be of type Dict
        Empty dict if none specified.
        @return: dict
        """
        if self._metadata is None:
            self.metadata = dict()
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: dict):
        """
        Metadata to be saved and loaded with the file
        @param metadata:
        @return:
        """
        if not isinstance(metadata, dict):
            raise TypeError(f"metadata of type: {type(metadata)} must be a dict")
        setattr(self, "_metadata", metadata)

    def serialize(self):
        return {"metadata": self.metadata}


class NameMixin(SerializerMixin):
    _name: str = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    def serialize(self):
        return {"name": self.name}


# TODO: for now this is assumed that each model has a uuid, this needs to be abstracted to pk and inherit the primary key of each model.
class IDMixin(SerializerMixin):
    _uuid: str = None

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, val):
        self._uuid = val

    def serialize(self):
        return {"uuid": self.uuid}


class HashMixin(SerializerMixin):
    _hash: str = None

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, val):
        self._hash = val

    def serialize(self):
        return {"hash": self.hash}


class UsernameMixin(SerializerMixin):
    _username: str = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        self._username = val

    def serialize(self):
        return {"username": self.username}


class EmailMixin(SerializerMixin):
    _email: str = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, val):
        self._email = val

    def serialize(self):
        return {"email": self.email}


class PasswordMixin(SerializerMixin):
    _password: str = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, val):
        self._password = val

    def serialize(self):
        return {"password": self.password}


class ToFileMixin:
    # _controller: SecleaAI
    _file_name: str = None
    _path: str = None

    @property
    def path(self):
        if self._path is None:
            self.path = None  # let setter assign default path
        return self._path

    @path.setter
    def path(self, val: str):
        val = val if val is not None else os.getcwd()
        ensure_path_exists(val)
        self._path = val

    @property
    def full_path(self):
        return os.path.join(self.path, self.file_name)

    @full_path.setter
    def full_path(self, val: Tuple[str, str]):
        self.path, self.file_name = val

    @property
    def file_name(self) -> str:
        """
        File name under which all object data is saved
        @return: file_name in metadata, generates uuid4 if none specified
        """
        if self._file_name is None:
            self.file_name = None  # let setter generate new name.
        return self._file_name

    @file_name.setter
    def file_name(self, val: str):
        """
        File name setter, if val is None uuid4.hex is set
        @param val:
        @return:
        """
        val = val if val is not None else uuid.uuid4().__str__()
        self._file_name = val

    def save_file(self, path=None) -> (str, str):
        """
        Save tracked object to a file,
        @return: (path, file_name)
        """
        path_file_name = get_compressor().compress(self.path, self.file_name, out_dir=path)
        return path_file_name

    def load_file(self):
        """
        @return:
        """
        self.path, self.file_name = get_compressor().decompress(self.path, self.file_name)


class MetadataMixin(AttrMetadataMixin):
    _metadata_file_name = ".metadata.json"

    def save_metadata(self, path):
        ensure_path_exists(path)
        save_json(os.path.join(path, self._metadata_file_name), self.metadata)

    def load_metadata(self, path):
        self.metadata = load_json(os.path.join(path, self._metadata_file_name))


class ObjectMixin:
    _object_file_name = "object"

    @property
    @abstractmethod
    def full_path(self):
        raise NotImplementedError

    @property
    def object_file_path(self):
        return os.path.join(self.full_path, self._object_file_name)

    @abstractmethod
    def save_object(self, obj: Any):
        raise NotImplementedError

    @abstractmethod
    def load_object(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def hash_object(self, obj) -> int:
        raise NotImplementedError

    def hash_object_with_project(self, obj, project) -> int:
        return hash((self.hash_object(obj), project))


class BaseModel(IDMixin, SerializerMixin):
    def __init__(self, **kwargs):
        print(f"Object initializing {self.__class__.__name__} : {kwargs.keys()}")
        self.deserialize(kwargs)

    @abstractmethod
    def serialize(self):
        pass


class Dataset(
    BaseModel,
    NameMixin,
    DescriptionMixin,
    AttrMetadataMixin,
    AttrDatasetMixin,
    HashMixin,
    AttrProjectMixin,
):
    def serialize(self):
        return self.get_serialized(
            self,
            [NameMixin, DescriptionMixin, IDMixin, AttrMetadataMixin, HashMixin, AttrProjectMixin],
        )

    def deserialize(self, obj: dict) -> Any:
        print("attempting deserialization: ")
        r = SerializerMixin.deserialize(self, obj)
        print("deserialization successful")
        return r


class Organization(BaseModel, NameMixin):
    def serialize(self):
        return {**self.get_serialized(self, [IDMixin, NameMixin])}


class Project(BaseModel, NameMixin, DescriptionMixin):
    organization: Organization.uuid

    def serialize(self):
        return {
            **self.get_serialized(self, [IDMixin, NameMixin]),
            "organization": self.organization,
        }


class User(BaseModel, UsernameMixin, PasswordMixin, EmailMixin):
    def serialize(self):
        return self.get_serialized(self, [IDMixin, UsernameMixin, PasswordMixin, EmailMixin])


class DatasetTransformation(BaseModel, NameMixin, DescriptionMixin):
    def serialize(self):
        return self.get_serialized(self, [NameMixin, DescriptionMixin, IDMixin])


class Model(BaseModel, NameMixin, DescriptionMixin, AttrFrameworkMixin):
    _model_name_key = "_model_name"

    def serialize(self):
        return self.get_serialized(self, [NameMixin, DescriptionMixin])

    @staticmethod
    @abstractmethod
    def get_params(model) -> dict:
        """
        Extract parameters of model
        @param model:
        @return:
        """
        pass

    @staticmethod
    @abstractmethod
    def get_application_type(model) -> ApplicationType:
        """
        Autodetect the application type of the model. eg. one of ApplicationType such as regression
        :param model:
        :return: ApplicationType The type of the application. eg. regression
        """


class ModelState(BaseModel, NameMixin, DescriptionMixin):
    def serialize(self):
        return self.get_serialized(self, [NameMixin, DescriptionMixin, IDMixin])


class TrainingRun(BaseModel, NameMixin, DescriptionMixin):
    def serialize(self):
        return self.get_serialized(self, [NameMixin, DescriptionMixin, IDMixin])
