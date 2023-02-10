from odoo.tests.common import TransactionCase


class TestProjectTaskNumber(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestProjectTaskNumber, self).setUp(*args, **kwargs)
        # create project
        self.project_1 = self.env["project.project"].create({"name": "Project 1"})
        self.project_2 = self.env["project.project"].create({"name": "Project 2"})
        self.tasks = self.env["project.task"]

    def test_add_new_task(self):
        """Add new project task and check task number"""
        # add tasks in 1st project
        self.task_1 = self.tasks.create(
            {"name": "Task one", "project_id": self.project_1.id}
        )
        # add tasks in 2nd project
        self.task_2 = self.tasks.create(
            {"name": "Task two", "project_id": self.project_2.id}
        )
        # find numbers of all tasks
        all_task_numbers = self.env["project.task"].search([]).mapped("task_number")
        # create a new task in the 1st project
        self.new_task = self.tasks.create(
            {"name": "New task", "project_id": self.project_1.id}
        )
        # chek the number of the new task
        n = int(self.new_task.task_number) - int(max(all_task_numbers))
        self.assertEqual(n, 1, "task number of new task must be one more")
