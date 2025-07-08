import base64
import struct
from odoo import models

def _tlv(tag, value):
    tag = struct.pack('B', tag)
    length = struct.pack('B', len(value))
    return tag + length + value.encode('utf-8')

class QRZATCA(models.AbstractModel):
    _name = 'report.custom_sa_invoice.qr_helper'

    def generate_qr_base64(self, seller_name, vat_number, timestamp, total, vat_amount):
        elements = b''.join([
            _tlv(1, seller_name),
            _tlv(2, vat_number),
            _tlv(3, timestamp),
            _tlv(4, "{:.2f}".format(total)),
            _tlv(5, "{:.2f}".format(vat_amount)),
        ])
        return base64.b64encode(elements).decode()
