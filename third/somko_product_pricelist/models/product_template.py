from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_get_pricelists_view(self):
        price_lines = []
        for pricelist in self.env['product.pricelist'].search([('company_id', '=', self.company_id.id)]):
            price_lines.append(
                self.env['pricelist.wizard.line'].create(self.create_pricelist_wizard_line_data(pricelist)).id
            )

        action = dict(
            name='Pricelists',
            type='ir.actions.act_window',
            res_model='pricelist.wizard',
            view_type='form',
            view_mode='form',
            target='new',
            context=dict(
                default_company_id=self.company_id.id,
                default_product_tmpl_id=self.id,
                default_pricelist_line_ids=price_lines,
            ),
        )
        return action

    def create_pricelist_wizard_line_data(self, pricelist):
        return {
            'pricelist_id': pricelist.id,
            'price': pricelist.get_product_price(self, 1, self.env.uid),
            'currency_id': pricelist.currency_id.id,
        }
