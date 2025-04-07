# my_custom_api/controllers/my_api.py
from odoo import http
from odoo.http import request

class MyCustomAPIController(http.Controller):

    @http.route('/api/hello', type='json', auth='public', methods=['POST'], csrf=False)
    def hello_world(self, **kwargs):
        return {"message": "Hello from Odoo!"}

    @http.route('/api/top-customers', type='json', auth='user', methods=['GET'], csrf=False)
    def top_customers(self, **kwargs):
        query = """
            SELECT partner_id, SUM(amount_total) as total
            FROM sale_order
            WHERE state = 'sale'
            GROUP BY partner_id
            ORDER BY total DESC
            LIMIT 10
        """
        request.env.cr.execute(query)
        results = request.env.cr.fetchall()

        customers = []
        for partner_id, total in results:
            partner = request.env['res.partner'].browse(partner_id)
            customers.append({
                'id': partner.id,
                'name': partner.name,
                'email': partner.email,
                'total_sales': total
            })

        return customers
    
    @http.route('/api/sales-total', type='json', auth='user', methods=['POST'], csrf=False)
    def sales_total(self, **kwargs):
        start = kwargs.get('start_date')  # e.g., "2025-04-01"
        end = kwargs.get('end_date')      # e.g., "2025-04-07"

        orders = request.env['sale.order'].sudo().search([
            ('date_order', '>=', start),
            ('date_order', '<=', end),
            ('state', '=', 'sale')
        ])

        total = sum(order.amount_total for order in orders)
        return {'total_sales': total, 'order_count': len(orders)}
    
    @http.route('/api/low-stock', type='json', auth='user', methods=['GET'], csrf=False)
    def low_stock_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([
            ('qty_available', '<', 10)
        ], limit=10)

        return [{
            'id': p.id,
            'name': p.name,
            'qty_available': p.qty_available
        } for p in products]


