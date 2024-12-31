from odoo import api, fields, models

class BreakFastItems(models.Model):
    _name = 'breakfast.items'
    _description = 'breakfast items'

    name = fields.Char(translate=True , required=True)

