# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    purchase_order_total = fields.Monetary(
        compute='_compute_purchase_order_total',
    )

    def _compute_purchase_order_total(self):
        r = {}
        if self.user_has_groups('purchase.group_purchase_manager'):
            r = dict([(g['product_tmpl_id'][0], g['price_total']) for g in
                      self.env['purchase.report'].read_group(
                          [
                              ('state', 'in', ['purchase', 'done']),
                              ('product_tmpl_id', 'in', self.ids),
                          ],
                          ['product_tmpl_id', 'price_total'],
                          ['product_tmpl_id'])])

        for product in self:
            product.purchase_order_total = r.get(product.id, 0)
