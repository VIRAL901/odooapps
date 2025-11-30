{
    'name': 'Auto Generate Purchase Order',
    'version': '16.0.1.0',
    'summary': 'Automatically generate Purchase Order based on customer preferences at weekly, monthly, or yearly intervals.',
    'author': 'SPD Solutions',
    'license': 'LGPL-3',
    'category': 'Purchase Order',
    'description': """
        Auto Generate Purchase Order
        ===================
        This module allows you to automatically generate Purchase Order for your customers based on their preferences. 
        Key Features:
        - Add a checkbox to enable Purchase Order automation per customer.
        - Select intervals: Weekly, Monthly, or Yearly.
        - Automatic Purchase Order generation using scheduled cron jobs.
        - Seamless integration with Odoo Purchase.
        """,
    'depends': ['purchase','contacts'],
    'images': ['static/description/banner.png'],
    'data':[
      'security/ir.model.access.csv',
      'data/po_cron.xml',
      'views/order_line_template.xml',
      'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'maintainer': 'SPD Solutions',
}
