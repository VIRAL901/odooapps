from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    auto_generate_sale_order = fields.Boolean(string="Auto Generate SO", default=False)
    so_generation_interval = fields.Selection(
        [('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')],
        string="Lead Generation Interval",
    )
    order_lines = fields.Many2one('order.line.template',string='Order Lines Template')