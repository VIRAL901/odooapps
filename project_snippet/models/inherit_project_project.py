from odoo import models,fields,api
import base64

class InheritProjectProject(models.Model):
    _inherit='project.project'

    state = fields.Selection([('open','Open'),('process','Process'),('done','Done')],string='State')
    website_publish = fields.Boolean(string='Website Publish')
    project_image = fields.Binary('Image',store=1)

    @api.depends('project_image')
    def get_encoded_image(self):
        for record in self:
            if record.project_image:
                record.project_image_base64 = base64.b64encode(record.project_image).decode('utf-8')
            else:
                record.project_image_base64 = False

    project_image_base64 = fields.Char(compute='get_encoded_image')