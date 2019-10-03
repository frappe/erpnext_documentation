# Deferred Expense

Deferred expense is a cost that has already been incurred, but which has not yet been consumed. The cost is recorded as an asset until such time as the underlying goods or services are consumed; at that point, the cost is charged to expense. A deferred expense is initially recorded as an asset, so that it appears on the balance sheet (usually as a current asset, since it will probably be consumed within one year).


### Deferred Expense Usecase

As an example of a deferred expense, ABC International pays $10,000 in April for its May rent. It defers this cost at the point of payment (in April) in the prepaid rent asset account. In May, ABC has now consumed the prepaid asset, so it 
credits the prepaid rent asset account and debits the rent expense account.

Other examples of deferred expenses are:

* Interest costs that are capitalized as part of a fixed asset for which the costs were incurred
* Insurance paid in advance for coverage in future months
* The cost of a fixed asset that is charged to expense over its useful life in the form of depreciation
* The cost incurred to register the issuance of a debt instrument
* The cost of an intangible asset that is charged to expense over its useful life as amortization

Following is how you can configure Deferred Expense accounting in ERPNext to automate the process.

### Item

In the Item master created for the subscription plan, under Deferred Expense section, check field **Enable Deferred Expense**. In this section, you can also select a Deferred Expense account (Asset Account, preferably Current Asset) for this particular item and no. of months.


### Purchase Invoice

On creation of Purchase Invoice for the Deferred Expense Item, instead of posting in the Expense Account, Deferred Expense account (Asset account) is Credited by the purchase amount.



### Journal Entry

Based on the From Date and To Date set in the Purchase Invoice Item table, Journal Entries are created automatically at the end of each month. It debits the value from Deferred Expense account and credits Expense Account selected for an Item in the Purchase Invoice. Following is the example of Income for the deferred Revenue Item is booked via multiple Journal Entries.


{next}
