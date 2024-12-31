from odoo import api, fields, models

class Resturant(models.Model):
    _name = 'resturant'
    _description = 'resturant'
    name = fields.Char(translate=True , required=True)
    address = fields.Char(translate=True)
    phone = fields.Char(translate=True , required=True)