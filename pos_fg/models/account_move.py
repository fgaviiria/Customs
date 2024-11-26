# -*- coding: utf-8 -*-
from odoo import models, fields, api
import base64
import io
import qrcode


class AccountMove(models.Model):
    _inherit = 'account.move'

    serial_number = fields.Char(string="Serial Number", compute='_serial', readonly=True)
    correlative_number = fields.Char(string="Correlative Number", compute='_correlative', readonly=True)
    qr_str = fields.Char(compute='_generate_str')

    @api.depends()
    def _serial(self):
        self.serial_number = self.payment_reference.split('/')[0] + self.payment_reference.split('/')[1]

    @api.depends()
    def _correlative(self):
        self.correlative_number = self.payment_reference.split('/')[2]

    def _generate_str(self):
        self.qr_str = self.name + '| ' + self.partner_id.name + '| ' + str(self.invoice_date) + '| ' + str(self.amount_residual) + '| ' + str(self.amount_total)

    def generate_qr_code(self):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(self.qr_str)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return {'x_qr_invoice': img_str}
