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
    students = fields.Many2many('gestor_de_matriculas.alumno', string="Alumnos")
    subjects = fields.Many2many('gestor_de_matriculas.asignatura', string="Asignaturas")
    total_hours = fields.Integer(string='Horas Totales')
    tutor = fields.Many2one('gestor_de_matriculas.profesor', string="Tutor")
    promotion = fields.Char(string="Promoción")