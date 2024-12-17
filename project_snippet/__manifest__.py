{
    'name': 'Project Snippet',
    'version': '17.0',
    'category': 'Website',
    'summary': """Instagram Feed Snippet.""",
    'description': """Project Snippet.""",
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
}
