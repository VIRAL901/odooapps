from odoo import http
import json


class ProductCatalog(http.Controller):

    @http.route(['/update/purchase_order_items'], type='http', auth='public', website=True)
    def update_sale_order_items(self, **kwgs):
        purchase_order_env = http.request.env["purchase.order"]
        purchase_order_env.user_input_qty_pol(
            float(kwgs.get("quantity")), int(kwgs.get("product_id")), int(kwgs.get("purchase_id")))
        return json.dumps({"message": True})
