odoo.define('your_module_name.department_capacity_check', function (require) {
    "use strict";

    var core = require('web.core');
    var Dialog = require('web.Dialog');
    var Model = require('web.Model');
    var _t = core._t;

    var Department = new Model('hr.department');

    Department.include({
        saveRecord: function () {
            var self = this;
            var res = this._super.apply(this, arguments);

            if (this.data.member_ids.length > this.data.capacity) {
                var def = new $.Deferred();
                Dialog.confirm(self, _t("Departmana kapasitesinden fazla kişi atadınız. Devam etmek istediğinizi onaylayınız veya lütfen işlemi iptal ediniz."), {
                    confirm_callback: function () {
                        def.resolve(res);
                    },
                    cancel_callback: function () {
                        def.reject();
                    }
                });
                return def.promise();
            }
            return res;
        }
    });
});
