from odoo import models
from num2words import num2words
import base64
import qrcode
from io import BytesIO

class AccountMove(models.Model):
    _inherit = "account.move"

    def amount_to_text_ar(self, amount):
        return num2words(amount, lang='ar') + ' ريال سعودي فقط'

    def generate_qr_base64(self):
        company = self.company_id
        qr_data = f'{company.name}|{company.vat}|{self.invoice_date}|{self.amount_total}|{self.amount_tax}'
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue()).decode()
