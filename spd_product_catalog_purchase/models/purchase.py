from odoo import models, fields, _


class SaleOrder(models.Model):
    _inherit = "purchase.order"

    def action_add_from_catalog(self):
        sale_order_line_env = self.env["purchase.order.line"]
        product_env = self.env["product.product"]
        sale_products_domain = [('sale_ok', '=', True)]
        sale_products = product_env.search(sale_products_domain)
        sale_products.write({'purchase_catalog_quantity': 0})
        cart_products_details = sale_order_line_env.search(
            [('order_id', "=", self.id)])
        if self.order_line:
            for line in self.order_line:
                line.product_id.purchase_catalog_quantity = line.product_qty

        kanban_view_id = self.env.ref(
            'spd_product_catalog_purchase.product_view_kanban_catalog').id
        search_view_id = self.env.ref(
            'spd_product_catalog_purchase.product_view_search_catalog').id

        return {
            'type': 'ir.actions.act_window',
            'name': _('Choose Products'),
            'res_model': 'product.product',
            'views': [(kanban_view_id, 'kanban'), (False, 'form')],
            'search_view_id': [search_view_id, 'search'],
            'domain': sale_products_domain,
            'context': {
                '_quantity_change': True,
                'purchase_id': self.id,
                'create': False
            },
            'help': _("""<p class="o_view_nocontent_smiling_face">
                            Create new products
                        </p>""")
        }

    def pol_by_cart(self, operation, product_id, purchase_id):
        pol_object = self.env["purchase.order.line"]
        pol_data = dict()
        pol_data["product_id"] = product_id.id
        pol_data["order_id"] = purchase_id.id
        pol_data["price_unit"] = product_id.lst_price
        pol_data["product_uom"] = product_id.uom_id.id

        if operation == "add":
            pol_data["product_qty"] = product_id.purchase_catalog_quantity
            pol_data['sequence'] = max(purchase_id.order_line.mapped('sequence') or [0])
            pol_object.create(pol_data)
            return

        sol_ = pol_object.search(
            [('order_id', '=', purchase_id.id), ('product_id', '=', product_id.id)])

        if operation == "remove":
            if product_id.purchase_catalog_quantity == 0:
                sol_.unlink()
                return
            sol_["product_qty"] = product_id.purchase_catalog_quantity

        elif operation == "update":
            sol_["product_qty"] = product_id.purchase_catalog_quantity
        return

    def user_input_qty_pol(self, _qty, product_id, purchase_id):
        pol_object = self.env["purchase.order.line"]
        product_object = self.env["product.product"]
        cart_product_details = pol_object.search(
            [('order_id', "=", purchase_id), ("product_id", "=", product_id)])
        product_id = product_object.search([('id', '=', product_id)])
        if len(cart_product_details) > 0:
            if _qty == 0:
                product_id.purchase_catalog_quantity = 0
                cart_product_details.unlink()
                return
            cart_product_details.product_qty = _qty
            return
        else:
            pol_data = dict()
            pol_data["product_id"] = product_id.id
            pol_data["order_id"] = purchase_id
            pol_data["price_unit"] = product_id.lst_price
            pol_data["product_uom"] = product_id.uom_id.id
            pol_data["product_qty"] = _qty
            pol_object.create(pol_data)
            return


class PaleOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def action_add_from_catalog(self):
        order = self.env['purchase.order'].browse(self.env.context.get('order_id'))
        return order.action_add_from_catalog()
