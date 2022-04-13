{
    'name': 'Sale Picking State',
    'summary': 'Add the status of all the outgoing picking'
    ' in the purchase order',
    'version': '11.0.1.0.0',
    'category': 'Sale Management',
    'website': 'http://www.somko.be',
    'author': 'Somko',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale',
        'stock',
        'sale_stock',
    ],
    'data': [
        'views/sale_order_view.xml',
    ]
}
