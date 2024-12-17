from odoo import http
from odoo.http import request
import time


class WebsiteSnippetPage(http.Controller):

    @http.route('/project_snippet', type='http', auth='public', website=True)
    def project_snippet(self, status=None):
        config = request.env['project.configuration'].sudo().search([], limit=1)
        projects_per_row = config.projects_per_row if config else 3
        total_projects_display = config.total_projects_display if config else 0
        is_ascending = config.is_ascending_order if config else False

        if status and status != 'all':
            projects = request.env['project.project'].sudo().search([('state', '=', status),('website_publish','=',True)],
                                                                    limit=total_projects_display)
        else:
            projects = request.env['project.project'].sudo().search([('website_publish','=',True)],
                                                                    limit=total_projects_display)

        sorted_projects = sorted(
            projects,
            key=lambda p: p.name.lower(),  # Sort by name (case-insensitive)
            reverse=not is_ascending  # Reverse if descending order is required
        )

        values = {
            'sorted_projects': sorted_projects,
            'projects_per_row': projects_per_row,
            'total_projects_display':total_projects_display,
        }

        if request.httprequest.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return request.render('insta_feed_snippet.project_snippet', values)

        return request.render('insta_feed_snippet.project_snippet', values)

