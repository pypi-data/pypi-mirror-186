from datetime import datetime
import requests
import json
from one_py_sdk.enterprise.authentication import AuthenticationApi
from one_py_sdk.shared.helpers.protobufhelper import DeserializeResponse


class HistorianApi:
    def __init__(self, env, auth: AuthenticationApi):
        self.Environment = env
        self.Authentication = auth
        self.AppUrl = "/historian/data/v1/"

    def GetHistorianData(self, twinRefId, date: datetime):
        date = f'{str(date.date())}T{str(date.time())}Z'
        url = f'{self.Environment}{self.AppUrl}{twinRefId}/{date}'
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.historianDatas.items

    def GetHistorianDataRange(self, twinRefId, startTime: datetime, endTime: datetime):
        startString = f'{str(startTime.date())}T{str(startTime.time())}'
        endString = f'{str(endTime.date())}T{str(endTime.time())}'
        url = f'{self.Environment}{self.AppUrl}{twinRefId}?startTime={startString}&endTime={endString}'
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.historianDatas.items
