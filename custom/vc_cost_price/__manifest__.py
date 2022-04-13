{
    'name': 'Vancamps - Cost Price',
    'version': '13.0.0.1',
    'author': 'Somko',
    'category': 'Vancamps',
    'description': """
        Adds 'Sales conditions' and 'company info' to the company. This information is used to display at the bottom
        of the reports.
    """,
    'summary': '',
    'website': 'http://www.somko.be',
    'images': [],
    'depends': ['mrp_account', 'purchase'],
    'data': [
        'views/product_views.xml',
        'wizard/vancamp_cost_price_compute_views.xml',
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
}
