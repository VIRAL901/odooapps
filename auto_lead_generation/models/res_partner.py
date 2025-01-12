from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    auto_generate_lead = fields.Boolean(string="Auto Generate Lead", default=False)
    lead_generation_interval = fields.Selection(
        [('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')],
        string="Lead Generation Interval",
    )