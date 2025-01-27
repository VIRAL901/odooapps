from odoo import models,fields

class InheritSaleOrder(models.Model):
    _inherit='sale.order'

    plan_id = fields.Many2one('sale.subscription.plan')