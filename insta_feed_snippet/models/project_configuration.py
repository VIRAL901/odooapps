from odoo import models,fields

class ProjectConfigiration(models.Model):
    _name = 'project.configuration'
    _description = 'Project Configuration'

    projects_per_row = fields.Integer(
        string="Projects Per Row",
        help="Number of projects displayed per row on the page."
    )

    total_projects_display = fields.Integer(
        string="Total Projects Displayed",
        help="The maximum number of projects shown on the website."
    )

    is_ascending_order = fields.Boolean(
        string="Display in Ascending Order",
        help="If checked, projects will be displayed in ascending order. If unchecked, they will be displayed in descending order."
    )

