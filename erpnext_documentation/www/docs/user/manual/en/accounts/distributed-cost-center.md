---
title: Distributed Cost Center
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A Distributed Cost Center is a Cost Center in which multiple Cost Centers are tagged with an appropriate percentage.
 keywords: frappe, erpnext, accounting reports, Cost Center, GL Entry.
---

<!-- add-breadcrumbs -->
# Distributed Cost Center

**A Distributed Cost Center is a *Cost Center* in which multiple Cost Centers are tagged with an appropriate percentage.**

For example, you can mention the Cost Center 'A' as a Distributed Cost Center. when its income, expense, and budget are shared among various Cost Centers like 'B' and 'C' with some percentage equivalence.

In ERPNext you can create Distributed Cost Center and use them in transactions and reports. Expense and income will not affect directly to the Cost Center. It will be distributed with the selected Cost Centers as 100% equal calculation.

## 1. How to create a Distributed Cost Center
1. Go to the Cost Center list, click on New.
1. Enter the Cost Center name.
1. Select the parent Cost Center.
1. Enable the checkbox, **Enable Distributed Cost Center**: On enabling this the distributed Cost Center table will show, Then select the Cost Center and allocate the corresponding percentage.
1. Once you are done click on Save.

  <img class="screenshot" alt="Distributed Cost Center" src="{{docs_base_url}}/assets/img/accounts/distributed_cost_center.png">

The following reports will be automatically updated when Cost Center filter is added:

  * [Accounting Reports](/docs/user/manual/en/accounts/accounting-reports)
    * Financial Statements
    * Budget Variance
    * General Ledger
  * [Profitability Analysis](/docs/user/manual/en/accounts/articles/tracking-project-profitability-using-cost-center)

### 2. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)