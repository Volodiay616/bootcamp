from odoo import fields, models


class SaleOrderLineReport(models.AbstractModel):
    _name = "sale.order.line.report"
    _description = "Add Line Number To Quotation / Order Report"
    # _auto = False   
    line_number = fields.Integer('# of Lines', readonly=True)
    
    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['action_report_saleorder']._get_report_from_name('sale.report_saleorder')
        # get the records selected for this rendering of the report
        docs = self.env[report.sale.order.line].browse(docids)
        # return a custom rendering context
        return {
            'line_number': docs
        }