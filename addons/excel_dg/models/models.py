# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import sys
from odoo import exceptions
import coloredlogs, logging
from termcolor import colored

logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class TodoList(models.Model):
    coloredlogs.install(level='DEBUG')
    logger.info('====================================================00')
    logger.warning("====================================================1")
    logger.error("====================================================2")
    logger.info('===================================================='+__name__)
    print colored('=================================================hello', 'red')
    print colored('=================================================world', 'green')
    Warning("==========================hola mundo")

    _name = "demo.todo_list__t"

    name_ct_ = fields.Char(string="Nombre TXT", size=50, required=True, index=True)
    date_ct_ = fields.Datetime(string="Fecha TXT", required=True)
    description_ct_ = fields.Text(string="Descripcion TXT")
    state_ct_ = fields.Selection([
        ('draft', 'Draft TXT'),
        ('assigned', 'Assigned TXT'),
        ('in_progress', 'In Progress TXT'),
        ('closed', 'Closed TXT')
    ], 'state ct TXT', default='draft')
    task_ids_ct_ = fields.One2many("demo.task__t", "todo_id_cta_")
    owner_ct_ = fields.Many2one("res.users", 'owner TXT', required=True, index=True)
    @api.one
    def assign_list(self):
        self.state = "draft"
    @api.onchange('name')
    def on_change_name(self):
        self.description = "%s \n\r %s" % (self.description, self.name_ct_)
class Tasks(models.Model):
    _name = "demo.task__t"

    name_cta_ = fields.Char(string="Tarea txt")
    hours_cta_ = fields.Integer(string="Horas txt")
    state_cta_ = fields.Selection([
        ('draft', 'Draft TXT'),
        ('assigned', 'Assigned TXT'),
        ('in_progress', 'In Progress TXT'),
        ('closed', 'Closed TXT')
    ], 'state cta TXT')
    todo_id_cta_ = fields.Many2one("demo.todo_list__t")
