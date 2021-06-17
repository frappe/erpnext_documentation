# Process Deferred Accounting

**Process Deferred Accounting is a log which is created on every processing of deferred revenue or expense.**

Process Deferred Accounting records are automatically created on booking Deferred Revenue or Expense. It is done via a background job but the user can also create a record for manual Deferred Revenue or Expense booking.

To access the Process Deferred Accounting list, go to:
> Home > Accounting > General Ledger > Process Deferred Accounting

## 1. Prerequisites
Before creating and using a Process Deferred Accounting, it is advised to create and understand the following first:

* [Deferred Revenue](/docs/user/manual/en/accounts/deferred-revenue)
* [Deferred Income](/docs/user/manual/en/accounts/deferred-expense)


## 2. How to create a Process Deferred Accounting
1. Go to Process Deferred Accounting list, click on New.
1. Enter the Company.
1. Select the type of deferred accounting process. Select 'Income' for booking deferred revenue or select 'Expense' for booking deferred expense
1. Expand the posting date.
1. Enter service Start Date and End Date.
1. Save and Submit.

<img class="screenshot" alt="Process Deferred Revenue" src="{{docs_base_url}}/v12/assets/img/accounts/process-deferred-accounting.png">

## 3. Features

### 3.1 On Submitting

On submitting a Process Deferred Accounting document, GL Entries for deferred revenue or expense booking will be created for all the invoices falling between the service Start Date and End Date.

Enter the account if Deferred Revenue or Expense has to be booked only for specific deferred income or expense account

### 3.2 Enabling automatic deferred accounting

To enable automatic deferred accounting, enable the 'Automatically Process Deferred Account Entry' checkbox by navigating to Accounts Settings.

To access Accounts Settings go to:
> Home > Accounting > Accounting Masters > Accounts Settings

<img class="screenshot" alt="Process Deferred Revenue" src="{{docs_base_url}}/v12/assets/img/accounts/process-deferred-accounting-settings.png">
