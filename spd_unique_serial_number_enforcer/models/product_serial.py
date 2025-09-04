# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import ValidationError

class StockProductionLot(models.Model):
    _inherit = 'stock.lot'

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing_lot_id = self.env['stock.lot'].search([('name', '=', record.name),
                                                            ('id', '!=', record.id)], limit=1)
            if existing_lot_id:
                raise ValidationError(_(f'The Lot/Serial Number {record.name} already exists!'))