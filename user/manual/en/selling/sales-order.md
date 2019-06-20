<!-- add-breadcrumbs -->
# Sales Order

**A Sales Order is a confirmation of an order from your customer.**

It is usually a binding Contract with your Customer. Once your customer confirms the Quotation you can convert your Quotation into a Sales Order.

<img class="screenshot" alt="Make Quotation from Opportunity" src="{{docs_base_url}}/assets/img/selling/selling-flow-so.png">

## 1. How to create a Sales Order
1. Go to **Selling > Sales > Sales Order > New Sales Order** or Type 'New Sales Order' into the "Global Search" field.
1. Select the Customer.
1. Under 'Delivery Date' set the date by which order is to be delivered.
1. With Order Type, you can set whether it's a Sales order, Maintenance order, or from the online [Shopping Cart](/docs/user/manual/en/website/shopping-cart) of your website. By default, this value is set to "Sales".
1. In the "Customer's Purchase Order" you can enter the Customers Purchase Order No. or other details which may be useful as a reference.
1. Enter the items and quantities to be delivered in the Item table. If Item Prices are set for the items, the Rate field will be populated automatically. If not, enter the item Rate manually. You can also overwrite the auto-populated Item Rate in case you want to change that value.
1. Click "Save" to save a draft of the Sales Order.
1. "Submit" to submit the Sales Order to the System.

### 1.1 Other ways to create a Sales Order
1. You can also create a Sales Order from a submitted Quotation via the Create button on the top right.

  <img class="screenshot" alt="Make Sales Order from Quotation" src="{{docs_base_url}}/assets/img/selling/make-SO-from-quote.png">

1. Or you can create a new Sales Order and pull details from a Quotation.

  <img class="screenshot" alt="Make Sales Order from Quotation" src="{{docs_base_url}}/assets/img/selling/so-from-quote.gif">

To allow for per-Customer, per-Item Pricing Rules, ("Customer A" pays $1.00 for "Item 1" but "Customer B" pays $1.25 for "Item 1"), there's a check box called 'Allow User to Edit Price List Rate in Transaction' in [Selling Settings](/docs/user/manual/en/selling/selling-settings). This enables saving the specific item price per customer when you change a price in the Sales Order.

## 2. Features

### 2.1 Currency and Price List
To know about Currency and Price List, [click here](/docs/user/manual/en/selling/articles/currency-and-price-list)

### 2.1 Set Source Warehouse
If you have the same stock in multiple warehouses, setting a warehouse here will cause all the items from the item table to be fetched from this warehouse. You need to have stock available in this 'source warehouse' you're setting. Note that this option will override the 'Default Warehouse' you've set in the Item master.

### 2.2 The Item Table
* **Delivery Date against each item**: If there are multiple items and if you enter a delivery date in the first row, the date will be copied to other rows as well where it is blank. You'll have to set these if not set globally at the top of the Sales Order.
  
    A Sales Order displays the billed amount, valuation rate, and gross profit in the items table when you click on the inverted triangle to expand a row. 

    You can also add items in the item table by scanning their barcodes if you have a barcode scanner. Know how to track them [here](/docs/user/manual/en/stock/articles/track-items-using-barcode)

* **Delivery Warehouse**: This is the warehouse from where the stock will be picked to be delivered to your customer.

* **Drop Ship**: This is a situation where you do not keep items in stock in your own Warehouse but deliver items directly to a customer from a distributor. To enable drop shipping for an item tick on the 'Supplier delivers to Customer'. When you tick on this, the Delivery Warehouse option will disappear since you're not shipping the item. Select your supplier in the 'Supplier' field.

    Further, if you create a purchase order from this sales order, it'll be created for the supplier you selected here and only the items which are valid for drop shipping.

* **Planning**: To know about the fields under planning [click here](/docs/user/manual/en/stock/projected-quantity).

