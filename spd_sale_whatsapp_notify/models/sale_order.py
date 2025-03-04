from odoo import models, fields, _
from odoo.exceptions import ValidationError


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        rtn = super().action_confirm()
        phone = self.partner_id.phone
        model = self.env['ir.model'].sudo().search([('model', '=', 'sale.order')])
        template = self.env['whatsapp.template'].sudo().search(
            [('model_id', '=', model.id), ('status', '=', 'approved')], limit=1)
        if not template:
            raise ValidationError(
                _('Template Not Found'))
        composer = self.env['whatsapp.composer'].sudo().create({
            'wa_template_id': template.id,
            'phone': phone,
            'res_ids': str([self.id]),
            'res_model': 'sale.order'
        })
        composer.action_send_whatsapp_template()
        return rtn
