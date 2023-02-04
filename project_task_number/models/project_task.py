from ast import Expression

from odoo import api, fields, models


class ProjectTask(models.Model):
    """Defines the task number"""

    _inherit = "project.task"

    task_number = fields.Char(readonly=True)

    @api.model
    def create(self, vals):
        """Create number of project task"""
        seq = self.env["ir.sequence"].next_by_code("project.task")
        vals["task_number"] = seq
        return super(ProjectTask, self).create(vals)

    @api.model
    def name_get(self):
        """Added task number to name of task"""
        result = []
        for task in self:
            name = (
                "[" + task.task_number + "] " + task.name + " - " + task.project_id.name
            )
            result.append((task.id, name))
        return result

    @api.model
    def _name_search(
        self,
        name,
        task_number,
        args=None,
        operator="ilike",
        limit=100,
        name_get_uid=None,
    ):
        args = args or []
        if operator == "ilike" and not (name or task_number or "").strip():
            domain = []
        else:
            domain = [
                "|",
                ("name", operator, name),
                ("task_number", operator, task_number),
            ]
        return self._search(
            Expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid
        )

    # @api.model
    # def name_search(self, name='', args=None, limit=100):

    #     res = super(ProjectTask, self).name_search(name='', args=None,
    #     operator='ilike', limit=100)

    #     ids = self.search(args + ['|', ('task_number', '=', name),
    #     ('name', '=', name)], limit=limit)

    #     if ids:

    #         return ids.name_get()

    #     return res
