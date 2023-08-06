import datetime
import hashlib

from biomage_programmatic_interface.sample import Sample


class Experiment:
    @staticmethod
    def create_experiment(connection, name=None):
        created_at = datetime.datetime.now().isoformat()
        hashed_string = hashlib.md5(created_at.encode())
        id = hashed_string.hexdigest()
        name = name if name else id
        experiment_data = {
            "id": id,
            "name": name,
            "description": "",
        }

        connection.fetch_api("v2/experiments/" + id, body=experiment_data)
        return Experiment(connection, id, name)

    def __init__(self, connection, id, name):
        self.__connection = connection
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __notify_upload(self, sample_id, sample_file_type):
        url = f"v2/experiments/{self.id}/samples/{sample_id}/sampleFiles/{sample_file_type}"
        json = {"uploadStatus": "uploaded"}
        self.__connection.fetch_api(url, json, "PATCH")

    def __create_sample_file(self, sample_uuid, sample_file):
        url = f"v2/experiments/{self.id}/samples/{sample_uuid}/sampleFiles/{sample_file.get_type()}"
        response = self.__connection.fetch_api(url, sample_file.to_json())
        return response.content

    def __create_samples(self, samples):
        url = f"v2/experiments/{self.id}/samples"
        body = [sample.to_json() for sample in samples]

        sample_ids_by_name = self.__connection.fetch_api(url, body).json()

        for sample in samples:
            sample.uuid = sample_ids_by_name[sample.name]

    def __upload_sample(self, sample):
        for sample_file in sample.get_sample_files():
            s3url_raw = self.__create_sample_file(
                sample.uuid,
                sample_file,
            )
            s3url = s3url_raw.decode("utf-8").replace('"', "")
            self.__connection.uploadS3(sample_file, s3url)

            self.__notify_upload(sample.uuid, sample_file.get_type())

    def upload_samples(self, samples_path):
        samples = Sample.get_all_samples_from_path(samples_path)

        self.__create_samples(samples)

        for sample in samples:
            try:
                self.__upload_sample(sample)
            except Exception as e:
                print(
                    f"Upload failed: {e}. This is likely an error within ",
                    "the python package for uploading.",
                    "Please send an email to hello@biomage.net and we ",
                    "will try to resolve this problem as soon as possible"
                )
