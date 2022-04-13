odoo.define('base_report_to_printer.print', function (require) {
    'use strict';

    var ActionManager = require('web.ActionManager');
    var core = require('web.core');
    var framework = require('web.framework');
    var rpc = require('web.rpc');


    ActionManager.include({
        _executeReportAction: function (action, options) {
            var action_val = _.clone(action);
            var _t = core._t;
            var self = this;
            var _super = this._super;

            if (action_val.report_type === 'qweb-pdf') {
                framework.blockUI();
                return rpc.query({
                    model: 'ir.actions.report',
                    method: 'print_action_for_report_name',
                    args: [action_val.report_name]
                }).then(function (print_action) {
                    if(print_action && print_action.action === 'pop_up'){
                        //self.ir_actions_act_window_close(action, options);
                        framework.unblockUI();
                        let url = window.location.href;
                        let arr = url.split("/");
                        let result = arr[0] + "//" + arr[2];
                        let printable = result + '/report/pdf/' + action_val.report_name + '/' + action_val.context.active_id;
                        printJS({
                            printable: printable,
                            type: 'pdf',
                            showModal: true,
                            onPrintDialogClose: () => {
                                    let el = document.getElementById("printJS")
                                    if (el) {
                                        el.parentNode.removeChild(el)
                                    }
                                },
                            onPdfOpen: () => console.log('Pdf was opened in a new tab due to an incompatible browser')
                        })
                    } else {
                        //self.ir_actions_act_window_close(action, options);
                        return _super.apply(self, [action_val, options]);
                    }
                });
            } else {
                return _super.apply(self, [action_val, options]);

            }
        }
    });
});
