<!-- add-breadcrumbs -->
# Purchase Invoice

**A Purchase Invoice is a bill you receive from your Suppliers against which you need to make the payment.**

Purchase Invoice is the exact opposite of your Sales Invoice. Here you
accrue expenses to your Supplier. Making a Purchase Invoice is very similar to
making a Purchase Order.

To access the Purchase Invoice list, go to:
> Home > Accounting > Accounts Payable > Purchase Invoice

![PI Flow](/docs/assets/img/accounts/pi-flow.png)

## 1. Prerequisites
Before creating and using a Purchase Invoice, it is advised to create the following first:

* [Item](/docs/user/manual/en/stock/item)
* [Supplier](/docs/user/manual/en/buying/supplier)
* [Purchase Order](/docs/user/manual/en/buying/purchase-order)
* [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt) (optional)


## 2. How to create a Purchase Invoice:
A Purchase Invoice is usually created from a Purchase Order or a Purchase Receipt. The Supplier's Item details will be fetched into the Purchase Invoice. However, you can also create a Purchase Invoice directly.

To fetch the details automatically in a Purchase Invoice, click on the **Get Items from**. The details can be fetched from a Purchase Order or Purchase Receipt.

For manual creation, follow these steps:

1. Go to the Purchase Invoice list, click on New.
1. Select the Supplier.
1. The posting date and time will be set to current, you can edit after you tick the checkbox below Posting Time.
1. Set the Due Date for payment.
1. Add Items and quantities in the Items table.
1. The Rate and Amount will be fetched.
1. Save and Submit.

 <img class="screenshot" alt="Purchase Invoice" src="{{docs_base_url}}/assets/img/accounts/purchase-invoice.png">

### 2.1 Additional options when creating a Purchase Invoice

* **Is Paid**: You can tick 'Is Paid' if the amount has already been paid via an [Advance Payment Entry](/docs/user/manual/en/accounts/advance-payment-entry). This should be ticked if there is full or partial payment.
* **Is Return (Debit Note)**: Tick this if the customer has returned the Items. To know more details, visit the [Debit Note](/docs/user/manual/en/accounts/debit-note) page.
* **Apply Tax Withholding Amount**: If the selected Supplier has a Tax Withholding Category set, this checkbox will be enabled. For more information, visit the [Tax Withholding Category](/docs/user/manual/en/accounts/tax-withholding-category) page.

### 2.2 Statuses

* **Draft**: A draft is saved but yet to be submitted to the system.
* **Return**: The Items have been returned to the Supplier.
* **Debit Note Issued**: The Items have been returned and a [Debit Note](/docs/user/manual/en/accounts/debit-note) has been issued against the invoice.
* **Submitted**: The Purchase Invoice has been submitted to the system and the general ledger has been updated.
* **Paid**: The invoice amount has been to the Supplier and a [Payment Entry](/docs/user/manual/en/accounts/payment-entry) has been submitted.
* **Unpaid**: The Purchase Invoice is yet to be paid.
* **Overdue**: The due date has passed for payment.
* **Canceled**: The invoice has been canceled due to some reason.


## 3. Features

### 3.1 Accounting Dimensions
Accounting Dimensions lets you tag transactions based on a specific Territory, Branch, Customer, etc. This helps in viewing accounting statements separately based on the criteria selected. To know more, visit the [Accounting Dimensions](/docs/user/manual/en/accounts/accounting-dimensions) page.

> Note: Project and Cost Center are treated as dimensions by default.

### 3.2 Holding the Invoice

Sometimes you may need to hold an invoice from being submitted.

**Hold Invoice**: Enable this checkbox to put the Purchase Invoice on hold. This can be done only before submitting the invoice. Once 'Hold Invoice' is enabled and the Purchase Invoice is submitted, the status will change to 'Temporarily on Hold'.

![PI Hold](/docs/assets/img/accounts/pi-hold.png)

Once the purchase invoice gets submit and you want to change 'Release Date' then you can take the help of the 'Hold Invoice' button, which is available on the top right.

If you want to hold submitted purchase invoice then you can hold using 'Block Invoice' option and If you want to unblock again then use 'Unblock Invoice' option.

![Block PI](/docs/assets/img/accounts/pi_block.png)   

