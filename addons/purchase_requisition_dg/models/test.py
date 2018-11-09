# -*- coding: utf-8 -*-
import copy
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# init = {
#     'origin': False,
#     'dest_address_id': False,
#     'date_order': '2018-11-08 00:48:23',
#     'name': 'PO00020',
#     'order_line': [123], 
#     'picking_type_id': 1, 
#     'notes': False, 
#     'date_planned': '2018-11-08 00:48:23', 
#     'company_id': 1, 
#     'currency_id': 3, 
#     'payment_term_id': 4, 
#     'incoterm_id': False, 
#     'message_follower_ids': False, 
#     'partner_ref': False, 
#     'partner_id': 17, 
#     'message_ids': False, 
#     'fiscal_position_id': False
# }
# orderline = [
#     0, False, {
#                 'product_id': 33,
#                 'product_uom': 1, 
#                 'analytic_tag_ids': [], 
#                 'price_unit': 0, 
#                 'date_planned': '2018-11-08 00:48:33', 
#                 'sequence': 10, 
#                 'taxes_id': [], 
#                 'product_qty': 1, 
#                 'account_analytic_id': False, 
#                 'name': '[CONS_DEL02] Little server'
#             }
# ]
# init['origin'] = True
# init['order_line'].append(orderline)
# print init
# print type(init)
# print type(orderline)
# print "hola"


# x = "<h3>Requisicion de compra pendiente de aprobación</h3>".encode('utf-8')
# x = unicode("<h3>Requisicion de compra pendiente de aprobación</h3>", 'utf-8')
# x = "<h3>Requisicion de compra pendiente de aprobación</h3>".encode('ascii', 'ignore').decode('ascii')
x = "<h3>Requisicion de compra pendiente de aprobación</h3>"
print x


a = [[6,9]]
b = copy.deepcopy(a)
b[0][0]=8
print a
print b