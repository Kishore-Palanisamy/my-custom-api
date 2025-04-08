{
    'name': 'My Custom API',
    'version': '17.0.1.0.0',
    'summary': 'Provides custom JSON API endpoints for reporting',
    'description': 
        """
            <h3>My Custom API Module</h3>
            <p>This module provides the following API endpoints:</p>
            <ul>
            <li><strong>/api/hello</strong> - Basic hello-world check</li>
            <li><strong>/api/top-customers</strong> - Top 10 customers by sales</li>
            <li><strong>/api/sales-total</strong> - Total sales in a date range</li>
            <li><strong>/api/low-stock</strong> - Products with low stock</li>
            </ul>
        """,
    'author': 'Kishore',
    'category': 'Sales/API',
    'depends': ['base', 'sale_management', 'stock', 'sale'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
