from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_picking_state(self):
        return [
            ('draft', ''),
            ('cancel', 'Cancelled'),
            ('not_send', 'Not Send'),
            ('partially_send', 'Partially send'),
            ('done', 'Done'),
        ]

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_picking_state(self):
        for sale in self:
            if sale.picking_ids:
                pickings_state = set(
                    [picking.state for picking in sale.picking_ids])
                if pickings_state == set(['cancel']):
                    sale.picking_state = 'cancel'
                elif (pickings_state == set(['cancel', 'done']) or
                      pickings_state == set(['done'])):
                    sale.picking_state = 'done'
                elif 'done' in pickings_state:
                    sale.picking_state = 'partially_send'
                else:
                    sale.picking_state = 'not_send'
            else:
                sale.picking_state = 'draft'

    picking_state = fields.Selection(
        string="Picking status", readonly=True,
        compute='_compute_picking_state',
        selection='get_picking_state',
        help="Overall status based on all pickings")
