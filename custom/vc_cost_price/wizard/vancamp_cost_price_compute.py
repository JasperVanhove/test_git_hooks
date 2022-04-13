# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Order Point Method:
#    - Order if the virtual stock of today is below the min of the defined order point
#

from odoo import api, models, tools

import logging

_logger = logging.getLogger(__name__)


class VancampsCostPriceCompute(models.TransientModel):
    _name = 'vancamps.cost.price.compute'
    _description = 'Compute Cost price'

    def cost_price_calculation(self):
        self.env['product.product'].search([]).action_cost_price_calculation()
        return {'type': 'ir.actions.act_window_close'}
