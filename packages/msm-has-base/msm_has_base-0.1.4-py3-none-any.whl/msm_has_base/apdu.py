from loguru import logger

PDU = dict[str, str]


def unpack(cmd: str) -> PDU:
    if len(cmd) % 2 != 0 or len(cmd) < 8:
        raise ValueError("Value is invalid")

    result = {}
    result['cla'] = cmd[:2]
    result['ins'] = cmd[2:4]
    result['p1'] = cmd[4:6]
    result['p2'] = cmd[6:8]

    if len(cmd) == 10:  # CLA INS P1 P2 Le
        result['le'] == cmd[8:10]

    if len(cmd) > 10:
        lc = cmd[8:10]
        result['lc'] = lc

        r = cmd[10:]
        if len(r) > int(lc, 16):
            result['le'] = r[-2:]
            result['data'] = r[:-2]
        else:
            result['data'] = r

    return result


def pack(pdu: PDU) -> str:
    _cla = pdu.get('cla')
    if not _cla:
        raise ValueError("The 'cla' can not be null")

    _ins = pdu.get('ins')
    if not _ins:
        raise ValueError("The 'ins' can not be null")

    _p1 = pdu.get('p1')
    if not _p1:
        raise ValueError("The 'p1' can not be null")

    _p2 = pdu.get('p2')
    if not _p2:
        raise ValueError("The 'p2' can not be null")

    _lc = pdu.get('lc', '')
    _data = pdu.get('data', '')
    if (not _lc and _data) or (_lc and not _data):
        raise ValueError(
            "The 'lc' and 'data' must be provided together")

    _le = pdu.get('le', '')

    return _cla + _ins + _p1 + _p2 + _lc + _data + _le
