# -*- coding: utf-8 -*-
# © 2016 Antiun Ingeniería S.L. - Jairo Llopis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class EventRegistration(models.Model):
    _inherit = "report.event.registration"

    square_meters = fields.Float(
        help="Amount of square meters reserved by this partner.",
    )
    location_id = fields.Many2one(
        "event.track.location",
        "Location",
        help="Location inside the fair (Main Hall, 3rd floor...)",
    )
    stand = fields.Char(
        oldname="section",
        help="Stand in the location (A-1, B-7...)",
    )

    def _get_select(self):
        result = super(EventRegistration, self)._get_select()
        result.update({
            "square_meters": "r.square_meters",
            "location_id": "r.location_id",
            "stand": "r.stand",
        })
        return result

    def _get_group_by(self):
        result = super(EventRegistration, self)._get_group_by()
        result.append("r.location_id")
        result.append("r.stand")
        return result
