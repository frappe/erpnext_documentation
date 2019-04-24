<!-- add-breadcrumbs -->
# Advance Payment Entry

Payment done by the customer before accepting delivery of the product is an
Advance Payment. For Orders of high value, the business houses expect to
receive advance payment.

__For Example:__ Consider a customer- Jane D'souza placing an order for a double
bed costing $10,000 She is asked to give some advance before the furniture
house begins work on her order. She gives them $5000 in cash.

### 1. How to create Advance Payment Entry
Once Sales Order or Purchase Order is submitted, you will find option to create Advance Payment entry against it.

1. Go to: **Accounts > Company and Accounts > Journal Entry > New**.
1. Expand the transaction row.
1. There will be a field called Is Advance.
1. Select Yes.
1. Save and Submit the Journal Entry.

This is what it looks like:
<img class="screenshot" alt="Advace Payment" src="{{docs_base_url}}/assets/img/accounts/advance-payment-1.png">  

If the customer has given $5000 as cash advance, it will be recorded as a
credit entry against the customer. To balance it with the debit entry [as per the Double
accounting system] enter $5000 as debit against the company's cash account. In
the row "Is Advance" click 'Yes'.

#### 1.2 Receive advance payment
You can receive the advances from a Sales Invoice.

<img class="screenshot" alt="Advace Payment" src="{{docs_base_url}}/assets/img/accounts/advance-payment-3.png">

When you make a new Sales Invoice for the same customer, mention the advance
in the Sales Invoice Form. To link the Sales Invoice to the Journal Entry which mentions the advance
payment entry, click on ‘Get Advances Received’.  Allocate the amount of
advance in the advances table. The accounting will be adjusted accordingly.

Save and submit the Sales Invoice.

### 2. Double entry accounting
Double entry bookkeeping is a system of accounting in which every transaction
has a corresponding positive and negative entry : debits and credits. Every
transaction involves a [debit entry
](http://www.e-conomic.co.uk/accountingsystem/glossary/debit)in one account
and a [credit
entry](http://www.e-conomic.co.uk/accountingsystem/glossary/credit) in another
account. This means that every transaction must be recorded in two accounts;
one account will be debited because it receives value and the other account
will be credited because it has given value.

<img class="screenshot" alt="Advance Payment" src="{{docs_base_url}}/assets/img/accounts/advance-payment-2.png">

Save and submit the Journal Entry. If this document is not saved it will not be pulled in
other accounting documents.

#### 3. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Journal Entry](/docs/user/manual/en/accounts/journal-entry)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
