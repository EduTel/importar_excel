# -*- coding: utf-8 -*-

import sys
import coloredlogs
import logging
from datetime import datetime
import odoo
from odoo import exceptions
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError, ValidationError
logger = logging.getLogger(__name__)

#  class partner_inherit(models.Model):
#      _inherit = 'res.partner'
#  
#      @api.multi
#      @api.depends('name')
#      def name_get(self):
#          result = []
#          for data in self:
#              name = data.name
#              result.append((data.id, name))
#          return result


class PurchaseRequisition(models.Model):
    """Nuevo modulo de Odoo Team"""
    coloredlogs.install(level='DEBUG')
    _name = "purchase.requisition"
    _description = 'Desc: Modulo de requisicion de compras'
    _inherit = ['mail.thread', 'mail.compose.message']
    logger.warning("====================================================Iniciando %s", _name)

    def _my_user_name(self):
        return self.env.user.id

    def _get_selection(self):
        return [
            ('draft', 'Borrador'),
            ('pending', 'Pendiente'),
            ('approved', 'Aprobada'),
            ('Completed', 'Completado')
        ]

    STATES_partner_id = {
        'approved': [('required', True)],
        'Completed': [('required', True)]
    }

    #  buyer_c = fields.Many2one('res.partner', string="Comprador", help="Buyer", default=_my_user_name, store=True , ondelete='set null' )
    name = fields.Char(string="Nombre", size=50, readonly=True, required=False, index=True, copy=False, store=True)
    requisition_date = fields.Datetime('Fecha de requerimiento', help="Date", default=fields.Datetime.now, store=True )
    responsible = fields.Many2one('res.users', string="Responsable", help="Responsable", required=True, store=True , ondelete='set null' )
    products = fields.One2many('require.propurchase_dg', 'purchase_id', string="Productos", help="Products", required=True , ondelete='set null')
    state = fields.Selection(_get_selection, string='Estado', default='draft')
    partner_id = fields.Many2one('res.partner', string='Proveedor', change_default=True, track_visibility='always', states=STATES_partner_id )


    def Completado(self):
        logger.warning("====================================================Completado")
        self.state = "Completed"
    
    def Pendiente(self):
        logger.warning("====================================================Pendiente")
        self.state = "pending"

    @api.one
    def get_sale_state(self):
        return dict(self._get_selection())[self.state]

    @api.model
    def create(self, vals):
        if not vals.get("name", False):
            sequence = self.env.ref("purchase_requisition_dg.sequence_reconcile_seq")
            vals["name"] = sequence.next_by_id()
        return super(PurchaseRequisition,self).create(vals)
    
    @api.multi
    def send_mail_template(self):
        #  template_id = ir_model_data.get_object_reference('soleman_sale', 'send_sale_approval_mail')[1]
        #  template_browse = self.env["mail.template"].browse(template_id)
        #  values = template_browse.generate_email(self.id, fields=None)
        #  emails = ";".join(users.mapped("email"))
        #  logging.getLogger("Emails").info(emails)
        #  values['email_to'] = emails
        #  values['email_from'] = "desarrollo@desiteg.com"
        #  values['auto_delete'] = False
        #  values['res_id'] = False
        #  values['subject'] = "Aprobación de Venta"
        #  mail_id = self.env["mail.mail"].create(values)
        #  mail_id.send()

        # Find the e-mail template
        template = self.env.ref('purchase_requisition_dg.mail_purchase_requisition_notification_dg')
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('mail_template_demo', 'example_email_template')
        # Send out the e-mail template to the user
        logger.warning("====================================================1 id: %s", template.id)
        send_mail = self.env['mail.template'].browse(template.id).send_mail(self.id)
        if send_mail:
            self.state = "pending"
            logger.warning("====================================================2 id: %s", send_mail)
        else:
            raise UserError(_('Error sending mail.'))



    # wizard
    #  @api.multi
    #  def sent_email(self):
    #      logger.warning("====================================================sent_email")
    #      self.ensure_one()
    #      template = self.env.ref('purchase_requisition_dg.mail_purchase_requisition_notification_dg', False)
    #      compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
    #      self.state = "pending"
    #      logger.warning("====================================================id: %s", compose_form.id)
    #      logger.warning("====================================================id: %s", template.id)
    #      context = dict(
    #          default_model='purchase.requisition',
    #          default_res_id=self.id,
    #          default_use_template=bool(template),
    #          default_template_id=template and template.id or "False",
    #          default_composition_mode='comment',
    #          mark_invoice_as_sent=True,
    #          force_email=True,
    #          # default_notify= True,
    #          # show_address = True
    #      )
    #      logger.warning("====================================================My Contexto creado")
    #      logger.warning(context)
    #      return {
    #          'name': _('Compose Email'),
    #          'type': 'ir.actions.act_window',
    #          'view_type': 'form',
    #          'view_mode': 'form',
    #          'res_model': 'mail.compose.message',
    #          'views': [(compose_form.id, 'form')],
    #          'view_id': compose_form.id,
    #          'target': 'new',
    #          'context': context,
    #      }

    logger.warning("====================================================Terminado")

class ProductList(models.Model):
    _name = "require.propurchase_dg"
    _order = 'id'
    # _inherit = ['purchase.order.line']

    logger.warning("====================================================Iniciando %s", _name)
    amount = fields.Integer(string='Cantidad', size=10, required=True, index=True, store=True, default=1 )
    note = fields.Text(string="Descripción", size=250, required=True, store=True)
    product_uom = fields.Many2one('product.uom', string='Unidad de medida', help="Unidad de medida", store=True , ondelete='set null')
    purchase_id = fields.Many2one('purchase.requisition', help="Comprador", readonly=True, required=True, store=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Producto', ondelete='cascade', help="Select a product")
    logger.warning("====================================================Terminado")
    #purchase.order.line().onchange

    #product_template.uom_po_id
    #product_template.uom_id
    # purchase.order.line().onchange(
    @api.model
    def create(self, vals):
        logger.warning("====================================================create")
        logger.error(type(vals.get("amount"))) #  generate_except_osv
        logger.error(vals.get("amount")) #  generate_except_osv
        if vals.get("amount") == "0":
            logger.warning("==========es un 0")
            #  generate_validation_error
            # raise ValueError(vals["amount"])
            raise UserError(_('No se permiten valores de 0 en las cantidades'))
            #  raise UserError(_('Configuration error!\nCould not find any account to create the invoice, are you sure you have a chart of account installed?'))
        return super(ProductList,self).create(vals)

    @api.onchange('product_id')
    def onchange_product_id(self):
        logger.warning("================================onchange_product_id")
        result = {}
        if not self.product_id:
            return result
        self.product_uom = self.product_id.uom_po_id or self.product_id.uom_id
        self.note = self.product_id.name

    @api.onchange('amount')
    def onchange_amount(self):
        logger.warning("================================onchange_amount")
        logger.warning(type(self.amount))
        logger.warning(self.amount)
        if self.amount == 0 or self.amount <= 0:
            logger.warning("==========es un 0")
            self.amount = "1"
            # return { 'warning': {'title': 'Product error', 'message':":("} }
            # raise odoo.osv.osv.except_osv(_('Warning'), _('No se permite valor de 0'))
            # raise UserError(_('No se permite valor de 0'))
