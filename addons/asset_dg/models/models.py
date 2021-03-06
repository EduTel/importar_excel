# -*- coding: utf-8 -*-
import sys
import coloredlogs
import logging
import copy
from datetime import datetime
import odoo
from odoo import exceptions
from odoo import models, fields, api, _
from mako.template import Template
from odoo.exceptions import Warning, UserError, ValidationError
logger = logging.getLogger(__name__)

class Assetadd(models.Model):
    """Nuevo modulo de Odoo Team"""
    coloredlogs.install(level='DEBUG')
    _description = 'Agregar campo'
    _inherit = ['account.asset.asset']
    logger.warning("====================================================Iniciando %s")
    notes = fields.Text(string="Observaciones", readonly=False, required=False, index=False, copy=True, store=True)
    user_id = fields.Many2one('res.users', string='Asignado A', required=False, default=lambda self: self.env.user)

class Partnerdd(models.Model):
    _inherit = 'res.partner'

    def _get_selection(self):
        return [
            ('pending', 'Pendiente'),
            ('validated', 'Validado')
        ]
    state = fields.Selection(_get_selection, string='Estado', default='pending')