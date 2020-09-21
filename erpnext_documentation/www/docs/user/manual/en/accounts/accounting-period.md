<!-- add-breadcrumbs -->
# Accounting Period

**An Accounting Period defines a time period in which financial statements are recorded.**

In ERPNext, Accounting Period is a timeframe outside which selected submittable transactions (like Sales/Purchase Invoice, Stock Entry, Payroll Entry, Journal Entry etc) are not allowed to be created. In other words, the selected transactions are only allowed to be created within the defined Accounting Period.

**Why is Accounting Period needed?**

When transactions are submitted, they affect the ledgers and the reports which process the ledger data.
This can cause issues when financial reports have to be generated for audit by authorities or for closing the accounting books for the financial year.

Here Accounting Period can be used to limit the time period within which transactions can be submitted to preserve
the integrity of the corresponding reports.

## 1. How to create an Accounting Period

### 1.1 What is the "Closed" option for the selected transactions used for?

![Accounting Period Child Table](/docs/assets/img/accounts/accounting-period-closed.png)

The "Closed" option in the childtable for transaction doctypes is used to select which of them are to be restricted after the end of the Accounting Period.

Do note that if the Accounting Period ends and if any of the selected transactions in the child table don't have "Closed" checked, then they won't be restricted after the Accounting Period ends.

1. Enter a name for the Accounting Period.
1. Define a time frame by setting Start and End Dates.
1. Add or remove transactions from the table. Note that all transactions listed in the table with "Closed" option checked will be restricted after the accounting period ends.
1. Save and Submit.
    ![Accounting Period](/docs/assets/img/accounts/accounting-period.png)


If you try to submit a closed transaction after its Accounting Period ends, you will see a validation error preventing you from doing so.
![Accounting Period](/docs/assets/img/accounts/accounting-period-1.png)

> Note: No role can submit transactions defined in the Accounting Period, even the Role set in 'Role Allowed to Set Frozen Accounts & Edit Frozen Entries' in [Account Settings](/docs/user/manual/en/accounts/accounts-settings).

## 2. Related Topics
* [How Accounting Period is used for Closing Accounting Books](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
* [Period Closing Voucher](/docs/user/manual/en/accounts/period-closing-voucher)
