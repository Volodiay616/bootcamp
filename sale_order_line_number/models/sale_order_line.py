from odoo import models, fields

class SaleOrderLine (models.Model):
    _inherit = 'sale.order.line'
    
    line_number = fields.Integer(compute="_compute_line_number")
    
    def _compute_line_number(self):
        n = 1
        for line in self:
            line.line_number = n
            n += 1 