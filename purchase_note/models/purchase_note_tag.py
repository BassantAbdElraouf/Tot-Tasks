from odoo import models, fields

class PurchaseNoteTag(models.Model):
    _name = 'purchase.note.tag'
    _description = 'Note Tag'

    name = fields.Char(required=True)
    color = fields.Integer()
