from odoo import models, fields, api


class curso(models.Model):
    _name = 'gestor_de_matriculas.curso'
    _description = 'Cursos'

    id_course = fields.Char(string="ID Curso", required = True)
    name = fields.Char(string="Nombre", required = True)
    shift = fields.Selection([
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('nocturno', 'Nocturno'),
        ('online', 'Online')
    ], string="Turno", default='matutino', required=True)
    teachers = fields.Many2many('gestor_de_matriculas.profesor', string="Profesores")
    students = fields.One2many('gestor_de_matriculas.alumno', 'actual_course', string="Alumnos")
    #subjects = fields.Many2Many('gestor_de_matriculas.asignaturas', string="Asignaturas")
    total_hours = fields.Integer(string='Horas Totales')
    tutor = fields.Many2one('gestor_de_matriculas.profesor', string="Tutor")
    year = fields.Char(string="Año")
    promotion = fields.Char(string="Promoción")