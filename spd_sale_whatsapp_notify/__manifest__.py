{
    'name': 'Send WhatsApp Message on Sale Confirmation in Odoo18',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Automatically send a WhatsApp message when a Sale Order is confirmed.',
    'description': """
        This module allows automatic WhatsApp message notifications to customers 
        when a Sale Order is confirmed in Odoo 18. It integrates with the WhatsApp 
        module to streamline customer communication.
    """,
    'author': 'SPD Solutions Pvt. Ltd.',
    'maintainer': 'SPD Solutions Pvt. Ltd.',
    'company': 'SPD Solutions Pvt. Ltd.',
    'depends': ['base', 'sale_management', 'whatsapp'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': ['static/description/banner.png'],
    'sequence': -1,
}
