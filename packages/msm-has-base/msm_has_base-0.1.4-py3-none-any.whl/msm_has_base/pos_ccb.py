from loguru import logger

from .pos import POS, POSAPI
from .card_reader import CardReader
from .epp import EPP


class CCBPos(POS):

    def __init__(self, bcr: CardReader, epp: EPP, api: POSAPI, device: str, merchant: str) -> None:
        super().__init__(bcr, epp, device, merchant)
        self.api = api

    def sign_in(self) -> str:
        resp = self.api.exec({
            "tranCode": "0800",
            "device": self.device,
            "merchant": self.merchant
        })

        with self.epp:
            r = self.epp.write_pin_key(resp['wkey'])
            logger.debug('write_pin_key {}, {}', r, resp['wsum'])

            if r.lower() != resp['wsum']:
                raise RuntimeError('Failed to write PIN key')

            r = self.epp.write_mac_key(resp['mkey'])
            logger.debug('write_mac_key {}, {}', r, resp['msum'])
            if r.lower() != resp['msum']:
                raise RuntimeError('Failed to write MAC key')

        return resp['batch']

    def sign_out(self) -> None:
        self.api.exec({
            "tranCode": "0820",
            "device": self.device
        })

    def pay(self, amount: int) -> dict:
        if amount < 1:
            raise RuntimeError('The amount must be greater than zero')

        bci = self.bcr.read_info(amount, '00')
        logger.debug("bci: {}", bci)

        if not bci:
            raise RuntimeError('Failed to read card information')

        pin = None
        with self.epp:
            pin = self.epp.read_pin(bci.pin_pan)
            logger.debug('pin: {}', pin)

        if not pin:
            raise RuntimeError('Failed to read PIN')

        resp = self.api.exec({
            "tranCode": "02002",
            'amount': amount,
            "accountSN": bci.pan_sn,
            "track2": bci.track2,
            "device": self.device,
            "password": pin,
            "ic55": bci.ic55
        })

        mac = None
        with self.epp:
            mac = self.epp.read_mac(resp['data'])
            logger.debug('mac: {}', mac)

        if not mac:
            raise RuntimeError('Failed to calculate MAC')

        result = self.api.exec({
            "tranCode": "0000",
            "id": resp['id'],
            "mac": mac
        })

        return result

    def write_off(self, amount: int, order_no: str, batch: str, auth_code: str) -> dict:
        if amount < 1:
            raise RuntimeError('The amount must be greater than zero')

        bci = self.bcr.read_info(amount, '00')
        logger.debug("bci: {}", bci)

        if not bci:
            raise RuntimeError('Failed to read card information')

        resp = self.api.exec({
            "tranCode": "04001",
            "device": self.device,
            "accountSN": bci.pan_sn,
            "track2": bci.track2,
            "ic55": bci.ic55,
            'amount': amount,
            'orderNo': order_no,
            'batch': batch,
            'authCode': auth_code,
            'merchant': self.merchant
        })

        mac = None
        with self.epp:
            mac = self.epp.read_mac(resp['data'])
            logger.debug('mac: {}', mac)

        if not mac:
            raise RuntimeError('Failed to calculate MAC')

        result = self.api.exec({
            "tranCode": "0000",
            "id": resp['id'],
            "mac": mac
        })

        return result