This is invoice level holding, Suppliers can be put on hold. [Learn more here](/docs/user/manual/en/buying/supplier#23-credit-limit).

### 3.3 Supplier Invoice Details

* **Supplier Invoice No**: The Supplier may identify this order with a number of his own. This is for reference.
* **Supplier Invoice Date**: The date on which the Supplier placed/confirmed your order from his end.

### 3.4 Address and Contact

* **Supplier Address:** This is the Billing Address of the Supplier.
* **Contact Person**: If the Supplier is a Company, the person to be contacted is fetched in this field if set in the [Supplier](/docs/user/manual/en/buying/supplier) form.
* **Shipping Address:** Address where the items will be shipped to.

For India, the following details can be recorded for GST purposes:

* Supplier GSTIN
* Place of Supply
* Company GSTIN

### 3.5 Currency and Price list
You can set the currency in which the Purchase Invoice order is to be sent. This is fetched from the Purchase Order. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on 'Ignore Pricing Rule' will ignore the [Pricing Rules](/docs/user/manual/en/accounts/pricing-rule) set in Accounts > Pricing Rule.

![PI Price List](/docs/assets/img/accounts/pi-price-list.png)

To know about Price Lists, [click here](/docs/user/manual/en/stock/price-lists).

To know about managing transactions in multiple currencies, [click here](/docs/user/manual/en/accounts/articles/managing-transactions-in-multiple-currency).

### 3.6 Subcontracting or 'Supply Raw Materials'

Setting 'Supply Raw Materials' option is useful for subcontracting where you provide the raw materials for manufacturing an Item. To know more, visit the [Subcontracting page](/docs/user/manual/en/manufacturing/subcontracting).

### 3.7 Items table

* **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Know how to track them [here](/docs/user/manual/en/stock/articles/track-items-using-barcode)

* The Item Code, name, description, Image, and Manufacturer will be fetched from the [Item master](/docs/user/manual/en/stock/item).

* **Manufacturer**: If the Item is manufactured by a specific manufacturer, it can be added here. This will be fetched if set in the Item master.

* **Quantity and Rate**: When you select the Item code, its name, description, and UOM will be fetched. The 'UOM Conversion Factor' is set to 1 by default, you can change it depending on the UOM received from the seller, more in the next section.

 'Price List Rate' will be fetched if a Standard Buying rate is set. 'Last Purchase Rate' shows the rate of the item from your last Purchase Order. Rate is fetched if set in the item master. You can attach an Item Tax Template to apply a specific tax rate to the item.

* **Item weights** will be fetched if set in the Item master else enter manually.

* **Discount on Price List Rate**: You can apply a discount on individual Items percentage-wise or on the total amount of the Item. Read [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) for more details.

* **Item Weight**: The Item Weight details per unit and Weight UOM are fetched if set in the Item master, else enter manually.

* **Accounting Details**: The Expense account can be changed here you wish to.

* **Deferred Expense**: If the expense for this Item will be billed over the coming months in parts, then tick on 'Enable Deferred Expense'. To know more, visit the [Deferred Expense page](/docs/user/manual/en/accounts/deferred-expense).

* **Allow Zero Valuation Rate**: Ticking on 'Allow Zero Valuation Rate' will allow submitting the Purchase Receipt even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

* **BOM**: If there is a [Bill of Materials](/docs/user/manual/en/manufacturing/bill-of-materials) created for the Item, it'll be fetched here. This is useful for reference when [subcontracting](/docs/user/manual/en/manufacturing/subcontracting).

* **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit [this page](/docs/user/manual/en/accounts/item-tax-template).

* **Page Break** will create a page break just before this Item when printing.

#### Update Stock
The **Update Stock** checkbox should be checked if you want ERPNext to automatically update your inventory. Consequently, there will be no need for a Delivery Note.

### 3.8 Taxes and charges
The Taxes and Charges will be fetched from the [Purchase Order](/docs/user/manual/en/buying/purchase-order) or [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt).

![PI Tax](/docs/assets/img/accounts/pi-tax.png)

Visit the [Purchase Taxes and Charges Template](/docs/user/manual/en/buying/purchase-taxes-and-charges-template) page to know more about taxes.

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit [this page](/docs/user/manual/en/accounts/tax-category).

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule
A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the [Shipping Rule](/docs/user/manual/en/selling/shipping-rule) page.

### 3.9 Additional Discount

Any additional discounts to the whole Invoice can be set in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.

![PI Discount](/docs/assets/img/accounts/pi-discount.png)

Visit the [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) page for more details.

### 3.10 Advance Payment
For high-value Items, the seller can request an advance payment before processing the order. The **Get Advances Received** button opens a popup from where you can fetch the orders where advance payment was made. To know more, visit the [Advance Payment Entry](/docs/user/manual/en/accounts/advance-payment-entry) page.

### 3.11 Payment Terms
The payment for an invoice may be made in parts depending on your understanding with the Supplier. This is fetched if set in the Sales Order.

![PI Payment Terms](/docs/assets/img/accounts/pi-pay-terms.png)


To know more, visit the [Payment Terms](/docs/user/manual/en/accounts/payment-terms) page.

### 3.12 Write Off
Write off happens when the Customer pays an amount less than the invoice amount. This may be a small difference like 0.50. Over several orders, this might add up to a big number. For accounting accuracy, this difference amount is 'written off'. To know more, visit the [Payment Terms](/docs/user/manual/en/accounts/payment-entry#25-deductions-or-loss) page.

### 3.13 Terms and Conditions
In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions)

### 3.14 Printing Settings

#### Letterhead
You can print your Purchase Invoice on your Company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the Items table. This can be seen when your print.

#### Print Headings
Purchase Invoice headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

There are additional checkboxes for printing the Purchase Invoice without the amount, this might be useful when the Item is of high value. You can also group the same Items in one row when printing.

### 3.15 GST Details (for India)
The following details can be set for GST:

* GST Category
* Invoice Copy
* Reverse Charge
* E-commerce GSTIN
* Eligibility For ITC
* Availed ITC Integrated Tax
* Availed ITC Central Tax
* Availed ITC State/UT Tax
* Availed ITC Cess

### 3.16 More Information

* **Is Opening Entry**: If this is an opening entry to affect your accounts select 'Yes'. i.e. if you're migrating from another ERP to ERPNext mid year, you might want to use an Opening Entry to update account balances in ERPNext.
* **Remarks**: Any additional remarks about the Sales Invoice can be added here.

### 3.17 After Submitting

On submitting a Sales Invoice, the following documents can be created against it:

1. [Journal Entry](/docs/user/manual/en/accounts/journal-entry)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payment Request](/docs/user/manual/en/accounts/payment-request)
1. [Landed Cost Voucher](/docs/user/manual/en/stock/landed-cost-voucher)
1. [Asset](/docs/user/manual/en/asset/asset)

