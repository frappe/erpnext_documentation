<!-- add-breadcrumbs -->
# Credit Note

**A Credit Note is a document sent by a seller to the Customer, notifying that a credit has been made to their account against the goods returned by the buyer.**

A Credit Note is issued for the value of goods returned by the Customer, it may be less than or equal to the total amount of the order. 

## 1. How to make a Credit Note

The user can make a Credit Note against the Sales Invoice or they can directly make Credit Note from the Sales Invoice without reference. Note that to create a Credit Note, the invoice must be paid using a [Payment Entry](/docs/user/manual/en/accounts/payment-entry).

1. Go to the respective Sales Invoice and click on **Create > Return / Credit Note**.
    ![Credit Note from Invoice](/docs/assets/img/accounts/credit-note-from-invoice.png)
1. The Customer and Item details will be fetched as set in the Sales Invoice.
1. If the Customer had paid partially or fully, make a Payment Entry against the original Sales Invoice.
1. Save and Submit.
    <img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/credit-note.png">

The Item quantity and Payment amount will be negative since it's a return.

### 1.1 How does Credit Note affect ledger
Once a Payment Entry is created against the original Sales Invoice, the amount will be added to the Customer's account in negative so that the next time they make a purchase, this amount will be adjusted. 

This is how the ledger is affected after a payment entry against a returned invoice:
![Credit Note Ledger](/docs/assets/img/accounts/credit-note-ledger.png)

Refer the [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice) page for any other details.

### 1.2 No payment was made against Sales Invoice
In case **no payment** was made against the original invoice, you could just cancel the Sales Invoice. But, if only 5 out of 10 Items are being returned from an invoice, creating a Credit Note is useful for updating the ledger.

## 2. Example

Customer Rohan had purchased PVC pipes worth Rs 300 + taxes and at the time of delivery, Customer found that the products were damaged. Now Rohan has returned the product a Credit Note will be issued.

Credit Note with payment entry in ERPNext for above example is as below:

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/credit_note_example1.gif">

### 3. Related Topics
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Debit Note](/docs/user/manual/en/accounts/debit-note)
1. [Sales Return](/docs/user/manual/en/stock/sales-return)