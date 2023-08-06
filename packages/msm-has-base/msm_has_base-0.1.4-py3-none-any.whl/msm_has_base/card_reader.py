import time

from .bc_reader import BCReader, BCInfo

READERS = tuple[BCReader]


class CardReader(object):

    def __init__(self, readers: READERS, timeout: int = 30):
        super(CardReader, self).__init__()
        self.timeout = timeout
        self.readers = readers

    def read_info(self, amount: int, trade: str, merchant: str = None) -> BCInfo:
        e_time = int(time.time()) + self.timeout
        while int(time.time()) < e_time:
            for reader in self.readers:
                with reader:
                    reader.detect()
                    reader.prepare()
                    return reader.read_info(amount, trade, merchant)

            time.sleep(0.1)

        raise RuntimeError('Failed to read card information')
