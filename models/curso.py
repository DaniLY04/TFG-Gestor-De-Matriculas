from odoo import models, fields, api


class curso(models.Model):
    _name = 'gestor_de_matriculas.curso'
    _description = 'Cursos'

    id_course = fields.Char(string="ID Curso", required = True)
    name = fields.Char(string="Nombre", required = True)
    shift = fields.Selection([
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('online', 'Online')
    ], string="Turno", default='matutino', required=True)
    teachers = fields.Many2many('gestor_de_matriculas.profesor', string="Profesores")
    students = fields.Many2many('gestor_de_matriculas.alumno', string="Alumnos")
    subjects = fields.Many2many('gestor_de_matriculas.asignatura', string="Asignaturas")
    total_hours = fields.Integer(string='Horas Totales')
    tutor = fields.Many2one('gestor_de_matriculas.profesor', string="Tutor")
    promotion = fields.Char(string="Promoción")

    @api.onchange('students')
    def _onchange_students(self):
        for curso in self:
            for alumno in curso.students:
                alumno.actual_course = curso.id

    @api.model
    def create(self, vals):
        curso = super().create(vals)
        curso.students.write({'actual_course': curso.id})
        return curso
    
    def write(self, vals):
        res = super().write(vals)
        for curso in self:
            if 'students' in vals:
                alumnos_actuales = self.env['gestor_de_matriculas.alumno'].search([('actual_course', '=', curso.id)])
                alumnos_quitar = alumnos_actuales - curso.students
                alumnos_quitar.write({'actual_course': False})
                curso.students.write({'actual_course': curso.id})
        return res