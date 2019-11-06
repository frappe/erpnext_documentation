<!-- add-breadcrumbs -->
# Sales Invoice

**A Sales Invoice is a bill that you send to your Customers against which the Customer makes the payment.**

Sales Invoice is an accounting transaction. On submission of Sales Invoice, the system updates the receivable and books income against a Customer Account.

To access the Sales Invoice list, go to:
> Home > Accounts > Accounts Receivable > Sales Invoice

![SO Flow](/docs/assets/img/accounts/so-flow.png)

## 1. Prerequisites
Before creating and using a Sales Invoice, it is advised to created the following first:

* [Item](/docs/user/manual/en/stock/item)
* [Customer](/docs/user/manual/en/CRM/customer)
* [Sales Order](/docs/user/manual/en/selling/sales-order)
* [Delivery Note](/docs/user/manual/en/stock/delivery-note) (optional)

## 2. How to create a Sales Invoice
A Sales Invoice is usually created from a Sales Order or a Delivery Note. The Customer's Item details will be fetched into the Sales Invoice. However, you can also create a Sales Invoice directly.

To fetch the details automatically in a Sales Invoice, click on the **Get Items from**. The details can be fetched from a Sales Order, Delivery Note, or a Quotation. 

For manual creation, follow these steps:

1. Go to the Sales Invoice list and click on New.
1. Select the Customer. 
1. Set the Payment Due Date.
1. In the Items table, select the Items and set the quantities.
1. The prices will be fetched automatically if [Item Price](/docs/user/manual/en/stock/item-price) is added, else add a price in the table.
1. The posting date and time will be set to current, you can edit after you tick the checkbox below Posting Time to make a backdated entry.
1. Save and Submit.

### 2.1 Additional options when creating a Sales Invoice

