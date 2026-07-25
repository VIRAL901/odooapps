{
    'name': 'Show Edit Save Button On Form View | Show Edit Save Buttons On Form View | Edit and Save Button',
    'version': '19.0.1.0.0',
    'summary': 'Show Edit Save Button On Form View. Classic Edit & Save Mode for Odoo | Edit Button | Show Edit Button | Show Edit Save Button On Form View | Edit Button In Form | Edit Save Button In Odoo | Edit Save Button | Edit Form Odoo | Show Edit Save Button On Form View | Classic Edit Save Workflow | Ninja Odoo Form Edit | Classic Edit & Save Mode for Odoo | Edit Save Button Like Odoo 15 | Edit Save Mode (Restrict Auto Edit-Save)',
    'description': """
This module enhances the Odoo user experience by introducing dedicated **Edit**, **Save**, 
and **Discard** buttons directly on form views.

By default, Odoo automatically switches between read and edit modes, which can sometimes lead 
to accidental data changes. This module provides a more controlled and user-friendly workflow, 
allowing users to explicitly decide when to edit and when to save records.

✨ **Key Features**
✔ Adds separate Edit, Save, and Discard buttons on form views  
✔ Prevents accidental modifications to records  
✔ Improves usability and data control  
✔ Seamless integration with Odoo 18 backend  
✔ Lightweight and performance-friendly  

🎯 **Benefits**
• Clear edit workflow for users  
• Better control over record updates  
• Ideal for administrative and operational users  
• Works with all standard and custom form views  

. Edit button
. Save Button
. edit and save button on form view
. edit save button

This module is perfect for businesses that require **precision, safety, and clarity** while 
editing records in Odoo.
""",
    'author': 'SPD Solutions',
    'company': 'SPD Solutions',
    'maintainer': 'SPD Solutions',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'web', 'project'],
    'category': 'Tools',
    'data':[
        'views/views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            '/spd_edit_save_button/static/src/views/form/form_controller.xml',
            '/spd_edit_save_button/static/src/views/form/form_controller.js',
        ]
    },
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
    'price':15,
    'currency':'USD'
}
