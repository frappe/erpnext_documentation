<!-- add-breadcrumbs -->
# Delivery Note

**A Delivery Note is made when a shipment is shipped from the company’s Warehouse to the customer.**

A copy of the Delivery Note is usually sent with the transporter. The Delivery
Note contains the list of Items that are sent in the shipment and updates the
inventory. The Delivery Note is an optional step and a Sales Invoice can be created directly from a Sales Order.

To access the Delivery Note list, go to:
> Home > Stock > Stock Transactions > Delivery Note

![Delivery Note flow](/docs/assets/img/stock/delivery-note-flow.png)


## 1. Prerequisites
Before creating and using a Delivery Note, it is advised that you create the following first:

* [Sales Order](/docs/user/manual/en/selling/sales-order)

## 2. How to create a Delivery Note
The entry of the Delivery Note is very similar to a Purchase Receipt. It is usually created from a “Submitted” Sales Order (that is not shipped) by clicking on Create > Delivery.

To create a Delivery Note _manually_ (not recommended), follow these steps:

1. Go to the Delivery Note list, click on New.
1. The Customer and Item details can be fetched by clicking on 'Get Items from > Sales Order'.
1. The UOM and Rates will be fetched automatically.
1. Save and Submit.

    <img class="screenshot" alt="Delivery Note" src="{{docs_base_url}}/assets/img/stock/delivery-note.png">

To fetch Items from a Sales Order, click on Get Items from > Sales Order. This will open a popup from where you can search for Sales Orders and select one.

You will notice that all the information about unshipped Items and other details are carried over from your Sales Order if you create the Delivery Note from there.

You can also edit the posting date and time, the current date and time are set when you create the Delivery Note.


### 2.1 Statuses

These are the statuses a Delivery Note can be in:

* **Draft**: A draft is saved but yet to be submitted to the system.
* **To Bill**: Yet to be billed using a [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice).
* **Completed**: Submitted and sent all the Items.
* **Canceled**: Canceled the Delivery Note.
* **Closed**: The purpose of the Close is to manage short-closing. For example, your Customer ordered for 20 qty but closed at 15 qty. The remaining 5 is not to be sent or billed.

### 2.2 Partial Deliveries

When you create a Delivery Note from a Sales Order, the quantities can be changed. So if the Sales Order contains 10 Items to be delivered and you're delivering only 5 this week and the remaining next week, then you can create 2 Delivery Notes in two weeks. 


## 3. Related Actions
### 3.1 Customer Purchase Order Details
You can enter the Customer's Purchase Order number here for Reference.

### 3.2 Address and Contact
* **Shipping Address**: The Customer's address where the Items will be shipped.
* **Contact Person**: If the Customer is an organization, add the Contact person in this field.

For India, the following details can be added for GST:

* Customer GSTIN
* Place of Supply
* Billing Address GSTIN 
* Company GSTIN
* Company Address Name

[Contacts](/docs/user/manual/en/CRM/contact) and [Addresses](/docs/user/manual/en/CRM/address) are stored separately so that you can attach multiple Contacts or Addresses to the customer.

### 3.3 Currency and Price List
You can set the currency in which the Deliver Note is to be sent. This is usually fetched if set in the Sales Order. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

To know about Price Lists, [click here](/docs/user/manual/en/stock/price-lists).

To know about managing transactions in multiple currencies, [click here](/docs/user/manual/en/accounts/articles/managing-transactions-in-multiple-currency).

### 3.3 Warehouses

* **Set Source Warehouse**: This is where the Items will be sourced from to send to the Customer.
* **To Warehouse**: In a regular Sales scenario, the Item exits your Warehouse and reaches the Customer. However, if you wish to retain sample stock, enter a Warehouse here.

### 3.4 Items Table
* **Barcode**: You can track Items using [barcodes](/docs/user/manual/en/stock/articles/track-items-using-barcode).

