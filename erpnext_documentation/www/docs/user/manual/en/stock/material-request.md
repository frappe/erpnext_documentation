<!-- add-breadcrumbs -->
# Material Request

**A Material Request is a simple document identifying a requirement of a set of Items (products or services) for a particular reason.**

A Material Request can be of the following types:

* **Purchase**: If the material being requested is to be purchased.
* **Material Transfer**: If the material being requested is to be shifted from one Warehouse to another.
* **Material Issue**: If the material being requested is to be Issued for some purpose like manufacturing.
* **Manufacture:** If the material being requested is to be produced.
* **Customer Provided**: If the material being requested is to be provided by Customer. To know more about this, visit the [Customer Provided Item](/docs/user/manual/en/manufacturing/articles/customer-provided-items) page.

<img class="screenshot" alt="Material Request" src="{{docs_base_url}}/assets/img/buying/material-request-flowchart.png">

To access the Material Request list, go to:
> Home > Stock > Stock Transactions > Material Request

## 1. How to create a Material Request
1. Go to the Material Request list, click on New.
1. Enter the required by date.
1. Select from one of the types as listed above.
1. You can fetch Items from a BOM, Sales Order, or Product Bundle.
  ![MR fetch from](/docs/assets/img/stock/mr-fetch-from.png)
1. Select the Item and set the quantity.
1. Select the Warehouse for which Items are required.
1. You can change the Required by Date for individual Items in this table.
1. Save and Submit.

### 1.1 Alternate ways of creating a Material Request
A Material Request can be generated automatically:

* From a [Sales Order](/docs/user/manual/en/selling/sales-order).
* When the Projected Quantity of an Item in Stores (Warehouses) reaches a particular level.
* From your a [Production Plan](/docs/user/manual/en/manufacturing/production-plan) to plan your manufacturing activities.

If your Items are inventory items, you must also mention the Warehouse where you expect these Items to be delivered. This helps to keep track of the [Projected Quantity](/docs/user/manual/en/stock/projected-quantity) for this Item.

> Info: Material Request is not mandatory. It is ideal if you have centralized
buying so that you can collect this information from various departments.

### 1.2 Statuses

These are the statuses a Material Request can be in:

* **Draft**: A draft is saved but yet to be submitted to the system.
* **Submitted**: Document is submitted to the system.
* **Stopped**: If no more materials are needed the Material Request can be stopped.
* **Canceled**: The materials are not needed at all and the request is canceled.
* **Pending**: The Purchase/Manufacture is pending to complete the Material Request.
* **Partially Ordered**: Purchse Orders for some Items from the Material Request are made and some are pending.
* **Ordered**: All Items in the Material Request are ordered via Purchase Orders.
* **Issued**: The materials are issued using a Material Issue Stock Entry.
* **Transferred**: The required materials are transferred from one Warehouse to another using a Stock Entry.
* **Received**: The materials were ordered and have been received at your Warehouse using a Purchase Receipt.

## 2. Features
### 2.1 Items table
* **Barcode**: You can track Items using [barcodes](/docs/user/manual/en/stock/articles/track-items-using-barcode).

* The Item Code, name, description, Image, and Manufacturer will be fetched from the Item master.

* The UoM, Conversion Factor, and Amount will be fetched. You change the Warehouse for which the material is being requested.

* Accounting details like Expense Account and Accounting Dimensions can be set for the Items.

* Page Break will create a page break just before this item when printing.

### 2.2 More Information
In the 'Requested For' field, you can set a Reference from where Material Request was generated.

### 2.3 Printing Details
#### Letterhead
You can print your Material Request on your company's letterhead. [Click here](/docs/user/manual/en/setting-up/print/letter-head) to learn more.

#### Print Headings
Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

### 2.4 Terms and Conditions
In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions)

### 2.5 After Submitting
You can create the following documents:

* [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation) 
* [Purchase Order](/docs/user/manual/en/buying/purchase-order) 
* [Supplier Quotation](/docs/user/manual/en/buying/supplier-quotation) 

<img class="screenshot" alt="Material Request" src="{{docs_base_url}}/assets/img/stock/material-request.png">


### 2.6 Automatically generate Material Requests

Material Requests can be generated automatically by enabling the setting in [Stock Settings](/docs/user/manual/en/stock/stock-settings#9-automatic-material-request) and setting the level in the [Item form](/docs/user/manual/en/stock/item#34-automatic-reordering). When the stock level dips below a certain quantity, setting a reorder will automatically create material requests for the Item.

## 3. Video
<div>
  <div class="embed-container">
    <iframe src="https://www.youtube.com/embed/55Gk2j7Q8Zw?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
  </div>
</div>

### 4. Related Topics
1. [Item](/docs/user/manual/en/stock/item)
1. [Auto Creation Of Material Request](/docs/user/manual/en/stock/articles/auto-creation-of-material-request)
1. [Pick List](/docs/user/manual/en/stock/pick-list#23-create-pick-list-from-material-request)
1. [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation) 
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order) 
1. [Supplier Quotation](/docs/user/manual/en/buying/supplier-quotation) 
