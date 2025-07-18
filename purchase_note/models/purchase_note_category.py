from odoo import models, fields

class PurchaseNoteCategory(models.Model):
    _name = 'purchase.note.category'
    _description = 'Note Category'

    name = fields.Char(required=True)
    description = fields.Text()
    color = fields.Integer()
