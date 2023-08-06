import requests

from .models import TypeMessage, StatusMessage, Response


class SigmaSMS:
    __debug: bool
    __token: str
    __sender: str
    __base_url: str = 'https://online.sigmasms.ru/api/'

    def __init__(self, debug: bool, sender: str, api_token: str):
        self.__debug = debug
        self.__sender = sender
        self.__token = api_token
        self.__headers: dict = {
            'Content-Type': 'application/json',
            'Authorization': self.__token
        }

    def send_sms(self, recipient: str, text: str) -> Response:
        if not self.__debug:
            url = f'{self.__base_url}sendings'
            message = {
                "recipient": recipient,
                "type": TypeMessage.SMS.value,
                "payload": {
                    "sender": self.__sender,
                    "text": text
                }
            }
            response = requests.post(url, json=message, headers=self.__headers)
            return Response(response.status_code, response.json())
        else:
            return Response(200, {'id': '', 'recipient': recipient, 'status': StatusMessage.SENT})

    def get_user(self, user_id: str) -> Response:
        url = f'{self.__base_url}users/{user_id}'
        response = requests.get(url, headers=self.__headers)
        return Response(response.status_code, response.json())
