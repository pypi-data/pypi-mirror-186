import requests
import json
from datetime import datetime, time, timedelta
from one_py_sdk.shared.helpers.protobufhelper import DeserializeResponse
from one_interfaces import user_pb2 as User
from one_interfaces import role_pb2 as role

import google


class AuthenticationApi:
    def __init__(self, env):
        self.Environment = env
        self.Token = Token()
        self.UserName = ""
        self.Password = ""
        self.User: User = User.User()
        self.IsAuthenticated = False

    def GetToken(self, user, password):
        data = {'username': user, 'password': password, 'grant_type': 'password', 'scope': 'FFAccessAPI openid',
                'client_id': 'VSTestClient', 'client_secret': '0CCBB786-9412-4088-BC16-78D3A10158B7'}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        url = self.Environment+"/connect/token"
        response = requests.post(url, headers=headers, data=data)
        if (response.status_code != 200):
            return ''
        self.__setToken(response)
        self.IsAuthenticated = True
        self.UserName = user
        self.Password = password
        return self.Token.access_token

    def GetUserInfo(self):
        headers = {'Accept': 'application/json',
                   "Authorization": self.Token.access_token}
        url = self.Environment+"/connect/userinfo"
        response = requests.get(url, headers=headers)
        self.__setInfo(response)
        return response.content

    def LoginResourceOwner(self, userName, password):
        data = {'username': userName, 'password': password, 'grant_type': 'password', 'scope': 'FFAccessAPI openid',
                'client_id': 'VSTestClient', 'client_secret': '0CCBB786-9412-4088-BC16-78D3A10158B7'}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        url = self.Environment+"/connect/token"
        response = requests.post(url, headers=headers, data=data)
        if (response.status_code != 200):
            return False
        self.__setToken(response)
        self.IsAuthenticated = True
        self.UserName = userName
        self.Password = password
        return True

    def Logout(self):
        headers = {'Accept': 'application/json',
                   "Authorization": self.Token.access_token}
        url = self.Environment+"/account/logout"
        response = requests.post(url, headers=headers)
        self.Token = Token()
        self.UserName = ""
        self.Password = ""
        self.User: User = User.User()
        self.IsAuthenticated = False

    def __setInfo(self, response):
        jResponse = json.loads(response.content)
        self.User.firstName.value = jResponse.get('given_name')
        self.User.lastName.value = jResponse.get('family_name')
        self.User.userName = jResponse.get('user_name')
        self.User.email.value = jResponse.get('email')
        self.User.tenantId = jResponse.get('ActiveTenantId')
        self.User.id = jResponse.get('sub')

    def __setToken(self, tokenResponse):
        token = Token()
        token.created = datetime.now()
        responseJson = json.loads(tokenResponse.content)
        self.IsAuthenticated = True
        token.token_type = responseJson['token_type']
        token.scope = responseJson['scope']
        token.access_token = token.token_type + \
            " " + responseJson['access_token']
        token.expires_in = token.created + \
            timedelta(seconds=responseJson['expires_in'])
        self.Token = token


class Token:
    def __init__(self):
        self.access_token: str
        self.expires_in: float
        self.token_type: str
        self.scope: str
        self.created: datetime

    def __repr__(self):
        return "Access token: %s, Created on: %s, Expires in: %s, Token Type: %s, Scope: %s  " % (self.access_token, self.created, self.expires_in, self.token_type, self.scope)
