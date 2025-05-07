from odoo import models, fields, api


class asignatura(models.Model):
    _name = 'gestor_de_matriculas.asignatura'
    _description = 'Asignaturas'

    id_subject = fields.Char(string="ID de la Asignatura", required = True)
    name = fields.Char(string="Nombre", required = True)
    weekly_hours = fields.Integer(string="Horas Semanales", required = True)
    courses = fields.Many2many('gestor_de_matriculas.curso', string="Cursos")
    teachers = fields.Many2many('gestor_de_matriculas.profesor', string="Profesores", relation='asignatura_profesor_rel')
    convalidable = fields.Boolean (string="Convalidable")