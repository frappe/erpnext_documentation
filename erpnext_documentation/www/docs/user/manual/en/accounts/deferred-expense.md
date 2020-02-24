# Deferred Expense

**Deferred expense is a cost that has already been incurred, but which has not yet been consumed.**

The cost is recorded as an asset until such time as the underlying goods or services are consumed; at that point, the cost is charged to expense. A Deferred Expense is initially recorded as an asset, so that it appears on the balance sheet (usually as a Current Asset, since it is not used as of now and will probably be consumed within one year).

## 1. How to use Deferred Expense

As an example of a Deferred Expense, Unico Plastics pays $10,000 in April for its May rent. It defers this cost at the point of payment (in April) in the prepaid rent asset account. In May, Unico Plastics has now consumed the prepaid asset, so it credits the prepaid rent asset account and debits the rent expense account.

Other examples of Deferred Expenses are:

* Interest costs that are capitalized as part of a fixed asset for which the costs were incurred
* Insurance paid in advance for coverage in future months
* The cost of a fixed asset that is charged to expense over its useful life in the form of depreciation
* The cost incurred to register the issuance of a debt instrument
* The cost of an intangible asset that is charged to expense over its useful life as amortization
* For an Internet Subscription, the amount is paid upfront and service is delivered every month. So it is Deferred Expense for the Customer.

Following is how you can configure Deferred Expense accounting in ERPNext to automate the process.

### 1.1 Item

In the Item master, under Deferred Expense section, check field **Enable Deferred Expense**. In this section, you can also select a Deferred Expense account (Asset Account, preferably Current Asset) for this particular item and no. of months.

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-item-expense.png">


### 1.2 Purchase Invoice

On creation of Purchase Invoice for the Deferred Expense Item, instead of posting in the Expense Account, Deferred Expense account (Asset account) is Credited by the purchase amount. Let's consider a simple example of an Internet subscription here:

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-purchase-invoice.gif">

### 1.3 Journal Entry

Based on the From Date and To Date set in the Purchase Invoice Item table, Journal Entries are created automatically at the end of each month. It debits the value from Deferred Expense account and credits Expense Account selected for an Item in the Purchase Invoice. 


{next}
