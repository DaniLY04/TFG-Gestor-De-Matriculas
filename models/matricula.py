from odoo import models, fields, api
import base64
import qrcode
from io import BytesIO
from urllib.parse import urljoin

class matricula(models.Model):
    _name = 'gdm.matricula'
    _description = 'Matrícula de Alumnos'    

    name = fields.Char()
    alumno = fields.Many2one('gdm.alumno', string='Alumno', required=True)
    name_alumno = fields.Char(related='alumno.name', string="Nombre", store=True)
    lastName = fields.Char(related='alumno.lastName', string="Apellidos", store=True)
    dni_nie = fields.Char(related='alumno.dni_nie', string="DNI/NIE", store=True)
    school_registration = fields.Char(related='alumno.school_registration', string="Nº Expediente", store=True)
    date_birth = fields.Date(related='alumno.date_birth', string="Fecha de Nacimiento", store=True)
    adress = fields.Char(related='alumno.adress', string="Dirección", store=True)
    phone = fields.Char(related='alumno.phone', string="Teléfono", store=True)
    photo = fields.Binary(related='alumno.photo', string="Foto", store=True)
    email = fields.Char(related='alumno.email', string="Email", store=True)

    curso_id = fields.Many2one('gdm.curso', string='Curso', required=True)
    access_score = fields.Integer(string='Puntuación de Acceso')
    access_method = fields.Integer(string='Método de Acceso')

    additional_files = fields.Many2many(
        'ir.attachment',
        'matricula_attachment_rel',
        'matricula_id',
        'attachment_id',
        string='Documentación de Titulación Necesaria'
    )

    asignaturas_convalidadas_ids = fields.Many2many(
        'gdm.asignatura',
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

    state = fields.Selection([
        ('repite', 'Repite'),
        ('promociona', 'Promociona'),
        ('nuevo', 'Nuevo Curso')
    ], string="Estado Académico", default='nuevo')

    qr_code = fields.Binary("QR Verificación", compute="_generate_qr_code")

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            sequence = self.env['ir.sequence'].next_by_code('gdm.matricula') or 'MTR-XXXX'
            curso_id = str(vals.get('curso_id', '0'))
            alumno = self.env['gdm.alumno'].browse(vals.get('alumno'))
            expediente = alumno.school_registration or 'NOEXP'
            vals['name'] = f'{sequence}-{curso_id}-{expediente}'
        return super().create(vals)
    

    def _generate_qr_code(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            pdf_url = urljoin(base_url, f"/report/pdf/gdm.report_matricula_document/{record.id}")
            
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=6, border=4)
            qr.add_data(pdf_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            qr_img_b64 = base64.b64encode(buffer.getvalue())
            record.qr_code = qr_img_b64
    