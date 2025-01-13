from odoo import models,fields

class InheritCrmLead(models.Model):
    _inherit='sale.order'

    def generate_so(self, interval):
        partners = self.env['res.partner'].search([
            ('auto_generate_sale_order', '=', True),
            ('so_generation_interval', '=', interval)
        ])
        for partner in partners:
            lines = partner.order_lines.order_line_ids  # Adjust this to the correct field if different

            sale_order = self.env['sale.order'].create({
                'partner_id': partner.id,
                'state':'sale'
            })

            for line in lines:
                self.env['sale.order.line'].create({
                    'order_id': sale_order.id,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.quantity,
                    'price_unit': line.price,
                })