from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    auto_generate_purchase_order = fields.Boolean(string="Auto Generate PO", default=False)
    po_generation_interval = fields.Selection(
        [('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')],
        string="Purchase Generation Interval",
    )
    order_lines = fields.Many2one('order.line.template',string='Order Lines Template')