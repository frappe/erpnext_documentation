---
title: Distributed Cost Center
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: In ERPNext, a Distributed cost center enhances the cost center dimension to allow the distribution of the tagged value to a set of cost centers. A distributed cost center can be created out of different ratios of ordinary cost centers and it can be tagged against the GL entries.
 keywords: frappe, erpnext, accounting reports, cost center, GL Entry.
---

<!-- add-breadcrumbs -->
# Distributed Cost Center
 
The Distributed cost center enhances the cost center dimension to allow the distribution of the tagged value to a set of cost centers. A distributed cost center can be created out of different ratios of ordinary cost centers and it can be tagged against the GL entries. Expense and income will not affect directly to the cost center. It will be distributed with the selected cost centers as 100% equal calculation.

## 1. How to create a Distributed Cost Center
1. Go to the cost center list, click on New.
1. Enter the cost center name.
1. Select the parent cost center.
1. Enable the checkbox, **Enable Distributed Cost Center**: On enabling this the distributed cost center table will show, Then select the cost center and allocate the corresponding percentage.
1. Once you are done click on Save.

  <img class="screenshot" alt="Distributed Cost Center" src="{{docs_base_url}}/assets/img/accounts/distributed_cost_center.png">

The following reports will be automatically updated when cost center filter is added:

  * [Accounting Reports](/docs/user/manual/en/accounts/accounting-reports)
    * Financial Statements
    * Budget Variance
    * General Ledger
  * [Profitability Analysis](/docs/user/manual/en/accounts/articles/tracking-project-profitability-using-cost-center)

### 2. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
