# -*- coding: utf-8 -*-
from odoo import models, fields, api


class IrSequence(models.Model):
    _inherit = "ir.sequence"

    limit = fields.Char()

    def _next_do(self):
        if self.limit and str(self.number_next_actual-1) == self.limit:
            self.number_next_actual = 0
        return super()._next_do()
