from odoo import fields, models, api


class LibraryUser(models.Model):
    _name = "library.user"
    _description = "Library User"

    name = fields.Char(string="Full Name", required=True)
    age = fields.Integer(string="Age", group_operator='Avg')
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')], string="Gender", required=True)
    email = fields.Char(string='Email',readonly=True)
    phone = fields.Char(string="Mobile No.")
    address = fields.Text(string="Address")
    birth_date = fields.Date(string="Birthdate")
    # Exercise2-Q14=================================================
    photo = fields.Image('Photo')

    def print_user(self):
        """
        This is a method of the button to demonstrate the usage of button
        -----------------------------------------------------------------
        @param self : object pointer / recordset
        """
        # TODO: Future Development
        print('PRINT')
        active_records = self.filtered('name')
        print("ACTIVE RECORDS------------------------>", active_records)
        print("ACTIVE RECORDS NAME------------------------>", active_records.name)
        print("ACTIVE RECORDS EMAIL------------------------>", active_records.email)
        print("ACTIVE RECORDS AGE------------------------>", active_records.age)
        print("ACTIVE RECORDS GENDER------------------------>", active_records.gender)

        active_records_name = active_records.mapped('name')
        active_records_name_2 = active_records.mapped(lambda r:r.name + str(r.age) + r.gender)
        print("active_records_name---------------------->", active_records_name)
        print("active_records_name_2---------------------->", active_records_name_2)


        active_records_name_age = active_records.mapped(lambda r: r.name + "," + str(r.age) + "," + r.gender)
        print("active_records_name_age------------------------------>", active_records_name_age)
        search = self.env['library.user'].search([])
        print('SEARCH------------------>',search)
        print('self.env[\'library.user\']--------------------->',self.env['library.user'])
        print('SELFFFFF---------------->',self)
        print('ENVIRONMENT------------------------>',self.env)
        print('ENVIRONMENT ATTRS---------------------------->',dir(self.env))
        print('ENV.ARGS-------------------->',self.env.args)
        print('CURSOR--------------------------->',self.env.cr)
        print('UID---------------------->',self.env.uid)
        print('USER------------------------->',self.env.user)
        print('CONTEXT------------------------->',self.env.context)
        print('COMPANY----------------------->',self.env.company)
        print('COMPANIES---------------------->',self.env.companies)
        print('LANG------------------------->',self.env.lang)

    def create_user_rec(self):
        """
        This is a method of the button to demonstrate the create() method
        -----------------------------------------------------------------
        @param self : object pointer
        """
        vals = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'email': self.email,
            'address': self.address,
            'phone': self.phone,
            'birth_date': self.birth_date,
            'photo': self.photo,
        }
        vals_list = [vals]
        print('vals list_______________________',vals_list)
        # creating record in the same object
        new_stds = self.create(vals_list)
        print('STDS', new_stds)

    def copy_rec(self):
        """
        This is method of the button it is created for demonstrate the copy() method.
        ---------------------------------------------------------------------------
        @param self : object pointer / recordset
        """
        default = {
            'name': self.name + '(copy)',
        }
        print('DEFAUTL===================',default)
        new_rec = self.copy(default=default)
        print("\nNew Rec", new_rec)


    def delete_user_rec(self):
        print('SELF------------------>', self)
        unlink = self.unlink()
        print("UNLINK------------------->", unlink)


    def browse_rec(self):
        """
        This si a button's method used to demonstrate browse() method
        --------------------------------------------------------------
        """
        stu_rec = self.browse(self.id)
        # for data in stu_rec:
        #     print(data.name)
        #     print(data.age)
        #     print(data.gender)
        #     print(data.email)
        #     print(data.phone)
        print('STU REC---------------------->', stu_rec)
        # user_dict = stu_rec.read(
        #     ['name', 'age', 'gender', 'email', 'address','phone'], load='')
        # print('USER DICTTT----------------------------->', user_dict)
        #
        user_details = self.browse(self.id)
        print('USER DETAILS--------------------------->', user_details)
        #
        # lang = self.env['book.language']
        # book_lang = lang.browse(self.id)
        # print('BOOK LANG-------------------->', book_lang)


    def search_rec(self):
        """
        This is the method of the button creating for demonstrate the search_rec() method
        ----------------------------------------------------------------------------
        @param self : pointer
        """

        for all_stud in self.search([]):
            print(all_stud.read(['name','age','gender','email','phone']))

        mt_dt = self.get_metadata()
        print('metadata',mt_dt)


        all_student = self.search([])
        print('ALL STUDENT----------------------------------------->', all_student)

        # male_student = self.search([('gender', '=', 'male')])
        # print('MALE STUDENT--------------------------->', male_student)
        #
        # female_student = self.search([('gender', '=', 'female')])
        # print('FEMALE STUDENT---------------------------------->', female_student)


        # for offset_3_student in self.search([], offset=3):
        #     print(offset_3_student.read(['name','email','phone','age']))
        # print('SKUP 3 RECORDS--------------------------------------->', offset_3_student)


        # for limit_3_student in self.search([], limit=3):
        #     print(limit_3_student.read(['name','email','phone','age']))
        # print('LIMIT 3 RECORDS--------------------------------------->', limit_3_student)

        # for off_2_limit_4_student in self.search([], offset=2, limit=4):
        #     print(off_2_limit_4_student.read(['name','age','gender','email']))
        # print('OFFSET 2 and LIMTI 4-------------------------------->', off_2_limit_4_student)


        # print("UNION------->", male_student | female_student)
        # for union in male_student | female_student:
        #     print(union.name)
        # print("INTERSECTION------------------->", male_student & female_student)
        # for union in male_student & female_student:
        #     print(union.name)
        # print("DIFF------------->", male_student - female_student)
        # for union in male_student - female_student:
        #     print(union.name)


        # total_stud = male_student - female_student
        # print('TOTAL STUD------------------->', total_stud)
        # for stud in total_stud:
        #     print("ID : ==================>",stud.id)
        #     print('NAME : ================>', stud.name)
        #     print('AGE : ================>', stud.age)
        #     print('GENDER : ================>', stud.gender)


    def name_get(self):
        """
        Overridden name_get() to display name and code both
        ---------------------------------------------------
        @param self: object pointer
        return : A list of tuple containing id and string
        """
        user_list = []
        for user in self:
            # print("USER================>",user) # library.user(id,)
            user_str = ''
            user_email = ''
            if user.name:
                print("if>>>>>>>>>>>>>>>>>>>")
                user_str += '[' + str(user.id) + ']'
                name = user.name.replace(' ', '').lower()
                user_email += name + "@gmail.com"
                user.email = user_email

            user_str += user.name
            user_email += user.name
            user_list.append((user.id, user_str))
        return user_list


    def copy(self,default = {}):
        print('COPY METHOD SELF------------------------>',self)
        default['name']= self.name + "(Copy)"
        default['age']= 30
        default['gender']='male'
        print('DEFAULT------------------------->',default)
        cpy = super(LibraryUser, self).copy(default=default)
        print("CPY---------------->",cpy)
        return cpy

    def delete(self):
        print("SELF------------------>",self)
        dlt = super(LibraryUser,self).unlink()
        print("DELETE------------------------->",dlt)
        return dlt


    # DOMAIN
    # Domain is a list of Tuple.
    # Each Tuple contains exactly 3 elements.
    # The first element is the field with which you want to search or filter.
    # The second element is the operator.
    # The third element is the operand.
    # This is similar to a condition we write in our WHERE condition in SQL query where we need 3 elements to search or filter.
    # The field must be the field of the model for which you're performing the search.
    # The operator can be relational operators. <, >, <=, >=, =, !=, in, not in
    # Special operators used in Odoo  like, ilike, =like, =ilike, child_of, parent_of
    # name like 'anup'(ODOO) -> name like '%anup%' (SQL)
    # name =like 'anup%' (ODOO) -> name like 'anup%' (SQL)
    # child_of and parent_of operators can be used only if there is a hierarchy in the model.
    # It is used to search records like search all my parents or all my children.
    # e.g. monitor_id child_of <id_of_the_record>
    # parent_of or child_of will always have operand as id.
    # Usage of Domain
    # 1. Relational Fields
    # 2. Action
    # 3. Search View
    # 4. Attrs
    # 5. Search Method ( we will see it in ORM Methods )

    # ATTRS
    # attrs is used in xml
    # attrs is a dictionary where the key is the attribute and value is a domain.
    # If the domain's result is True the attribute gets set.
    # The attribute can be used are required, readonly and invisible.

    # 1.create()
    # @api.model_create_multi
    # def create(self, vals_lst):
    # @param self : object / recordset
    # @param vals_lst : A list of dictionary containing fields and values
    # This method is used to create record(s)
    # It returns a recordset containing one or more records which were created

    # 2. write()
    # def write(self,vals):
    # @param self: recordset containing records
    # @param vals: dictionary containing fields and values
    # This method is used to update records
    # It returns True

    # 3. browse()
    # @api.model
    # def browse(self,id/[ids]):
    # @param self: object or recordset
    # @param id / [ids]: It can be either a single id or a list of ids
    # This method provides recordset of the id(s) passed.
    # It returns recordset containing one or more records

    # 4. read()
    # def read(self,fields=None,load='_classic_read'):
    # @param self: recordset containing records
    # @param fields: list of fields you want to read / None for all fields
    # @param load: Used for M2O field only default value as given above
    # This method is used to fetch field and values in dictionary.
    # It returns a list of dictionary

    # 5. copy()
    # def copy(self,default=None):
    # @param self: recordset containing record
    # @param default: A dictionary to update field values before duplicating
    # This method is used to duplicate a record
    # It is a combination of read and create methods.
    # It returns a recordset of the newly created record

    # 6. unlink()
    # def unlink(self):
    # @param self: recordset containing record(s)
    # This method is used to delete records
    # It returns True

    # 7. search()
    # @api.model
    # def search(self, args,offset=0,limit=None,order=None,count=False)
    # @param self: object pointer or recordset
    # @param args: Domain (List of conditions)
    # @param offset: No of records to skip
    # @param limit: Max no of records to fetch
    # @param order: name of the field by which you want to sort
    # @param count: True / False
    # It is used to search records based on condition and certain criteria.
    # It returns recordset if count = False
    # It returns count of recrods if count = True

    # 8. search_count()
    # @api.model
    # def search_count(self, args):
    # @param self: object pointer or recrodset
    # @param args: Domain
    # This method is used to count no of recrods based on condition
    # It basically calls search method with count=True
    # It returns an integer(no of records)

    # 9. search_read()
    # @api.model
    # def search_read(self, domain=None,fields=None,offset=0,limit=None,order=None):
    # @param self: object pointer or recrodset
    # @param fields: List of fields you want to fetch / read
    # @param offset: no of records to skip
    # @param limit : Max no of records to fetch
    # @param order: Name of the filed by which you want to sort
    # It is used to search the records based on certain criteria and then fetch the dictionary of list for  records
    # It is a combination of search and read method
    # It returns a list of dictionary