* The Item Code, name, description, Image, and Manufacturer will be fetched from the [Item master](/docs/user/manual/en/stock/item).

* **Discount and Margin**: You can apply a discount on individual Items percentage-wise or the total amount of the Item. Read [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) for more details.

* **Rate**: The Rate is fetched if set in the [Price List](/docs/user/manual/en/stock/price-lists) and the total Amount is calculated.

* **Item Tax Template**: You can set an Item Tax Template to apply a specific Tax amount to this particular Item. To know more, visit [this page](/docs/user/manual/en/accounts/item-tax-template).

* The Item Weight details per unit and Weight UOM are fetched if set in the Item master.

* **Warehouse and Reference**: The Warehouse from which the Items are sent to the Customer is shown. Also, a Sales Order will be shown if this Delivery Note was the creation flow: 'Sales Order > Deliver Note'. 

* **Batch No and Serial No**: If your Item is serialized or batched, you will have to enter [Serial Number](/docs/user/manual/en/stock/serial-no) and [Batch](/docs/user/manual/en/stock/batch) in the Items table. You are allowed to enter multiple Serial Numbers in one row (each on a separate line) and you must enter the same number of Serial Numbers as the quantity.

    The 'Available Qty at From Warehouse', 'Available Batch Qty at From Warehouse', and 'Installed Qty' will be shown. To know more about installation, visit the [Installation Note](/docs/user/manual/en/stock/installation-note) page.

    **Note**: The Item has to be serialized or batched for these features to work. If the Item is serialized a popup will appear where you can enter the Serial Numbers.

* Expense Account is the account from which the amount will be debited. Ticking on 'Allow Zero Valuation Rate' will allow submitting the Delivery Note even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

* Accounting Dimensions help to tag each transaction with different Dimensions without the need for creating new Cost Centers. You need to create Accounting Dimensions first, to know more, visit [this page](/docs/user/manual/en/accounts/accounting-dimensions). 

* **Page Break** will create a page break just before this Item when printing.

### 3.5 Tracking Quality Inspection
If for certain Items, it is mandatory to record Quality Inspections (if you have set it in your Item master), you will need to update the “Quality Inspection" field. The system will only allow you to “Submit” the
Delivery Note if you update the “Quality Inspection”.

After enabling Inspection Criteria in the [Item form](/docs/user/manual/en/stock/item#216-inspection-criteria) for Sales and attaching a Quality Inspection Template there, Quality Inspections can be recorded in Delivery Notes.

### 3.5 Taxes and Charges
The Taxes and Charges will be fetched from the [Sales Order](/docs/user/manual/en/buying/purchase-order).

Visit the [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template) page to know more about taxes. 

The total taxes and charges will be displayed below the table.

To add taxes automatically via a Tax Category, visit [this page](/docs/user/manual/en/accounts/tax-category).

Make sure to mark all your taxes in the Taxes and Charges table correctly for an accurate valuation.

#### Shipping Rule
A Shipping Rule helps set the cost of shipping an Item. The cost will usually increase with the distance of shipping. To know more, visit the [Shipping Rule](/docs/user/manual/en/selling/shipping-rule) page.

### 3.6 Additional Discount
Any additional discounts to the whole order can be set in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.
Read [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) for more details.

### 3.7 Terms and Conditions
In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions)

### 3.8 Transporter Information

If you outsource transporting Items to their delivery location, the transporter details can be added. This is not the same as [drop shipping](/docs/user/manual/en/selling/articles/drop-shipping).

* **Transporter**: The Supplier who will transport the Item to your Customer. The transporter feature should be enabled in the Supplier master to select the [Supplier](/docs/user/manual/en/buying/supplier) here.
* **Driver**: You can add a Driver here who will drive the mode of transport.

![Delivery Note Transport](/docs/assets/img/stock/delivery-note-transport.png)

The following details can be recorded:

* Distance in km
* Mode of Transport whether road, air, rail, or ship. 

