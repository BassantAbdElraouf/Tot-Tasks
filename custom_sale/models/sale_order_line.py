from odoo import models, fields,api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _onchange_product_discount(self):
        for line in self:
            if line.product_id and line.product_id.categ_id:
                line.discount = line.product_id.categ_id.category_discount or 0.0

