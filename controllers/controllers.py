# -*- coding: utf-8 -*-
# from odoo import http


# class Gdm(http.Controller):
#     @http.route('/gdm/gdm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gdm/gdm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gdm.listing', {
#             'root': '/gdm/gdm',
#             'objects': http.request.env['gdm.gdm'].search([]),
#         })

#     @http.route('/gdm/gdm/objects/<model("gdm.gdm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gdm.object', {
#             'object': obj
#         })

