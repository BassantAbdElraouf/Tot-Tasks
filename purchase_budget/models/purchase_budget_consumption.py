from odoo import models, fields

class PurchaseBudgetConsumption(models.Model):
    _name = 'purchase.budget.consumption'

    budget_line_id = fields.Many2one('purchase.budget.line', string="Budget Line", required=True)
    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")
    amount_spent = fields.Float(string="Amount Spent")
    date = fields.Date()