The other fields int the item table are similar as explained in [Quotation](/docs/user/manual/en/selling/quotation#23-the-items-table).

### 2.3 Packing List

The “Packing List” table will be automatically updated when you “Save” the Sales Order. If any Items in your table are Product Bundle (packets), then the “Packing List” will contain the exploded (detailed) list of your Items.

You will be asked to select a Delivery Warehouse even for a product bundle item, this warehouse will be then updated in the Packing List items. You can change the warehouse in the packing list items in case items in your product bundle come from different warehouses.

Here is what a Packing List looks like:

<img class="screenshot" alt="Packing List" src="{{docs_base_url}}/assets/img/selling/so-packing-list.png">

### 2.4 Taxes and Charges
To know about setting up taxes visit [this page](/docs/user/manual/en/setting-up/setting-up-taxes).
To know about Taxes and Charges in a quotation, [click here](/docs/user/manual/en/selling/articles/taxes-and-charges)

### 2.5 Additional Discount
To know about Additional Discount, [click here](/docs/user/manual/en/selling/articles/additional-discount)

### 2.6 Payment Terms
To know about Payment Terms, [click here](/docs/user/manual/en/selling/articles/payment-terms)

### 2.7 Terms and Conditions
To know about Terms and Conditions, [click here](/docs/user/manual/en/selling/articles/terms-and-conditions)

### 2.8 Print Settings
To know about Print Settings, [click here](/docs/user/manual/en/selling/articles/print-settings)

### 2.9 More Information
Campaign and Source (lead source) are explained in [Quotation](/docs/user/manual/en/selling/quotation#29-more-information).

**Inter Company Order Reference**: If two of your companies are part of the same organization or have a parent-child relationship, you can link a Purchase Order to this Sales Order. Know more about inter-company invoicing [here](/docs/user/manual/en/accounts/inter-company-invoices).
**Project**: If your Sales Order is part of a project, you can link it here and the Project progress will be updated.

### 2.10 Billing and Delivery Status

* **Status**: The status of the Sales Order whether a Draft, On Hold, To Deliver and Bill, To Bill, To Deliver, Completed, Cancelled, or Closed.
* **Amount Billed and Delivered percent**: The percentage of amount billed and the items delivered from the Sales Order.

### 2.11 Commission
If the sale took place via one of your Sales Partners, you can add their commission details here. Enter the commission rate and the commission amount will be displayed below.

### 2.12 Sales Team
**Sales Persons:** ERPNext allows you to add multiple Sales Persons who may have worked on this deal. You can change the contribution percentage of the Sales Persons and track how much incentives they earned on this deal.

<img class="screenshot" alt="Sales Team in Sales Order" src="{{docs_base_url}}/assets/img/selling/so-sales-team.png">

### 2.13 Auto Repeat Section
Auto repeating Sales Orders is like a subscription. Set a start and end date for the auto-repeat. Select the Auto Repeat created. To know more about auto repeat [click here](/docs/user/manual/en/accounts/auto_repeat).

### 2.14 Submitting
Sales Order is a “Submittable” transaction. You will be able to execute further steps (like making a Delivery Note) only after “Submitting” a Sales Order.

Once you “Submit” your Sales Order, you can trigger actions from the Sales Order:

* You can Update the items in the Sales Order by clicking on the Update Items button. If you need to update any other details, you'll have to cancel the Sales Order, amend, then save and submit.

* Status: Once submitted, you can hold a Sales Order or Close it.

* Create: From a submitted Sales Order, you can create the following:

    * Delivery Note - To make a shipment entry. You can also make Delivery Note for selected items based on the delivery date.
    * Work Order - To start a Work Order with the raw materials.
    * Sales Invoice - To bill the Order.
    * Material Request - To request re-stocking materials if out of stock.
    * Request for Raw Materials - To request raw materials required for manufacturing.
    * Project - To create a project based on the Sales Order.
    * Subscription - To auto repeat the Sales Order, i.e., make it a subscription.
    * Payment Request - To make a Payment Request.
    * Payment - To record payment against the Sales Order.

These actions can also be seen at the top of the Dashboard. You can also make an accounting Journal Entry based on the Sales Order from the dashboard.

<img class="screenshot" alt="Actions from Submitted Sales Order" src="{{docs_base_url}}/assets/img/selling/submit-so.png">


### 2.15 Sales Order with Order type Maintenance

When the 'Order Type' of the Sales Order is 'Maintenance' follow these steps:

1. Enter Currency, Price list, and Item details.
2. Mention taxes and other information.
3. Save and Submit the form.
4. Once the form is submitted, the Create button will provide these choices specific to the maintenance Order Type.

    i) Maintenance Visit ii) Maintenance Schedule.


> **Note 1:**   
By clicking on the Action button and selecting 'Maintenance Visit' you can directly fill the visit form. The Sales Order details will be fetched directly.    

> **Note 2:**    
By clicking on the Action button and selecting 'Maintenance Schedule' you can fill the schedule details. The Sales Order details will be fetched directly.

> **Note 3:**    
By clicking on the Invoice button you can make an Invoice for your
services. The sales orders details will be fetched directly.

### 3. Related Topics
1. [Quotation](/docs/user/manual/en/selling/quotation)
1. [Close Sales Order](/docs/user/manual/en/selling/articles/close-sales-order)
1. [Amending Sales Order After Submit](/docs/user/manual/en/selling/articles/amending-sales-order-after-submit)

{next}
