<!-- add-breadcrumbs -->
# Purchase Invoice

Purchase Invoice is the exact opposite of your Sales Invoice. It is the bill
that your Supplier sends you for products or services delivered. Here you
accrue expenses to your Supplier. Making a Purchase Invoice is very similar to
making a Purchase Order.

### 1. How to create a Purchase Invoice:

1. Go to **Accounts > Billing > Purchase Invoice > New**.
1. Select the Supplier.
1. The posting date and time will be set to current, you can edit after you tick the checkbox below Posting Time.
1. Set the Due Date for payment. 
1. You can tick Is Paid if the amount has already been paid.
1. Add items and quantities in the items table.
1. The Rate and Amount will be fetched.
1. Save and Submit.

To fetch the details automatically, click on the Get items from button and choose the Purchase Order or Purchase Receipt.
You can also create a Purchase Invoice by clicking on “Make Purchase Invoice” in a Purchase Order or Purchase Receipt.

<img class="screenshot" alt="Purchase Invoice" src="{{docs_base_url}}/assets/img/accounts/purchase-invoice.png">

### 2. Features
#### 2.1 Posting Date
The concept of “Posting Date” is again same as Sales Invoice. “Bill No” and
“Bill Date” helps to track the bill number as set by your Supplier for
reference.

#### 2.2 Is Paid option
The **Is Paid** checkbox should be checked if there is a part or full payment 
on the invoice at posting date.

#### 2.3 Update Stock
The **Update Stock** checkbox should be checked if you want ERPNext to automatically
 update your inventory. Consequently, there will be no need for a Delivery Note.

### 3. More
#### 3.1 Accounting Impact
Similar to a Sales Invoice, in a Purchase Invoice you have to enter an Expense or an Asset account for
each row in your Items table. This helps to indicate if the Item is an Asset
or an Expense. You must also enter a Cost Center. These can also be set in the
Item master.

The Purchase Invoice will affect your accounts as follows:

* Accounting entries (GL Entry) for a typical double entry “purchase”:
* Debits:
   * Expense or Asset (net totals, excluding taxes)
   * Taxes (/assets if VAT-type or expense again)
* Credits:
  * Supplier
  
#### 3.2 Accounting Treatment When **Is Paid** is checked
If **Is Paid** is checked, ERPNext will also make the following
accounting entries:

Debits:
  * Supplier

Credits:
  * Bank/Cash Account

To see entries in your Purchase Invoice after you “Submit”, click on “View
Ledger”.

#### 3.3 Is purchase an “Expense” or an “Asset”?

If the Item is consumed immediately on purchase, or if it is a service, then
the purchase becomes an “Expense”. For example, a telephone bill or travel
bill is an “Expense” - it is already consumed.

For inventory Items, that have a value, these purchases are not yet “Expense”,
because they still have a value while they remain in your stock. They are
“Assets”. If they are raw-materials (used in a process), they will become
“Expense” the moment they are consumed in the process. If they are to be sold
to a Customer, they become “Expense” when you ship them to the Customer.

#### 3.4 Deducting Taxes at Source

In many countries, the law may require you to deduct taxes, while paying your
suppliers. These taxes could be based on a standard rate. Under these type of
schemes, typically if a Supplier crosses a certain threshold of payment, and
if the type of product is taxable, you may have to deduct some tax (which you
pay back to your government, on your Supplier’s behalf).

To do this, you will have to make a new Tax Account under “Tax Liabilities” or
similar and credit this Account by the percent you are bound to deduct for
every transaction.

For more help, please contact your Accountant!

#### 3.5 Hold Payments For A Purchase Invoice
There are two ways to put a purchase invoice on hold:

- Date Span Hold
- Explicit Hold

#### 3.6 Explicit Hold
Explicit hold holds the purchase invoice indefinitely. 
To do it, in the "Hold Invoice" section of the purchase invoice form, simply 
check the "Hold Invoice" checkbox. In the "Reason For Putting On Hold" text 
field, type a comment explaining why the invoice is to be put on hold.

If you need to hold a submitted invoice, click the "Make" drop down button 
and click "Block Invoice". Also add a comment explaining why the invoice is 
to be put on hold in the dialog that pops up and click "Save".

#### 3.7 Date Span Hold
Date span hold holds the purchase invoice until a 
specified date. To do it, in the "Hold Invoice" section of the purchase 
invoice form, check the "Hold Invoice" checkbox. Next, input the release date 
in the dialog that pops up and click "Save". The release date is the date 
that the hold on the document expires.

After the invoice has been saved, you can change the release date by clicking 
on the "Hold Invoice" drop down button and then "Change Release Date". This 
action will cause a dialog to appear. 

<img class="screenshot" alt="Purchase Invoice on hold" src="{{docs_base_url}}/assets/img/accounts/purchase-invoice-hold.png">

Select the new release date and click "Save". You should also enter a comment 
in the "Reason For Putting On Hold" field.

Take note of the following:

- All purchases that have been placed on hold will not included in a Payment Entry's references table
- The release date cannot be in the past.
- You can only block or unblock a purchase invoice if it is unpaid.
- You can only change the release date if the invoice is unpaid.

#### 4. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Item Wise Taxation](/docs/user/manual/en/accounts/item-tax-template)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Payment Request](/docs/user/manual/en/accounts/payment-request)
1. [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation)
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
