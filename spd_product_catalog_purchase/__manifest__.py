{
    "name": "Product Catalog in Purchase Odoo16",
    "version": "16.0.1.0.0",
    "category": "Purchase/Purchase",
    "summary": "Easily manage products in purchase orders directly from the product kanban view.",
    "description": """
Product Catalog for Odoo
=========================
This module enables users to add and remove products in purchase orders directly from the product kanban view. It streamlines the sales process, making it faster and more efficient.

Key Features:
- Add products to purchase orders from the product kanban view.
- Remove products from purchase orders with ease.
- Simplified user experience for managing purchase orders.
    """,
    "author": "SPD Solutions Pvt. Ltd.",
    "maintainer": "SPD Solutions Pvt. Ltd.",
    "depends": ['purchase'],
    "data": [
        "views/purchase_views.xml",
        "views/product_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "spd_product_catalog_purchase/static/src/**/*"
        ],
    },
    "images": ["static/description/banner.png"],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "auto_install": False,
}
