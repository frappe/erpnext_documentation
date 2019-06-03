<!-- add-breadcrumbs -->
# Accounting Dimensions

>Introduced in Version 12

### What is Dimensional Accounting?

Dimensional accounting is basically tagging each transaction with appropriate dimensions like Branch, Business Unit, etc. This allows you to maintain each segment separately, thereby limiting the overall maintenance on GL accounts and your chart of accounts remains pure.

In ERPNext you can create configurable accounting dimensions and use them in transactions and reports.


### 1. How to create Accounting Dimensions in ERPNext.

1. Go to **Accounting > Settings > Accounting Dimensions**.
1. Select the reference document which you want to use as custom dimension. For example, if you select Department as reference document, the dimension will based on Department.
1. Enter the name of the dimension (This name will appear in the transactions for which dimensions are created).
1. Check "Mandatory" checkbox if you want the dimension to be mandatory in the transactions.
1. Optionally there is a "Disable" checkbox available which allows you to disable a specific dimension in case you don't need it anymore.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/accounting-dimension.png">


### 2. Features

As you create the dimension, custom fields will be created using a background job for that specific dimension. You can see them in Accounting Dimensions section inside the transactions which have an impact on Accounting entries (GL Entry).

#### 2.1 Using dimensions in transactions:

To tag a transaction with a dimension you can select the specific dimension in Accounting Dimensions section as shown in the screenshot below.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-section.png">

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-transaction.png">

#### 2.2 Filtering Reports based on dimensions

You can also filter various financial reports like Profit and Loss Statement, Balance Sheet, General Ledger based on these dimensions.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/report-dimensions.png">


#### 2.3 Making accounting dimensions mandatory for "Profit and Loss" and "Balance Sheet" Accounts
Profit and Loss is the group of Income and Expense accounts that represent your accounting transactions over a period.

The Balance Sheet accounts are Application of Funds (Assets) and Sources of Funds (Liabilities) that signify the net-worth of your company at any given time.

By selecting the check boxes `Mandatory for Profit and Loss Account` or `Mandatory for Balance Sheet` you can configure you dimensions to be mandatroy for `Profit and Loss` and `Balance Sheet Accounts`.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-mandatory.png">


#### 2.4 Disabling accounting dimensions when no longer required

You can also disable the dimensions if you don't require them anymore. The old transactions having accounting dimensions will remain intact.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-disable.png">


#### Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Budgeting](/docs/user/manual/en/accounts/budgeting)
1. [Accounting Reports](/docs/user/manual/en/accounts/accounting-reports)
