# -*- coding: utf-8 -*-
# from odoo import http


# class Basvuru(http.Controller):
#     @http.route('/basvuru/basvuru', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/basvuru/basvuru/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('basvuru.listing', {
#             'root': '/basvuru/basvuru',
#             'objects': http.request.env['basvuru.basvuru'].search([]),
#         })

#     @http.route('/basvuru/basvuru/objects/<model("basvuru.basvuru"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basvuru.object', {
#             'object': obj
#         })
