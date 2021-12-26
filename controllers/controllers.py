# -*- coding: utf-8 -*-
# from odoo import http


# class FranSalon(http.Controller):
#     @http.route('/fran_salon/fran_salon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fran_salon/fran_salon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fran_salon.listing', {
#             'root': '/fran_salon/fran_salon',
#             'objects': http.request.env['fran_salon.fran_salon'].search([]),
#         })

#     @http.route('/fran_salon/fran_salon/objects/<model("fran_salon.fran_salon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fran_salon.object', {
#             'object': obj
#         })
