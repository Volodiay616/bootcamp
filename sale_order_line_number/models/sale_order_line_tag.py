from odoo import fields, models


class SaleOrderLineTag (models.Model):
    _name = "sale.order.line.tag"
    _description = "Sale Order Line Tags"
    
    name = fields.Char(required=True)
    color = fields.Integer()
    salesman_id = fields.Many2one('res.users', string='User', track_visibility='onchange', readonly=True, states={'draft': [('readonly', False)]}, default=lambda self: self.env.user)
    