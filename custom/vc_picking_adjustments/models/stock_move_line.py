from odoo import models, fields


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    lot_number = fields.Char(string="Lotnummer")
