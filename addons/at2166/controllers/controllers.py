# -*- coding: utf-8 -*-
from odoo import http

# class At2166(http.Controller):
#     @http.route('/at2166/at2166/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/at2166/at2166/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('at2166.listing', {
#             'root': '/at2166/at2166',
#             'objects': http.request.env['at2166.at2166'].search([]),
#         })

#     @http.route('/at2166/at2166/objects/<model("at2166.at2166"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('at2166.object', {
#             'object': obj
#         })