from odoo import models, fields
# import base64
# import qrcode
# from io import BytesIO
from odoo import api

# class AccountMove(models.Model):
#     _inherit = 'account.move'
#
#     zatca_qr_code = fields.Char(compute="_generate_zatca_qr", store=False)
#
#     def _generate_zatca_qr(self):
#         for rec in self:
#             qr_content = f"{rec.company_id.name}|{rec.company_id.vat}|{rec.invoice_date}|{rec.amount_total}|{rec.amount_tax}"
#             qr_img = qrcode.make(qr_content)
#             buffered = BytesIO()
#             qr_img.save(buffered, format="PNG")
#             img_str = base64.b64encode(buffered.getvalue()).decode()
#             rec.zatca_qr_code = img_str
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    custom_sn = fields.Integer(string="S.N")
    custom_item = fields.Char(string="Item")
    custom_description = fields.Text(string="Description")
    custom_qty = fields.Float(string="Quantity")
    custom_unit = fields.Char(string="Unit")
    custom_rate = fields.Float(string="S. Rate")
    custom_discount = fields.Float(string="Discount (%)")
    custom_amount = fields.Float(string="Amount", compute='_compute_custom_amount', store=True)
    custom_vat_percent = fields.Float(string="VAT %")
    custom_vat_amount = fields.Float(string="VAT", compute='_compute_custom_amount', store=True)
    custom_total_price = fields.Float(string="Total Price", compute='_compute_custom_amount', store=True)
    @api.depends('custom_qty', 'custom_rate', 'custom_discount', 'custom_vat_percent')
    def _compute_custom_totals(self):
        for line in self:
            qty = line.custom_qty or 0.0
            rate = line.custom_rate or 0.0
            discount = line.custom_discount or 0.0
            vat_pct = line.custom_vat_percent or 0.0

            base_amount = qty * rate
            discount_amount = base_amount * (discount / 100.0)
            net_amount = base_amount - discount_amount
            vat_amount = net_amount * (vat_pct / 100.0)
            total = net_amount + vat_amount

            line.custom_amount = net_amount
            line.custom_vat_amount = vat_amount
            line.custom_total_price = total