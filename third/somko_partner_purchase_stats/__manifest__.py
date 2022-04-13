# -*- coding: utf-8 -*-
####################################################################
#
# © 2020-Today Somko Consulting (<http://www.somko.com>)
#
# License OPL-1 or later (https://www.odoo.com/documentation/user/11.0/legal/licenses/licenses.html)
#
####################################################################
{
    'name': "Detailed purchase stats",
    'version': '13.0.0.1',
    'category': 'Purchase',
    'summary': "Shows purchase order details for purchase stats on vendor",
    'description': "Shows purchase order details for purchase stats on vandor",
    'author': 'Somko',
    'website': 'www.somko.be',
    'depends': [
        'purchase',
        'purchase_stock',

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
