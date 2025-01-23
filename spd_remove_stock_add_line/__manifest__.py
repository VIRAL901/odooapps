{
    'name': 'Hide Add a Line in Delivery',
    'version': '17.0.1.0',
    'description': 'This module customizes the delivery order to hide the "Add a Line" option.',
    'summary': 'Hides the "Add a Line" option in delivery orders to prevent adding lines manually.',
    'author': "SPD Solutions Pvt. Ltd.",
    'license': 'LGPL-3',
    'category': 'Inventory/Delivery',
    'depends': [
        'stock',
    ],
    'assets': {
        'web.assets_backend': [
            'spd_remove_stock_add_line/static/src/js/hide_add_line.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
