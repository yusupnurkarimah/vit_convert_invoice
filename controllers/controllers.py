# -*- coding: utf-8 -*-
from odoo import http

# class VitConvertInvoice(http.Controller):
#     @http.route('/vit_convert_invoice/vit_convert_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_convert_invoice/vit_convert_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_convert_invoice.listing', {
#             'root': '/vit_convert_invoice/vit_convert_invoice',
#             'objects': http.request.env['vit_convert_invoice.vit_convert_invoice'].search([]),
#         })

#     @http.route('/vit_convert_invoice/vit_convert_invoice/objects/<model("vit_convert_invoice.vit_convert_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_convert_invoice.object', {
#             'object': obj
#         })