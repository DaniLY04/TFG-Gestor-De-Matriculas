from odoo import models, fields, api


class alumno(models.Model):
    _name = 'gestor_de_matriculas.alumno'
    _description = 'Alumnos'

    _inherits = {'gestor_de_matriculas.persona': 'persona_id'}

    persona_id = fields.Many2one(
        comodel_name='gestor_de_matriculas.persona',
        string='Datos de Persona',
        required=True,
        ondelete='cascade',
    )
    
    latest_study = fields.Char(string="Ultimo Estudio",required = True)
    #actual_course = fields.Many2one()
    #report_card = fields.One2many('gestor_de_matriculas.boletin_notas')
    #school_registration = fields.One2Many('gestor_de_matriculas.matricula',required = True)