# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Project Task Number",
    "version": "14.0.0.0.1",
    "category": "Sales",
    "author": "Cetmix bootcamp",
    "website": "https://github.com/volodiay616/bootcamp",
    "license": "AGPL-3",
    "depends": ["project"],
    "summary": "Numbers of tasks in Project Task",
    "application": False,
    "installable": True,
    "data": ["views/project_task_number_views.xml"],
    "post_init_hook": "_task_number_post_init",
}
