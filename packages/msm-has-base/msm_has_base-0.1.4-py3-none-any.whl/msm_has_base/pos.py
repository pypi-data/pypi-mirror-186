import base64
import json
import requests

from abc import ABC, abstractmethod
from loguru import logger

from .card_reader import CardReader
from .epp import EPP

__TOKEN__ = '696939654e404e293635284634453324596a427a574938624e7056532b2c36'


class POSAPI(object):

    def __init__(self, url: str, token: str = None, pwd: str = None):
        super(POSAPI, self).__init__()
        self.url = url
        self.token = token
        self.pwd = pwd

    @property
    def certificate(self):
        if self.token and self.pwd:
            return (self.token, self.pwd)
        else:
            return tuple(bytes.fromhex(__TOKEN__).decode('utf-8').split('$'))

    def exec(self, params: dict) -> dict:
        logger.debug('request: {}', params)
        r = requests.post(self.url, auth=self.certificate,
                          data=params, timeout=15)
        json_text = base64.decodebytes(r.text.encode('utf-8')).decode('utf-8')
        result = json.loads(json_text)
        logger.debug('response: {}', result)
        return result


class POS(ABC):

    def __init__(self, bcr: CardReader, epp: EPP, device: str, merchant: str) -> None:
        super().__init__()
        self.bcr = bcr
        self.epp = epp
        self.device = device
        self.merchant = merchant

    @abstractmethod
    def sign_in(self) -> str:
        pass

    @abstractmethod
    def sign_out(self) -> None:
        pass

    @abstractmethod
    def pay(self, amount: int) -> dict:
        pass

    @abstractmethod
    def write_off(self, amount: int, order_no: str, batch: str, auth_code: str) -> dict:
        pass
