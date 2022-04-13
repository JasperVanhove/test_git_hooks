from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = 'res.partner'


    default_purchase_account_ids = fields.One2many(
        comodel_name='default.purchase.account',
        string='Default purchase accounts',
        inverse_name='partner_id'
    )