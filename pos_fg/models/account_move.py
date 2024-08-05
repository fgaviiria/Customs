# -*- coding: utf-8 -*-
from odoo import models, fields, api
import base64
import io
import qrcode


class AccountMove(models.Model):
    _inherit = 'account.move'

    serial_number = fields.Char(string="Serial Number", compute='_serial', readonly=False)
    correlative_number = fields.Char(string="Correlative Number", compute='_correlative', readonly=False)

    @api.depends('payment_reference')
    def _serial(self):
        serial_number = self.payment_reference.split('/')

    @api.depends('payment_reference')
    def _correlative(self):
        correlative_number = self.payment_reference.split()

    def generate_qr_code(self):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(self)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return {'x_qr_invoice': img_str}
