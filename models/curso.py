from odoo import models, fields, api


class gestor_de_matriculas(models.Model):
    _name = 'gestor_de_matriculas.gestor_de_matriculas'
    _description = 'gestor_de_matriculas.gestor_de_matriculas'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()