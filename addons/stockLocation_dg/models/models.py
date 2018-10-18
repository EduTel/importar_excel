# -*- coding: utf-8 -*-

import sys
from odoo import exceptions
import coloredlogs, logging

logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class TodoList(models.Model):
    coloredlogs.install(level='DEBUG')
    logger.warning("====================================================Iniciando")

    _inherit = 'stock.location'
    
    posx = fields.Char('Corridor (X)', default="0", help="Optional localization details, for information purpose only")
    posy = fields.Char('Shelves (Y)', default="0", help="Optional localization details, for information purpose only")

    logger.warning(_inherit)
    logger.warning("====================================================Terminado")