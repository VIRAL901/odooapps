{
    'name': 'Auto Generate Sale Order',
    'version': '15.0.1.0',
    'summary': 'Automatically generate Sale Order based on customer preferences at weekly, monthly, or yearly intervals.',
    'author': 'SPD Solutions Pvt. Ltd.',
    'license': 'LGPL-3',
    'category': 'Sale Order',
    'description': """
        Auto Generate Sale Order
        ===================
        This module allows you to automatically generate Sale Order for your customers based on their preferences. 
        Key Features:
        - Add a checkbox to enable Sale Order automation per customer.
        - Select intervals: Weekly, Monthly, or Yearly.
        - Automatic Sale Order generation using scheduled cron jobs.
        - Seamless integration with Odoo Sale.
        """,
    'depends': ['sale_management','contacts'],
    'images': ['static/description/banner.png'],
    'data':[
      'security/ir.model.access.csv',
       'data/so_cron.xml',
      'views/order_line_template.xml',
      'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'maintainer': 'SPD Solutions Pvt. Ltd.',
}
