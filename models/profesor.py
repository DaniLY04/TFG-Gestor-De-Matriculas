from odoo import models, fields, api


class profesor(models.Model):
    _name = 'gdm.profesor'
    _description = 'Profesores'

    _inherits = {'gdm.persona': 'persona_id'}

    persona_id = fields.Many2one(
        comodel_name='gdm.persona',
        string='Datos de Persona',
        required=True,
        ondelete='cascade',
    )
    
    ssn = fields.Char(string="Numero de la Seguridad Social",required = True)
    is_tutor = fields.Boolean(string="Tutor", default = False)
    course_tutor = fields.Many2one('gdm.curso', string="Curso Tutorizado")
    courses = fields.Many2many('gdm.curso', string="Cursos Impartidos")
    subjects = fields.Many2many('gdm.asignatura', string="Asignaturas" , relation='asignatura_profesor_rel')
    qualifications = fields.Text(string="Titulos Académicos")

    _sql_constraints = [
        ('unique_ssn', 'UNIQUE(ssn)', 'Ya existe un profesor con ese SSN.')
    ]