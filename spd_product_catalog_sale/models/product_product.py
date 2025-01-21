from odoo import models, fields, _


class Product(models.Model):
    _inherit = "product.product"

    sale_catalog_quantity = fields.Float()

    def action_open_product_edit_kanban(self):
        form_view = self.env.ref(
            'product.product_normal_form_view')
        return {
            'type': 'ir.actions.act_window',
            'name': _('Edit Product'),
            'res_model': 'product.product',
            'res_id': self.id,
            'views': [(form_view.id, 'form')],
            'target': 'self'
        }

    def utilizable_cart_details(self):
        context = self._context.copy() or {}
        cart_object = self.env["sale.order.line"]
        cart_details = dict()
        total_count = cart_object.search_count(
            [('product_id', '=', self.id),
             ('order_id', '=', context.get('sale_id'))])
        cart_details["total_count"] = total_count
        cart_data = cart_object.search(
            [('product_id', '=', self.id),
             ('order_id', '=', context.get('sale_id'))])
        cart_details["cart_data"] = cart_data
        return cart_details

    def initiate_sol(self, operation, sale_id):
        so_object = self.env["sale.order"]
        sale_object = so_object.search([("id", "=", sale_id)])
        if operation == "add":
            so_object.sol_by_cart(operation, self, sale_object)
        elif operation == "remove":
            so_object.sol_by_cart(operation, self, sale_object)
        elif operation == "update":
            so_object.sol_by_cart(operation, self, sale_object)

    def action_set_quantity_sale_order(self, quantity, operation=None):
        context = self._context.copy() or {}
        cart_details = self.utilizable_cart_details()
        if operation == "remove":
            self.sale_catalog_quantity -= quantity
            if cart_details.get("total_count") != 0:
                if self.sale_catalog_quantity == 0:
                    sale_order_id = cart_details.get("cart_data").order_id
                    self.env['sale.order'].user_input_qty_sol(0, self.id, sale_order_id.id)
                else:
                    self.initiate_sol("remove", context.get("sale_id"))
        else:
            self.sale_catalog_quantity += quantity
            if cart_details.get("total_count") != 0:
                self.initiate_sol("update", context.get("sale_id"))
            else:
                self.initiate_sol("add", context.get("sale_id"))

    def action_btn_remove_quantity(self):
        if self.sale_catalog_quantity == 0:
            self.sale_catalog_quantity = 0
            return
        return self.action_set_quantity_sale_order(1, operation="remove")

    def action_btn_add_quantity(self):
        return self.action_set_quantity_sale_order(1, operation="add")

    def action_remove_product_so_line(self):
        return self.action_set_quantity_sale_order(self.sale_catalog_quantity, operation="remove")

    def action_add_product_so_line(self):
        return self.action_set_quantity_sale_order(1, operation="add")
