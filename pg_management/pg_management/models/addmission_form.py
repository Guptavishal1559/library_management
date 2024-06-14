from odoo import fields, models, api
from odoo.exceptions import UserError


class AddmissionForm(models.Model):
    _name = "addmission.form"
    _description = 'Addmission Form'

    name = fields.Char(string="Full Name", required=True)
    room_no = fields.Integer(string="Room No.")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('ohter', 'Other')], string="Gender")
    deposite = fields.Integer(string="Deposite Amt", default="1000")
    phone = fields.Char(string="Mobile No.", required=True)
    phone2 = fields.Char(string="Mobile No. 2", required=True)
    email = fields.Char(string="Email")
    address = fields.Text(string='Address')
    join_date = fields.Date(string="Join Date", default=fields.Date.today())
    photo = fields.Image(string="Photo")
    study_job = fields.Selection([('study','Study'),
                                  ('job','Job')],string="Study/Job")
    company_institute_name_add = fields.Text(string="Company/Institue Name & Address")
    father_name = fields.Char(string='Father\'s Name')
    father_occupation = fields.Char(string='Father\'s Occupation')
    facility_ids = fields.Many2many('pg.facility', string='Facility')
    room_id = fields.Many2one('room.type', string='Room Id')


    def name_create(self, name):
        """
        Overridden name_create method to add the name along with the code
        -----------------------------------------------------------------
        @param self: object pointer
        @param name: neme of the record typed in the relational field
        """
        vals = {
            'name':name,
            'email': name.lower()+'@gmail.com'
        }
        demo = self.create(vals)
        return demo.id,demo.display_name

    @api.model_create_multi
    def create(self, values):
        rtn = super(AddmissionForm, self).create(values)
        return rtn

    def unlink(self):
        print("SELF===================>>>", self)
        for data in self:
            if data.age > 18:
                raise UserError("You can't delete this record")
        dele = super(AddmissionForm, self).unlink()
        return dele
