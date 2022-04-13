from odoo import models, fields, api, _


class ReportPartnerLedger(models.AbstractModel):
    _inherit = "account.partner.ledger"

    @api.model
    def _get_columns_name(self, options):
        columns = super(ReportPartnerLedger, self)._get_columns_name(options=options)
        self._remove_initial_balance_from_columns(columns)

        return columns

    @api.model
    def _get_report_line_partner(self, options, partner, initial_balance, debit, credit, balance):
       report_line = super(ReportPartnerLedger, self)._get_report_line_partner(options, partner, initial_balance, debit, credit, balance)
       self._remove_initial_balance_column_from_report_line(report_line)

       return report_line

    @api.model
    def _get_report_line_move_line(self, options, partner, aml, cumulated_init_balance, cumulated_balance):
        report_line_move_line = super(ReportPartnerLedger, self)._get_report_line_move_line(options, partner, aml, cumulated_init_balance, cumulated_balance)
        self._remove_initial_balance_column_from_report_move_line(report_line_move_line)

        return report_line_move_line

    def _remove_initial_balance_from_columns(self, columns):
        for i in range(len(columns)):
            if 'name' in columns[i] and columns[i]['name'] == _('Initial Balance'):
                del columns[i]
                break

    def _remove_initial_balance_column_from_report_line(self, report_line):
        if 'columns' in report_line and len(report_line['columns']) > 0:
            report_line['columns'].pop(0)

    def _remove_initial_balance_column_from_report_move_line(self, report_move_line):
        if 'columns' in report_move_line and len(report_move_line['columns']) > 0:
            report_move_line['columns'].pop(5)