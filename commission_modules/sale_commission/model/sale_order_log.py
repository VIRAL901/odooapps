from odoo import models,fields

class InheritSaleOrderLog(models.Model):
    _inherit='sale.order.log'

    plan_id = fields.Many2one('sale.subscription.plan',related='order_id.plan_id',store=True)