<!-- add-breadcrumbs -->
# Implementation Strategy

Before you start managing your company operations in ERPNext, you must first become familiar with the system and the terms used. For this, we recommend the two-phase implementation strategy. A **Test Phase**, where you enter dummy records representing your day-to-day transactions, and a **Live Phase**, where you start entering the live data.

## 1. Test Phase

  * Read the [Manual](/docs/user/manual/en).
  * Create a trial instance on [erpnext.com](https://erpnext.com).
  * Create [Customer Group](/docs/user/manual/en/CRM/customer-group), [Item Group](/docs/user/manual/en/stock/item-group), [Warehouse](/docs/user/manual/en/stock/warehouse), [Supplier Group](/docs/user/manual/en/buying/supplier-group) records.
  * Create a few [Customer](/docs/user/manual/en/CRM/customer), [Supplier](/docs/user/manual/en/buying/supplier) and [Item](/docs/user/manual/en/stock/item) records.
  * Complete a standard sales cycle:  [Lead](/docs/user/manual/en/CRM/lead) > [Opportunity](/docs/user/manual/en/CRM/opportunity) > [Quotation](/docs/user/manual/en/selling/quotation) > [Sales Order](/docs/user/manual/en/selling/sales-order) > [Delivery Note](/docs/user/manual/en/stock/delivery-note) > [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice) > [Payment Entry](/docs/user/manual/en/accounts/payment-entry).
  * Complete a standard purchase cycle: [Material Request](/docs/user/manual/en/stock/material-request) > [Purchase Order](/docs/user/manual/en/buying/purchase-order) > [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt) > [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice) > [Payment Entry](/docs/user/manual/en/accounts/payment-entry).
  * If applicable complete a manufacturing cycle: [BOM](/docs/user/manual/en/manufacturing/bill-of-materials) > [Production Plan](/docs/user/manual/en/manufacturing/production-plan) > [Work Order](/docs/user/manual/en/manufacturing/work-order) > [Stock Entry](/docs/user/manual/en/stock/stock-entry)
  * Create [Custom DocType](/docs/user/manual/en/customize-erpnext/doctype), [Custom Field](/docs/user/manual/en/customize-erpnext/custom-field), [Print Format](https://docs.erpnext.com/docs/user/manual/en/setting-up/print/print-format).
  * Replicate a real life scenario into the system.

## 2. Live Phase

Once you are familiar with ERPNext, set it up and start entering your live data!

* Sign up for a new instance at [https://erpnext.com](https://erpnext.com). Alternatively, you can just [delete the transactions](/docs/user/manual/en/setting-up/articles/delete-a-company-and-all-related-transactions) but keep the master data in the instance you have already created.
* Import the master data like customers, suppliers, items via [Data Import Tool](/docs/user/manual/en/setting-up/data/data-import).
* Review the module-wise settings like [Selling Settings](/docs/user/manual/en/selling/selling-settings), [Buying Settings](/docs/user/manual/en/buying/buying-settings), [Stock Settings](/docs/user/manual/en/stock/stock-settings). 
* Import opening stock using [Stock Reconciliation](/docs/user/manual/en/stock/stock-reconciliation#1-how-to-create-a-stock-reconciliation-to-post-opening-stock).
* Import outstanding invoices using [Opening Invoice Creation Tool](/docs/user/manual/en/accounts/opening-invoice-creation-tool)
* Import [opening balance](/docs/user/manual/en/accounts/opening-balance).
* Go-live!

{next}
