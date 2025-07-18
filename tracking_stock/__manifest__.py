{
    'name': 'Stock Enhancements',
    'version': '18.0.0.1.0',
    'author': 'Bassant AbdElraouf',
    'category': 'Stocks',
    'depends': ['base','sale','contacts','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_item_damage_view.xml',
        'views/stock_transfer_note_view.xml',
        'views/stock_location_restriction_view.xml',
        'views/stock_picking_temperature_log_view.xml',
    ],
    'application': False,
    'installable': True,
}
