# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Sale Order Line Number",
    "version": "14.0.0.0.1",
    "category": "Sales",
    "author": "Cetmix bootcamp",
    "website": "https://github.com/volodiay616/bootcamp",
    "license": "AGPL-3",
    "depends": ["sale"],
    "summary": "Line numbers in Sales Order lines",
    "application": False,
    "installable": True,
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        # 'report/sale_order_line_report_views.xml',
        "report/sale_order_line_report_templates.xml",
        "views/sale_order_line_views.xml",
        "views/sale_order_line_tag_views.xml",
        "report/sale_order_line_report_views.xml",
    ],
    "demo": [
        "data/demo_data.xml",
    ],
}
