<!-- add-breadcrumbs -->
# Migrate To Perpetual Inventory

Perpetual Inventory Valuation is activated by default in the system.

For the users who are currently following periodic inventory valuation system, and wish to migrate to perpetual inventory valuation system, please follow the steps explained below.

### 1. How to Migrate to Perpetual Inventory

1. To enable perpetual Inventory, ensure that the Stock in Hand Account is synced with the value of actual stock value in your Warehouse(s). To sync it, you will have to create a Journal Entry for the difference amount against expense account (generally used in Purchase Invoice).

  For example, when perpetual inventory was disabled, you must be having Expense (Cost of Goods Sold) booked via Purchase Invoices. Now, you will have to create a Journal Entry to move the value of existing stock from expense account to stock in hand account.

  Cr. Expense account ......... XXX
  
  Dr. Stock in Hand account ... XXX

  It can also work other-way round if you were selecting a stock in hand account in the Purchase Invoice.

1. Before enabling Perpetual Inventory, ensure that Stock Accounts (ledger) is linked for the existing Warehouse. The stock account for a Warehouse can be set at three levels.

  * In the Warehouse master itself
  * In the Parent Warehouse master
  * Default Stock in Hand Account in the Company master, if you maintain only one Stock-in-hand account for all the Warehouses.

1. Journal Entry to Update Stock Received but not Billed account

  An account "Stock Received but not Billed" is an adjustment account which reflects the value of the stock for which Purchase Receipt has been submitted, but Purchase Invoice is yet to created. A Journal Entry should be created to update the value open Purchase Receipt pending for billing into "Stock Received but not Billed" account.

  To know the value of the stock received but not billed, you can refer the report "Received Items Pending for Billing" in the Accounts module.

  Create a Journal Entry as follows to update the value in Stock Received but not Billed account.

  Cr. Stock Received but not Billed ........... XXX
  
  Dr. Expense Account (COGS) .................. XXX

1. Setup the following default accounts for each Company 

  * Stock Received But Not Billed
  * Stock Adjustment Account
  * Expenses Included In Valuation
  * Cost Center
  * Activate Perpetual Inventory

1. Go to: **Home > Accounting > Company**
    
    <img class="screenshot" alt="Perpetual Inventory" src="{{docs_base_url}}/assets/img/accounts/perpetual-1.png">

#### 2. Related Topics
1. [Accounting Of Inventory Stock](/docs/user/manual/en/stock/accounting-of-inventory-stock)
1. [Perpetual Inventory](/docs/user/manual/en/stock/perpetual-inventory)