{
    'name': 'Sales and Invoice Multi Currency Converison',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Sales and Invoice Multi Currency Converison',
    'description': """Sales and Invoice Multi Currency Conversion
            multi currency conversion
            sale multi currency conversion
            invoice multi currency conversion
    """,
    'depends': ['base','sale_management','account'],
    'data': [
        'views/sale_order.xml',
        'views/account_move.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'spd_sale_invoice_currency_conversion/static/src/components/tax_totals/*',
        ],
    },
    'author': 'SPD Solutions',
    'company': 'SPD Solutions',
    'maintainer': 'SPD Solutions',
    "images": ["static/description/banner.png"],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': 10,
    'currency': 'USD',
}
