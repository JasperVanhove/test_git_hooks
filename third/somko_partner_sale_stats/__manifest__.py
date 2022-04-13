# -*- coding: utf-8 -*-
####################################################################
#
# © 2020-Today Somko Consulting (<http://www.somko.com>)
#
# License OPL-1 or later (https://www.odoo.com/documentation/user/11.0/legal/licenses/licenses.html)
#
####################################################################
{
    'name': "Detailed sales stats",
    'version': '13.0.0.1',
    'category': 'Sales',
    'summary': "Shows sale order details for sale stats on customer",
    'description': "Shows sale order details for sale stats on customer",
    'author': 'Somko',
    'website': 'www.somko.be',
    'depends': [
        'sale_stock',
        'somko_sale_stats',
    ],
    'data': [
        'views/res_partner.xml'
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
