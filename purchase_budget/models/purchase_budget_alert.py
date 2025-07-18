from odoo import models, fields

class PurchaseBudgetAlert(models.Model):
    _name = 'purchase.budget.alert'

    budget_line_id = fields.Many2one('purchase.budget.line', string="Budget Line", required=True)
    consumed_percentage = fields.Float()
    alert_type = fields.Selection([
        ('warning', 'Warning'),
        ('critical', 'Critical'),
        ('exceeded', 'Exceeded')
    ])
    notified_to = fields.Many2one('res.users', string="Notified To")
    note = fields.Text()
