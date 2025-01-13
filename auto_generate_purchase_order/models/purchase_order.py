from odoo import models,fields


class InheritCrmLead(models.Model):
    _inherit='purchase.order'

    def generate_po(self, interval):
        partners = self.env['res.partner'].search([
            ('auto_generate_purchase_order', '=', True),
            ('po_generation_interval', '=', interval)
        ])
        for partner in partners:
            lines = partner.order_lines.order_line_ids

            purchase_order = self.env['purchase.order'].create({
                'partner_id': partner.id,
                'state':'purchase'
            })

            for line in lines:
                self.env['purchase.order.line'].create({
                    'order_id': purchase_order.id,
                    'product_id': line.product_id.id,
                    'product_qty': line.quantity,
                    'price_unit': line.price,
                })