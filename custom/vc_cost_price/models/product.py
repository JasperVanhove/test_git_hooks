from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    margin = fields.Float(string='Margin %')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_cost_price_calculation(self):
        for res in self:
            if res.categ_id.margin:
                res.standard_price = res.list_price - res.list_price * res.categ_id.margin / 100.0
            else:
                last_invoice = self.env['account.move.line'].search([('product_id', '=', res.id), ('move_id.type', '=', 'in_invoice')], order='date desc, id desc', limit=1)
                if last_invoice:
                    res.standard_price = last_invoice.price_unit * last_invoice.product_uom_id.factor / res.uom_id.factor
                elif res.bom_count:
                    res.standard_price = res._get_price_from_bom()

            for seller in res.seller_ids:
                last_invoices = self.env['account.move.line'].search(
                    [('product_id', '=', res.id), ('move_id.type', '=', 'in_invoice'),
                     ('move_id.partner_id', '=', seller.name.id)],
                    order='date desc, id desc').filtered(lambda x: x.quantity / x.product_uom_id.factor >= seller.min_qty / seller.product_uom.factor)
                if last_invoices:
                    seller.price = last_invoices[0].price_unit * last_invoices[0].product_uom_id.factor / seller.product_uom.factor