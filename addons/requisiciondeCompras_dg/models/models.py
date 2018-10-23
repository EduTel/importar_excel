# -*- coding: utf-8 -*-

import sys
import coloredlogs
import logging
from datetime import datetime
from odoo import exceptions
from odoo import models, fields, api, _
from odoo.exceptions import Warning


logger = logging.getLogger(__name__)


class partner_inherit(models.Model):
    _inherit = 'res.partner'

    @api.multi
    @api.depends('name')
    def name_get(self):
        result = []
        for data in self:
            name = data.name
            result.append((data.id, name))
        return result


class TodoList(models.Model):
    coloredlogs.install(level='DEBUG')
    _name = "require.purchase_dg"
    logger.warning("====================================================Iniciando %s", _name)

    # inherit = 'stock.location'
    # SELECT * FROM public.res_users ORDER BY id ASC LIMIT 100
    # name = fields.Char(
    #     string="Name",                   # Optional label of the field
    #     compute="_compute_name_custom",  # Transform the fields in computed fields
    #     store=True,                      # If computed it will store the result
    #     select=True,                     # Force index on field
    #     readonly=True,                   # Field will be readonly in views
    #     inverse="_write_name"            # On update trigger
    #     required=True,                   # Mandatory field
    #     translate=True,                  # Translation enable
    #     help='blabla',                   # Help tooltip text
    #     company_dependent=True,          # Transform columns to ir.property
    #     search='_search_function'        # Custom search function mainly used with compute
    # )
    # self.env.user.write_date
    # self.env['res.users'].browse(context.get('uid'))
    # self.search_read
    # self.search
    # self.
    # default=lambda self: self.env['res.partner'].search_read([], ['name'])
    # <field name="company_id" options="{'no_create': True}" groups="base.group_multi_company"/>
    # self.env['ir.actions.act_window'].browse(act_id).read()[0]
    # self.pool.get('res.country').browse
    # domain=[('id', '=', _my_user_name )]
    # 'module' object has no attribute 'one2many'
    # domain=[('parent_id', '=', env['res.partner'].id)]


    # @api.model
    def _my_user_name(self):
        # name = self.env['res.partner'].search([('id', '=', self.env.user.partner_id)])
        return self.env.user.partner_id

    name_c = fields.Char(string="Nombre", size=50, required=True, index=True)
    date_c = fields.Datetime('Fecha', help="Date", readonly=True, default=fields.Datetime.now, store=True )
    buyer_c = fields.Many2one('res.partner', string="Comprador", help="Buyer", default=_my_user_name, readonly=True, store=True , ondelete='set null' )
    products_c = fields.One2many('require.propurchase_dg', 'purchase_id_c', string="Productos", help="Products", required=True)
    state_c = fields.Selection([
        ('draft', 'Borrador'),
        ('pending', 'Pendiente'),
        ('approved', 'Aprobada')
    ], string='Estado', default='draft')

    logger.warning("====================================================Usuario")
    logger.warning("====================================================id: %s", buyer_c)
    # logger.warning(_inherit)
    logger.warning("====================================================Terminado")

    # @api.model
    # def _default_user(self):
    #     return self.env.context.get('buyer_c', self.env.user.login)

    @api.returns('res.partner')
    def afun2(self):
        pass
    # raise ValidationError(_('Prorata temporis can be applied only for time method "number of depreciations".'))
    #  api.one is meant to be used when method is called only on one record

    @api.one
    def assign_list(self):
        pass
    @api.one
    def assign_list(self):
        pass


class ProductList(models.Model):
    _name = "require.propurchase_dg"
    logger.warning("====================================================Iniciando %s", _name)
    name_c = fields.Char(string="Nombre", size=50, required=True, index=True)
    note_c = fields.Text(string="Descripción", size=150, required=True)
    purchase_id_c = fields.Many2one('require.purchase_dg', help="Comprador", readonly=True, required=True)
    logger.warning("====================================================Terminado")
