# -*- coding: utf-8 -*-
{
    'name': "Face Recognition Attendance System in Odoo17",
    'summary': """
        This module enhances security by capturing employee images during manual check-in and check-out times,
        displaying the captured image on the employee attendance line.
    """,

    'description': """
        This module uses video streaming to capture images for attendance tracking and employee verification.
        The system captures images at both check-in and check-out.
    """,
    'images': ['static/description/banner.png'],
    'author': 'SPD Solutions Pvt. Ltd.',
    'category': 'Human Resources',
    'version': '17.0.0.1',
    'license': 'AGPL-3',
    'depends': ['base', 'hr_attendance', 'hr_org_chart'],
    'data': [
        'views/hr_attendance_view.xml',
    ],
    'price': 20.00,
    'currency': 'USD',
    'assets': {
        'web.assets_backend': [
            'spd_screenshort_by_attendence/static/src/components/attendance_menu/attendance_ss.xml',
            'spd_screenshort_by_attendence/static/src/components/attendance_menu/my_attendance_ss.js',
            'spd_screenshort_by_attendence/static/src/components/attendance_menu/style.css',
        ],
    },
    'models': [
        'hr.attendance',
    ],
}


