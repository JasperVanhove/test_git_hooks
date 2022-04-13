# -*- coding: utf-8 -*-
from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _order = 'date_order desc, order_id, sequence, id'

    date_order = fields.Datetime(
        string='Order Date',
        related='order_id.date_order',
        store=True,
    )
    categ_id = fields.Many2one(
        comodel_name='product.category',
        string='Product Category',
        store=True,
        related='product_id.product_tmpl_id.categ_id',
    )
    default_code = fields.Char(
        string='Default code',
        related='product_id.default_code',
    )
    qty_returned = fields.Integer(
        string='Qty Returned',
        compute='_compute_qty_returned',
        store=True,
    )
    qty_to_receive = fields.Integer(
        string='Qty to receive',
        compute='_compute_qty_to_receive',
    )

    @api.depends('qty_received', 'product_uom_qty')
    def _compute_qty_to_receive(self):
        for line in self:
            line.qty_to_receive = line.product_uom_qty - line.qty_received

    @api.depends('move_ids.state', 'move_ids.scrapped',
                 'move_ids.product_uom_qty', 'move_ids.product_uom',
                 'move_ids.returned_move_ids',
                 'move_ids.returned_move_ids.product_uom_qty',
                 'move_ids.returned_move_ids.product_uom', )
    def _compute_qty_returned(self):
        for line in self.filtered(lambda r: r.move_ids):
            qty = 0.0
            for move in line.move_ids.mapped('returned_move_ids'):
                qty += move.product_uom._compute_quantity(
                    move.product_uom_qty, line.product_uom)
            line.qty_returned = qty
