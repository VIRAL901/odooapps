
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_commission_forecast = fields.Boolean("Achievement Forecast", implied_group='spd_sale_commission.group_commission_forecast')
