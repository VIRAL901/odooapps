from odoo import http
import json


class ProdctCatalog(http.Controller):

    @http.route(['/update/sale_order_items'], type='http', auth='public', website=True)
    def update_sale_order_items(self, **kwgs):
        sale_order_env = http.request.env["sale.order"]
        sale_order_env.user_input_qty_sol(
            float(kwgs.get("quantity")), int(kwgs.get("product_id")), int(kwgs.get("sale_id")))
        return json.dumps({"message": True})
