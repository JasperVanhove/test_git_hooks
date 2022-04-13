from datetime import datetime

from odoo import fields, models


class PricelistWizard(models.TransientModel):
    _name = 'pricelist.wizard'
    _description = 'Pricelist prices of a product'

    product_tmpl_id = fields.Many2one('product.template')
    pricelist_line_ids = fields.Many2many('pricelist.wizard.line', 'wizard_id', 'Prices')
    company_id = fields.Many2one('res.company')
    date = fields.Datetime('Date', default=datetime.now())


class PricelistWizardLine(models.TransientModel):
    _name = 'pricelist.wizard.line'
    _description = 'Pricelist price line of a product'

    pricelist_id = fields.Many2one('product.pricelist', 'Pricelist')
    price = fields.Monetary('Price')
    currency_id = fields.Many2one('res.currency')
