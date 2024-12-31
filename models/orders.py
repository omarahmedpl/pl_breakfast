from odoo import models, fields, api
import pyperclip
from odoo.http import request
class Orders(models.Model):
    _name = 'orders'
    _description = 'Orders'

    name = fields.Char(translate=True, required=True)
    date = fields.Datetime(required=True, default=fields.Datetime.now)
    resturant = fields.Many2one('resturant', required=True)
    order_items = fields.One2many('order.items', 'order_id', string="Order Items")
    def action_view_details(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/pl_breakfast/order_details/{self.id}',
            'target': 'blank',
        }

    def action_copy_details(self):
        # Access the current record using self
        details = f"Order Name: {self.name}\nOrder Date: {self.date}\nRestaurant: {self.resturant.name}\n\nItems:\n"
        items = request.env['order.items'].sudo().search([('order_id', '=', self.id)])
        # Add each item and its quantity to the details
        for item in items:
            details += f"- {item.item_id.name}: {item.quantity}\n"

        # Copy the details to the clipboard
        pyperclip.copy(details)

        # Optionally, show a notification to the user
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Order details copied to clipboard!',
                'type': 'success',
                'sticky': False,
            },
        }