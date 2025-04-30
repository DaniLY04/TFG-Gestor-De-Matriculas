from odoo import models, fields, api


class profesor(models.Model):
    _name = 'gestor_de_matriculas.profesor'
    _description = 'Profesores'

    _inherits = {'gestor_de_matriculas.persona': 'persona_id'}

    persona_id = fields.Many2one(
        comodel_name='gestor_de_matriculas.persona',
        string='Datos de Persona',
        required=True,
        ondelete='cascade',
    )
    
    ssn = fields.Integer(string="Numero de la Seguridad Social",required = True)
    is_tutor = fields.Boolean(string="Tutor", default = False)
    course_tutor = fields.Many2one('gestor_de_matriculas.curso', string="Curso Tutorizado")
    courses = fields.Many2many('gestor_de_matriculas.curso', string="Cursos Impartidos")
    #subjects = fields.Many2Many('gestor_de_matriculas.asignaturas', string="Asignaturas")
    qualifications = fields.Text(string="Titulaciones")

    _sql_constraints = [
        ('unique_ssn', 'UNIQUE(ssn)', 'Ya existe un profesor con ese SSN.')
    ]