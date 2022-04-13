{
    'name': 'Vancamps - Picking adjustments',
    'version': '13.0.0.1',
    'author': 'Somko',
    'category': 'Vancamps',
    'description': """
    """,
    'summary': '',
    'website': 'http://www.somko.be',
    'images': [],
    'depends': [
        'base',
        'account',
        'stock',
        'sale_stock',
        'web'
    ],
    'data': [
        'views/document_template.xml',
        'views/stock_move_line.xml',
        'views/report_delivery_slip.xml',
        'views/report_invoice_document.xml',
        'views/report_picking.xml',
        'wizard/stock_backorder_confirmation_views.xml'
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
}
