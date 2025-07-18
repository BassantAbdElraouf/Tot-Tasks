{
    'name': 'Purchase Note',
    'version': '18.0.0.1.0',
    'author': 'Bassant AbdElraouf',
    'category': 'Purchases',
    'depends': ['base','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
        'views/purchase_note_view.xml',
        'views/purchase_note_category_view.xml',
        'views/purchase_note_tag_view.xml',
        'views/purchase_note_attachment_view.xml',
    ],
    'application': False,
    'installable': True,
}
