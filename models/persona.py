from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class persona(models.Model):
    _name = 'gestor_de_matriculas.persona'
    _description = 'Clase Padre Para Las Personas'

    type_document = fields.Selection([
        ('dni', 'DNI'),
        ('nie', 'NIE'),
    ], string="Tipo de Documento", default='dni', required=True)

    dni = fields.Char(string="DNI")
    nie = fields.Char(string="NIE")

    dni_nie = fields.Char(string="DNI/NIE",store = True)

    isDniSelected = fields.Boolean(compute='_compute_document_selection')
    isNieSelected = fields.Boolean(compute='_compute_document_selection')

    name = fields.Char(string="Nombre", required=True)
    lastName = fields.Char(string="Apellidos", required=True)
    date_birth = fields.Date(string="Fecha De Nacimiento", required=True)
    adress = fields.Char(string="Dirección", required=True)
    phone = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Correo Electrónico", required=True)
    photo = fields.Binary(string='Foto')

    @api.depends('dni', 'nie')
    def _compute_dni_nie(self):
        for rec in self:
            rec.dni_nie = rec.dni or rec.nie or ''

    @api.depends('type_document')
    def _compute_document_selection(self):
        for record in self :
            if record.type_document == 'dni':
                record.isDniSelected = True
                record.isNieSelected = False
            elif record.type_document == 'nie':
                record.isNieSelected = True
                record.isDniSelected = False

    @api.constrains('dni', 'nie')
    def _check_dni_nie(self):
        for record in self:
            if record.dni:
                self._validate_dni(record.dni)
            if record.nie:
                self._validate_nie(record.nie)
    
    def _validate_dni(self, dni):
        dni = dni.upper().strip()
        if not re.fullmatch(r'\d{8}[A-Z]', dni):
            raise ValidationError("Formato de DNI inválido. Debe ser 8 dígitos y una letra.")
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        num = int(dni[:8])
        if dni[-1] != letras[num % 23]:
            raise ValidationError(f"DNI inválido: la letra no es correcta.")

    def _validate_nie(self, nie):
        nie = nie.upper().strip()
        if not re.fullmatch(r'[XYZ]\d{7}[A-Z]', nie):
            raise ValidationError("Formato de NIE inválido. Debe empezar por X, Y o Z, seguido de 7 dígitos y una letra.")
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        mapping = {'X': '0', 'Y': '1', 'Z': '2'}
        num_str = mapping[nie[0]] + nie[1:8]
        num = int(num_str)
        if nie[-1] != letras[num % 23]:
            raise ValidationError(f"NIE inválido: la letra la letra no es correcta.")    

    _sql_constraints = [
        ('unique_dni_nie', 'UNIQUE(dni, nie)', 'Ya existe un cliente con este DNI/NIE.')
    ]

