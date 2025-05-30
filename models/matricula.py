from odoo import models, fields

class matricula(models.Model):
    _name = 'gestor_de_matriculas.matricula'
    _description = 'Matrícula de Alumnos'

    

    alumno = fields.Many2one('gestor_de_matriculas.alumno', string='Alumno', required=True)
    nombre = fields.Char(related='alumno.name', string="Nombre", store=True)
    apellidos = fields.Char(related='alumno.lastName', string="Apellidos", store=True)
    dni_nie = fields.Char(related='alumno.dni_nie', string="DNI/NIE", store=True)
    numero_expediente = fields.Char(related='alumno.school_registration', string="Nº Expediente", store=True)
    fecha_nacimiento = fields.Date(related='alumno.date_birth', string="Fecha de Nacimiento", store=True)
    direccion = fields.Char(related='alumno.adress', string="Dirección", store=True)
    telefono = fields.Char(related='alumno.phone', string="Teléfono", store=True)
    foto = fields.Binary(related='alumno.photo', string="Foto", store=True)
    email = fields.Char(related='alumno.email', string="Email", store=True)

    curso_id = fields.Many2one('gestor_de_matriculas.curso', string='Curso', required=True)
    puntuacion_acceso = fields.Integer(string='Puntuación de Acceso')
    metodo_acceso = fields.Integer(string='Método de Acceso')

    archivos_adicionales = fields.Many2many(
        'ir.attachment',
        'matricula_attachment_rel',
        'matricula_id',
        'attachment_id',
        string='Documentación de Titulación Necesaria'
    )

    asignaturas_convalidadas_ids = fields.Many2many(
        'gestor_de_matriculas.asignatura',
        'matricula_asignatura_rel',
        'matricula_id',
        'asignatura_id',
        string="Asignaturas Convalidadas",
        domain="[('convalidable','=',True)]"
    )


    documentacion_convalidacion = fields.Many2many(
        'ir.attachment',
        'matricula_convalidacion_rel',
        'matricula_id',
        'attachment_id',
        string='Documentación para Convalidación'
    )

    repite = fields.Boolean(string='¿Repite?')
    promociona = fields.Boolean(string='¿Promociona?')
