from odoo import models, fields

class PurchaseNote(models.Model):
    _name = 'purchase.note'
    _description = 'Purchase Note'

    purchase_id = fields.Many2one('purchase.order', required=True)
    name = fields.Char(required=True)
    description = fields.Text()
    category_id = fields.Many2one('purchase.note.category')
    tag_ids = fields.Many2many('purchase.note.tag', string="Tags")
    attachment_ids = fields.One2many('purchase.note.attachment', 'note_id')
