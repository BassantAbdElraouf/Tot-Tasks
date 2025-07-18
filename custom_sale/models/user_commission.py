from odoo import models, fields

class UserCommission(models.Model):
    _name = 'user.commission'

    user_id = fields.Many2one('res.users', string='User', required=True)
    min_amount = fields.Float(string='Min Amount', required=True)
    max_amount = fields.Float(string='Max Amount', required=True)
    commission = fields.Float(string='Commission (%)', required=True)
