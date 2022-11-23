# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Promote',
    'version': '14.0.0.0.1',
    'category': 'Sales',
    'depends': ['sale', 'product'],
    'summary': "To promote a selected product using tags",
    'application': False,
    'installable': True,
    'data':[
        'security/ir.model.access.csv',
        'views/sale_product_promote.xml'
    ],
    'demo':[
        # 'data/demo_data.xml',
    ],
}
