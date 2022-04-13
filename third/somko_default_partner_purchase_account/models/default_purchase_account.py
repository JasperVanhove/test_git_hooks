import odoo.addons.decimal_precision as dp
from odoo import models, fields


class DefaultPurchaseAccount(models.Model):
    _name = 'default.purchase.account'
    _description = 'Default Purchase account'

    _sql_constraints = [
        ('partner_account_uniq', 'unique (account_id,partner_id)', 'Account must be unique!'),
    ]

    account_id = fields.Many2one(
        comodel_name='account.account',
        string='Account',
        required=True,
        domain=lambda self: [('user_type_id.id', '=', self.env.ref('account.data_account_type_expenses').id)]
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner'
    )
    name = fields.Text(
        string='Description',
        required=True
    )
    tax_id = fields.Many2one(
        string="Tax",
        comodel_name='account.tax',
        domain=[('type_tax_use','=','purchase')]
    )
    price_unit = fields.Float(
        string='Unit Price',
        required=True,
        digits=dp.get_precision('Product Price'),
        default=1.0
    )
    company_id = fields.Many2one(
        string='Company',
        comodel_name='res.company',
        required=True,
        default=lambda self: self.env.user.company_id
    )




