{
    "name" : "Backend theme in Odoo18",
    "version" : "18.0.0.1",
    "category" : "theme",
    'summary': 'Change backend colors',
    "description": """
    This module for changing backend colors
    """,
    "depends" : ['base'],
    'assets': {
        'web.assets_backend': [
            'spd_backend_theme/static/src/css/backend.css',
        ],
    },
    'qweb': [],
    'author': 'SPD Solutions',
    'company': 'SPD Solutions',
    'maintainer': 'SPD Solutions',
    'license':'OPL-1',
    'price':10,
    'currency':"USD",
    "images": ["static/description/banner.png"],
    "auto_install": False,
    "installable": True,
}
