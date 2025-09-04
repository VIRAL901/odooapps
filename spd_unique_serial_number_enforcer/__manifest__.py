# -*- coding: utf-8 -*-
{
    'name': "Unique Lot/Serial Number Enforcer",
    'version': '17.0.1.0.0',
    'summary': "Prevents duplicate product serial/lot numbers across your inventory.",
    'description': """
        This module enforces strict uniqueness of all product serial and lot numbers in Odoo 18.
        Any attempt to create or modify a serial number that already exists will be blocked,
        ensuring complete traceability, compliance, and error-free stock management.
        Perfect for businesses that require robust tracking for warranty, recall, or quality assurance.
    """,
    'category': 'Inventory',
    'author': "SPD Solutions",
    'maintainer': "SPD Solutions",
    'license': 'LGPL-3',
    'depends': ['base','stock'],
    "images": ["static/description/banner.png"],
    'installable': True,
    'application': False,
    'auto_install': False,
}
