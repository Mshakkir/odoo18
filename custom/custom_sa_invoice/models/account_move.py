from odoo import models, fields, api
from .. import zatca_qr
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    zatca_qr_code = fields.Char("ZATCA QR Code", compute="_compute_zatca_qr", store=True)

    @api.depends('invoice_date', 'amount_total', 'amount_tax')
    def _compute_zatca_qr(self):
        for move in self:
            if not move.invoice_date:
                move.zatca_qr_code = ''
                continue

            seller_name = move.company_id.name or ''
            vat_number = move.company_id.vat or ''
            timestamp = move.invoice_date.strftime('%Y-%m-%dT%H:%M:%SZ')  # ISO 8601
            total = "%.2f" % move.amount_total
            vat = "%.2f" % move.amount_tax

            qr_data = zatca_qr.generate_zatca_qr(
                seller_name, vat_number, timestamp, total, vat
            )
            move.zatca_qr_code = qr_data
