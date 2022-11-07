# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Order Line Number',
    'version': '14.0.0.0.1',
    'category': 'Sales',
    'depends': ['sale'],
    'summary': "Line numbers in Sales Order lines",
    'application': False,
    'installable': True,
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_line.xml'
    ],
}
