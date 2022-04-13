{
    'name': 'Vancamps - Supplier Email',
    'version': '13.0.0.1',
    'author': 'Somko',
    'category': 'Vancamps',
    'description': """
        Gives contacts separate emails for sales and purchases.
    """,
    'summary': '',
    'website': 'http://www.somko.be',
    'images': [],
    'depends': ['purchase'],
    'data': [
        'views/res_partner_views.xml',
        'data/mail_template_data.xml'
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
}
