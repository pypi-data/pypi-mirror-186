import requests
import json
from one_py_sdk.enterprise.authentication import AuthenticationApi
from one_py_sdk.shared.helpers.protobufhelper import DeserializeResponse
from one_interfaces import user_pb2 as User


class CoreApi:
    def __init__(self, env, auth: AuthenticationApi):
        self.AppUrl = "/enterprise/core/v1/"
        self.Environment = env
        self.Authentication = auth

    def GetUser(self, userId, expand=None):
        user = User.User()
        if (expand != None):
            url = self.Environment+self.AppUrl+"User/"+userId+"expand="+expand
        else:
            url = self.Environment+self.AppUrl+"User/"+userId
        headers = {'Authorization': self.Authentication.Token.access_token,
                   "Accept": "application/x-protobuf"}
        response = DeserializeResponse(requests.get(url, headers=headers))
        if response.errors:
            return response
        return response.content.users.items[0]


class UserHelper:
    def GetUserFromUserInfo(userInfo):
        jResponse = json.loads(userInfo.content)
