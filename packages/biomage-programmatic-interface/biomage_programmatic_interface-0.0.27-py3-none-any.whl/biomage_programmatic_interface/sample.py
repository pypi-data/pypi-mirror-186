from os import listdir
from os.path import isfile, join

from biomage_programmatic_interface.sample_file import SampleFile
from biomage_programmatic_interface.utils import is_file_hidden


class Sample:
    def __init__(self, name):
        self.__name = name
        self.__uuid = None
        self.__sample_files = []

    @property
    def name(self):
        return self.__name

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid):
        if self.__uuid is not None:
            raise Exception(f"uuid already set for sample {self.__name}")
        self.__uuid = uuid

    def to_json(self):
        return {"name": self.__name, "sampleTechnology": "10x", "options": {}}

    def get_sample_files(self):
        return self.__sample_files

    def add_sample_file(self, sample_file):
        self.__sample_files.append(sample_file)

    @staticmethod
    def __find_all_files_recursively(path):
        file_paths = listdir(path)
        ret = {}
        for file_path in file_paths:
            full_path = join(path, file_path)

            if is_file_hidden(full_path):
                continue

            if isfile(full_path):
                file = SampleFile(full_path)

                if not file.is_valid_type():
                    continue

                folder_name = file.folder

                if ret.get(folder_name) is None:
                    ret[folder_name] = Sample(folder_name)
                ret[folder_name].add_sample_file(file)
                continue

            ret.update(Sample.__find_all_files_recursively(full_path))
        return ret

    @staticmethod
    def get_all_samples_from_path(path):
        return Sample.__find_all_files_recursively(path).values()
