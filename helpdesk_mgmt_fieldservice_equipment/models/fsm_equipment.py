# Copyright 2022 Rafnix Guzman
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import base64
import io

from odoo import api, fields, models


class FsmEquimentQr(models.Model):

    _inherit = "fsm.equipment"
    
    helpdesk_ticket_ids = fields.One2many('helpdesk.ticket', 'fsm_equipment_id', 'Tickets')