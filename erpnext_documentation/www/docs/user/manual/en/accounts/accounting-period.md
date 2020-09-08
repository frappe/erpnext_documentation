<!-- add-breadcrumbs -->
# Accounting Period

**An Accounting Period defines a time period in which financial statements are recorded.**

In ERPNext, Accounting Period is a timeframe outside which selected submittable transactions (like Sales/Purchase Invoice, Stock Entry, Payroll Entry, Journal Entry etc) are not allowed to be created. In other words, the selected transactions are only allowed to be created within the Accounting Period.

## 1. Why is Accounting Period needed?

When transactions are submitted they affect the ledgers and hence the reports which process the ledger data.
This can cause issues when financial reports have to be generated for audit by authorities or for closing the accounting books for the financial year.

Here Accounting Period can be used to limit the time period within which transactions can be submitted to preserve
the integrity of the corresponding reports.

## 2. What is the "Closed" option for the selected transactions used for?

If you have added a transaction to an Accounting Period and you want to prevent its submission before the Accounting Period
closes then you can select the "Closed" checkbox to do that.

Do note that if the Accounting Period ends, none of the transactions will be submittable.

## 3. How to create an Accounting Period
1. Enter a name for the Accounting Period.
1. Define a time frame by setting Start and End Dates.
1. Add or remove transactions from the table. Note that all transactions listed in the table will be restricted after the accounting period closes/ends.
1. You can Close a transaction before the Accounting Period ends too like discussed above.
1. Save and Submit.
    ![Accounting Period](/docs/assets/img/accounts/accounting-period.png)


If you try to submit a closed transaction or after its Accounting Period ends, you will see a validation error preventing you from doing so.
![Accounting Period](/docs/assets/img/accounts/accounting-period-1.png)

> Note: No role can submit transactions defined in the Accounting Period, even the Role set in 'Role Allowed to Set Frozen Accounts & Edit Frozen Entries' in [Account Settings](/docs/user/manual/en/accounts/accounts-settings).

## 2. Related Topics
* [How Accounting Period is used for Closing Accounting Books](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
* [Period Closing Voucher](/docs/user/manual/en/accounts/period-closing-voucher)