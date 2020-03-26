<!-- add-breadcrumbs -->
# Accounting Dimensions

> Introduced in Version 12

Dimensional accounting means tagging each transaction with appropriate dimensions like Branch, Business Unit, etc. This allows you to maintain each segment separately, thereby limiting the overall maintenance on GL accounts and your Chart of Accounts remains pure.

Cost Center and Project are treated as dimensions by default in ERPNext. On setting a field in Accounting Dimension, that field will be added in transactions reports where applicable. 

In ERPNext you can create configurable accounting dimensions and use them in transactions and reports.

To access the Accounting Dimension list, go to:
> Home > Accounting > Settings > Accounting Dimensions

## 1. How to create Accounting Dimension in ERPNext.

1. Go to the Accounting Dimension list and click on New.
1. Select the Reference Document which you want to use as a custom dimension. For example, if you select Department as Reference Document, the dimension will be based on Department.
1. Enter the name of the dimension (This name will appear in the transactions for which dimensions are created).
1. Inside the Dimension Defaults table you can mention company specific default dimensions as shown in the screenshot below. This dimension will be automatically fetched in the transaction against that specific company.
1. Check "Mandatory" checkbox if you want the dimension to be mandatory in the transactions.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/accounting-dimension.png">


## 2. Features

As you create the dimension, custom fields will be created using a background job for that specific dimension. You can see them in Accounting Dimensions section inside the transactions which have an impact on Accounting entries (GL Entry).

### 2.1 Using dimensions in transactions

To tag a transaction with a dimension you can select the specific dimension in Accounting Dimensions section as shown in the screenshot below.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-section.png">

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-transaction.png">

### 2.2 Filtering Reports based on dimensions

You can also filter various financial reports like Profit and Loss Statement, Balance Sheet, General Ledger based on these dimensions.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/report-dimensions.png">

### 2.3 Making accounting dimensions mandatory for "Profit and Loss" and "Balance Sheet" Accounts
Profit and Loss is the group of Income and Expense accounts that represent your accounting transactions over a period.

The Balance Sheet accounts are Application of Funds (Assets) and Sources of Funds (Liabilities) that signify the net-worth of your company at any given time.

By selecting the check boxes 'Mandatory for Profit and Loss Account' or 'Mandatory for Balance Sheet' you can configure your dimensions to be mandatory for 'Profit and Loss' and 'Balance Sheet Accounts'.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-mandatory.png">

### 2.4 Disabling accounting dimensions when no longer required

You can also disable the dimensions if you don't require them anymore. The old transactions having accounting dimensions will remain intact.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-disable.png">


### Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Budgeting](/docs/user/manual/en/accounts/budgeting)
1. [Accounting Reports](/docs/user/manual/en/accounts/accounting-reports)
