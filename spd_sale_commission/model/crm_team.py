
from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    commission_plan_ids = fields.Many2many('sale.commission.plan', string="Commission Plan",
                                           help='Default commission plan for team members.')

    invoiced_target = fields.Float('Invoicing Target')
