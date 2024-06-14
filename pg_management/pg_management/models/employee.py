from odoo import fields, models, api

class PgEmployee(models.Model):
    _name = "pg.employee"
    _description = 'PG Employee'


    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')], string="Gender")
    phone = fields.Char(string="Mobile No.", required=True)
    email = fields.Char(string="Email")
    address = fields.Text(string='Address')
    join_date = fields.Date(string="Join Date", default=fields.Date.today())
    photo = fields.Image(string="Photo")
    department = fields.Selection([('food','Food'),
                                   ('manager','Manager'),
                                   ('cleaning','Cleaning'),
                                   ('cloths','Cloths')],string='Department')

