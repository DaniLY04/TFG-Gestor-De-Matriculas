from odoo import models, fields, api


class alumno(models.Model):
    _name = 'gdm.alumno'
    _description = 'Alumnos'

    _inherits = {'gdm.persona': 'persona_id'}

    persona_id = fields.Many2one(
        comodel_name='gdm.persona',
        string='Datos de Persona',
        required=True,
        ondelete='cascade',
    )
    
    latest_study = fields.Char(string="Ultimo Estudio",required = True)
    actual_course = fields.Many2one('gdm.curso', string="Curso Actual")
    school_registration = fields.Char(string="Numero de Expediente", required = True)