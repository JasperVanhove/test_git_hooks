from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    sales_conditions = fields.Text(string="Sales conditions", translate=True)
    company_info_footer = fields.Text(string="Company footer info", translate=True)

