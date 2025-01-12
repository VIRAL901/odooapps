from odoo import models,fields

class InheritCrmLead(models.Model):
    _inherit='crm.lead'

    def generate_leads(self, interval):
        partners = self.env['res.partner'].search([
            ('auto_generate_lead', '=', True),
            ('lead_generation_interval', '=', interval)
        ])
        for partner in partners:
            lead_name = f'Lead for {partner.name} on {fields.Date.today()}'
            self.env['crm.lead'].create({
                'name': lead_name,
                'partner_id': partner.id,
            })