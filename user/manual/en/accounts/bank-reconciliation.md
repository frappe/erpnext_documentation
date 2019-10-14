<!-- add-breadcrumbs -->
# Bank Reconciliation

**A Bank Reconciliation entry is used to match ERPNext account statements with your bank account statements.**

If you are receiving payments or making payments via cheques, the bank statements will not accurately match the dates of your entry, this is because the bank usually takes time to “clear” these payments.

Also, you may have mailed a cheque to your Supplier and it may be a few days before it is received and deposited by the Supplier. In ERPNext you can synchronize your bank statements and your Journal Entries using the transaction dates.

## 1. What is a Bank Reconciliation Statement?
The Bank Reconciliation Report provides the difference between the bank balance shown in an organization's bank statement, as provided by the bank against the amount shown in the companies Chart of Accounts.

This is what a Bank Reconciliation statement looks like:

<img class="screenshot" alt="Bank Reconciliation statement" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation-2.png"> 

In the report, check whether the field 'Balance as per bank' matches the Bank Account Statement. If it is matching, it means that the Clearance Date is correctly updated for all the bank entries. If there is a mismatch, it's because of bank entries for which Clearance Date is not yet updated.

To access Bank Reconciliation, go to:
> Home > Accounts > Banking and Payments > Update Bank Transaction Date

## 2. How to Update Bank Transaction Dates

1. Go to Update Bank Transaction Dates.
1. Select your Bank Account.
1. Select a from and to date.
1. You can choose to include reconciled entries and POS transactions.
1. Click on the **Get Payment Entries** button.
1. Now you will get all the “Bank Voucher” type entries.
1. In each of the entries, on the rightmost column, update the “Clearance Date” field and click on the **Update Clearance Date** button.

By doing this you will be able to sync your bank statements and entries into the system.

<img class="screenshot" alt="Bank Reconciliation" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation.png">
 
## 3. Types of reconciliation tools

ERPNext has two reconciliation tools:

1. A manual reconciliation tool allowing to set clearance dates against payment entries, sales invoice payments or journal entries
2. A semi-automatic reconciliation tool allowing to clear bank transactions against payment entries, sales, and purchase invoices payments, journal entries or expense claims.

### 3.1 Manual Bank Reconciliation Tool

To view this report, go to **Accounts > Banking and Payments > Bank Reconciliation Statement**. In the report, check whether the field 'Balance as per bank' matches the Bank Account Statement. If it is matching, it means that the Clearance Date is correctly updated for all the bank entries. If there is a mismatch, it's because the Clearance Date is not yet updated for the bank entries.


### 3.2 Semi-automatic Bank Reconciliation Tool

#### Bank statement upload

You can upload a Bank Statement in CSV or XLS format into ERPNext using the Bank Reconciliation tool.

1. Download a bank statement from your bank's website

 <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/sample_bank_statement.png">
 Make sure you have at least the date, the debit/credit and the currency on every row of your bank statement.

1. Configure the import format in the Bank DocType

 <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/bank_configuration.png">

 Your file will be read and then ERPNext will use this mapping to dispatch all information into the corresponding fields in the Bank Transaction DocType.

1. Upload your file into ERPNext

 <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/bank_transaction_upload.gif">


#### Bank account synchronization

You can use Plaid (see [Plaid Integrations page](/docs/user/manual/en/erpnext_integration/plaid_integration)) to automatically synchronize your bank account with ERPNext. All your bank transactions will be automatically imported into ERPNext.

Once all your bank transactions are imported into ERPNext, you can reconcile them with your existing payments. If it finds a payment that appears to match with the selected bank transaction, ERPNext will propose you a corresponding payment.

If that payment matches, just click on reconcile to reconcile it with this bank transaction.

<img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/auto_reconciliation.gif">

If ERPNext doesn't propose you any payment, you can always select the corresponding payment manually:

<img class="screenshot" alt="Reconcile bank transactions manually" src="{{docs_base_url}}/assets/img/accounts/manual_reconciliation.gif">

You can also create a new payment or invoice directly from the bank reconciliation dashboard.

<img class="screenshot" alt="New payment entry" src="{{docs_base_url}}/assets/img/accounts/new_payment.gif">

### 4. Related Topics
1. [Payment Reconciliation](/docs/user/manual/en/accounts/payment-reconciliation)
1. [Bank Guarantee](/docs/user/manual/en/accounts/bank-guarantee)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
