from odoo import models, fields

class PurchaseNoteAttachment(models.Model):
    _name = 'purchase.note.attachment'
    _description = 'Note Attachment'

    note_id = fields.Many2one('purchase.note', required=True)
    attachment = fields.Binary(string="File")
    file_name = fields.Char(string="File Name")
