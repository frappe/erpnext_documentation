<!-- add-breadcrumbs -->
# Period Closing Voucher

At the end of every year or (quarterly or maybe even monthly), after completing auditing, you can close your books of accounts. This means that you make all your special entries like:

  * Depreciation
  * Change in value of Assets
  * Defer taxes and liabilities
  * Update bad debts

Then book your Profit or Loss.

By doing this, your balance in your Income and Expense Accounts becomes zero. You start a new Fiscal Year (or period) with a balanced Balance Sheet and fresh Profit and Loss account. In ERPNext after making all the special entries via Journal Entry for the current fiscal year, you should set all your Income and Expense accounts to zero via a Period Closing Voucher.

### 1. How to create a Period Closing Voucher

1. Go to: **Accounts > Tools > Period Closing Voucher > New**.
1. Set a posting date.
1. Select the account.
1. Enter remarks.
1. Save and Submit.

#### 1.2 The fields explained
* **Transaction Date** will be Period Closing Voucher's creation date.
* **Posting Date** will be when this entry should be executed. If your Fiscal Year ends on 31st December, then that date should be selected as Posting Date in the Period Closing Voucher.
* **Closing Fiscal Year** will be an year for which you are closing your financial statement.

<img class="screenshot" alt="Period Closing Voucher" src="{{docs_base_url}}/assets/img/accounts/period-closing-voucher.png">

The Period Closing Voucher will make accounting entries (GL Entry). This wil make all your Income and Expense Accounts zero and transfer Profit/Loss balance to the Closing Account.

You should select a liability account like Reserves and Surplus, or Any Revenue Reserve account or into Owners Capital account as Closing Account.

**Note:** If accounting entries are made in a closing fiscal year, even after Period Closing Voucher was created for that Fiscal Year, you should create another Period Closing Voucher. Later voucher will only transfer the pending P&L balance into Closing Account Head.</div>

#### 2. Related Topics
1. [Fiscal Year](/docs/user/manual/en/accounts/fiscal-year)
1. [Tax Withholding Category](/docs/user/manual/en/accounts/tax-withholding-category)
