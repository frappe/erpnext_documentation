<!-- add-breadcrumbs -->
# Invoice Discounting

**Invoice discounting is the practice of using a company's unpaid sales invoices as collateral for a short term loan, which is issued by a bank or a finance company.**

To access the Invoice discounting list, go to:
> Home > Accounting > Banking and Payments > Invoice Discounting

## 1. Prerequisites

You need to create following ledgers in order to post invoice discounting transactions.

* **Short Term Loan:** A ledger under the 'Current Liabilities' > 'Loans (Liabilities)' group for loan.
* **Bank Account Charges:** An expense ledger for charges levied by the bank.
* **Accounts Receivable Credit Account:** A control account of type receivable.
* **Accounts Receivable Discounted Account:** A receivable account for invoices which have been discounted.
* **Accounts Receivable Unpaid Account:** A receivable account for invoices which were discounted and remain unpaid even after the loan period is over.

## 2. How to Post an Invoice Discounting Transaction

1. Go to the Invoice Discounting list, click on New.
1. Enter Posting Date and Loan Start Date. Enter the Loan Period in days.
1. Select invoices either manually in the table or by clicking on the 'Get Invoices' button on the top right.
1. Select Short Term Loan Account, Bank Account, and Bank Charges Account.
1. Select Accounts Receivable Credit Account, Accounts Receivable Discounted Account and Accounts Receivable Unpaid Account.
1. Click on Save then Submit.
1. After submitting the Invoice Discounting form, click on the **Disburse Loan**.
  <img class="screenshot" alt="Lead" src="{{docs_base_url}}/assets/img/accounts/invoice_discounting.png">
1. You'll be taken to a [Journal Entry](/docs/user/manual/en/accounts/journal-entry) screen. Save and Submit the Journal Entry.
  ![Journal Entry](/docs/assets/img/accounts/invoice-discounting-je.png)
  
## 2. Features

### 2.1 Import Invoices
Click on 'Get Invoices' button to import invoices. You can import invoices by filtering on certain criteria.

* Invoices created against a specific Customer.
* Date range between which the invoices were raised.
* Minimum and maximum amount.

You can also specify multiple of the above filters.

### 2.2 Closing the Loan
When you repay the loan at the end of the loan period or before that, you can update the same by clicking on 'Close Loan' button.
  ![Journal Entry](/docs/assets/img/accounts/invoice-discounting-disbursed.png)
System will prepare the Journal Entry. Review and Submit the it.

### 2.3 Auto Update of Ledgers at the end of Loan Period
If the loan is not repaid at the end of loan period, system will create a Journal Entry via a scheduled job to shift value from 'Accounts Receivable Discounted Account' to 'Accounts Receivable Unpaid Account'. This will make it easy to trace the invoices which were discounted and remained unpaid at the end of the loan period.
