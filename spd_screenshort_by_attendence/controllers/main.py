# -*- coding: utf-8 -*-
from odoo import _, http
from odoo.exceptions import AccessError
from odoo.http import request
from odoo import fields
from odoo.tools.float_utils import float_round
from datetime import date, datetime, time

class MainSetup(http.Controller):

    def _get_geoip_response(self,latitude=False, longitude=False):
        return {
            'city': request.geoip.city.name or _('Unknown'),
            'country_name': request.geoip.country.name or request.geoip.continent.name or _('Unknown'),
            'latitude': latitude or request.geoip.location.latitude or False,
            'longitude': longitude or request.geoip.location.longitude or False,
            'ip_address': request.geoip.ip,
            'browser': request.httprequest.user_agent.browser,
            'mode': 'systray'
        }

    def _get_employee_info_response(self,employee):
        response = {}
        if employee:
            response = {
                'id': employee.id,
                'hours_today': float_round(employee.hours_today, precision_digits=2),
                'hours_previously_today': float_round(employee.hours_previously_today, precision_digits=2),
                'last_attendance_worked_hours': float_round(employee.last_attendance_worked_hours, precision_digits=2),
                'last_check_in': employee.last_check_in,
                'attendance_state': employee.attendance_state,
                'display_systray': employee.company_id.attendance_from_systray,
                'employee_name': employee.name,
                'employee_avatar': employee.image_256,
                'total_overtime': float_round(employee.total_overtime, precision_digits=2),
                'kiosk_delay': employee.company_id.attendance_kiosk_delay * 1000,
                'attendance': {'check_in': employee.last_attendance_id.check_in,
                               'check_out': employee.last_attendance_id.check_out},
                'overtime_today': request.env['hr.attendance.overtime'].sudo().search([
                    ('employee_id', '=', employee.id), ('date', '=', datetime.today()),
                    ('adjustment', '=', False)]).duration or 0,
                'use_pin': employee.company_id.attendance_kiosk_use_pin,
                'display_overtime': employee.company_id.hr_attendance_display_overtime
            }
        return response

    @http.route('/update_attandance', type='json', auth='user')
    def set_image_last_attandance(self,latitude=False, longitude=False,**kw):
        employee = request.env.user.employee_id
        geo_ip_response = self._get_geoip_response(latitude=latitude,
                                                   longitude=longitude)
        attendance_id = employee._attendance_action_change(geo_ip_response)
        check_in = kw['check_in']
        if attendance_id and 'check_in_out_image' in kw:
            sign = kw.get('check_in_out_image')[kw.get('check_in_out_image').index(",") + len(","):]
            if check_in:
                attendance_id.write({'check_in_image': sign})
            else:
                attendance_id.write({'check_out_image': sign})

        res = self._get_employee_info_response(employee)
        return res