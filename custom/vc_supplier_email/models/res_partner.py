from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    email_supplier = fields.Char(help='Email address used for situations where the contact assumes a supplier role.')

    @api.onchange('email')
    def _onchange_email(self):
        for record in self:
            if not record.email_supplier:
                record.email_supplier = record.email