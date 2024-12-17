{
    'name': 'Instagram Feed Snippet',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': """Instagram Feed Snippet.""",
    'description': """Instagram Feed Snippet.""",
    'depends': ['website', 'sale_management','project'],
    'data': [
        'security/ir.model.access.csv',
        'views/search_snippet_templates.xml',
        'views/project_snippet.xml',
        'views/inherit_project_form.xml',
        'views/project_configuration.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    # 'assets': {
    #     'web.assets_frontend': [
    #         '/insta_feed_snippet/static/src/image/carousel.jpg',
    #         'insta_feed_snippet/static/src/js/caroursel.js',
    #     ],
    # },
}
