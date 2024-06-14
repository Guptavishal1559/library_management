from odoo import fields,models,api


class RoomType(models.Model):
    _name = 'room.type'
    _description = 'Room Type'

    name = fields.Char(string="Room Type", required=True)
    code = fields.Char(string="Code",size=4)
    price = fields.Float(string="Price", digits=(16,2))