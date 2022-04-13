# -*- coding: utf-8 -*-
####################################################################
#
# © 2020-Today Somko Consulting (<http://www.somko.com>)
#
# License OPL-1 or later (https://www.odoo.com/documentation/user/11.0/legal/licenses/licenses.html)
#
####################################################################
{
    'name': "Detailed sales stats base",
    'version': '13.0.0.1',
    'category': 'Sales',
    'summary': "Sale order lines for sale stats",
    'description': """
        Sale order lines for sale stats
        (used by product_sale_stats and partner_sale_stats)
    """,
    'author': 'Somko',
    'website': 'www.somko.be',
    'depends': [
        'sale_stock'
    ],
    'data': [],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
