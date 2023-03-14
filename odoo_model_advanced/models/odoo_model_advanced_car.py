# -*- coding: utf-8 -*-
from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)


class Car(models.Model):
    _name = 'odoo_model_advanced_car'
    _description = 'Coche'

    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')
    under_fuel = fields.Boolean(
        string='Necesita repostar', compute='_compute_under_fuel')

    def _compute_under_fuel(self):
        print('_compute_under_fuel')
        if self.fuel_litres < 50:
            self.under_fuel = True
        else:
            self.under_fuel = False

    def action_stuff(self):
        try:
            print('función action_stuff ejecutándose')
        except TypeError:
            return False
