{
    "name": "School Management",
    "version": "18.0.1.0.0",
    "author": "SPD Solution Pvt. Ltd.",
    "category": "School Management",
    "license": "AGPL-3",
    "complexity": "easy",
    "summary": "A comprehensive module for managing school operations, including students, teachers, and parents.",
    "description": """
School Management
=================
This module provides a complete solution for managing schools in Odoo. Key features include:
- Student management with roll number assignment and class promotions.
- Teacher and parent management.
- Reports for identity cards, leaving certificates, and teacher IDs.
- Integration with HR, CRM, and Accounting modules.
- Predefined mail templates for notifications.
- Secure access controls for different user roles.
- Demo data for testing and exploration.
""",
    "images": ["static/description/banner.png"],
    "depends": ["hr", "crm", "account"],
    "data": [
        "security/school_security.xml",
        "security/ir.model.access.csv",
        "data/student_sequence.xml",
        "data/mail_template.xml",
        "wizard/terminate_reason_view.xml",
        "views/student_view.xml",
        "views/school_view.xml",
        "views/teacher_view.xml",
        "views/parent_view.xml",
        "wizard/assign_roll_no_wizard.xml",
        "wizard/move_standards_view.xml",
        "report/report_view.xml",
        "report/identity_card.xml",
        "report/leaving_certificate.xml",
        "report/teacher_identity_card.xml",
    ],
    "demo": ["demo/school_demo.xml"],
    "assets": {"web.assets_backend": ["/spd_school/static/src/scss/schoolcss.scss"]},
    "installable": True,
    "application": True,
    'price':30,
    'currency':'USD'
}
