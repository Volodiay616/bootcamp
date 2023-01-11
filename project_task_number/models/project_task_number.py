from odoo import fields, models

class ProjectTaskNumber(models.Model):
    """"""
    _inherit = "project.task"
    
    task_number = fields.Char(compute = "_compute_task_number", readonly = True)
    
    @api.depends("order_id.order_line", "sequence")
    def _compute_task_number(self):
        order_ids = self.mapped("order_id")
        for order in order_ids:
            n = 1
            for line in order.order_line.sorted(lambda l: l.sequence):
                line.line_number = n
                n += 1
        
        for journal in self:
            vals_write = {}
            for seq_field in sequence_fields:
                if not journal[seq_field]:
                    vals = {
                        'name': _('Securisation of %s - %s') % (seq_field, journal.name),
                        'code': 'SECUR%s-%s' % (journal.id, seq_field),
                        'implementation': 'no_gap',
                        'prefix': '',
                        'suffix': '',
                        'padding': 0,
                        'company_id': journal.company_id.id}
                    seq = self.env['ir.sequence'].create(vals)
                    vals_write[seq_field] = seq.id
            if vals_write:
                journal.write(vals_write)
    