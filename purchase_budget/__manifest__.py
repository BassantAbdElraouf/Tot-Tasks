{
    'name': 'Purchase Budget',
    'version': '18.0.0.1.0',
    'author': 'Bassant AbdElraouf',
    'category': 'Purchases',
    'depends': ['base','purchase','hr','sale','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_budget_plan_view.xml',
        'views/purchase_budget_line_view.xml',
        'views/purchase_budget_consumption_view.xml',
        'views/purchase_budget_alert_view.xml',
    ],
    'application': False,
    'installable': True,
}
