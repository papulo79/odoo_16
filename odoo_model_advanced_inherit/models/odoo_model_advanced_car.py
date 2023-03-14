# -*- coding: utf-8 -*-
from odoo import models
import logging
_logger = logging.getLogger(__name__)


class Car(models.Model):
    _inherit = 'odoo_model_advanced_car'

    def action_stuff(self):
        print('He realizado cambios sin que seas consciente')
        return super().action_stuff()
