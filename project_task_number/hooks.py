from odoo import SUPERUSER_ID, api


def _task_number_post_init(cr, registry):
    """Assigns a task number to all existing tasks"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    # all_tasks = env['project.task'].mapped("project_id")
    all_tasks = env["project.task"].search([])
    for tasks in all_tasks.sorted(lambda l: l.id):
        tasks.task_number = env["ir.sequence"].next_by_code("project.task")
