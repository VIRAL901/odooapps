{
    "name": "Audit Log",
    "summary": "Track and monitor user actions, HTTP sessions, and requests in Odoo 18.0.",
    "version": "18.0.1.0.0",
    "category": "Tools",
    "author": "SPD Solutions Pvt. Ltd.",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "data/ir_cron.xml",
        "views/auditlog_view.xml",
        "views/http_session_view.xml",
        "views/http_request_view.xml",
    ],
    "images": ["static/description/banner.png"],
    "price": 10.00,
    "currency": "USD",
    "installable": True,
    "application": True,
    "description": """
Audit Log for Odoo18
===================
The Audit Log module provides robust tracking and monitoring capabilities for user activities, HTTP sessions, and requests.

Key Features:
- Log user actions across the platform.
- Monitor HTTP sessions and identify active users.
- Track HTTP requests for enhanced debugging.
- Configurable security access for log visibility.

Use Cases:
- Enhance security by tracking sensitive operations.
- Debug issues using request and session data.

Technical Support:
------------------
For any assistance or customization requests, contact SPD Solutions Pvt. Ltd.
""",
}
