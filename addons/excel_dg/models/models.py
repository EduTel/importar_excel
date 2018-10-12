# -*- coding: utf-8 -*-
#!/usr/local/bin/ipython

import sys
from odoo import exceptions
import coloredlogs, logging
from termcolor import colored




from odoo import models, fields, api, _
from odoo.exceptions import Warning

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#coloredlogs.install(level='DEBUG')
#coloredlogs.install(level='DEBUG', logger=logger)

class TodoList(models.Model):
    coloredlogs.install(level='DEBUG')
    logger.info('====================================================0')
    logger.warning("====================================================1")
    logger.error("====================================================2")
    logger.info('===================================================='+__name__)
    
    print colored('=================================================hello', 'red')
    print colored('=================================================world', 'green')

    _name = "demo.todo_list"

    name = fields.Char(string="Nombre", size=50, required=True, index=True)
    date = fields.Datetime(string="Fecha", required=True)
    owner = fields.Many2one("res.users", required=True, index=True)
    description = fields.Text(string="Descripcion")
    task_ids = fields.One2many("demo.task", "todo_id")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed')
    ], default='draft')

    @api.one
    def assign_list(self):
        self.state = "draft"

    @api.onchange('name')
    def on_change_name(self):
        self.description = "%s \n\r %s" % (self.description, self.name)


class Tasks(models.Model):
    _name = "demo.task"

    name = fields.Char(string="Tarea")
    hours = fields.Integer(string="Horas")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed')
    ])
    todo_id = fields.Many2one("demo.todo_list")
