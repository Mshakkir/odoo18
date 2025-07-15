from odoo import models, fields, api
import base64
import qrcode
from io import BytesIO
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    zatca_qr_code = fields.Binary("ZATCA QR", compute="_generate_zatca_qr", store=True)

    @api.depends('amount_total', 'amount_tax', 'invoice_date', 'partner_id', 'company_id')
    def _generate_zatca_qr(self):
        for rec in self:
            if not rec.company_id or not rec.company_id.vat:
                rec.zatca_qr_code = False
                continue

            def _encode_field(tag, value):
                data = bytes([tag, len(value)]) + value.encode('utf-8')
                return data

            qr_bytes = b''.join([
                _encode_field(1, rec.company_id.name or ""),
                _encode_field(2, rec.company_id.vat or ""),
                _encode_field(3, rec.invoice_date.strftime('%Y-%m-%d %H:%M:%S') if rec.invoice_date else ""),
                _encode_field(4, str(rec.amount_total)),
                _encode_field(5, str(rec.amount_tax))
            ])

            qr_base64 = base64.b64encode(qr_bytes)
            qr_img = qrcode.make(qr_base64.decode())
            buffer = BytesIO()
            qr_img.save(buffer, format="PNG")
            qr_data = base64.b64encode(buffer.getvalue())
            rec.zatca_qr_code = qr_data


    amount_discount = fields.Monetary(
        string="Discount Amount",
        currency_field='currency_id',
        compute='_compute_amount_discount',
        store=True
    )

    @api.depends('invoice_line_ids.custom_discount', 'invoice_line_ids.custom_qty', 'invoice_line_ids.custom_rate')
    def _compute_amount_discount(self):
        for move in self:
            total_discount = 0.0
            for line in move.invoice_line_ids:
                qty = line.custom_qty or 0.0
                rate = line.custom_rate or 0.0
                discount_pct = line.custom_discount or 0.0
                total_discount += (qty * rate) * (discount_pct / 100.0)
            move.amount_discount = total_discount

