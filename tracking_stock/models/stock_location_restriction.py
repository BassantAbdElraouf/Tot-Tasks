from odoo import models, fields,api

class StockLocationRestriction(models.Model):
    _name = 'stock.location.restriction'

    location_id = fields.Many2one('stock.location', required=True, ondelete='cascade')
    restriction_type = fields.Selection([
        ('flammable', 'Flammable'),
        ('chemical', 'Chemical'),
        ('refrigerated', 'Refrigerated'),
        ('no_food', 'No Food Allowed'),
        ('electronic_only', 'Electronic Items Only')
    ], required=True)
    description = fields.Text()
