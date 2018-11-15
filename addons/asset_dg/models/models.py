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