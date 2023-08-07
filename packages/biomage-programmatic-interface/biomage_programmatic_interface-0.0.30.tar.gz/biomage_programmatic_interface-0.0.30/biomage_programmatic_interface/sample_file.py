import uuid
from os.path import getsize

from biomage_programmatic_interface.objectS3 import ObjectS3


class SampleFile(ObjectS3):
    def __init__(self, path):
        super().__init__(path)
        self.__uuid = str(uuid.uuid4())

    @classmethod
    def from_sample_file(cls, sample_file):
        return SampleFile(sample_file.path)

    @property
    def name(self):
        return self.path.split("/")[-1]

    @property
    def uuid(self):
        return self.__uuid

    @property
    def folder(self):
        return self.path.split("/")[-2]

    def get_size(self):
        return getsize(self.path)

    def is_valid_type(self):
        return self.get_type() is not None

    def get_type(self):
        file_types = {
            "matrix.mtx": "matrix10x",
            "barcodes.tsv": "barcodes10x",
            "features.tsv": "features10x",
            "genes.tsv": "features10x",
        }

        for file_type_key in file_types.keys():
            if file_type_key in self.name:
                return file_types[file_type_key]
        return None

    def to_json(self):
        return {
            "sampleFileId": self.__uuid,
            "size": self.get_size(),
        }
