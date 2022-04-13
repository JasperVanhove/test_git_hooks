# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    purchase_order_total = fields.Monetary(
        compute='_compute_purchase_order_total',
    )

    def _compute_purchase_order_total(self):
        purchase_data = self.env['purchase.order'].read_group(
            domain=[('partner_id', 'child_of', self.ids),
                    ('state', 'in', ['purchase', 'done'])],
            fields=['partner_id', 'amount_untaxed'],
            groupby=['partner_id'])
        mapped_data = dict(
            [(m['partner_id'][0], m['amount_untaxed']) for m in
             purchase_data])
        for partner in self:
            # het the partner id and all its child ids
            partner_ids = [partner.id] + partner.child_ids.ids
            # sum for all the partner's child
            partner.purchase_order_total = sum(
                mapped_data.get(child, 0) for child in partner_ids)
