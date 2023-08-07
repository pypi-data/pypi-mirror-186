import backoff
import boto3
import requests

import biomage_programmatic_interface.exceptions as exceptions
from biomage_programmatic_interface.experiment import Experiment

HTTP_METHODS = {"POST": requests.post, "PATCH": requests.patch, "GET": requests.get}


class Connection:
    def __init__(self, username, password, instance_url, verbose=True):
        self.verbose = verbose
        self.__api_url = self.__get_api_url(instance_url)
        self.username = username
        self.password = password
        self.instance_url = instance_url
        cognito_params = self.__get_cognito_params().json()
        self.clientId = cognito_params["clientId"]
        self.region = cognito_params["clientRegion"]
        self.__authenticate()

    def __get_cognito_params(self):
        try:
            return requests.get(self.__api_url + "v2/programmaticInterfaceClient")
        except Exception:
            raise exceptions.InstanceNotFound() from None

    def __authenticate(self):
        client = boto3.client("cognito-idp", region_name=self.region)

        try:
            resp = client.initiate_auth(
                ClientId=self.clientId,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={"USERNAME": self.username, "PASSWORD": self.password},
            )
        except Exception:
            raise exceptions.IncorrectCredentials() from None

        print("Authentication succesfull") if self.verbose else ""

        self.__jwt = resp["AuthenticationResult"]["IdToken"]

    def __get_api_url(self, instance_url):
        if instance_url == "local":
            return "http://localhost:3000/"
        if instance_url.startswith("https://"):
            return instance_url
        return f"https://api.{instance_url}/"

    @backoff.on_exception(
        backoff.constant,
        requests.exceptions.HTTPError,
        max_tries=3,
        jitter=backoff.full_jitter,
    )
    def fetch_api(self, url, body, method="POST"):
        headers = {
            "Authorization": "Bearer " + self.__jwt,
            "Content-Type": "application/json",
        }

        response = HTTP_METHODS[method](
            self.__api_url + url, json=body, headers=headers
        )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                print("fetch_api: refresh expired token")
                self.__authenticate()
            raise e

        return response

    def uploadS3(self, objectS3, signed_url, compress=True):
        if compress and not objectS3.is_compressed():
            objectS3.compress()
        headers = {"Content-type": "application/octet-stream"}
        with open(objectS3.path, "rb") as file:
            try:
                response = requests.put(signed_url, headers=headers, data=file.read())
                response.raise_for_status()
            except Exception as e:
                print(f"exception: uploadS3: {objectS3}: {signed_url}")
                raise e

        print(f"Uploaded {objectS3.path} to S3") if self.verbose else ""

    def create_experiment(self, experiment_name=None):
        experiment = Experiment.create_experiment(self, experiment_name)
        print(f"Experiment {experiment.name} created!") if self.verbose else ""
        return experiment
