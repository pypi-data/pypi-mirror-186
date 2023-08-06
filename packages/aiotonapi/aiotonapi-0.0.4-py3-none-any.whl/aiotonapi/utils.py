import base64
import struct
import libscrc


def raw_to_userfriendly(address, tag=0x11):
    workchain_id, key = address.split(':')
    workchain_id = int(workchain_id)
    key = bytearray.fromhex(key)

    short_ints = [j * 256 + i for i, j in zip(*[iter(key)] * 2)]
    payload = struct.pack(f'Bb{"H" * 16}', tag, workchain_id, *short_ints)
    crc = libscrc.xmodem(payload, )
    e_key = payload + struct.pack('>H', crc)

    return base64.urlsafe_b64encode(e_key).decode("utf-8")


def userfriendly_to_raw(address):
    k = base64.urlsafe_b64decode(address)[1:34]
    workchain_id = struct.unpack('b', k[:1])[0]
    key = k[1:].hex().upper()

    return f'{workchain_id}:{key}'


def nano_to_amount(value: int | float, precision: int) -> float:
    converted_value = round(value / 10 ** 9, 9)

    return float(f'{converted_value:.{precision}f}')


def amount_to_nano(value: int | float):
    return int(value * (10 ** 9))


def base64_to_text(text: str) -> str:
    return base64.b64decode(text).decode('utf-8')


def text_to_base64(text: str) -> str:
    return base64.b64encode(bytes(text, 'utf-8')).decode('utf-8')
