from odoo import models, fields, api


class asignatura(models.Model):
    _name = 'gdm.asignatura'
    _description = 'Asignaturas'

    id_subject = fields.Char(string="ID de la Asignatura", required = True)
    name = fields.Char(string="Nombre", required = True)
    weekly_hours = fields.Integer(string="Horas Semanales", required = True)
    courses = fields.Many2many('gdm.curso', string="Cursos")
    teachers = fields.Many2many('gdm.profesor', string="Profesores", relation='asignatura_profesor_rel')
    convalidable = fields.Boolean (string="Convalidable")