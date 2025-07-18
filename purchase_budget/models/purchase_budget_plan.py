from odoo import models, fields

class PurchaseBudgetPlan(models.Model):
    _name = 'purchase.budget.plan'

    name = fields.Char(required=True)
    fiscal_year = fields.Integer(string="Fiscal Year")
    department_id = fields.Many2one('hr.department', string="Department")
    start_date = fields.Date()
    end_date = fields.Date()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('closed', 'Closed')
    ], default='draft')
