<!-- add-breadcrumbs -->
# Budgeting

In ERPNext, you can set and manage budgets against a cost center or a project. This is useful in controlling your expenses.

For example, if you are doing online sales, you can set a budget for search ads, and configure ERPNext to stop or warn you from over spending beyond the set budget.

Budgets are also great for planning purposes. When you are making plans for the next financial year, you would typically target a revenue based on which you would set your expenses. Setting a budget will ensure that your expenses do not get out of hand, at any point.

#### 1. How to Create a new Budget
1. Go to:**Accounts > Budget and Cost Center > Budget > New**.
1. Select a cost center.
1. In the accounts table, select an income/expense account for which a budget is to be set.
    <img class="screenshot" alt="Budget" src="{{docs_base_url}}/assets/img/accounts/budget-account.png">
1. Enter the budget amount for that account.
1. Save and Submit.

#### 1.2  Monthly Distribution

If you have seasonal business, you can also define a Monthly Distribution record, to distribute the budget between months. If you don't set the monthly distribution, ERPNext will calculate the budget on yearly basis or in equal proportion for every month.

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/monthly-budget-distribution.png">

#### 1.3 Control Actions (Alerts)

Control actions can be triggered while material request is being submitted, purchase order is being submitted or while actual expense is being posted (through a journal entry or a purchase invoice). You can set a control action in the Budget form bases on Material Request, Purchase Order, or on actual expenses. Further you can set a control action for annual or monthly budgets.

There are three types of control actions.

* **Stop**: This will not allow users to submit the transaction.
* **Warn**: This will show a warning message but lets the user submit the transaction.
* **Ignore**: This will neither prevent the user from submitting transaction nor show an error message.

You can set separate action for monthly and annual budgets.

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/budget-warning.png">

### 2. Budget Variance Report

At any point of time, user can check Budget Variance Report to analyze the actual expense incurred vs budget allocated against a cost center or a project.

To check Budget Variance report, go to:

**Accounts > Budget and Cost Center > Budget Variance Report**

<img class="screenshot" alt="Budget Variance Report" src="{{docs_base_url}}/assets/img/accounts/budget-variance-report.png">

Here is a video demonstration:
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/wWHkB0jlXNk?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

#### 3. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
