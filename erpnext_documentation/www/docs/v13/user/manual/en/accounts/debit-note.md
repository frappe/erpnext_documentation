<!-- add-breadcrumbs -->
# Debit Note

**A Debit Note is a document sent by a buyer to the Supplier notifying that a debit has been recorded against the goods returned to the Supplier.**

A Debit Note is issued for the value of the goods returned. In some cases, sellers are seen sending Debit Notes which should be treated as like another invoice.

A Debit is for your record of the debit against the Items your return.

## 1. How to create Debit Note

The user can make a Debit Note against the Purchase Invoice or they can directly make Debit Note from the Purchase Invoice without reference.

1. Go to the respective Purchase Invoice and click on **Create > Return / Debit Note**.
 ![Debit Note from Invoice](/docs/v13/assets/img/accounts/debit-note-from-purchase-invoice.png)
1. The Supplier and Item details will be fetched as set in the Purchase Invoice.
1. If you had paid partially or fully, make a Payment Entry against the original Purchase Invoice.
1. Save and Submit.

 ![Debit Note](/docs/v13/assets/img/accounts/debit-note.png)

The other steps are similar to a [Purchase Invoice](/docs/v13/user/manual/en/accounts/purchase-invoice).


### 1.1 How does Debit Note affect ledger
The Debit Note will reverse the impact of the purchase invoice.

![Debit Note Ledger](/docs/v13/assets/img/accounts/debit-note-ledger.png)

Refer the [Purchase Invoice](/docs/v13/user/manual/en/accounts/purchase-invoice) page for any other details.

### 1.2 No payment was made against Sales Invoice
In case **no payment** was made against the original invoice, you could just cancel the Sales Invoice. But, if only 5 out of 10 Items are being returned from an invoice, creating a Debit Note is useful for updating the ledger.

## 2. Example
From Supplier Blue Mills, you had purchased Cotton worth Rs 2400 + taxes and at the time of delivery, you found that the products were damaged. Now you returned the product a Debit Note will be issued.

Debit Note with payment entry in ERPNext for above example is as below:

![Creating Debit Note](/docs/v13/assets/img/accounts/creating-debit-note.gif)

### 3. Related Topics
1. [Payment Entry](/docs/v13/user/manual/en/accounts/payment-entry)
1. [Credit Note](/docs/v13/user/manual/en/accounts/credit-note)

{next}
