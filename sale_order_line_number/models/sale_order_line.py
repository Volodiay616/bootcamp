from dataclasses import field
from odoo import api, models, fields

class SaleOrderLineTag (models.Model):
    _name = "sale.order.line.tag"
    _description = "Sale Order Line Tags"
    
    name = fields.Char(required=True)
    color = fields.Integer()
    

class SaleOrderLine (models.Model):
    _inherit = 'sale.order.line'
    
    tag_ids = fields.Many2many(comodel_name="sale.order.line.tag")
    
    line_number = fields.Integer(
        compute = "_compute_line_number",
        store = True
        )
    
        
    @api.depends("order_id.order_line", "sequence")
    def _compute_line_number(self):
        order_ids = self.mapped("order_id")
        for order in order_ids:
            n = 1
            for line in order.order_line.sorted(lambda l: l.sequence):
                line.line_number = n
                n += 1