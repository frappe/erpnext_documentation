<!-- add-breadcrumbs -->
# Stock Entry

**A Stock Entry lets you record Item movement between Warehouses.**

To access the Stock Entry list, go to:
> Home > Stock > Stock Transactions > Stock Entry

Stock Entries can be made for the following purposes:

* **Material Issue**: If the material is being issued to someone in or outside the company (Outgoing Material). The Items will be deducted from the Warehouse set under Source Warehouse.
* **Material Receipt**: If the material is being received (Incoming Material). The Items will be added to the Warehouse set under Target Warehouse.
* **Material Transfer**: If the material is being moved from one internal Warehouse to another.
* **Material Transfer for Manufacturing**: If raw materials are being transferred for manufacturing. The transfer can happen against a [Work Order](/docs/user/manual/en/manufacturing/work-order) or a [Job Card](/docs/user/manual/en/manufacturing/job-card). To know more, visit the [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials) page.
* **Material Consumption for Manufacture**: There can be multiple consumption stock entries against a manufacturing Work Order. [Refer this link for more details](/docs/user/manual/en/manufacturing/articles/material_consumption)
* **Manufacture**: If the Material is being received from a Manufacturing/Production Operation.
* **Repack**: If the Original item/items are being repacked into new item/items.
* **Subcontract**: If the Material is being issued for a sub-contract activity. This entry is made from a Purchase Order. To know more, visit the [subcontracting](/docs/user/manual/en/manufacturing/subcontracting) page.
* **Send to Warehouse**: If the Material is being sent at a Warehouse and needs confirmation at the receiving end, this document will be selected in the Stock Entry with type 'Receive to Warehouse' to confirm how many items were received. The status will be 'Goods In Transit' until all goods are received, after which the status will change to 'Goods Transferred'.
* **Receive to Warehouse**: If the Material is being received at a Warehouse the Stock Entry with type 'Send to Warehouse' will be selected here and the number of goods received will be updated.

To know more in detail about the stock entry types, [visit this page](/docs/user/manual/en/stock/articles/stock-entry-purpose).


## 1. Prerequisites
Before creating and using a Stock Entry, it is advised that you create the following first:

* [Warehouse](/docs/user/manual/en/stock/warehouse)
* [Item](/docs/user/manual/en/stock/item)


## 2. How to create a Stock Entry
Stock Entries for Manufacturing purposes are usually created from a [Work Order](/docs/user/manual/en/manufacturing/work-order). To create a Stock Entry manually for other purposes, follow these steps:

1. Go to the Stock Entry list, click on New.
1. Select the Stock Entry Purpose from the ones listed above.
1. If you set the Default Source or Target Warehouses, they'll be automatically filled for the rows in the Items table.
1. Source/Target Warehouses will be available as per the Stock Entry Purpose you selected.
1. Select Items and enter a quantity.
1. The basic rate will be fetched and the amount will be calculated automatically.
1. Save and Submit.

    <img class="screenshot" alt="Stock Entry" src="{{docs_base_url}}/assets/img/stock/stock-entry.png">

Usually, "Source Warehouse" and "Target Warehouse" both are set for recording a movement.

### 2.1 Additional options when creating a Stock Entry

* **Work Order**: If this is a Manufacturing entry, the Work Order will be shown in this field.
* **Edit Posting Date and Time**: Will allow you to edit the Stock Entry's date and time.
* **Inspection Required**: If a [Quality Inspection](/docs/user/manual/en/stock/quality-inspection) needs to be performed on the Items before submitting the Stock Entry.
* **From BOM**: If this is a Manufacturing entry, the associated BOM for the Item being manufactured will be shown.

### 2.2 Stock Entry Type
You can also create a Stock Entry Type where only the name will be different, for example 'Scrap Entry'. The purpose will be Material Transfer but the name will be different. This is useful if you want certain Users to have access only to specific actions related to stock.

![Stock Entry Type](/docs/assets/img/stock/stock-entry-type.png)

## 3. Features

### 3.1 The Items table
Details about the Item, Rate, Quantity, etc. will be shown here.

Ticking on 'Allow Zero Valuation Rate' will allow submitting the Purchase Receipt even if the Valuation Rate of the Item is 0. This can be a sample item or due to a mutual understanding with your Supplier.

Different Source and Target Warehouses can be set for different Items.

### 3.2 Additional Costs

If the stock entry is an incoming entry i.e any item is receiving at a target warehouse, you can add related additional costs (like Shipping Charges, Customs Duty, Operating Costs, etc) associated with the process. The additional costs will be considered to calculate the Valuation Rate of the items.

To add additional costs, enter the description and amount of the cost in the Additional Costs table.

<img class="screenshot" alt="Stock Entry Additional Costs" src="{{docs_base_url}}/assets/img/stock/additional-costs-table.png">

The added Additional Costs will be distributed among the receiving items (where the Target Warehouse mentioned) proportionately based on the Basic Amount of the items. And the distributed additional cost will be added to the basic rate of the item, to calculate Valuation Rate.

Quantity and Rate is shown as follows when you expand the Items table.
<img class="screenshot" alt="Stock Entry Item Valuation Rate" src="{{docs_base_url}}/assets/img/stock/stock-entry-item-valuation-rate.png">

### 3.3 Accounting Dimensions
You can tag different transactions based on different dimensions. By default, [Projects](/docs/user/manual/en/projects/project) can be considered as a dimension as it is a common practice to track costs of different projects. To know more about Accounting Dimensions, [visit this page](/docs/user/manual/en/accounts/accounting-dimensions).

### 3.4 Printing Settings

#### Letterhead
You can print your Purchase Receipt on your company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

#### Print Headings
Purchase Receipt headings can also be changed when printing the document. You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

### 3.5 More Information

* **Is Opening**: If this entry is the opening stock entry for the Items.
* **Remarks**: Any additional remarks about the Item.
* **Percentage Transferred**: The percentage of Items transferred depending on Stock Entry purpose.
* **Total Amount**: The total amount of Items transferred.

### 3.6 Perpetual Inventory

If the perpetual inventory system is enabled, additional costs will be booked in Expense Account mentioned in the Additional Costs table .

<img class="screenshot" alt="Additional Costs General Ledger" src="{{docs_base_url}}/assets/img/stock/stock-entry-additional-cost.png">

<img class="screenshot" alt="Additional Costs General Ledger" src="{{docs_base_url}}/assets/img/stock/additional-costs-general-ledger.png">

### 3.7 After Submitting
After submitting a Stock Entry, you can go to the stock ledger or the accounting ledger from the dashboard.

<img class="screenshot" alt="Additional Costs General Ledger" src="{{docs_base_url}}/assets/img/stock/stock-entry-submit.png">

## 4. Video

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Njt107hlY3I?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 5. Related Topics
1. [Stock Entry Purpose](/docs/user/manual/en/stock/articles/stock-entry-purpose)
1. [Stock Reconciliation](/docs/user/manual/en/stock/stock-reconciliation)
1. [Opening Stock Balance Entry For Serialized And Batch Item](/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Stock Reconciliation](/docs/user/manual/en/stock/stock-reconciliation)
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)
1. [Production Plan](/docs/user/manual/en/manufacturing/production-plan)
1. [Job Card](/docs/user/manual/en/manufacturing/job-card)
