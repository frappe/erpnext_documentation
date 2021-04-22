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

**A Distributed Cost Center is a Cost Center in which multiple Cost Centers are tagged with an appropriate percentage.**

If a business has a master Cost Center with dependent Cost Centers. In every master Cost Center transaction, it is difficult to update the budget, profit, and loss to each dependent Cost Center manually with the allocated percentage of the master Cost Center. This feature helps to automate the process of manual entry.

For example, In your business, If the Cost Center 'B' and 'C' depend on Cost Center 'A' by 20% and 80%. Then, you can mention 'A' as a Distributed Cost Center. It helps to reflect income, expense, and budget of 'A' in 'B' and 'C' with allocated percentages.

In ERPNext you can create Distributed Cost Center and use them in transactions and reports.

## 1. How to create a Distributed Cost Center
1. Go to the Cost Center list, click on New.
1. Enter the Cost Center name.
1. Select the parent Cost Center.
1. Enable the checkbox, **Enable Distributed Cost Center**: On enabling this, the distributed Cost Center table will show. Here, select the Cost Centers and allocate the corresponding percentage.
1. Once you are done click on Save.

  ![Distributed Cost Center](/docs/v13/assets/img/accounts/distributed-cost-centers.png)


The following reports will be automatically updated when Cost Center filter is added:

  * [Accounting Reports](/docs/v13/user/manual/en/accounts/accounting-reports)
    * Financial Statements
    * Budget Variance
    * General Ledger
  * [Profitability Analysis](/docs/v13/user/manual/en/accounts/articles/tracking-project-profitability-using-cost-center)

### 2. Related Topics
1. [Cost Center](/docs/v13/user/manual/en/accounts/cost-center)

{next}
