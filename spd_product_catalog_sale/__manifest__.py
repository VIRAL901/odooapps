{
    "name": "Product Catalog in Sales Odoo16",
    "version": "16.0.1.0.0",
    "category": "Sales/Sales",
    "summary": "Easily manage products in sales orders directly from the product kanban view.",
    "description": """
Product Catalog for Odoo
=========================
This module enables users to add and remove products in sales orders directly from the product kanban view. It streamlines the sales process, making it faster and more efficient.

Key Features:
- Add products to sales orders from the product kanban view.
- Remove products from sales orders with ease.
- Simplified user experience for managing sales orders.
    """,
    "author": "SPD Solutions Pvt. Ltd.",
    "maintainer": "SPD Solutions Pvt. Ltd.",
    "depends": ["sale",'sale_management'],
    "data": [
        "views/sale_views.xml",
        "views/product_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "spd_product_catalog_sale/static/src/**/*"
        ],
    },
    "images": ["static/description/banner.png"],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "auto_install": False,
}
