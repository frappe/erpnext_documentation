<!-- add-breadcrumbs -->
# Advance Payment Entry

**Payment done by the customer before accepting delivery of the product is an Advance Payment.**

For Orders of high value, businesses expect advance payment.

Consider a Customer- Jane D'souza placing an order for a luxury furniture item costing ₹24,000 She is asked to give some advance before the furniture house begins work on her order. She gives them ₹10,000 in cash.

In ERPNext, advance payment entry is created using the same Payment Entry form. The only difference is that Payment Entry is made against a Sales Order and advance payment entry is made against a Sales Invoice.

![PE from SO](/docs/assets/img/accounts/advance-payment-1.png)

> Note: If payment is not linked to an invoice, it is considered as an advance payment.

## 1. Prerequisites
To create an advance payment entry, these need to be created first:

* [Sales Order](/docs/user/manual/en/selling/sales-order)

    Or

* [Purchase Order](/docs/user/manual/en/buying/purchase-order)

## 2. How to create Advance Payment Entry
Once a Sales Order or Purchase Order is submitted, you will find an option to create a Payment against it.

1. Go to Sales Order and click on **Make > Payment Entry**.
1. Set/check the accounts.
1. Save and Submit.


Any Payment Entry that is not linked to an invoice is considered as advance payment by the ERPNext system.

If the Customer has given $5,000 as cash advance, it will be recorded as a
credit entry against the Customer. To balance it with the Debit Entry [as per the Double
accounting system] $5000 is debited against the Company's cash account.

### 2.2 Receive advance payment
You can receive the advances from a Sales Invoice.

<img class="screenshot" alt="Advace Payment" src="{{docs_base_url}}/assets/img/accounts/advance-payment-3.png">

When making a new Sales Invoice for the same Customer, mention the advance
in the Sales Invoice Form. To link the Sales Invoice to the Payment which mentions the advance
payment entry, click on the **Get Advances Received**. The amounts will be fetched automatically.

Save and submit the Sales Invoice.

### 2.3 Double entry accounting
Double entry bookkeeping is a system of accounting in which every transaction
has a corresponding positive and negative entry - debits and credits. Every
transaction involves a [debit entry](http://www.e-conomic.co.uk/accountingsystem/glossary/debit) in one account
and a [credit entry](http://www.e-conomic.co.uk/accountingsystem/glossary/credit) in another.

This means that every transaction must be recorded in two accounts; one account will be debited because it receives value and the other account will be credited because it has given value. Keep this in mind if you make payments using Journal Entry instead of Payment Entry.

Save and submit the Payment Entry after complete payment has been made against the invoice.

### 4. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Journal Entry](/docs/user/manual/en/accounts/journal-entry)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
