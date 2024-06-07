from odoo import fields,models,api


class AuthorDetails(models.Model):
    _name = "author.details"
    _description = "Author Details"

    name = fields.Char("Author Name",required=True)
    nationality = fields.Char("Nationality")
    born = fields.Date("Born")
    died = fields.Date("Died")
    photo = fields.Binary("Upload your Image")
