from odoo import fields, models,api

class PgFacility(models.Model):
    _name = 'pg.facility'
    _description = 'PG Facility'

    name = fields.Char(string="Facility", required=True)
    # guest_id = fields.Many2one('pg.guest',string='Guest',ondelete='set null')
