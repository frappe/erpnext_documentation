<!-- add-breadcrumbs -->
# Accounting Dimensions

Accounting Dimensions are available in ERPNext from version 12 onwards.

### 1.What is dimensional accounting?
Dimensional accounting is basically tagging each transaction with appropriate dimensions like Branch, Business Unit, etc. This allows you to maintain each segment separately, thereby limiting the overall maintenance on GL accounts and your chart of accounts remains pure.

In ERPNext you can create custom configurable accounting dimensions and use them in transactions and reports.

### 2.How to create accounting dimensions in ERPNext?

1. Go to **Accounting > Settings > Accounting Dimensions**.
1. Select the reference document which you want to use as custom dimension.
1. Enter the name of the dimension (This name will appear in the transactions for which dimensions are created).
1. Check "Mandatory" checkbox if you want the dimension to be mandatory in transactions.
1. Optionally there is a "Disable" checkbox available which allows you to disable a specific dimension in case you don't need it anymore.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/accounting-dimension.png">

Once you create the dimensions you see these custom accounting dimensions in Accounting Dimensions section while making invoices or during any other transactions that affects the General Ledger.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-section.png">

Once you submit the transaction these transactions will be reflected in GL Entries as well wherever necessary

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/gl-entry.png">

You can also filter various financial reports like Profit and Loss Statement, Balance Sheet, General Ledger based on these dimensions.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/report-dimension.png">