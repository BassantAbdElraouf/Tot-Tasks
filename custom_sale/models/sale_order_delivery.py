from odoo import models, fields

class DeliverySaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_date = fields.Datetime(string="Delivery Deadline")

    def action_confirm(self):
        print("1")
        res = super().action_confirm()
        for order in self:
            for picking in order.picking_ids:
                if order.delivery_date:
                    print("2")
                    picking.date_deadline = order.delivery_date
        return res
