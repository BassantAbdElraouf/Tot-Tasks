from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    note_count = fields.Integer(
        compute='_compute_note_count',
        string='Notes'
    )

    def _compute_note_count(self):
        for rec in self:
            rec.note_count = self.env['purchase.note'].search_count([
                ('purchase_id', '=', rec.id)
            ])

    def action_view_purchase_notes(self):
        self.ensure_one()
        return {
            'name': 'Purchase Notes',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.note',
            'view_mode': 'list,form',
            'domain': [('purchase_id', '=', self.id)],
            'context': {'default_purchase_id': self.id},
        }

