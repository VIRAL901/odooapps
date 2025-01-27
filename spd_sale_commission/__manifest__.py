{
    'name': 'Sales Commission in Odoo17',
    'version': '17.0',
    'category': 'Sales/Commission',
    'sequence': 1,
    'summary': "Manage your salespersons' commissions in Odoo17",
    'description': """
    """,
    'depends': ['sale_management','sale_subscription'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/sale_commission_settings.xml',
        'wizard/sale_commission_add_multiple_user.xml',
        'views/sale_commission_plan_view.xml',
        'views/sale_commission_achievement_view.xml',
        'views/sale_commission_forecast_view.xml',
        'views/crm_team_views.xml',
        'report/commission_report.xml',
        'report/achievement_report.xml',
        'views/sale_commission_menu.xml',
    ],
    'demo': [
        'data/sale_commission_demo.xml'
    ],
    'installable': True,
    'license': 'OEEL-1',
    'price':5,
    'currency':'USD',
    'assets': {
        'web.assets_backend': [
            'spd_sale_commission/static/src/js/commission_plan_graph/commission_plan_graph.js',
            'spd_sale_commission/static/src/js/commission_plan_graph/commission_plan_graph.scss',
            'spd_sale_commission/static/src/js/commission_plan_graph/commission_plan_graph.xml',
        ],
    }
}
