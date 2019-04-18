<!-- add-breadcrumbs -->
# Journal Entry

All types of accounting entries other than **Sales Invoice** and **Purchase Invoice** are made using the **Journal Entry**. A **Journal Entry** 
is a standard accounting transaction that affects
multiple Accounts and the sum of debits is equal to the sum of credits. A Journal Entry Impacts the main ledger.

### 1. How to create a Journal Entry
1. Go to: **Accounts > Company and Accounts > Journal Entry > New**.
1. The default Entry Type will be Journal Entry.
1. You can change the Posting Date.
1. Expand the table, select an Account from which amount is debited.
1. Select the party type and party if it's a Debtor entry.
1. Select the cost center (depending on whether income or Expense).
1. Add a row where the amount will be credited.
1. Note that, in the end, total debit and credit amounts should add up to be the same.
1. Save and Submit.

<img class="screenshot" alt="Journal Entry" src="{{docs_base_url}}/assets/img/accounts/journal-entry.png">

### 2. Features
#### 2.1 Reverse Journal Entry
In any submitted Journal Entry, there is a dedicated button to reverse a Journal Entry. On clicking the button, the system creates a new Journal Entry by reversing debit and credit amount against all the accounts.

<img alt="Reverse Journal Entry" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reverse-journal-entry.png">

#### 2.2 Difference Entry
The “Difference” field is the difference between the Debit and Credit amounts.
This should be zero if the Journal Entry is to be “Submitted”. If this
number is not zero, you can click on “Make Difference Entry” and it will automatically add a new row
with the amount required to make the total as zero.

#### 2.3 Reference Type
When editing a row, you can also select a Reference Type to link the Journal Entry with an Invoice, Order, Claim, Loan etc,. Link it to a voucher or invoice if it affects the “outstanding” amount of that invoice. **Is Advance**: Select “Yes” if you want to make it selectable in an Invoice. Other information in case it is a Bank Payment or a bill.

### 3. Some examples of common Journal Entries
Let's take a look at some of the common accounting entries that can be done via Journal
Voucher.

#### 3.1 Expenses (non accruing)

Many times it may not be necessary to accrue an expense, but it can be
directly booked against an expense Account on payment. For example a travel
allowance or a telephone bill. You can directly debit Telephone Expense
(instead of your telephone company) and credit your Bank on payment.

  * Debit: Expense Account (like Telephone expense).
  * Credit: Bank or Cash Account.

#### 3.2 Bad Debts or Write Offs

If you are writing off an Invoice as a bad debt, you can create a Journal
Voucher similar to a Payment, except instead of debiting your Bank, you can
debit an Expense Account called Bad Debts.

  * Debit: Bad Debts Written Off.
  * Credit: Customer.

> Note: There may be regulations in your country before you can write off bad
debts.

#### 3.3 Depreciation

Depreciation is when you write off certain value of your assets as an expense.
For example if you have a computer that you will use for say 5 years, you can
distribute its expense over the period and pass a Journal Entry at the end
of each year reducing its value by a certain percentage.

  * Debit: Depreciation (Expense).
  * Credit: Asset (the Account under which you had booked the asset to be depreciated).

> Note: There may be regulations in your country that define by how much
amount you can depreciate a class of Assets.

#### 3.4 Credit Note

"Credit Note" is made for a Customer against a Sales Invoice when the 
company needs to adjust a payment for returned goods. When a Credit Note
is made, the seller can either make a payment to the customer or adjust 
the amount in another invoice.

  * Debit: Sales Return Account.
  * Credit: Customer Account.
  
#### 3.5 Debit Note

"Debit Note" is made for a Supplier against a Purchase Invoice or accepted 
as a credit note from supplier when a company returns goods. When a Debit
Note is made, the company can either receive a payment from the supplier or 
adjust the amount in another invoice.

  * Debit: Supplier Account.
  * Credit: Purchase Return Account.

#### 3.6 Excise Entry

When a Company buys goods from a Supplier, company pays excise duty
on these goods to Supplier. And when a company sells these goods to Customers, 
it receives excise duty. Company will deduct payable excise duty and deposit balance 
in Govt. account.

  * When a Company buys goods with Excise duty: 
    * Debit: Purchase Account, Excise Duty Account.
  	* Credit: Supplier Account.
	
  * When a Company sells goods with Excise duty: 
    * Debit: Customer Account.
    * Credit: Sales Account, Excise Duty Account.

> Note: Applicable in India, might not be applicable for your country. 
Please check your country regulations.

#### 4. Related Topics
1. [Inter Company Journal Entry](/docs/user/manual/en/accounts/inter-company-journal-entry)
1. [Credit Note](/docs/user/manual/en/accounts/credit-note)
1. [Debit Note](/docs/user/manual/en/accounts/debit-note)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Difference Entry Button](/docs/user/manual/en/accounts/articles/difference-entry-button)
1. [Finance Book](/docs/user/manual/en/accounts/articles/finance-book)