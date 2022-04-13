# -*- coding: utf-8 -*-
####################################################################
#
# © 2019-Today Somko Consulting (<http://www.somko.com>)
#
# License OPL-1 or later (https://www.odoo.com/documentation/user/11.0/legal/licenses/licenses.html)

####################################################################
{
    'name': 'Somko - Product Pricelist',
    'version': '13.0.0.1',
    'author': 'Somko',
    'category': 'Sales',
    'description': """
    Adds an pricelist overview to the product template.
    """,
    'website': 'https://www.somko.be',
    'images': [],
    'depends': ['product'],
    'data': [
        'views/product_template.xml',
        'wizards/pricelist_wizard.xml'
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
}