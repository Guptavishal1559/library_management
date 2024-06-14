from odoo import fields, models, api
from datetime import datetime

class PgGuest(models.Model):
    _name = "pg.guest"
    _description = "Pg Guest"

    name = fields.Char(string="Guest Name",required=True)
    age = fields.Integer(string="Age", default=18)
    email = fields.Char(string='Email',default="test@gmail.com")
    phone = fields.Char(string='Mobile No.')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ('other','Other')],string="Gender")

    address = fields.Text(string="Address")
    check_in_date = fields.Date(string="Check IN(Date)",default=fields.Date.today())
    check_out_date = fields.Date(string="Check Out(Date)",default=fields.Date.today())
    price_per_day = fields.Float(string="Price Per Day")
    facility_ids = fields.Many2many('pg.facility',string='Facility')
    room_id = fields.Many2one('room.type',string='Room Id')


    @api.model
    def default_get(self,field_list=[]):
        print('fields------------>>>',field_list)
        rtn = super(PgGuest, self).default_get(field_list)
        print("Return Statement=====================>",rtn)
        return rtn



