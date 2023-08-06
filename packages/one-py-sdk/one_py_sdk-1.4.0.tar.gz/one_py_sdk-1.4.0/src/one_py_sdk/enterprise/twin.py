import requests
import json
from one_py_sdk.enterprise.authentication import AuthenticationApi
from one_py_sdk.shared.helpers.protobufhelper import DeserializeResponse
import uuid


class DigitalTwinApi:
    def __init__(self, env, auth: AuthenticationApi):
        self.AppUrl = "/enterprise/twin/v1/"
        self.Environment = env
        self.Authentication = auth

    def Get(self, twinRefId: str):
        url = self.Environment+self.AppUrl+"DigitalTwin/Ref/"+twinRefId
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.DigitalTwins.items

    def GetTwinMeasurementsByRefId(self, twinRefId):
        url = self.Environment+self.AppUrl+"DigitalTwin/Ref/"+twinRefId
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return json.loads(response.content.DigitalTwins.items[0].twinData.value).get('measurement')

    def GetTwinData(self, twinRefId):
        url = self.Environment+self.AppUrl+"DigitalTwin/Ref/"+twinRefId
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return json.loads(response.content.DigitalTwins.items[0].twinData.value)

    def TwinMeasurements(self, twinRefId, twinMeasurements):
        try:
            usefulDictionary = {"Telemetry Id": twinRefId,
                                "Value": twinMeasurements['value'],
                                "String Value": twinMeasurements['stringValue'],
                                "Timestamp": twinMeasurements['timestamp'].get('jsonDateTime'),
                                "TelemetryPath": self.findTelemetryPath(twinRefId)}
            return usefulDictionary
        except (TypeError):
            return ("No twin data found for "+twinRefId)

    def GetDigitalTwinTypes(self):
        requestId = uuid.uuid4()
        url = self.Environment+self.AppUrl + \
            "DigitalTwinType?requestId="+str(requestId)
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.digitalTwinTypes.items

    def GetDigitalTwinType(self, twinTypeId: str):
        requestId = uuid.uuid4()
        url = f'{self.Environment}{self.AppUrl}DigitalTwinType/{twinTypeId}?requestId={str(requestId)}'
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.digitalTwinTypes.items

    def GetDigitalTwinSubtypes(self):
        requestId = uuid.uuid4()
        url = self.Environment+self.AppUrl + \
            "DigitalTwinSubType?requestId="+str(requestId)
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.digitalTwinSubtypes.items

    def GetDescendantsByType(self, twinRefId: str, twinTypeId: str, items=True):
        requestId = uuid.uuid4()
        url = self.Environment+self.AppUrl+"DigitalTwin/Ref/"+twinRefId + \
            "/Type/"+twinTypeId+"/Descendants?requestId="+str(requestId)
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        if items:
            return response.content.DigitalTwins.items
        else:
            return response.content.DigitalTwins

    def GetDescendantsBySubType(self, twinRefId: str, twinSubtypeId: str):
        requestId = uuid.uuid4()
        url = self.Environment+self.AppUrl+"DigitalTwin/Ref/"+twinRefId + \
            "/Subtype/"+twinSubtypeId+"/Descendants?requestId="+str(requestId)
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.DigitalTwins.items

    def GetDescendants(self, twinRefId: str):
        requestId = uuid.uuid4()
        url = self.Environment+self.AppUrl+"DigitalTwin/Ref/" + \
            twinRefId+"/Descendants?requestId="+str(requestId)
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.DigitalTwins.items

    def GetDescendantsByRefByCategory(self, twinRefId: str, categoryId: int, items=True):
        requestId = uuid.uuid4()
        url = f'{self.Environment}{self.AppUrl}DigitalTwin/Ref/{twinRefId}/Category/{categoryId}/Descendants?requestId={str(requestId)}'
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        if items:
            return response.content.DigitalTwins.items
        else:
            return response.content.DigitalTwins

    def FindTelemetryPath(self, twinRefId):
        statusCode = ""
        twinPath = []
        while (True):
            url = self.Environment+self.AppUrl + \
                "DigitalTwin/Ref/"+str(twinRefId)
            headers = {'Authorization': self.Authentication.Token.access_token,
                       "Accept": "application/x-protobuf"}
            response = DeserializeResponse(requests.get(url, headers=headers))
            if (response.statusCode != 200):
                break
            twinRefId = response.content.DigitalTwins.items[0].parentTwinReferenceId.value
            twinPath.append(response.content.DigitalTwins.items[0].name.value)
        twinPathString = ""
        while (len(twinPath) > 0):
            twinPathString = twinPathString+str(twinPath.pop())+"/"
        return twinPathString
