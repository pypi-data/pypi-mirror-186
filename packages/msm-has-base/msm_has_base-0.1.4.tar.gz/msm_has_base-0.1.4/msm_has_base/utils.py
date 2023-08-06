def xor(a: str, b: str) -> str:
    ba = bytes.fromhex(a)
    bb = bytes.fromhex(b)

    result = b''
    for i in range(len(ba)):
        result += (ba[i] ^ bb[i]).to_bytes(1, 'big')

    return result.hex()
