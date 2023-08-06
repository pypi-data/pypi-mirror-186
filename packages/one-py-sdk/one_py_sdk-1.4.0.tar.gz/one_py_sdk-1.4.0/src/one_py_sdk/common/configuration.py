import requests
import json
from logging import Logger
from one_py_sdk.shared.helpers.protobufhelper import DeserializeResponse


class ConfigurationApi:
    def __init__(self, env, auth):
        self.AppUrl = "/common/configuration/v2/"
        self.Environment = env
        self.Authentication = auth

    def GetSpreadsheetViews(self, authTwinId, configurationTypeId='bedc5ff2-bc8e-4916-9560-ccc28701d792'):
        url = f'{self.Environment}{self.AppUrl}?authTwinRefId={authTwinId}&configurationTypeId={configurationTypeId}'
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.configurations.items
