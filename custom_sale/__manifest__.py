{
    'name': 'Sale Enhancements',
    'version': '18.0.0.1.0',
    'author': 'Bassant AbdElraouf',
    'category': 'Sales',
    'depends': ['base','sale','contacts','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_sale_order_view.xml',
        'views/product_discount_view.xml',
        'views/user_commission_view.xml',

    ],
    'application': False,
    'installable': True,
}
