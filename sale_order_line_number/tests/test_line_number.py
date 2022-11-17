from odoo.tests.common import Form, TransactionCase


class TestOrderLine(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestOrderLine, self).setUp(*args, **kwargs)
        
        #Create core elements invoked in the tests
        self.customer_bob = self.env["res.partner"].create(
            {
                "name": "Bob"
            }
        )
        self.sale_order_1 = self.env["sale.order"].create({
            "partner_id": self.customer_bob.id
        })
        
        self.product_cat = self.env["product.product"].create(
            {
                "name": "Cat"
            }
        )
        
        self.product_dog = self.env["product.product"].create(
            {
                "name": "Dog"
            }
        )
                
    def test_add_new_line (self):
        """Add new line to SO and check line number"""
        
        #Ad line #1
        with Form(self.sale_order_1) as f:
            with f.order_line.new() as line_1:
                line_1.product_id = self.product_cat
                line_1.sequence = 10
            f.save()
        
        so_line_1 = self.sale_order_1.order_line[0]
        
        self.assertEqual(so_line_1.line_number, 1, "line number must be equal to 1")
        self.assertEqual(so_line_1.product_id, self.product_cat, "must be product cat")

        #Ad line #2
        with Form(self.sale_order_1) as f:
            with f.order_line.new() as line_2:
                line_2.product_id = self.product_dog
                line_2.sequence = 11
            f.save()
        
        so_line_2 = self.sale_order_1.order_line[1]
        
        self.assertEqual(so_line_2.line_number, 2, "line number must be equal to 2")
        self.assertEqual(so_line_2.product_id, self.product_dog, "must be product dog")
          
        self.sale_order_1.order_line[1].sequence = 6
              
        
        so_line_2.invalidate_cache()
        self.assertEqual(so_line_2.line_number, 1, "line number must be equal to 1")
        self.assertEqual(so_line_1.line_number, 2, "line number must be equal to 2")
        
        
        
        self.assertEqual(so_line_1.product_id, self.product_cat, "must be product cat")
        self.assertEqual(so_line_2.product_id, self.product_dog, "must be product dog") 
        
        
        # Delete first line
        so_line_2.unlink()
        
        self.assertEqual(so_line_1.line_number, 1, "line number must be equal to 1")
        
        