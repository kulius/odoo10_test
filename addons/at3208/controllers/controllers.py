# -*- coding: utf-8 -*-
from odoo import http

# class At3208(http.Controller):
#     @http.route('/at3208/at3208/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/at3208/at3208/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('at3208.listing', {
#             'root': '/at3208/at3208',
#             'objects': http.request.env['at3208.at3208'].search([]),
#         })

#     @http.route('/at3208/at3208/objects/<model("at3208.at3208"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('at3208.object', {
#             'object': obj
#         })