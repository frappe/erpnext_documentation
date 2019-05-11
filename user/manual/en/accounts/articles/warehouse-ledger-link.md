# Stock and Accounting Module Integration

The value of stock stored in the warehouses needs to be tracked.

Each warehouse is linked to a ledger in chart of accounts through the 'Account' field in the warehouse.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/stock_asset_ledger_in_warehouse.png">

If the Account field is empty in a warehouse, then the Account mentioned in the parent of that warehouse is considered. If an Account could not be determined by tracing the hierarchy, then the Default Inventory Account mentioned in the Company record is considered.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/default_inventory_account.png">

When a company is created, a ledger named 'Stock In Hand' is created by default in Chart of Accounts.

**Chart of Accounts > Assets > Current Assets > Stock Assets > Stock In Hand.**

If required, you can create additional ledgers under 'Stock Assets' group.

<img class="screenshot" alt="Stock Asset Ledger" src="{{docs_base_url}}/assets/img/accounts/stock_asset_ledger.png">
