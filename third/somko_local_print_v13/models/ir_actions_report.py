# Copyright (c) 2007 Ferran Pegueroles <ferran@pegueroles.com>
# Copyright (c) 2009 Albert Cervera i Areny <albert@nan-tic.com>
# Copyright (C) 2011 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright (C) 2011 Domsense srl (<http://www.domsense.com>)
# Copyright (C) 2013-2014 Camptocamp (<http://www.camptocamp.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, exceptions, fields, models, _


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    property_printing_action_id = fields.Many2one(
        comodel_name='printing.action',
        string='Default Behaviour',
        company_dependent=True,
    )

    printing_action_ids = fields.One2many(
        comodel_name='printing.report.xml.action',
        inverse_name='report_id',
        string='Actions',
        help='This field allows configuring action and printer on a per '
             'user basis'
    )

    @api.model
    def print_action_for_report_name(self, report_name):
        """ Returns if the action is a direct print or pdf

        Called from js
        """
        report = self._get_report_from_name(report_name)
        if not report:
            return {}
        result = report.behaviour()
        serializable_result = {
            'action': result['action']
        }
        return serializable_result

    def _get_user_default_print_behaviour(self):
        user = self.env.user
        return {
            'action': user.printing_action or 'client'
        }

    def _get_report_default_print_behaviour(self):
        result = {}
        report_action = self.property_printing_action_id
        if report_action and report_action.action_type != 'user_default':
            result['action'] = report_action.action_type
        return result

    def behaviour(self):
        self.ensure_one()
        printing_act_obj = self.env['printing.report.xml.action']

        result = self._get_user_default_print_behaviour()
        result.update(self._get_report_default_print_behaviour())

        # Retrieve report-user specific values
        print_action = printing_act_obj.search([
            ('report_id', '=', self.id),
            ('user_id', '=', self.env.uid),
            ('action', '!=', 'user_default'),
        ], limit=1)
        if print_action:
            # For some reason design takes report defaults over
            # False action entries so we must allow for that here
            result.update({k: v for k, v in
                          print_action.behaviour().items() if v})
        return result

