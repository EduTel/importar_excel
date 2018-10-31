# -*- coding: utf-8 -*-

import sys
import coloredlogs
import logging
from datetime import datetime
from odoo import exceptions
from odoo import models, fields, api, _
from odoo.exceptions import Warning

logger = logging.getLogger(__name__)


class PurchaseRequisition(models.Model):
    coloredlogs.install(level='DEBUG')
    _name = "purchase.requisition"
    logger.warning("====================================================Iniciando %s", _name)

    def _my_user_name(self):
        return self.env.user.id

    name = fields.Char(string="Nombre", size=50, readonly=True, required=False, index=True, copy=False)
    requisition_date = fields.Datetime('Fecha de requerimiento', help="Date", default=fields.Datetime.now, store=True )
    responsible = fields.Many2one('res.users', string="Responsable", help="Responsable", store=True , ondelete='set null' )
    products = fields.One2many('require.propurchase_dg', 'purchase_id', string="Productos", help="Products", required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('pending', 'Pendiente'),
        ('approved', 'Aprobada'),
        ('Completed', 'Completado')
    ], string='Estado', default='draft')

    # @api.one
    # def status_Confirmar(self):
    #     self.state = "pending"

    @api.model
    def create(self, values):
        if not values.get("name", False):
            sequence = self.env.ref("purchase_requisition_dg.sequence_reconcile_seq")
            values["name"]= sequence.next_by_id()
        return super(PurchaseRequisition,self).create(values)
    
    @api.multi
    def sent_email(self):
        logger.warning("====================================================status_Confirmar")
        self.state = "pending"
        self.ensure_one()
        logger.warning("====================================================status_Confirmar 1")
        template = self.env.ref('purchase_requisition_dg.mail_purchase_requisition_notification_dg', False)
        logger.warning("====================================================status_Confirmar 2")
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        logger.warning("====================================================status_Confirmar 3")
        ctx = dict(
            default_model='account.payment',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_composition_mode='comment',
            mark_invoice_as_sent=True,
            force_email=True
        )
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }

    logger.warning("====================================================Terminado")

class ProductList(models.Model):
    _name = "require.propurchase_dg"
    logger.warning("====================================================Iniciando %s", _name)
    amount = fields.Integer(string='Cantidad', size=50, required=True, index=True)
    note = fields.Text(string="Descripción", size=250, required=True)
    product_uom_id = fields.Many2one('product.uom', string='Unidad de medida', help="Unidad de medida", store=True , ondelete='set null')
    purchase_id = fields.Many2one('purchase.requisition', help="Comprador", readonly=True, required=True)
    logger.warning("====================================================Terminado")
