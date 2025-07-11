from odoo import models, fields
import base64
import qrcode
from io import BytesIO

class AccountMove(models.Model):
    _inherit = 'account.move'

    zatca_qr_code = fields.Char(compute="_generate_zatca_qr", store=False)

    def _generate_zatca_qr(self):
        for rec in self:
            qr_content = f"{rec.company_id.name}|{rec.company_id.vat}|{rec.invoice_date}|{rec.amount_total}|{rec.amount_tax}"
            qr_img = qrcode.make(qr_content)
            buffered = BytesIO()
            qr_img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            rec.zatca_qr_code = img_str