* **Include Payment (POS)**: If this invoice is for a Point of Sale. [Know more here](/docs/user/manual/en/accounts/sales-invoice#323-pos-invoices).
* **Is Return Credit Note**: Tick this if the customer has returned the Items. To know more details, visit the [Credit Note](/docs/user/manual/en/accounts/credit-note) page.

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/sales-invoice.png">

For India:
**e-Way Bill No**: According to GST rules, transporters need to carry an e-Way Bill. To know how to generate an e-Way Bill, [visit this page](/docs/user/manual/en/regional/india/auto-generate-e-way-bill-JSON).

### 2.2 Statuses

These are the statuses a Sales Invoice can be in:

* **Draft**: A draft is saved but yet to be submitted to the system.
* **Return**: The Item is returned by the Customer for any reason.
* **Credit Note Issued**: The Item is returned by the Customer and a [Credit Note](/docs/user/manual/en/accounts/credit-note) is created against the invoice.
* **Submitted**: The invoice is submitted to the system and the general ledger has been updated.
* **Paid**: Customer has made the payment and a [Payment Entry](/docs/user/manual/en/accounts/payment-entry) has been submitted.
* **Unpaid**: Invoice is generated but payment is pending but within the payment due date.
* **Unpaid and Discontinued**: Payment is pending and any ongoing subscription has been discontinued.
* **Overdue**: Payment is pending beyond the payment due date.
* **Overdue and Discontinued**: Payment is pending beyond the payment due date and any ongoing subscription has been discontinued.
* **Canceled**: The Sales Invoice is canceled due to any reason.


## 3. Features
### 3.1 Dates

* **Posting Date**: The date on which the Sales Invoice will affect your books of
accounts i.e. your General Ledger. This will affect all your balances in that
accounting period.

* **Due Date**: The date on which the payment is due (if you have sold on credit).
The credit limit can be set from the [Customer](/docs/user/manual/en/CRM/customer) master.

### 3.2 Accounting Dimensions
Accounting Dimensions lets you tag transactions based on a specific Territory, Branch, Customer, etc. This helps in viewing accounting statements separately based on the criteria selected. To know more, visit the [Accounting Dimensions](/docs/user/manual/en/accounts/accounting-dimensions) page.

> Note: Project and Cost Center are treated as dimensions by default.

### 3.3 Customer PO Details

* **Customer's Purchase Order**: The customer may identify this order with a number of his own. This is for reference.
* **Customer's Purchase Order Date**: The date on which the Customer placed the Purchase Order from his end.

 ![Customer Address](/docs/assets/img/accounts/si-customer.png)

### 3.4 Address and Contact

* **Customer Address:** This is the Billing Address of the Customer.
* **Contact Person**: If the Customer is a company, the person to be contacted is fetched in this field if set in the [Customer](/docs/user/manual/en/CRM/customer) form.
* **Territory:** A [Territory](/docs/user/manual/en/selling/territory) is the region where the Customer belongs to, fetched from the Customer form. The default value is All Territories. 
* **Shipping Address:** Address where the items will be shipped to.

For India, the following details can be recorded for GST purposes:

* Billing Address GSTIN
* Customer GSTIN
* Place of Supply
* Company GSTIN

### 3.5 Currency and Price list
You can set the currency in which the Sales Invoice order is to be sent. This is fetched from the Sales Order. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on 'Ignore Pricing Rule' will ignore the [Pricing Rules](/docs/user/manual/en/accounts/pricing-rule) set in Accounts > Pricing Rule.

To know about Price Lists, [click here](/docs/user/manual/en/stock/price-lists).

To know about managing transactions in multiple currencies, [click here](/docs/user/manual/en/accounts/articles/managing-transactions-in-multiple-currency).


### 3.6 The Items table

#### Update Stock
Ticking this checkbox will update the Stock Ledger on submitting the Sales Invoice. If you've created a Delivery Note, the Stock Ledger will be changed. If you're **skipping** the creation of Delivery Note, tick this checkbox.

* **Scan Barcode**: You can add Items in the Items table by scanning their barcodes if you have a barcode scanner. Know how to track them [here](/docs/user/manual/en/stock/articles/track-items-using-barcode)

* The Item Code, name, description, Image, and Manufacturer will be fetched from the [Item master](/docs/user/manual/en/stock/item).

* **Discount and Margin**: You can apply a discount on individual Items percentage-wise or on the total amount of the Item. Read [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) for more details.

* **Rate**: The Rate is fetched if set in the [Price List](/docs/user/manual/en/stock/price-lists) and the total Amount is calculated.

* **Drop Ship**: Drop Shipping is when you make the sales transaction, but the Item is delivered by the Supplier. To know more, visit the [Drop Shipping](/docs/user/manual/en/selling/articles/drop-shipping) page.

* **Accounting Details**: The Income and Expense accounts can be changed here you you wish to. If this Item is an [Asset](/docs/user/manual/en/asset/asset), it can be linked here. This is useful when you're [selling an Asset](/docs/user/manual/en/asset/selling-an-asset).

* **Deferred Revenue**: If the income for this Item will be billed over the coming months in parts, then tick on 'Enable Deferred Revenue'. To know more, visit the [Deferred Revenue page](/docs/user/manual/en/accounts/deferred-revenue).

* **Item Weight**: The Item Weight details per unit and Weight UOM are fetched if set in the Item master.

* **Stock Details**: The following details will be fetched from the Item master:
 * **Warehouse**: The Warehouse from where the stock will be sent.
 * **Available Qty at Warehouse**: The quantity available in the selected Warehouse.

* **Batch No and Serial No**: If your Item is serialized or batched, you will have to enter [Serial Number](/docs/user/manual/en/stock/serial-no) and [Batch](/docs/user/manual/en/stock/batch) in the Items table. You are allowed to enter multiple Serial Numbers in one row (each on a separate line) and you must enter the same number of Serial Numbers as the quantity.

* **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit [this page](/docs/user/manual/en/accounts/item-tax-template).

* References: If this Sales Invoice was created from a Sales Order/Delivery Note, it'll be referred here. Also, the Delivered Quantity will be shown.

* **Page Break** will create a page break just before this Item when printing.

### 3.7 Timesheet

If you want to bill Employees working on Projects on an hourly basis (contract based),
they can fill out Timesheets which consists of their billing rate. When you make a new
Sales Invoice, select the Project for which the billing is to be made, and the
corresponding Timesheet entries for that Project will be fetched.

If your Company's Employees are working at a location and it needs to be billed, you can create an Invoice based on the Timesheet.

![SI Timesheet](/docs/assets/img/accounts/si-timesheet.png)

To know more, [visit this page](/docs/user/manual/en/projects/sales-invoice-from-timesheet).

### 3.8 Taxes and Charges
The Taxes and Charges will be fetched from the [Sales Order](/docs/user/manual/en/selling/sales-order) or [Delivery Note](/docs/user/manual/en/stock/delivery-note).

Visit the [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template) page to know more about taxes. 

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit [this page](/docs/user/manual/en/accounts/tax-category).

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

![SI Tax](/docs/assets/img/accounts/si-tax.png)

#### Shipping Rule
A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the [Shipping Rule](/docs/user/manual/en/selling/shipping-rule) page.

### 3.9 Loyalty Points Redemption

If the Customer is enrolled in a Loyalty Program, they can choose to redeem it. To know more, visit the [Loyalty Program](/docs/user/manual/en/accounts/loyalty-program) page.

### 3.10 Additional Discount
Any additional discounts to the whole Invoice can be set in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.
Visit the [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) page for more details.

![SI Add Discount](/docs/assets/img/accounts/si-add-discount.png)

### 3.11 Advance Payment
For high-value Items, the seller can request an advance payment before processing the order. The **Get Advances Received** button opens a popup from where you can fetch the orders where advance payment was made. To know more, visit the [Advance Payment Entry](/docs/user/manual/en/accounts/advance-payment-entry) page.

### 3.12 Payment Terms
The payment for an invoice may be made in parts depending on your understanding with the Supplier. This is fetched if set in the Sales Order. To know more, visit the [Payment Terms](/docs/user/manual/en/accounts/payment-terms) page.

### 3.13 Write Off
Write off happens when the Customer pays an amount less than the invoice amount. This may be a small difference like 0.50. Over several orders, this might add up to a big number. For accounting accuracy, this difference amount is 'written off'. To know more, visit the [Payment Terms](/docs/user/manual/en/accounts/payment-entry#25-deductions-or-loss) page.

### 3.14 Terms and Conditions
In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions)

### 3.15 Transporter Information

If you outsource transporting Items to their delivery location, the transporter details can be added. This is not the same as [drop shipping](/docs/user/manual/en/selling/articles/drop-shipping).

* **Transporter**: The Supplier who will transport the Item to your Customer. The transporter feature should be enabled in the Supplier master to select the [Supplier](/docs/user/manual/en/buying/supplier) here.
* **Driver**: You can add a Driver here who will drive the mode of transport.

The details are usually fetched from the Delivery Note.

 ![Delivery Note Transport](/docs/assets/img/accounts/si-transporter.png)

The following details can be recorded:

* Distance in km
* Mode of Transport whether road, air, rail, or ship. 

For India, GST:

* GST Transporter ID
* Transport Receipt No
* Vehicle No
 The GST Vehicle Type can be changed

The Transport Receipt Date and Driver Name will be fetched.

### 3.16 Printing Settings

#### Letterhead
You can print your Sales Invoice on your Company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the Items table. This can be seen when your print.

#### Print Headings
Sales Invoice headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

There are additional checkboxes for printing the Sales Invoice without the amount, this might be useful when the Item is of high value. You can also group the same Items in one row when printing.

### 3.17 GST Details (for India)

The following details can be set for GST:

* GST Category
* Invoice Copy
* Reverse Charge
* E-commerce GSTIN
* Print Heading

### 3.18 More Information
The following Sales details can be recorded:

* **Campaign**: If this invoice is a part of on ongoing sales Campaign, it can be linked. To know more, visit the [Campaign page](/docs/user/manual/en/CRM/campaign).
* **Source**: A Lead Source can be tagged here to know the source of sales. To know more, visit the [Lead Source](/docs/user/manual/en/CRM/lead_source) page.

 ![SI More info](/docs/assets/img/accounts/si-more-info.png)

### 3.19 Accounting Details

* **Debit To**: The account against which debit will be booked.
* **Is Opening Entry**: If this is an opening entry to affect your accounts select 'Yes'. i.e. if you're migrating from another ERP to ERPNext mid year, you might want to use an Opening Entry to update account balances in ERPNext.
* **C-Form Applicable**: A C Form is used for reduction of applicable taxes, select yes if applicable to your transaction. Note: C Form is not applicable in India since GST.
* **Remarks**: Any additional remarks about the Sales Invoice can be added here.

 ![SI Accounting Details](/docs/assets/img/accounts/si-acc-details.png)

### 3.20 Commission

If the sale took place via one of your Sales Partners, you can add their commission details here. This is usually fetched from the Sales Order/Delivery Note.

### 3.21 Sales Team

**Sales Persons:** ERPNext allows you to add multiple Sales Persons who may have worked on this deal. This is also fetched from the Sales Order/Delivery Note.

### 3.22 Automatically Fetching Item Batch Numbers

If you are selling an Item from a [Batch](/docs/user/manual/en/stock/batch),
ERPNext will automatically fetch a batch number for you if "Update Stock" 
is checked. The batch number will be fetched on a First Expiring First Out 
(FEFO) basis. This is a variant of First In First Out (FIFO) that gives the highest priority to the soonest to expire Items. 

Note that if the first batch in the queue cannot satisfy the order on the invoice, 
the next batch in the queue that can satisfy the order will be selected. If no batch can satisfy the order, ERPNext will cancel its attempt to automatically fetch a suitable batch number.

### 3.23 POS Invoices

Consider a scenario where the retail transaction is carried out. For e.g: A retail shop.
If you check the **Is POS** checkbox, then all your **POS Profile** data is fetched
into the Sales Invoice and you can easily make payments.

Also, if you check the **Update Stock** the stock will also update automatically,
without the need for a Delivery Note.

<img class="screenshot" alt="POS Invoice" src="{{docs_base_url}}/assets/img/accounts/pos-sales-invoice.png">

### 3.24 After Submitting

On submitting a Sales Invoice, the following documents can be created against it:

1. [Journal Entry](/docs/user/manual/en/accounts/journal-entry)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payment Request](/docs/user/manual/en/accounts/payment-request)
1. [Invoice Discounting](/docs/user/manual/en/accounts/invoice_discounting)
1. [Delivery Note](/docs/user/manual/en/stock/delivery-note)

