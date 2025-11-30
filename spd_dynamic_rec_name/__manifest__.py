{
    'name': 'Dynamic Record Name Configuration',
    'category': 'Tools',
    'summary': 'Configure dynamic record names with custom fields and separators.',
    'version': '18.0.1.0',
    'author': "SPD Solutions",
    'description': """
        Dynamic Record Name Configuration
        ==================================
        This module allows you to configure dynamic record names for any model in Odoo. 
        Key Features:
        - Configure the record name (rec_name) dynamically for each model.
        - Select multiple fields to form the record name.
        - Add custom separators between fields.

        Use this module to enhance the readability and organization of your records by tailoring record names to suit your business needs.
    """,
    'depends': ["base"],
    'data': [
        "security/ir.model.access.csv",
        "views/recname_description_view.xml",
    ],
    'images': ["static/description/banner.png"],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'maintainer': "SPD Solutions",
}
