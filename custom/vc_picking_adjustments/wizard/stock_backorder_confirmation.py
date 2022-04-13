# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare


class StockBackorderConfirmation(models.TransientModel):
    _inherit = 'stock.backorder.confirmation'

    pick_ids = fields.Many2many('stock.picking', 'stock_picking_backorder_rel')
    show_print_button = fields.Boolean(default=False)
    pickings_to_print = fields.Many2many('stock.picking', 'stock_picking_backorder_to_print_rel')

    def _process(self, cancel_backorder=False):
        self.ensure_one()
        if cancel_backorder:
            for pick_id in self.pick_ids:
                moves_to_log = {}
                for move in pick_id.move_lines:
                    if float_compare(move.product_uom_qty,
                                     move.quantity_done,
                                     precision_rounding=move.product_uom.rounding) > 0:
                        moves_to_log[move] = (move.quantity_done, move.product_uom_qty)
                pick_id._log_less_quantities_than_expected(moves_to_log)
        self.pick_ids.with_context(cancel_backorder=cancel_backorder).action_done()
        # return self.env.ref('stock.action_report_delivery').report_action(self.pick_ids)
        if not cancel_backorder:
            pickings_to_print = self.env['stock.picking'].search([('backorder_id', 'in', self.pick_ids.ids), ('printed', '=', False)]).ids
            if pickings_to_print:
                self.write({'pickings_to_print': [(6, 0, pickings_to_print)], 'show_print_button': True})
                return self.pickings_to_print.do_print_picking()

    def process(self):
        if not self.show_print_button:
            return self._process()
        else:
            self.write({'show_print_button': True})
            return {
                'type': 'ir.actions.do_nothing'
            }

    def process_cancel_backorder(self):
        if not self.show_print_button:
            return self._process(cancel_backorder=True)
        else:
            self.write({'show_print_button': True})
            return {
                'type': 'ir.actions.do_nothing'
            }

    def print_backorder(self):
        return self.pickings_to_print.do_print_picking()