![SI Submit](/docs/assets/img/accounts/si-submit.png)


## 4. More
### Accounting Impact

All Sales must be booked against an “Income Account”. This refers to an
Account in the “Income” section of your Chart of Accounts. It is a good
practice to classify your income by type (like product income, service income
, etc). The Income Account must be set for each row of the Items table.

> Tip: To set default Income Accounts for Items, you can set it in the Item or
Item Group.

The other account that is affected is the Account of the Customer. That is
automatically set from “Debit To” in the heading section.

You can also mention the Cost Centers in which your Income must be booked.
Remember that your Cost Centers tell you the profitability of the different
lines of business or product. You can also set a default Cost Center in the
Item master. See also: [Accounting Dimensions](/docs/user/manual/en/accounts/accounting-dimensions).

### Accounting entries (GL Entry) for a typical double entry “Sale”:
When booking a sale (accrual):

* **Debit:** Customer (grand total)
* **Credit:** Income (net total, minus taxes for each Item)
* **Credit:** Taxes (liabilities to be paid to the government)

 ![SI Ledger](/docs/assets/img/accounts/si-ledger.png)

> To see entries in your Sales Invoice after you “Submit”, click on “View
Ledger”.

## 5. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Journal Entry](/docs/user/manual/en/accounts/journal-entry)
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Item Wise Taxation](/docs/user/manual/en/accounts/item-tax-template)
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
1. [Quotation](/docs/user/manual/en/selling/quotation)
1. [Delivery Note](/docs/user/manual/en/stock/delivery-note)
