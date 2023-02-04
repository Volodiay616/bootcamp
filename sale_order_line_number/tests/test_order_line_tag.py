from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestOrderLineTag(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestOrderLineTag, self).setUp(*args, **kwargs)

        # User Salesman
        self.Users = self.env["res.users"].with_context(no_reset_password=True)
        self.user_salesman = self.Users.create(
            {
                "name": "Salesman",
                "login": "Salesman",
                "groups_id": [(4, self.env.ref("sales_team.group_sale_salesman").id)],
            }
        )

        # User Manager
        self.Users = self.env["res.users"].with_context(no_reset_password=True)
        self.user_manager = self.Users.create(
            {
                "name": "Manager",
                "login": "Manager",
                "groups_id": [(4, self.env.ref("sales_team.group_sale_manager").id)],
            }
        )

        # User Senior Salesman
        self.Users = self.env["res.users"].with_context(no_reset_password=True)
        self.user_senior_salesman = self.Users.create(
            {
                "name": "Senior Salesman",
                "login": "Senior Salesman",
                "groups_id": [(4, self.env.ref("group_sale_senior_salesman").id)],
            }
        )

    def test_so_line_tag_access(self):
        """Test access to sale order line tags"""

        LineTagSalesman = self.env["sale.order.line.tag"].with_user(self.user_salesman)
        LineTagSeniorSalesman = self.env["sale.order.line.tag"].with_user(
            self.user_senior_salesman
        )
        LineTagManager = self.env["sale.order.line.tag"].with_user(self.user_manager)

        tag_salesman = LineTagSalesman.create({"name": "Tag Salesman"})
        tag_senior_salesman = LineTagSeniorSalesman.create(
            {"name": "Tag Senior Salesman"}
        )
        tag_manager = LineTagManager.create({"name": "Tag Manager"})

        # Fetch tags as user Salesman
        tag_ids = LineTagSalesman.search(
            [("id", "in", [tag_salesman.id, tag_manager.id, tag_senior_salesman.id])]
        )

        self.assertIn(tag_salesman, tag_ids, "Tag Salesman must be in tags!")
        self.assertEqual(len(tag_ids), 1, "Must be one record only!")

        # Test Salesman tag access write
        with self.assertRaises(AccessError):
            tag_salesman.name = "New Name"

        # Test Salesman tag access unlink
        with self.assertRaises(AccessError):
            tag_salesman.with_user(self.user_salesman).unlink()
            # tag_salesman.sudo(self.user_salesman).unlink()

        # Fetch tags as user senior_salesman
        tag_senior_salesman_ids = LineTagSeniorSalesman.search(
            [("id", "in", [tag_salesman.id, tag_manager.id, tag_senior_salesman.id])]
        )

        self.assertEqual(len(tag_senior_salesman_ids), 3, "Must be three record!")

        # Fetch tags as user manager

        tag_manager_ids = LineTagManager.search(
            [("id", "in", [tag_salesman.id, tag_manager.id, tag_senior_salesman.id])]
        )

        self.assertEqual(len(tag_manager_ids), 3, "Must be three record!")
