import requests

from .models import *


class SigmaSMS:
    __debug: bool
    __token: str
    __base_url: str = 'https://online.sigmasms.ru/api/'

    def __init__(self, debug: bool, token: str):
        self.__debug = debug
        self.__token = token
        self.__headers: dict = {
            'Content-Type': 'application/json',
            'Authorization': self.__token
        }

    def send_sms(self, message: SMSMessage) -> SentMessage:
        if not self.__debug:
            url = f'{self.__base_url}sendings'
            response = requests.post(url, data=message.json(), headers=self.__headers)
            return SentMessage.parse_obj(response.json())
        else:
            return SentMessage.parse_obj({'id': '', 'recipient': message.recipient, 'status': StatusMessage.SENT})

    def get_user(self, user_id: str) -> dict:
        url = f'{self.__base_url}users/{user_id}'
        response = requests.get(url, headers=self.__headers)
        return response.json()
