from odoo import models, fields,api

class ProductDiscount(models.Model):
    _inherit = 'product.category'

    category_discount = fields.Float(string="Discount (%)")


