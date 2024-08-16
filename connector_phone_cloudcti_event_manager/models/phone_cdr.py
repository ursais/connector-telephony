import phonenumbers

from odoo import models

class PhoneCDR(models.Model):
    _inherit = "phone.cdr"

    def cloudcti_open_outgoing_notification(self):
        called_id = self._context.get("call_no")
        caller_id = self.env.user.phone
        if caller_id and called_id and caller_id != called_id:
            phone = phonenumbers.format_number(
                phonenumbers.parse(caller_id, 'US'),
                phonenumbers.PhoneNumberFormat.NATIONAL
            )
            other = phonenumbers.format_number(
                phonenumbers.parse(called_id, 'US'),
                phonenumbers.PhoneNumberFormat.NATIONAL
            )
            partner = (
                self.env["phone.common"]
                .sudo()
                .get_record_from_phone_number(other)
            )
            if len(self.partner_ids):
                self.partner_ids[0].cloudcti_outgoing_call_notification()
