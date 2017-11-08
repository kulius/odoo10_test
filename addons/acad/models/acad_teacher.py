from openerp import models, fields, api

class AcadTeacher(models.Model):
    _name="acad.teacher"
    name=fields.Char()
    code = fields.Char()
    memo = fields.Char()
    course_ids=fields.One2many("acad.course","teacher_id")
    teacher_ids = fields.Many2many("acad.teacher")