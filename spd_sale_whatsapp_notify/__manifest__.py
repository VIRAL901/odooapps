{
    'name': 'Send WhatsApp Message on Sale Confirmation in Odoo17',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Automatically send a WhatsApp message when a Sale Order is confirmed.',
    'description': """
        This module allows automatic WhatsApp message notifications to customers 
        when a Sale Order is confirmed in Odoo 18. It integrates with the WhatsApp 
        module to streamline customer communication.
        Whatsapp Integration
        Whatsapp Message
        Whatsapp Message at Sales Confirmation
        Sale Order
        Sale Order Confirm
    """,
    'author': 'SPD Solutions',
    'maintainer': 'SPD Solutions',
    'company': 'SPD Solutions',
    'depends': ['base', 'sale_management', 'whatsapp'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': ['static/description/banner.png'],
    'sequence': -1,
}
