
import base64
from io import BytesIO

def _encode_tlv(tag, value):
    tag = bytes([tag])
    length = bytes([len(value.encode('utf-8'))])
    return tag + length + value.encode('utf-8')

def generate_zatca_qr(seller_name, vat_number, timestamp, total, vat_total):
    tlv = b''.join([
        _encode_tlv(1, seller_name),
        _encode_tlv(2, vat_number),
        _encode_tlv(3, timestamp),
        _encode_tlv(4, total),
        _encode_tlv(5, vat_total),
    ])
    return base64.b64encode(tlv).decode('utf-8')
