{
    'name': 'Auto Generate Leads',
    'version': '15.0.1.0',
    'summary': 'Automatically generate leads based on customer preferences at weekly, monthly, or yearly intervals.',
    'author': 'SPD Solutions Pvt. Ltd.',
    'license': 'LGPL-3',
    'category': 'Customer Relationship Management (CRM)',
    'description': """
        Auto Generate Leads
        ===================
        This module allows you to automatically generate leads for your customers based on their preferences. 
        Key Features:
        - Add a checkbox to enable lead automation per customer.
        - Select intervals: Weekly, Monthly, or Yearly.
        - Automatic lead generation using scheduled cron jobs.
        - Seamless integration with Odoo CRM.
        """,
    'depends': ['crm'],
    'data': [
        'data/lead_cron.xml',
        'views/res_partner_views.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'maintainer': 'SPD Solutions Pvt. Ltd.',
}
