# -*- coding: utf-8 -*-

import sys
import coloredlogs
import logging
from odoo import exceptions
from odoo import models, fields, api, _
from odoo.exceptions import Warning


logger = logging.getLogger(__name__)


class TodoList(models.Model):
    coloredlogs.install(level='DEBUG')
    _name = "require.purchase.dg"
    logger.warning("====================================================Iniciando %s", _name)
    
    # logger.warning("====================================================id: %s", self.env.user.id)
    # logger.warning("====================================================name: %s", self.env.user.login)

    

    # inherit = 'stock.location'
    # SELECT * FROM public.res_users ORDER BY id ASC LIMIT 100

    date_c = fields.Char('Date_c', default="0", help="Date")
    buyer_c = fields.Char('buyer_c', default="0", help="Buyer", readonly=True)

    logger.warning("====================================================Usuario")
    logger.warning("====================================================id: %s", buyer_c)

    # logger.warning(_inherit)
    logger.warning("====================================================Terminado")

    @api.model
    def _default_user(self):
        return self.env.context.get('buyer_c', self.env.user.login)