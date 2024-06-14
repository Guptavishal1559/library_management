from odoo import fields, models, api
from datetime import datetime
from datetime import timedelta


class Stock(models.Model):
    _name = 'library.stock'
    _description = 'Stock'
    _rec_name = 'book_id'

    book_id = fields.Many2one('book.dept', 'Book Name', store=True, required=True)
    isbn = fields.Char('ISBN', related="book_id.isbn", store=True)
    price = fields.Float('Price', group_operator='Avg')
    remaining_qty = fields.Integer('Remaining Quantity')
    total_qty = fields.Integer('Total Quantity')
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    sequence = fields.Integer('Sequence')
    # date = fields.Date('Date', default=datetime.today())
    # end_date = fields.Date('Date', default=datetime.today())

    # exercise2-Q1============================================================================
    language = fields.Many2one('book.language', 'Language', related="book_id.language_id", store=True)

    # exercise2-Q3============================================================================
    book_ids = fields.Many2many('book.type', string='Genre', related="book_id.genre_ids")

    # The Many2many field will have the first attribute as the comodel_name being a relational field.
    # The second attribute is the label of the field.
    # The field does not get stored in the table in database.
    # Unlike O2M it does not have an inverse field.
    # Here it creates a lookup table with the name "'comodel's table name + _ + current model's table name + '_'  + rel".
    # So in our case it will be book_type_library_stock_rel.
    # There are two fields which will be used for the ids of both the models for mapping.
    # First field will be current model's field and will have the name "current_model's table name + _id".
    # In our case it is library_stock_id.(A Foreign Key to Student)
    # Similarly second field will be comodel's field and will have the name "comodel's table name + _id".
    # So it will be book_type_id.(A Foreign Key to Activtiy)
    # The mapping will help us fetch the activities to be displayed against the student.

    # exercise2-Q4============================================================================
    # book_ids = fields.Many2many('book_type','stock_type_rel','stock_id','type_id','Genre')
    # book_ids = fields.Many2many('book_type','stock_type_rel','stock_id','type_id',string='Genre')
    # You can also write the many2many field along with the details of lookup table.
    # Firstly you need to give the name of the model as first attribute.
    # Second one will be the name of the lookup table.
    # Third will be the field of the current model. (Foreign Key to current model)
    # Fourth will be the field of comodel. (Foreign Key to Comodel)
    # fifth will be the label of the field.

    photo = fields.Image('Photo')

    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')], default="draft", string="Status")
    author_ids = fields.Many2many('author.details', string='Author Name', store=True)

    parent_id = fields.Many2one('library.user', 'Parent')

    # This is reserved field used for hierarchy
    # It is basically a many2one field to itself

    child_ids = fields.One2many('library.stock', 'parent_id', 'Subordinates')
    # This is also a reserved field and works for hierarchy.
    # It is an O2M field and field will be always parent_id

    parent_path = fields.Char('Parent Path', index=True)

    # This is a reserved field which is used only if we have hierarchy in the model.
    # It will be used for faster searching of the extended hierarchy. (Subordinates of subordinates)
    # Not needed on the view.
    # It stores the complete hierarchy of all the parent's ids including current record's id.
    # For e.g. 1/2/4/5/3
    # Here current record is with id 3, parent of 3 is 5, parent of 5 is 4, parent of 4 is 2 and finally parent of 2 is 1.

    currency_id = fields.Many2one('res.currency', 'Currency')
    final_fees_amount = fields.Monetary(currency_field='currency_id', string='Fees Amount')

    color = fields.Integer("Color")

    def action_confirm(self):
        self.status = 'confirm'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Kya Baat hai Rainbow_man Create ho gaya',
                'type': 'rainbow_man',
            }
        }

    @api.onchange('book_id')
    def onchange_book_id(self):
        for rec in self:
            rec.author_ids = rec.book_id.author_ids
        # lines = []
        # for line in rec.book_id.author_ids:
        #     val = {
        #         'name': line.name,
        #         'nationality': line.nationality,
        #         'born': line.born,
        #         'died': line.died,
        #     }
        #     print('val', val)
        #     lines.append(line)


    def print_rec(self):
        """
        This is a mehtod of the button to demonstrate the print() method
        --------------------------------------------------------------
        @param self: pointer object
        """
        print("PRINT")
        active_records = self.filtered('book_id.name')
        print("Active Records=================>>>", active_records)
        print("Active Records isbn=================>>>", active_records.isbn)
        print("Active Records language=================>>>", active_records.language.name)
        for book_type in active_records.book_ids:
            print("book_type book_ids=================>>>", book_type.name)

        print("SLEF==================>>>", self)
        active_records_map = self.mapped('book_id.name')
        print("Active Records Map=================>>>", active_records_map)
        print("ENVIRONMENT================>>>", self.env)
        print("ENVIRONMENT ARGS=========================>>>", self.env.args)
        print("DIRECTORY OF ENVIRONMENT============================>>>", dir(self.env))
        print("CURSOR==============================>>>", self.env.cr)
        print("USER===============================>>>", self.env.user)
        print("UID===========================>>>", self.env.uid)
        print("CONTEXT===========================>>>", self.env.context)
        print("COMPANY=============================>>>", self.env.company)
        print("COMPANIES==============================>>>", self.env.companies)
        print("LANG==================================>>>", self.env.lang)

    def search(self, args, offset=0, limit=None, order=None, count=False):
        """
        Overridden Search method to fetch inactive records as well
        ------------------------------------------------------------
        @param self: object pointer
        @param args: Domain / list of conditions
        @param offset: no of record to skip
        @param limit: no of record to show
        @param order: field name for sorting
        @param count: True/False
        :return : Recordset if count=False else no of records
        """
        args = ['|', ('active', '=', False), ('active', '=', True)] + args
        return super().search(args, offset=offset, limit=limit, count=count, order=order)

    def create_rec(self):
        """
        This is a method of the button to demonstrate the create() method
        --------------------------------------------------------------
        @param self: pointer object
        """
        vals = {
            'book_id': self.book_id.id,
        }
        data_list = [vals]
        print('Data List===============>>', data_list)
        create_data = self.create(data_list)
        print('Create Data=====================>>>>', create_data)

    def search_rec(self):
        """
        This is a method of the button to demonstrate the search() method
        -----------------------------------------------------------------
        @param self: pointer object
        """
        fetch_all_records = self.search([])
        print("Fetch_All_Records------------------->>>", fetch_all_records)

        for search_hindi in self.search([('language.name', '=', 'Hindi')]):
            print("search----------->", search_hindi.language.name)
        print("SEARCH======================>>>", search_hindi)

        no_of_language = self.search_count([])
        print("no_of_language_____________________ ", no_of_language)
        no_of_english_book = self.search_count([('language.name', '=', 'English')])
        print("no_of_english_book---------------------->", no_of_english_book)

    def browse_rec(self):
        """
        This is a method of the button to demonstrate the browse() method
        ------------------------------------------------------------------
        @param self: pointer object
        """
        record = self.browse(4)
        print("RECORD---------------------->", record)

    def copy_rec(self):
        res = self.copy()

    def delete_rec(self):
        print("Self-------------", self)
        print("Unlink----------------------", self.unlink())
