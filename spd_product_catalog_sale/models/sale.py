from odoo import models, fields, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_add_from_catalog(self):
        sale_order_line_env = self.env["sale.order.line"]
        product_env = self.env["product.product"]
        sale_products_domain = [('sale_ok', '=', True)]
        sale_products = product_env.search(sale_products_domain)
        sale_products.write({'sale_catalog_quantity': 0})
        cart_products_details = sale_order_line_env.search(
            [('order_id', "=", self.id)])
        if self.order_line:
            for line in self.order_line:
                line.product_id.sale_catalog_quantity = line.product_uom_qty

        kanban_view_id = self.env.ref(
            'spd_product_catalog_sale.product_view_kanban_catalog').id
        search_view_id = self.env.ref(
            'spd_product_catalog_sale.product_view_search_catalog').id

        return {
            'type': 'ir.actions.act_window',
            'name': _('Choose Products'),
            'res_model': 'product.product',
            'views': [(kanban_view_id, 'kanban'), (False, 'form')],
            'search_view_id': [search_view_id, 'search'],
            'domain': sale_products_domain,
            'context': {
                '_quantity_change': True,
                'sale_id': self.id,
                'create': False
            },
            'help': _("""<p class="o_view_nocontent_smiling_face">
                            Create new products
                        </p>""")
        }

    def sol_by_cart(self, operation, product_id, sale_id):
        sol_object = self.env["sale.order.line"]
        sol_data = dict()
        sol_data["product_id"] = product_id.id
        sol_data["order_id"] = sale_id.id
        sol_data["price_unit"] = product_id.lst_price
        sol_data["product_uom"] = product_id.uom_id.id

        if operation == "add":
            sol_data["product_uom_qty"] = product_id.sale_catalog_quantity
            sol_data['sequence'] = max(sale_id.order_line.mapped('sequence') or [0])
            sol_object.create(sol_data)
            return

        sol_ = sol_object.search(
            [('order_id', '=', sale_id.id), ('product_id', '=', product_id.id)])

        if operation == "remove":
            if product_id.sale_catalog_quantity == 0:
                sol_.unlink()
                return
            sol_["product_uom_qty"] = product_id.sale_catalog_quantity

        elif operation == "update":
            sol_["product_uom_qty"] = product_id.sale_catalog_quantity
        return

    def user_input_qty_sol(self, _qty, product_id, sale_id):
        sol_object = self.env["sale.order.line"]
        product_object = self.env["product.product"]
        cart_product_details = sol_object.search(
            [('order_id', "=", sale_id), ("product_id", "=", product_id)])
        product_id = product_object.search([('id', '=', product_id)])
        if len(cart_product_details) > 0:
            if _qty == 0:
                product_id.sale_catalog_quantity = 0
                cart_product_details.unlink()
                return
            cart_product_details.product_uom_qty = _qty
            return
        else:
            sol_data = dict()
            sol_data["product_id"] = product_id.id
            sol_data["order_id"] = sale_id
            sol_data["price_unit"] = product_id.lst_price
            sol_data["product_uom"] = product_id.uom_id.id
            sol_data["product_uom_qty"] = _qty
            sol_object.create(sol_data)
            return


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def action_add_from_catalog(self):
        order = self.env['sale.order'].browse(self.env.context.get('order_id'))
        return order.action_add_from_catalog()
