🧩 Module: purchase_note

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
--------------------------------------------------------------------------------------------------------------

🧩 Module: tracking_stock

🎯 Purpose:
Enhance warehouse tracking with safety, quality, and traceability measures.

📦 Models:
1. stock.item.damage
Records damaged items during storage or transportation.

2. stock.transfer.note
Notes added by staff during internal or external transfers.

3. stock.location.restriction
Defines storage location restrictions (e.g., hazardous or flammable materials).

4. stock.picking.temperature.log
Logs product temperature during transport — especially useful for sensitive goods.
---------------------------------------------------------------------------------------------------------------
🧩 Module: custom_sale

🎯 Purpose:
Automate discounts, track user commissions, and manage delivery deadlines in the sales process.

📦 Models:

1. user.commission
Defines commission brackets for users based on sale amount ranges.

2. sale.order.line 
Auto-applies product category discounts when a product is selected.

3. sale.order
Adds a delivery deadline field synced to pickings on confirmation.

4. product.category
Adds a default discount field used in sale order lines.






