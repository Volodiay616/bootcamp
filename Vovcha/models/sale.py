from odoo import models, fields

class SaleOrderLine (model.Models):
    _inherit = 'sale.order.line'
    line_number = fields.Integer() 