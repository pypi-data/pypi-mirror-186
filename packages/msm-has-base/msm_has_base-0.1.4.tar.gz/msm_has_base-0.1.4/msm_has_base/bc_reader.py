import re

from abc import ABC, abstractmethod
from loguru import logger

from .pboc import PBOC


class BCInfo(object):

    def __init__(self, pan: str = '', pan_sn: str = '', track2: str = '', ic55: str = ''):
        super(BCInfo, self).__init__()
        self.pan = pan  # 主账号
        self.pan_sn = pan_sn  # 主账号序列号
        self.track2 = track2  # 二磁
        self.ic55 = ic55  # 55 域

    @property
    def pin_pan(self) -> str:
        r = re.sub(r'\D', '', self.pan)
        t = ''
        if len(r) <= 12:
            t = r
        else:
            t = r[-13:-1]

        return t.encode().rjust(16, b'\x00').hex()

    def __repr__(self) -> str:
        return 'pan: %s, pan sn: %s, pin pan: %s, track2: %s, ic55: %s' % (self.pan, self.pan_sn, self.pin_pan, self.track2, self.ic55)


class BCReader(ABC):

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def detect(self) -> None:
        pass

    @abstractmethod
    def prepare(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def read_info(self, amount: int, trade: str, merchant: str = None) -> BCInfo:
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.close()
        except Exception as e:
            logger.debug(e)

        return True


class CPUReader(BCReader):

    @abstractmethod
    def run(self, hex_cmd: str) -> str:
        pass


class RFCPUReader(CPUReader):

    def read_info(self, amount: int, trade: str, merchant: str = None) -> BCInfo:
        raise NotImplementedError()


class SmartReader(CPUReader):

    def read_info(self, amount: int, trade: str, merchant: str = None) -> BCInfo:
        records = {}

        _pboc = PBOC(self.run)

        r = _pboc.select('315041592e5359532e4444463031')
        logger.debug(r)

        sfi = r['88'][0]
        aids = _pboc.get_aids(sfi)

        for i in range(len(aids)):
            r = _pboc.select(aids[i], i > 0)

            pdol = r['9F38']
            r = _pboc.gpo(pdol, amount)

            aip = r['80'][:2]
            afls = r['80'][2:]
            records = _pboc.read_records(afls)

            records['82'] = aip

        d_9f13 = _pboc.get_data('9F13')
        records.update(d_9f13)

        d_9f36 = _pboc.get_data('9F36')
        records.update(d_9f36)

        cdol1 = records['8C']
        r = _pboc.ac(cdol1, amount, trade, merchant)
        records.update(r)

        logger.debug('records: {}', records)

        d_55_list = (
            b'\x9f\x26', b'\x08', records['9F26'],
            b'\x9f\x27', b'\x01', records['9F27'],
            b'\x9f\x10', (len(records['9F10'])).to_bytes(
                1, 'big'), records['9F10'],
            b'\x9f\x37', b'\x04', records['9F37'],
            b'\x9f\x36', b'\x02', records['9F36'],
            b'\x95', b'\x05', records['95'],
            b'\x9a', b'\x03', records['9A'],
            b'\x9c', b'\x01', records['9C'],
            b'\x9f\x02', b'\x06', records['9F02'],
            b'\x5f\x2a', b'\x02', records['5F2A'],
            b'\x82', b'\x02', records['82'],
            b'\x9f\x1a', b'\x02', records['9F1A'],
            b'\x9f\x03', b'\x06', records['9F03'],
            b'\x9f\x33', b'\x03', records['9F33']
        )

        result: BCInfo = BCInfo()
        result.ic55 = b''.join(d_55_list).hex()
        result.track2 = records['57'].hex()
        result.pan = records['5A'].hex()
        result.pan_sn = records['5F34'].hex()
        logger.debug('result: {}', result)
        return result
