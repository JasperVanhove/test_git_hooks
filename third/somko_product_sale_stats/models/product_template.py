# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sale_order_total = fields.Monetary(
        compute='_compute_sale_order_total',
    )

    def _compute_sale_order_total(self):
        r = {}
        if self.user_has_groups('sales_team.group_sale_salesman'):
            r = dict([(g['product_tmpl_id'][0], g['price_subtotal']) for g in
                      self.env['sale.report'].read_group(
                          [
                              ('state', 'in', ['sale', 'done']),
                              ('product_tmpl_id', 'in', self.ids),
                          ],
                          ['product_tmpl_id', 'price_subtotal'],
                          ['product_tmpl_id'])])

        for product in self:
            product.sale_order_total = r.get(product.id, 0)
