from odoo import models,fields,api

class OrderLineTemplate(models.Model):
    _name='order.line.template'
    _description='Order Line Template'

    partner_id = fields.Many2one('res.partner',string='Contact')
    order_line_ids = fields.One2many('order.line','template_id',string='Lines')
    name = fields.Char('Name')


class OrderLineTemplate(models.Model):
    _name = 'order.line'
    _description = 'Order Line'

    template_id = fields.Many2one('order.line.template', string='Template')
    product_id = fields.Many2one('product.product',string='Product')
    quantity = fields.Float(string='Quantity')
    price = fields.Float('Price')
    total = fields.Float('Total',compute='_compute_total',store=1)

    @api.depends('price','quantity')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.price * rec.quantity