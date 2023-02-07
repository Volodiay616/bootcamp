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
    def _name_search(self, name, args=None, operator="ilike", limit=100):
        args = list(args or [])
        if operator == "ilike" and not (name or "").strip():
            domain = []
        else:
            domain = [
                "|",
                ("name", operator, name),
                ("task_number", operator, name),
            ]
        return self._search(Expression.AND([domain, args]), limit=limit)
