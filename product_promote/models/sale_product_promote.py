from odoo import api, fields, models

class SaleProductPromote (models.Model):
    _name = "sale.product.promote"
    _description = "Products To Promoute"
    
    # _inherits = {'product.product': 'promote_id'}
    _inherits = {'product.template': 'promote_id'}
    
    

