from odoo import models, fields,api

class StockItemDamage(models.Model):
    _name = 'stock.item.damage'

    product_id = fields.Many2one('product.product', required=True)
    location_id = fields.Many2one('stock.location', required=True)
    damage_type = fields.Selection([
        ('storage', 'Storage'),
        ('transport', 'Transport'),
        ('handling', 'Handling')
    ], required=True)
    quantity = fields.Float(required=True)
    damage_reason = fields.Text()
    date_damaged = fields.Date(default=fields.Date.context_today)
    reported_by = fields.Many2one('res.users', default=lambda self: self.env.user)
