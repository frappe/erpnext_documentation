<!-- add-breadcrumbs -->
# Bank Reconciliation

**A Bank Reconciliation Statement is used to match ERPNext account ledgers with your bank account statements.**

If you are receiving payments or making payments via cheques or other non-instantaneous means, the bank statement for a given calendar period will not exactly match your ledger for that account over the same period. The mismatch occurs because the bank usually takes time to “clear” these payments. Also, you may have mailed a cheque to your Supplier and it may be a few days before it is received and deposited by the Supplier.

In ERPNext you can synchronize your bank statements and your Journal Entries using "Clearance Dates." Even if all of your disbursements and receipts are electronic and instantaneous, comparing bank statements and your account ledger is very valuable for ensuring that you have not forgotten to record any transactions, and that your bank has not erroneously posted anything to your account that does not reflect an authorized transaction.

## 1. What is a Bank Reconciliation Statement?
The Bank Reconciliation Statement (a built-in report in ERPNext) provides the difference between the bank balance shown in a statement, as provided by the bank, against the amount shown in the company's Chart of Accounts.

This is what a Bank Reconciliation Statement looks like:

<img class="screenshot" alt="Bank Reconciliation statement" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation-2.png"> 

In the report, check whether the field 'Balance as per bank' matches the Bank Account Statement. If it is matching, it means that the Clearance Date is correctly updated for all the bank entries. If there is a mismatch, it's because of bank entries for which Clearance Date is not yet updated.

## 2. How to reconcile your account ledger

ERPNext has two rather different tools for setting account entries as cleared in order to harmonize the Bank Reconciliation Statement with the statement you receive from your financial institution.

1. A manual reconciliation tool allowing you to directly set clearance dates on payment entries, sales invoice payments or journal entries. This tool does not involve importing any electronic data from your bank into ERPNext. Hence, you might use it with a paper statement: you can review all of your recorded transactions, and for each one that shows up on your paper statement, manually enter its clearance date into ERPNext. When all of the entries on your paper statement correspond to cleared entries in ERPNext, then the "Balance as per bank" on the Bank Reconciliation Statement should match the balance reported by your bank.
2. A semi-automatic reconciliation tool allowing you to reconcile bank transactions against payment entries, sales and purchase invoices, journal entries or expense claims. To use this tool, you must first import the information from your bank statement into ERPNext (as a list of Bank Transaction documents). There are a couple of different methods to accomplish that import. Then you can access a reconcile screen that lets you match the Bank Transactions against ledger entries one by one.

The following sections detail each of these tools in turn.

### 2.1 Manual Bank Reconciliation Tool

To access this tool, simply enter "Bank Clearance" in the search box of the top menubar in ERPNext and click on the "Bank Clearance" option that comes up. You will see a form that looks like this:

<img class="screenshot" alt="Bank Clearance emptyform" src="{{docs_base_url}}/assets/img/accounts/InitialClearanceForm.png">

Enter the ERPNext Account that you want to reconcile in the top left box, the Bank Account you want to reconcile it against in the top right, and the other information in the top section as desired.

Then click on the **Get Payment Entries** button. You will then see the form populate with all of the matching accounting entries, to look something like this:

<img class="screenshot" alt="Bank Clearance emptyform" src="{{docs_base_url}}/assets/img/accounts/AccountClearanceForm.png">

You can see the already reconciled entries (the ones with a value already set for Clearance Date) and the as-of-yet unreconciled entries (the ones for which Clearance Date is blank). Now suppose that the $13,480 payment on row 3 shows up on your next bank statement. You can then simply click in the Clearance Date cell of that row and enter the date that the payment appeared on your bank statement.

When you have filled in all of the Clearance Date entries that you wish, you can click on the **Update Clearance Date** button (below the "Payment Entries" grid) and the entries will be marked as cleared. Now you can go back to the Bank Reconciliation Statement report, and verify whether the "Balance as per bank" line now matches your statement.

### 2.2 Semi-automatic Bank Reconciliation Tool

#### Bank statement upload

You can upload a Bank Statement in CSV or XLS format into ERPNext using the Bank Reconciliation tool. You can access the Bank Reconciliation tool (which is different from the Bank Reconciliation Statement report) by typing "Bank Reconciliation" in the search box in the top menubar and selecting "Open Bank Reconciliation."

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

#### Reconciling Bank Transactions with accounting entries

Once all your bank transactions are imported into ERPNext, you can reconcile them with your existing payments. On the Bank Reconciliation page, enter your Company and Bank Account. Then from the **Menu** button at the top right, select "Reconcile this Account." That will produce a list of all of the unreconciled Bank Transactions for that account that you have imported. If you click on a transaction or choose "Reconcile" from the **Actions** menu button at the right end of a line, a payment reconciliation popup will be displayed.

If it finds any payments that appear to match with the selected bank transaction, ERPNext will propose them to you as possibilities for reconciliation. If any of the options is a correct match, just click on the **Reconcile** button next to it to reconcile that payment with this bank transaction.

<img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/auto_reconciliation.gif">

If ERPNext doesn't propose any payment, you can always select the corresponding payment manually:

<img class="screenshot" alt="Reconcile bank transactions manually" src="{{docs_base_url}}/assets/img/accounts/manual_reconciliation.gif">

You can also create a new payment or invoice directly from the bank reconciliation dashboard.

<img class="screenshot" alt="New payment entry" src="{{docs_base_url}}/assets/img/accounts/new_payment.gif">

### 4. Related Topics
1. [Payment Reconciliation](/docs/user/manual/en/accounts/payment-reconciliation)
1. [Bank Guarantee](/docs/user/manual/en/accounts/bank-guarantee)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
