from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id', 'company_id')
    def onchange_purchase_partner_id(self):
        if self.type in ['in_invoice', 'in_refund']:
            if self.partner_id and len(self.partner_id.default_purchase_account_ids) > 0:
                lines = [(5, 0, 0)]
                for account in self.partner_id.default_purchase_account_ids:
                    vals = {'name': account.name,
                            'account_id': account.account_id.id,
                            'tax_ids': account.tax_id,
                            'price_unit': account.price_unit,
                            'quantity': 1,
                            'exclude_from_invoice_tab': False,
                            'recompute_tax_line': True,
                            }

                    lines.append((0, 0, vals))

                self.line_ids.unlink()
                self.invoice_line_ids = lines

                for line in self.invoice_line_ids:
                    line._onchange_price_subtotal()

                self._onchange_invoice_line_ids()
                self._recompute_dynamic_lines(recompute_all_taxes=True)



