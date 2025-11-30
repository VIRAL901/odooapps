{
    'name': 'Many2many Filter in Task(Calendar View)',
    'version': '18.0.0.1',
    'category': 'Extra Tools',
    'author': "SPD Solutions",
    'summary': 'Add Many2many Filter for Assignee in Tasks Calendar View',
    'description': """This module adds a Many2many filter in the task Calendar view. 
        It enhances the user experience by allowing filtering tasks by assignees.""",
    'depends': ['web', 'project'],
    'installable': True,
    'application': True,
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_task_calendar.xml',
    ],
}
