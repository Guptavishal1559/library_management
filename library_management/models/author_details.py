from odoo import fields,models,api


class AuthorDetails(models.Model):
    _name = "author.details"
    _description = "Author Details"

    name = fields.Char("Author Name",required=True)
    nationality = fields.Char("Nationality")
    born = fields.Date("Born")
    died = fields.Date("Died")
    photo = fields.Binary("Upload your Image")
    # book_dept_id = fields.Many2one('book.dept',string="Book")


    def print_rec(self):
        """
        This is a button method to demonstrate the print() method
        -----------------------------------------------------------
        @param self: object pointer
        """
        print("PRINT")
        print("SELF",self)
        print("Env",self.env)

    def create_rec(self):
        """
        This is a button method to demonstrate the create() method
        ----------------------------------------------------------
        @param self: pointer object
        """
        vals = {
            'name':self.name,
            'nationality': self.nationality,
            'born':self.born,
            'died':self.died,
        }
        self.create(vals)

    def browse_rec(self):
        """
        This is a button method to demonstrate the browse() method
        ----------------------------------------------------------
        @param self: object pointer
        """
        print("BROWSE-----------------",self.browse(self.id))

    def search_rec(self):
        """
        This is a button method to demonstrate the seacrch() method
        -------------------------------------------------------------
        @param self: pointer object
        """
        fetch_all_data = self.search([])
        print("Fetch All Data------------------",fetch_all_data)

        only_indina_nation = self.search([('nationality','=','Indian')])
        print("Only Indian Nation------------------------",only_indina_nation)

        only_england_nation = self.search([('nationality', '=', 'England')])
        print("Only England Nation------------------------", only_england_nation)

        print("UNION---------------",only_indina_nation | only_england_nation)
        print("INTERSECTION--------------",only_indina_nation & only_england_nation)
        print("DIFF----------------------",only_indina_nation - only_england_nation)

        count_all_record = self.search_count([])
        print("Count All Record-------------------",count_all_record)
        count_indian_nation = self.search_count([('nationality','=','Indian')])
        print("Count Indian Nation----------------------",count_indian_nation)


    def copy_rec(self):
        """
        This is a button method to demostrate the copy() method
        ------------------------------------------------------
        @param self: object pointer
        """
        default = {
            'name':self.name + "(Copy)"
        }
        self.copy(default=default)

    def delete_rec(self):
        """
        This is a button method to demonstrate the delete() method
        ---------------------------------------------------------
        @param self: pointer object
        """
        self.unlink()
