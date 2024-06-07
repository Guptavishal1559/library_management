from odoo import fields, models, api
from datetime import datetime,timedelta


class bookIssue(models.Model):
    _name = "book.issue"
    _description = "Book Issue"
    # _sql_constraints = []
    # This will be used to add constraints in SQL table.
    # It is a list of tuple where each tuple is one constraint
    # The tuple contains exactly 3 elements
    # First one is the name of the constraint
    # Second one is the constraint how we write in SQL
    # Third one is the warning that gets raised when constraint fail
    _sql_constraints = [
        ('check_age', 'check(age>=18)', 'The age has to be a at least 18!'),
        # ('unique_student_code', 'unique(student_code)', 'The code of the student must be unique!')
    ]


    name_id = fields.Many2one('library.user', string="Full Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')], string="Gender", required=True)
    email = fields.Char(string="Email")
    phone = fields.Integer(string="Mobile No.")
    address = fields.Text(string="Address")
    # Exercise2-Q6==================================================
    book_name = fields.Many2one("book.dept", "Book Name", required=True, ondelete='restrict')
    book_price = fields.Float(string="Book Price Per Day")
    book_quantity = fields.Integer(string="Quantity")
    date = fields.Date(string="Date", default=datetime.now())
    days = fields.Integer(string="Days")
    return_date = fields.Date(string="Return Date", compute="_cal_return_date")
    currency_id = fields.Many2one('res.currency', string="Currency")
    total_amt = fields.Monetary(currency_field='currency_id', string="Total Amount", compute="_cal_return_date")
    # Exercise2-Q12===================================================
    ref = fields.Reference([('library.stock', ' Stock'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')

    status = fields.Selection([('draft', 'Draft'),
                               ('isssued', 'Issued'),
                               ('expired', 'Expired'),
                               ('returned', 'Returned')], string='Status', default='draft')

    # Exercise2-Q13===================================================
    document = fields.Binary('Document')
    # Binary field is used to store the binary data basically content of a document
    file_name = fields.Char('File Name')

    @api.depends('date', 'days', 'return_date', 'total_amt', 'book_price')
    def _cal_return_date(self):
        # self.return_date = self.date + timedelta(days=self.days)
        for issue in self:
            issue.return_date = issue.date + timedelta(days=issue.days)
            issue.total_amt = issue.book_price * issue.days

    @api.onchange('name_id')
    def onchange_name_id(self):
        """
        This is onchange method to get the value of fields
        --------------------------------------------------
        @params self: object pointer / recordset
        """
        # records = self.filtered('gender')
        # print('Records----------------------->',records)
        for rec in self:
            if rec.name_id:
                rec.age = rec.name_id.age
                rec.gender = rec.name_id.gender
                rec.email = rec.name_id.email
                rec.phone = rec.name_id.phone
                rec.address = rec.name_id.address
            else:
                rec.age = ''
                rec.gender = ''
                rec.email = ''
                rec.phone = ''
                rec.address = ''

        for issue in self:
            print('selffffff-------------', self)
            price = 0.0
            if issue.gender == 'male':
                price = 3000
            elif issue.gender == 'female':
                price = 1000
            elif issue.gender == 'other':
                price = 500
            else:
                price = 0.0
            issue.book_price = price

    def print_rec(self):
        """
        This is a method of the button to demonstrate the Print() method
        -----------------------------------------------------------------
        @param self: object pointer
        """
        print("PRINT")
        print("self=====================>>",self)
        print("ENV=======================>>",self.env)
        print("ENV ARGS=====================>>",self.env.args)
        print("USER=====================>>",self.env.user)
        print("DIRECTORY=======================>>",dir(self.env))
        print('CURSOR--------------------------->', self.env.cr)
        print('UID---------------------->', self.env.uid)
        print('CONTEXT------------------------->', self.env.context)
        print('COMPANY----------------------->', self.env.company)
        print('COMPANIES---------------------->', self.env.companies)
        print('LANG------------------------->', self.env.lang)

    def create_rec(self):
        """
        This is a method of the button to demonstrate the create() method
        ----------------------------------------------------------------
        @param self: object pointer
        """
        vals = {
            'name_id':self.name_id,
            'age':self.age,
            'gender': self.gender,
            'email':self.email,
        }
        data = [vals]
        print("Create data---------------------><>",data)
        create_data = self.create(data)
        print("data Successfully created===================>>",create_data)
