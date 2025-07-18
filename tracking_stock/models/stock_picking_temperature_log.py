from odoo import models, fields,api

class StockPickingTemperatureLog(models.Model):
    _name = 'stock.picking.temperature.log'

    picking_id = fields.Many2one('stock.picking', required=True)
    temperature = fields.Float(required=True)
    measured_at = fields.Datetime(default=fields.Datetime.now)
    measured_by = fields.Many2one('res.users', default=lambda self: self.env.user)
    note = fields.Text()
