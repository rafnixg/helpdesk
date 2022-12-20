# Copyright 2022 Rafnix Guzman
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FsmEquimentHelpdeskTicket(models.Model):

    _inherit = "fsm.equipment"

    helpdesk_ticket_ids = fields.One2many(
        "helpdesk.ticket", "fsm_equipment_id", "Tickets"
    )

    helpdesk_ticket_count = fields.Integer(compute="_compute_helpdesk_ticket_count")

    def _compute_helpdesk_ticket_count(self):
        for fsm_equipment in self:
            fsm_equipment.helpdesk_ticket_count = len(fsm_equipment.helpdesk_ticket_ids)

    def smart_button_helpdesk_ticket(self):
        self.ensure_one()

        result = self.env["ir.actions.act_window"]._for_xml_id(
            "helpdesk_mgmt.helpdesk_ticket_action"
        )
        result.update(
            {
                "domain": [("id", "in", self.helpdesk_ticket_ids.ids)],
            }
        )
        return result
