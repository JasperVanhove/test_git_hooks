# -*- coding: utf-8 -*-
####################################################################
#
# © 2019-Today Somko Consulting (<http://www.somko.com>)
#
# License OPL-1 or later (https://www.odoo.com/documentation/user/11.0/legal/licenses/licenses.html)
#
####################################################################
{
    'name': "Detailed purchase stats product",
    'version': '13.0.0.1',
    'category': 'Purchase',
    'summary': "Shows purchase order details for purchase stats on product",
    'description': "Shows purchase order details for purchase stats on product",
    'author': 'Somko',
    'website': 'www.somko.be',
    'depends': [
        'product',
        'purchase',
    ],
    'data': [
        'views/purchase_views.xml'
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
