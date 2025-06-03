from odoo import models, fields, api

class BoletinNotas(models.Model):
    _name = 'gdm.boletin_notas'
    _description = 'Boletines De Notas'

    name = fields.Char(string="Código", default='Nuevo', readonly=True)
    
    student = fields.Many2one('gdm.alumno', string="Alumno", required=True)
    student_dni = fields.Char(related='student.dni_nie', string="DNI/NIE", store=True, readonly=True)
    student_last_name = fields.Char(related='student.lastName', string="Apellidos", store=True, readonly=True)

    course = fields.Many2one('gdm.curso', string="Curso", compute="_compute_course", store=True)
    course_id_course = fields.Char(related='course.id_course', string="ID Curso", store=True, readonly=True)
    course_name = fields.Char(related='course.name', string="Nombre Curso", store=True, readonly=True)
    course_promotion = fields.Char(related='course.promotion', string="Promoción", store=True, readonly=True)

    tutor = fields.Many2one('gdm.profesor', string="Tutor", compute="_compute_tutor", store=True)

    note = fields.One2many('gdm.boletin_nota_linea', 'notes_report', string="Notas")
    remarks = fields.Text(string="Comentarios del Profesor")
    
    @api.depends('student')
    def _compute_course(self):
        for record in self:
            record.course = record.student.actual_course.id if record.student.actual_course else False

    @api.depends('course')
    def _compute_tutor(self):
        for record in self:
            record.tutor = record.course.tutor.id if record.course.tutor else False

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('gdm.boletin_notas')
        if 'student' in vals:
            alumno = self.env['gdm.alumno'].browse(vals['student'])
            if alumno.actual_course:
                vals['course'] = alumno.actual_course.id
                vals['tutor'] = alumno.actual_course.tutor.id if alumno.actual_course.tutor else False
                note_lines = []
                for subjects in alumno.actual_course.subjects:
                    note_lines.append((0, 0, {
                        'subjects': subjects.id,
                        'note': 0.0
                    }))
                vals['note'] = note_lines

        return super(BoletinNotas, self).create(vals)

class BoletinNotaLinea(models.Model):
    _name = 'gdm.boletin_nota_linea'
    _description = 'Línea de Nota en Boletín'

    notes_report = fields.Many2one('gdm.boletin_notas', string="Boletín", ondelete='cascade')
    subjects = fields.Many2one('gdm.asignatura', string="Asignatura", required=True)
    note = fields.Float(string="Nota")

    @api.constrains('note')
    def _check_nota_range(self):
        for record in self:
            if record.note < 0.0 or record.note > 10.0:
                raise models.ValidationError("La nota debe estar entre 0 y 10.")