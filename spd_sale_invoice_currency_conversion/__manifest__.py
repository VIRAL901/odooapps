{
    'name': 'Sales and Invoice Multi Currency Converison',
    'version': '18.0.0.0',
    'category': 'Sales',
    'summary': 'Sales and Invoice Multi Currency Converison',
    'description': """Sales and Invoice Multi Currency Converison""",
    'depends': ['base','sale_management','accountant'],
    'data': [
        'views/sale_order.xml',
        'views/account_move.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'spd_sale_invoice_currency_conversion/static/src/components/tax_totals/*',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
