from odoo import fields,models

class Language(models.Model):
    _name = "book.language"
    _description = "Language"

    name = fields.Char(string="Language")