For India, GST:

* GST Transporter ID
* Transport Receipt No
* Vehicle No
    The GST Vehicle Type can be changed

The Transport Receipt Date and Driver Name will be fetched.

### 3.9 More Information

The Delivery Note can be linked to the following for tracking purposes:

* [Project](/docs/user/manual/en/projects/project)
* [Campaign](/docs/user/manual/en/CRM/campaign)
* [Source](/docs/user/manual/en/CRM/lead_source)

### 3.10 Printing Settings

#### Letterhead
You can print your Delivery Note on your company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the Items table. This can be seen when your print.

#### Print Headings
Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

There are additional checkboxes for printing the Delivery Note without the amount, this might be useful when the Item is of high value. You can also group the same Items in one row when printing.

### 3.11 Status
The status of the document and installation percentage is shown here. Any additional instructions for delivery can be entered here.

### 3.12 Commission

If the sale took place via one of your Sales Partners, you can add their commission details here. This is usually fetched from the Sales Order.

### 3.13 Sales Team
**Sales Persons:** ERPNext allows you to add multiple Sales Persons who may have worked on this deal.

This is usually fetched from a Sales Order, for example:

<img class="screenshot" alt="Sales Team in Sales Order" src="{{docs_base_url}}/assets/img/selling/so-sales-team.png">

### 3.14 Shipping Packets or Items with Product Bundle

If you are shipping Items that have a [Product Bundle](/docs/user/manual/en/selling/product-bundle), ERPNext will automatically create a “Packing List” table for you based on the sub-Items in that Item.

If your Items are serialized, then for Product Bundle type of Items, you will have
to update the Serial Number in the “Packing List” table.

### 3.15 Packing Items into Cases, for Container Shipment

If you are doing making the delivery via container shipment or by weight, then you can use the Packing
Slip to break up your Delivery Note into smaller units. To know more about a Packing Slip, visit [this page](/docs/user/manual/en/stock/packing-slip).
go to:

You can create multiple Packing Slips for your Delivery Note and ERPNext will
ensure that the quantities in the Packing Slip do not exceed the quantities in
the Delivery Note. Note that you can create a Packing Slip from a Delivery Note only when the Delivery Note is in the Draft stage.

### 3.16 After Submitting

When the Delivery Note is submitted, a Stock Ledger Entry is made for each Item and stock is updated. Pending
Quantity in the Sales Order is updated (if applicable).

The Dashboard will show the following options:

* [Installation Note](/docs/user/manual/en/stock/installation-note)
* [Sales Return](/docs/user/manual/en/stock/sales-return)
* [Delivery Trip](/docs/user/manual/en/stock/delivery-trip)
* [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)

![Delivery Note after submit](/docs/assets/img/stock/delivery-note-submit.png)

> Tip: To disallow the creation of Delivery Notes without a Sales Order against it:

### 3.17 Returning a Sales Order
Once you've delivered a Sales Order using a Delivery Note, you can create a return entry in case the [Customer](/docs/user/manual/en/CRM/customer) returns the Item. To know more, visit the [Sales Return](/docs/user/manual/en/stock/sales-return) page.

### 3.18 Skipping Delivery Note

If you don't want to create a Delivery Note after a Sales Order and directly want to create a Sales Invoice, enable the feature for it in [Selling Settings](/docs/user/manual/en/selling/selling-settings#32-delivery-note-required).


### 4. Related Topics
1. [Warehouse](/docs/user/manual/en/stock/warehouse)
1. [Delivery Note Stock Error](/docs/user/manual/en/stock/articles/delivery-note-stock-error)
1. [Material Transfer From Delivery Note](/docs/user/manual/en/stock/articles/material-transfer-from-delivery-note)
1. [Installation Note](/docs/user/manual/en/stock/installation-note)
1. [Delivery Trip](/docs/user/manual/en/stock/delivery-trip)