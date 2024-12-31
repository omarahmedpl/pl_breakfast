from odoo import models, fields

class OrderItems(models.Model):
    _name = 'order.items'
    _description = 'Order Items'

    order_id = fields.Many2one('orders', string="Order", required=True)
    item_id = fields.Many2one('breakfast.items', string="Item", required=True)
    quantity = fields.Integer(string="Quantity")