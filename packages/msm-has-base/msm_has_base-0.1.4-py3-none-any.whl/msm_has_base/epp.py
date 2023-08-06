from abc import ABC, abstractmethod
from loguru import logger

from .utils import xor


class EPP(ABC):

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def clear_keys(self) -> None:
        pass

    @abstractmethod
    def write_device_key(self, hex_data: str) -> str:
        pass

    @abstractmethod
    def write_master_key(self, hex_data: str) -> str:
        pass

    @abstractmethod
    def write_pin_key(self, hex_data: str) -> str:
        pass

    @abstractmethod
    def write_mac_key(self, hex_data: str) -> str:
        pass

    @abstractmethod
    def read_pin(self, card_no: str, timeout: int = 60) -> str:
        pass

    @abstractmethod
    def on_key_press(self, cnt: int = 0) -> None:
        pass

    def read_mac(self, hex_data: str) -> str:
        if len(hex_data) != 16:
            raise NotImplementedError()

        mab = hex_data.upper().encode('ascii').hex()
        enc = xor(self.des_encrypt(mab[:16]), mab[16:])
        enc = self.des_encrypt(enc)
        return enc[:8].upper().encode('ascii').hex()

    @abstractmethod
    def des_encrypt(self, hex_data: str) -> str:
        pass

    @abstractmethod
    def des_decrypt(self, hex_data: str) -> str:
        pass

    def __enter__(self):
        self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.close()
        except Exception as e:
            logger.debug(e)

        return True
