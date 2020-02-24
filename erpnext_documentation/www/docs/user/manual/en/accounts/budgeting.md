<!-- add-breadcrumbs -->
# Budgeting

**Budgeting is a financial plan that helps controlling Company expenses.**

In ERPNext, you can set and manage budgets against a Cost Center or a Project. This is useful in controlling your expenses. With version 12, you can also create separate [Accounting Dimensions](/docs/user/manual/en/accounts/accounting-dimensions) to tag transactions with different fields.

For example, if you are doing online sales, you can set a budget for search advertisements and configure ERPNext to stop or warn you from overspending beyond a set budget.

Budgets are also great for planning purposes. When you are making plans for the next Financial Year, you would typically target a revenue based on which you would set your expenses. Setting a budget will ensure that your expenses do not get out of hand at any point.

To access the Budget list, go to:
> Home > Accounting > Cost Center and Budgeting > Budget

## 1. How to Create a new Budget
1. Go to the Budget list and click on New.
1. Select what to budget against, Cost Center, Project, or an [Accounting Dimensions](/docs/user/manual/en/accounts/accounting-dimensions).
1. In the accounts table, select an income/expense account for which a budget is to be set. Let's set a budget for telephone expenses for the year.
 <img class="screenshot" alt="Budget" src="{{docs_base_url}}/assets/img/accounts/budget-account.png">
1. Enter the budget amount for that account.
1. Save and Submit.


## 2. Features
### 2.1 Monthly Distribution

You can also define a Monthly Distribution record to distribute the budget between months. If you don't set the monthly distribution, ERPNext will calculate the budget yearly or in equal proportion for every month.

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/monthly-budget-distribution.png">

### 2.2 Control Actions (Alerts)

Control actions can be triggered when:

* A [Material Request](/docs/user/manual/en/stock/material-request) is being submitted
* A [Purchase Order](/docs/user/manual/en/buying/purchase-order) is being submitted 
* When an actual expense is being posted (through a journal entry or a purchase invoice).

You can set a control action in the Budget based on Material Request, Purchase Order, or on actual expenses. Further, you can set a control action for annual or monthly budgets.

![Control Actions](/docs/assets/img/accounts/control-actions.png)

There are three types of control actions.

* **Stop**: This will not allow users to submit the transaction.
* **Warn**: This will show a warning message but lets the user submit the transaction.
* **Ignore**: This will neither prevent the user from submitting transactions nor show an error message.

You can set separate actions for monthly and annual budgets. If you exceed the budget, a warning will be shown:

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/budget-warning.png">

## 3. Budget Variance Report

At any point in time, you can check the Budget Variance Report to analyze the actual expense incurred vs budget allocated against a cost center or a project.

To check the Budget Variance report, go to:

> Home > Accounting > Cost Center and Budgeting > Budget Variance Report

<img class="screenshot" alt="Budget Variance Report" src="{{docs_base_url}}/assets/img/accounts/budget-variance-report.png">

## 4. Video
Here is a video demonstration:
<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/wWHkB0jlXNk?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
 </iframe>
</div>

## 5. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
