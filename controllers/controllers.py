# -*- coding: utf-8 -*-
# from odoo import http


# class GestorDeMatriculas(http.Controller):
#     @http.route('/gestor_de_matriculas/gestor_de_matriculas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_de_matriculas/gestor_de_matriculas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_de_matriculas.listing', {
#             'root': '/gestor_de_matriculas/gestor_de_matriculas',
#             'objects': http.request.env['gestor_de_matriculas.gestor_de_matriculas'].search([]),
#         })

#     @http.route('/gestor_de_matriculas/gestor_de_matriculas/objects/<model("gestor_de_matriculas.gestor_de_matriculas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_de_matriculas.object', {
#             'object': obj
#         })

