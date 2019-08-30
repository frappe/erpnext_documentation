---
title: Pick List
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders. This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many Stock Keeping Unit(SKU).
 keywords: Pick List, Picking Slip, frappe, Pick Ticket, erpnext new features, erp, open source erp, free erp, stock
---

# Pick List

**A Pick List is a document that indicates which items should be taken from your inventory to fulfill orders.**

This is particularly useful for shippers with a large amount of inventory, volume of orders, or customers ordering many Stock Keeping Unit(SKU).
Pick list selects Warehouse where an Item is available on FIFO (First-In-First-Out) basis.
Selection of Warehouse for a batched item is different. In case of batched items, Warehouse where the batch is nearer to its expiry will be selected.

To access Pick List, go to:

> Home > Stock > Stock Transactions > Pick List

## 1. Prerequisites

Before creating and using a Pick List, it is advised that you create the following first:

- [Stock Item](/docs/user/manual/en/stock/item)
- [Warehouse](/docs/user/manual/en/stock/warehouse)

## 2. How to create Pick List

1. Go to the Pick List list, click on New.
1. Set the Company.
1. Select the Purpose of Pick List. These are the options under Purpose:

   - **Delivery against Sales Order:** This option will let you add Items from a Sales Order. After submitting Pick List a new Delivery Note can be created based on the Warehouse from which items were picked.

   - **Material Transfer for Manufacture:** This will let you select a Work Order from which raw materials will be pulled for picking. You will be presented with an option to select the number of finished goods for which you want to pick raw materials. After picking the stock you can create Stock Entry for the picked items i.e., raw materials.

   - **Material Transfer:** This will let you select a Material Request for which you want to pick items. After picking the stock you can create a Stock Entry for the picked items.

1. Add Item and the quantity you want to pick in the Item Locations table. Click on **Get Item Locations** to get the Warehouse and other details for each Item.

1. **Parent Warehouse:** If a parent Warehouse is selected, Warehouses only under that parent Warehouse will be suggested.

1. **Get Item Locations:** Once items to be picked is finalized you can click on the **Get Item Locations** button to get Warehouse selection for each item. Since Warehouse will be automatically fetched if you get an Item from any reference document, this button can be useful to manually add additional Items or change the quantity of existing Items in the Item Locations table.

1. **Item Locations:** This will have the information of the item location (Warehouse), Serial Number for serialized items and batch no for batched items.
 <img class='screenshot' alt='Item Locations' src='{{docs_base_url}}/assets/img/stock/pick-list-item-locations.png'>

 If Serial Numbers are involved, the Item row will look like this:
 <img class='screenshot' alt='Item Location Detail' src='{{docs_base_url}}/assets/img/stock/pick-list-item-location-detail.png'>

1. Save and Submit.
 <img class='screenshot' alt='Submitted Pick List' src='{{docs_base_url}}/assets/img/stock/pick-list-submitted-doc.png'>

### 2.1 Create Pick List from a Sales Order

1. Go to a [Sales Order](/docs/user/manual/en/selling/sales-order).
1. Click on the **Create** button on the top right of the form and then click the **Pick List** option.
1. Once you click Pick List, all the data required for Pick List will be fetched from the Sales Order.
1. You should be able to see the Item Locations Table with the Warehouse selected for each item.
1. Save this document and it can be used for stock picking by the person performing this activity.
1. Submit the document once the stock picking is done and picked item quantities are updated in the document.

**Tip:** You can create a Pick List for multiple Sales Order from the same Customer. Click on Get Items and select the Sales Orders.

> **Note:**
>
> - Pick list can only be created for Sales Orders which has pending Items to be delivered.
> - A **Delivery Note** can be created only if the Pick List is submitted.

### 2.2 Create Pick List from a Work Order

1. Go to a [Work Order](/docs/user/manual/en/stock/work-order).
1. Click **Create Pick List** button.
1. You'll see the dialog box asking for the quantity of Finished Goods Item. This is required to calculate the number of raw material items required to manufacture the entered quantity of Finished Goods Item.
<img class='screenshot' alt='Dailog For qty' src='{{docs_base_url}}/assets/img/stock/pick-list-dialog-for-qty.png'>

1. You should be able to see the Item locations table with the Warehouse selected for each raw material item.
1. Save this document and then this document can be forwarded to the person who is picking the stock.
1. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:**
>
> - Pick list can only be created for Work Orders that are still in the state of 'Not Started' or 'In Progress'.
> - A **Stock Entry** can be created only after the Pick List is submitted.

### 2.3 Create Pick List from Material Request

1. Go to a [Material Request](/docs/user/manual/en/stock/material-request).
1. Click on **Create** button and then click **Pick List** option.
1. You should be able to see the Item Locations table with the Warehouse selected for each item in Material Request.
1. Save this document and then this document can be forwarded to the person picking the stock.
1. Submit the document once the stock picking is done and the picked item is updated in the document accordingly.

> **Note:**
>
> - Only Material Requests with type 'Material Transfer' can be used for Pick List creation.
> - A **Stock Entry** of type 'Material Transfer' can be created after the Pick List is submitted.

## 3. Related Topics

1. [Sales Order](/docs/user/manual/en/selling/sales-order)
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)
1. [Material Request](/docs/user/manual/en/stock/material-request)
