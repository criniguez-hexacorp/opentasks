# -*- coding: utf-8 -*-
# from odoo import http


# class Opentasks(http.Controller):
#     @http.route('/opentasks/opentasks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/opentasks/opentasks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('opentasks.listing', {
#             'root': '/opentasks/opentasks',
#             'objects': http.request.env['opentasks.opentasks'].search([]),
#         })

#     @http.route('/opentasks/opentasks/objects/<model("opentasks.opentasks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opentasks.object', {
#             'object': obj
#         })
