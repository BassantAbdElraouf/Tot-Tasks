from odoo import models, fields,api

class StockTransferNote(models.Model):
    _name = 'stock.transfer.note'

    picking_id = fields.Many2one('stock.picking', required=True)
    note = fields.Text(required=True)
    created_by = fields.Many2one('res.users', default=lambda self: self.env.user)
    created_on = fields.Datetime(default=fields.Datetime.now)
