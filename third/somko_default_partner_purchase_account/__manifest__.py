# -*- coding: utf-8 -*-
####################################################################
#
# © 2019-Today Somko Consulting (<http://www.somko.com>)
#
# License OPL-1 or later (https://www.odoo.com/documentation/user/11.0/legal/licenses/licenses.html)
#
####################################################################
{
    'name': 'Somko - Default Partner Purchase account',
    'version': '13.0.0.1',
    'author': 'Somko',
    'category': 'Accounting & Finance',
    'description': """ This module ensures that standard purchase invoices can be entered on the contact card. If a partner has been chosen on a purchase invoice, these standard purchase accounts are taken over.
    """,
    'summary': ' Automatic completion of invoice lines based on previously entered purchase accounts on the contact card.',
    'website': 'http://www.somko.be',
    'images': [],
    'depends': [
        'base', 'account'
    ],
    'data': [
        'security/ir.rule.xml',
        'views/partner_views.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
}
