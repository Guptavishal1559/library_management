from odoo import fields,models

class Type(models.Model):
    _name = "book.type"
    _description = "Type"

    name = fields.Char(string="Type")