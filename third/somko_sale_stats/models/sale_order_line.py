from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
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
    qty_to_deliver = fields.Integer(
        string='Qty to deliver',
        compute='_compute_qty_to_deliver',
        store=True,
    )

    @api.depends('qty_delivered', 'product_uom_qty')
    def _compute_qty_to_deliver(self):
        super(SaleOrderLine, self)._compute_qty_to_deliver()

        for line in self:
            line.qty_to_deliver = line.product_uom_qty - line.qty_delivered

    @api.depends('move_ids.state', 'move_ids.scrapped',
                 'move_ids.product_uom_qty', 'move_ids.product_uom')
    def _compute_qty_returned(self):
        for line in self.filtered(
                lambda r: r.qty_delivered_method == 'stock_move'):
            qty = 0.0
            mv = line.move_ids.filtered(
                lambda r:
                line.product_id == r.product_id and r.state == 'done' and not
                r.scrapped and r.to_refund and
                r.location_dest_id.usage != "customer"
            )
            for move in mv:
                qty += move.product_uom._compute_quantity(
                    move.product_uom_qty, line.product_uom)
            line.qty_returned = qty
