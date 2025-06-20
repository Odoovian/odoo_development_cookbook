{
    'name': "Hostel Management",
    'summary': "Manage Hostel easily",
    'description': "Efficiently manage the entire residential facility in the school.",
    # Supports reStructuredText(RST) format (description is Deprecated),
    'author': "Ayesha Siddika Suchi (Odoovian)",
    'website': "https://odoovian.odoo.com/",
    'category': 'Hostel Management/Hostel',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        "data/data.xml",
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel.xml",
        "views/hostel_room.xml",
        "views/hostel_student.xml",
        "views/hostel_amenities.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'web/static/src/xml/**/*',
        ],
    },
    'demo': ['demo.xml'],
    'application': True,
    'installable': True,
}
