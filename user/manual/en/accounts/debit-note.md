<!-- add-breadcrumbs -->
# Debit Note

**A Debit Note is a document sent by a buyer to the Supplier notifying that a debit has been recorded against the goods returned to the Supplier.**

A Debit Note is issued for the value of the goods returned. In some cases, sellers are seen sending Debit Notes which should be treated as like another invoice.

A Debit is for your record of the debit against the Items your return.

## 1. How to create Debit Note

The user can make a Debit Note against the Purchase Invoice or they can directly make Debit Note from the Purchase Invoice without reference.

1. Go to the respective Purchase Invoice and click on **Create > Return / Debit Note**.
 ![Debit Note from Invoice](/docs/assets/img/accounts/debit-note-from-invoice.png)
1. The Supplier and Item details will be fetched as set in the Purchase Invoice.
1. If you had paid partially or fully, make a Payment Entry against the original Purchase Invoice.
1. Save and Submit.
 <img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/debit-note.png">

The other steps are similar to a [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice).


### 1.1 How does Debit Note affect ledger
Once a Payment Entry is created against the original Purchase Invoice, the amount will be added to the Supplier's account in negative so that the next time you make a purchase, this amount will be adjusted. 

This is how the ledger is affected after a payment entry against a returned invoice:
![Debit Note Ledger](/docs/assets/img/accounts/debit-note-ledger.png)

Refer the [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice) page for any other details.

### 1.2 No payment was made against Sales Invoice
In case **no payment** was made against the original invoice, you could just cancel the Sales Invoice. But, if only 5 out of 10 Items are being returned from an invoice, creating a Debit Note is useful for updating the ledger.

## 2. Example
From Supplier Blue Mills, you had purchased Cotton worth Rs 2400 + taxes and at the time of delivery, you found that the products were damaged. Now you returned the product a Debit Note will be issued.

Debit Note with payment entry in ERPNext for above example is as below:

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/debit_note_example1.gif">

### 3. Related Topics
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Credit Note](/docs/user/manual/en/accounts/creit-note)
