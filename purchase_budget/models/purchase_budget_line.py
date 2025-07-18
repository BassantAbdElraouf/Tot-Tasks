from odoo import models, fields

class PurchaseBudgetLine(models.Model):
    _name = 'purchase.budget.line'

    budget_plan_id = fields.Many2one('purchase.budget.plan', string="Budget Plan", required=True)
    product_category_id = fields.Many2one('product.category', string="Product Category")
    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account")
    planned_amount = fields.Float(string="Planned Amount")
    notes = fields.Text()
