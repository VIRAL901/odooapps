{
    "name": "Leaflet Map View (OpenStreetMap Integration)",
    "summary": "Enhance your Odoo 17 experience with a custom 'Leaflet Map' view. Display markers using the powerful Leaflet.js library.",
    "description": """
Leaflet Map View for Odoo 17
===================================
This module integrates the Leaflet.js library with Odoo 17, allowing you to add a custom map view (`leaflet_map`). The view is perfect for displaying geolocated data with markers on OpenStreetMap.
    """,
    "version": "17.0.1.0",
    "author": "SPD Solution Pvt. Ltd.",
    "license": "AGPL-3",
    "category": "Extra Tools",
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "data/ir_config_parameter.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "web_view_leaflet_map/static/src/**/*",
        ],
    },
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
    "uninstall_hook": "uninstall_hook",
}
