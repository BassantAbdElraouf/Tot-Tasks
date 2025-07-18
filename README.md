🧩 Module: purchase_note
Extends: purchase

🎯 Purpose:
To enable structured notes on purchase orders with classification and attachments.

📦 Models:
1. purchase.note.category
Note categories (e.g., Financial, Technical, Administrative…)

2. purchase.note
The actual note linked to a purchase order.

3. purchase.note.tag
Optional tags for classification and filtering.
4. purchase.note.attachment
Attachments related to the notes (files, documents, etc.)
------------------------------------------------------------------------------------------------------------
🧩 Module: purchase_budget

🎯 Purpose:
Link purchasing operations to budgets and control expenses efficiently

📦 Models:
1. purchase.budget.plan
Represents the monthly or yearly budget plan associated with each department.

2. purchase.budget.line
Defines budget lines for each type of purchase (equipment, office supplies, maintenance...).

3. purchase.budget.consumption
Tracks actual budget consumption based on confirmed purchase orders.

4. purchase.budget.alert
Triggers alerts when a specific budget threshold is exceeded.

