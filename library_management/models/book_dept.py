from odoo import fields, models, _, api


class bookDept(models.Model):
    _name = "book.dept"
    _description = 'Book Department'


    code = fields.Char(string="Code", required=True, copy=False, readonly=True, default=lambda self: _('new'))
    name = fields.Char(string="Book Name", required=True)
    isbn = fields.Char('ISBN')
    # book_price = fields.Float(string="Book Price", digits=(16, 2))
    genre_ids = fields.Many2many('book.type', string="Genre")
    publish_date = fields.Date("Publish Date")
    language_id = fields.Many2one('book.language', string="Language")
    stock_id = fields.Many2one('library.stock', string='stock')
    currency_id = fields.Many2one('res.currency', 'Currency')
    book_price = fields.Monetary(currency_field='currency_id', string='Book Price')
    # exercise2-Q2====================================================================
    # exercise2-Q5====================================================================
    author_ids = fields.Many2many('author.details', string="Author Details", ondelete="cascade")
    # quantity = fields.Integer(string="Quantity")
    color = fields.Integer('Color')
    issue_id = fields.Many2one('book.issue', string='Book Issue')


    @api.model
    def name_search(self,name,args=None,operator="ilike",limit=100):
        args = args or []
        # print("Name", name)
        # print("Operator", operator)
        # print("Args", args)
        # print("Limit", limit)
        if name:
            records = self.search(['|','|',('name', operator, name),('language_id',operator,name)])
            return records.name_get()
        return self.search([('name', operator, name)]+args, limit=limit).name_get()

    def print_rec(self):
        """
        This is a method of the button to demonstrate the print() method
        ---------------------------------------------------------------
        @param self: pointer object
        """
        print("PRINT")
        print("SELF----------------->>>>", self)
        print("Environment------------------------>>>", self.env)
        print("Environment Args-------------------->>>", self.env.args)
        print("Company----------------------->>>", self.env.company)
        print("User----------------------->>>", self.env.user)
        print("Directoty of ENV---------------------------->>>", dir(self.env))
        print("Lang-------------------->>>", self.env.lang)
        print("Manage-------------------->>>", self.env.manage)
        print("Keys-------------------->>>", self.env.keys)
        print("Items-------------------->>>", self.env.items)
        print("Values-------------------->>>", self.env.values)
        print("Reset-------------------->>>", self.env.reset)
        print("Su-------------------->>>", self.env.su)
        print("Ref-------------------->>>", self.env.ref)
        print("User-------------------->>>", self.env.user)
        print("Companies-------------------->>>", self.env.companies)


    def create_rec(self):
        """
        This is a method of the button to demonstrate the create() method
        --------------------------------------------------------------
        @param self: pointer object
        """
        vals = {
            'name': self.name,
            'isbn': self.isbn,
            'book_price': self.book_price,
            'genre': self.genre,
            'publish_date': self.publish_date,
            'language_id': self.language_id,
            'stock_id': self.stock_id,
        }
        data = [vals]
        print("DATA------------------->>>", data)
        create_data = self.create(data)
        print("CREATE DATA----------------------->>>", create_data)


    def search_rec(self):
        """
        This is a method of the button to demonstrate the search() method
        ----------------------------------------------------------------
        @param self: pointer object
        """
        all_data = self.search([])
        print("All data--------------------->>>",all_data)

        all_hindi_book = self.search([('language_id.name','=','Hindi')])
        print("All Hindi Book------------------->>>",all_hindi_book)

        count_of_all_book = self.search_count([])
        print("Count of all book--------------------------->>>>",count_of_all_book)

        no_of_hindi_book = self.search_count([('language_id.name','=','Hindi')])
        print("No of Hindi Book----------------------->>>",no_of_hindi_book)

        no_of_english_book = self.search_count([('language_id.name', '=', 'English')])
        print("No of English Book----------------------->>>", no_of_english_book)

        no_of_gujrati_book = self.search_count([('language_id.name', '=', 'Gujrati')])
        print("No of Gujarati Book----------------------->>>", no_of_gujrati_book)

        no_of_marathi_book = self.search_count([('language_id.name', '=', 'Marathi')])
        print("No of Marathi Book----------------------->>>", no_of_marathi_book)

        print("UNION------------>>>",no_of_hindi_book | no_of_english_book)
        print("UNION------------->>>",no_of_marathi_book | no_of_gujrati_book)

        print("INTERSECTION------------>>>", no_of_hindi_book & no_of_english_book)
        print("INTERSECTION------------->>>", no_of_marathi_book & no_of_gujrati_book)

        print("DIFF------------>>>", no_of_hindi_book - no_of_english_book)
        print("DIFF------------->>>", no_of_marathi_book - no_of_gujrati_book)


    def browse_rec(self):
        """
        This is a method of the button to demonstrate the browse() method
        ----------------------------------------------------------------
        @param self: pointer object
        """
        ids = self.id
        use_of_browse = self.browse(ids)
        print("Use of Browse--------------------->>>",use_of_browse)


    def delete_rec(self):
        """
        This is a method of the button to demonstrate the delete() method
        -----------------------------------------------------------------
        @param self: pointer object
        """
        print("DELETE THE RECORD",self.unlink())


    def copy_rec(self):
        """
        This is a mehtod of the button to dmenonstrate the copy() method
        ----------------------------------------------------------------
        @param self: pointer object
        """
        default = {
            'name': self.name + "(Copy)",
        }
        print("defautl--------------->>>",default)
        data_copy = self.copy(default=default)
        print("COPY DATA------------------------>>>",data_copy)

    @api.model
    def create(self, vals):
        if vals.get('code', _('new')) == _('new'):
            vals['code'] = self.env['ir.sequence'].next_by_code('book.dept') or _('new')
        res = super(bookDept, self).create(vals)
        return res