![PI Submit](/docs/assets/img/accounts/pi-submit.png)

## 4. More
### 4.1 Accounting Impact
Similar to a Sales Invoice, in a Purchase Invoice you have to enter an Expense or an Asset account for
each row in your Items table. This helps to indicate if the Item is an Asset
or an Expense. You can also change the Cost Center. These can also be set in the
Item master. The Cost Center can be set at the Company level.

The Purchase Invoice will affect your accounts as follows:

* Accounting entries (GL Entry) for a typical double entry “purchase”:
* Debits:
 * Expense or Asset (net totals, excluding taxes)
 * Taxes (/assets if VAT-type or expense again)
* Credits:
 * Supplier

![PI Ledger](/docs/assets/img/accounts/pi-ledger.png)

### 4.2 Accounting When **Is Paid** is checked
If **Is Paid** is checked, ERPNext will also make the following
accounting entries:

Debits:

 * Supplier

Credits:

 * Bank/Cash Account

To see entries in your Purchase Invoice after you “Submit”, click on “View
Ledger”.

### 4.3 Is purchase an “Expense” or an “Asset”?

If the Item is consumed immediately on purchase, or if it is a service, then
the purchase becomes an “Expense”. For example, a telephone bill or travel
bill is an “Expense” - it is already consumed.

For inventory Items, that have a value, these purchases are not yet “Expense”,
because they still have a value while they remain in your stock. They are
“Assets”. If they are raw-materials (used in a process), they will become
“Expense” the moment they are consumed in the process. If they are to be sold
to a Customer, they become “Expense” when you ship them to the Customer.

### 4.4 Deducting Taxes at Source

In many countries, the law may require you to deduct taxes, while paying your
suppliers. These taxes could be based on a standard rate. Under these type of schemes, typically if a Supplier crosses a certain threshold of payment, and
if the type of product is taxable, you may have to deduct some tax (which you
pay back to your government, on your Supplier’s behalf).

To do this, you will have to make a new Tax Account under “Tax Liabilities” or
similar and credit this Account by the percent you are bound to deduct for
every transaction.

### 4.5 Hold Payments For A Purchase Invoice
There are two ways to put a purchase invoice on hold:

- Date Span Hold
- Explicit Hold

#### Explicit Hold
Explicit hold holds the purchase invoice indefinitely.
To do it, in the "Hold Invoice" section of the purchase invoice form, simply check the "Hold Invoice" checkbox. In the "Reason For Putting On Hold" text field, type a comment explaining why the invoice is to be put on hold.

If you need to hold a submitted invoice, click the "Make"  button
and click "Block Invoice". Also, add a comment explaining why the invoice is to be put on hold in the dialog that pops up and click "Save".

#### Date Span Hold
Date span hold holds the purchase invoice until a specified date. To do it, in the "Hold Invoice" section of the purchase invoice form, check the "Hold Invoice" checkbox. Next, input the release date in the dialog that pops up and click "Save". The release date is the date
that the hold on the document expires.

After the invoice has been saved, you can change the release date by clicking on the "Hold Invoice" drop down button and then "Change Release Date". This action will cause a dialog to appear.

<img class="screenshot" alt="Purchase Invoice on hold" src="{{docs_base_url}}/assets/img/accounts/purchase-invoice-hold.png">

Select the new release date and click "Save". You should also enter a comment
in the "Reason For Putting On Hold" field.

Take note of the following:

- All purchases that have been placed on hold will not be included in a Payment Entry's references table
- The release date cannot be in the past.
- You can only block or unblock a purchase invoice if it is unpaid.
- You can only change the release date if the invoice is unpaid.

### 5. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Item Wise Taxation](/docs/user/manual/en/accounts/item-tax-template)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payment Request](/docs/user/manual/en/accounts/payment-request)
1. [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation)
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
