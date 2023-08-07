from __future__ import annotations

from abc import ABCMeta

from .mixin import ToFileMixin, MetadataMixin, Dataset, Model, ObjectMixin, DatasetTransformation


class ObjectManager(ToFileMixin, MetadataMixin, ObjectMixin, metaclass=ABCMeta):
    object_manager_key = "_object_manager"

    def __init__(self, file_name=None, path=None):
        self.full_path = path, file_name
        self.metadata.update({self.object_manager_key: self.__class__.__name__})

    @ToFileMixin.file_name.setter
    def file_name(self, val) -> str:
        ToFileMixin.file_name.fset(self, val)
        self.metadata.update({"file_name": self.file_name})
        return self.file_name

    def save_file(self, path=None) -> (str, str):
        self.save_metadata(self.full_path)
        return super(ObjectManager, self).save_file(path=path)

    def load_file(self):
        super(ObjectManager, self).load_file()
        self.load_metadata(self.full_path)


class DatasetManager(ObjectManager, Dataset, metaclass=ABCMeta):
    pass


class ModelManager(ObjectManager, Model, metaclass=ABCMeta):
    pass


class DatasetTransformationManager(ObjectManager, DatasetTransformation, metaclass=ABCMeta):
    pass
