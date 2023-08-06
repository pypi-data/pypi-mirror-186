odoo.define('somenergia.custom_greeting_message', function(require) {
    
    GreetingMessage = require('hr_attendance.greeting_message');
    var core = require('web.core');
    mixins = require('web.mixins');

    var _t = core._t;
    
    var NewGreetingMessage = GreetingMessage.include({
        init: function(parent, action) {
            var self = this;
            this._super.apply(this, arguments);
            this.activeBarcode = true;

            // if no correct action given (due to an erroneous back or refresh from the browser), we set the dismiss button to return
            // to the (likely) appropriate menu, according to the user access rights
            if(!action.attendance) {
                this.activeBarcode = false;
                this.getSession().user_has_group('hr_attendance.group_hr_attendance_user').then(function(has_group) {
                    if(has_group) {
                        self.next_action = 'hr_attendance.hr_attendance_action_kiosk_mode';
                    } else {
                        self.next_action = 'hr_attendance.hr_attendance_action_my_attendances';
                    }
                });
                return;
            }

            this.next_action = action.next_action || 'hr_attendance.hr_attendance_action_my_attendances';
            // no listening to barcode scans if we aren't coming from the kiosk mode (and thus not going back to it with next_action)
            if (this.next_action != 'hr_attendance.hr_attendance_action_kiosk_mode' && this.next_action.tag != 'hr_attendance_kiosk_mode') {
                this.activeBarcode = false;
            }
    
            this.attendance = action.attendance;
            // We receive the check in/out times in UTC
            // This widget only deals with display, which should be in browser's TimeZone
            this.attendance.check_in = this.attendance.check_in && moment.utc(this.attendance.check_in).local();
            this.attendance.check_out = this.attendance.check_out && moment.utc(this.attendance.check_out).local();
            this.previous_attendance_change_date = action.previous_attendance_change_date && moment.utc(action.previous_attendance_change_date).local();
    
            // check in/out times displayed in the greeting message template.
            this.format_time = 'HH:mm:ss';
            this.attendance.check_in_time = this.attendance.check_in && this.attendance.check_in.format(this.format_time);
            this.attendance.check_out_time = this.attendance.check_out && this.attendance.check_out.format(this.format_time);
            this.employee_name = action.employee_name;
            this.attendanceBarcode = action.barcode;
            this.warning_msg = action.warning_msg;
        },
        farewell_message: function () {
            if (this.warning_msg) {
                this.$('.o_hr_attendance_warning_message').show().append(_t("<b>" + this.warning_msg + "</b>"));
            }
        },
    });
    return {NewGreetingMessage: NewGreetingMessage};
});