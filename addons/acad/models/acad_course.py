from openerp import models, fields, api

class AcadCourse(models.Model):
    id
    _name="acad.course"
    name=fields.Char()
    teacher_code= fields.Many2one("acad.teacher",string="teacher")
    teacher_id = fields.Many2one("acad.teacher",string="teacher")
    teacher_memo = fields.Many2one("acad.teacher", string="teacher")



    student_ids = fields.Many2many("acad.student")