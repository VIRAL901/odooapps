# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrAttendanceInherit(models.Model):
    _inherit = "hr.attendance"

    check_in_image = fields.Binary("Check In Image", attachment=True)
    check_out_image = fields.Binary("Check Out Image", attachment=True)
