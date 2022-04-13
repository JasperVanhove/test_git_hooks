# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_order_total = fields.Monetary(
        compute='_compute_sale_order_total',
    )

    def _compute_sale_order_total(self):
        sale_data = self.env['sale.order'].read_group(
            domain=[('partner_id', 'child_of', self.ids),
                    ('state', 'in', ['sale', 'done'])],
            fields=['partner_id', 'amount_untaxed'],
            groupby=['partner_id'])
        mapped_data = dict(
            [(m['partner_id'][0], m['amount_untaxed']) for m in
             sale_data])
        for partner in self:
            # let's obtain the partner id and all its child ids
            partner_ids = [partner.id] + partner.child_ids.ids
            # then we can sum for all the partner's child
            partner.sale_order_total = sum(
                mapped_data.get(child, 0) for child in partner_ids)
