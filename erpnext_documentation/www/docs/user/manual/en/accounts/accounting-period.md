<!-- add-breadcrumbs -->
# Accounting Period

**An Accounting Period defines a period of time in which financial statements are recorded.**

In ERPNext, defining an Accounting Period freezes the entries for the selected transactions in the selected time frame. This means that the selected transactions will not be submittable in the defined Accounting Period.

Consider that you want to generate financial reports for business in Quarter 3 and you want to allow submitting only specific entries in that period. Or you want to freeze all entries that affect the General Ledger. Accounting Period in ERPNext allows doing exactly this.

## 1. How to create an Accounting Period
1. Enter a name for the Accounting Period.
1. Define a time frame by  setting Start and End Dates.
1. Add or remove transactions from the table. Note that all transactions listed in the table will be frozen.
1. Save.
    ![Accounting Period](/docs/assets/img/accounts/accounting-period.png)


You will see a prompt if you try to submit a transaction defined in the Accounting Period.
![Accounting Period](/docs/assets/img/accounts/accounting-period-1.png)

> Note: No role can submit transactions defined in the Accounting Period, even the Role set in 'Role Allowed to Set Frozen Accounts & Edit Frozen Entries' in [Account Settings](/docs/user/manual/en/accounts/accounts-settings).

## 2. Related Topics
* [Period Closing Voucher](/docs/user/manual/en/accounts/period-closing-voucher)