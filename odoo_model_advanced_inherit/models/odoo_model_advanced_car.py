# -*- coding: utf-8 -*-
from odoo import models
import logging
_logger = logging.getLogger(__name__)


class Car(models.Model):
    _inherit = 'odoo_model_advanced_car'

    def action_stuff(self):
        msg = '**************** action_stuff heredado %s -> %s ****************' % (
            self.env.user.name, self.env.uid)
        print(msg)
        return super().action_stuff()
