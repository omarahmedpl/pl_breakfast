from odoo import http
from odoo.http import request

class OrderDetailsController(http.Controller):
    @http.route('/pl_breakfast/order_details/<int:order_id>', auth='user', methods=['GET'], type='http', csrf=False)
    def order_details(self, order_id, **kw):
        order = request.env['orders'].sudo().search([('id', '=', order_id)])
        order_items = request.env['order.items'].sudo().search([('order_id', '=', order_id)])
        return request.render('pl_breakfast.order_details', {'order': order, 'order_items': order_items})