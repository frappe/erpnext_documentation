<!-- add-breadcrumbs -->
# Batch

Batch feature in ERPNext allows you to group multiple units of an item,
and assign them a unique value/number/tag called Batch No.

This is done based on the Item. If the Item is batched, then a Batch number must be mentioned in every stock transaction. Batch numbers can be maintained manually or automatically

### 1. How to create a new Batch

To set item as a batch item, "Has Batch No" field should be checked in the Item master. If you have not selected "Automatically Create New Batch" when creating an Item, you will have to make Batches Manually as you go along. 

To create new Batch No. master for an item, go to:

1. Go to: **Stock > Serial No and Batch > Batch > New**.
1. Set the Batch ID.
1. Enter the item.
1. If any transaction is done with an item, batch cannot be set or unset.
1. Save.

#### 1.2 Item Setup
If you want automatic batch creation at the time of Purchase Receipt, you must check "Create New Batches Automatically"

<img class="screenshot" alt="Item Setup for Batches" src="{{docs_base_url}}/assets/img/stock/item_setup_for_batch.png">

### 2. Features
#### 2.1 Splitting and Moving Batches

When you open a batch, you will see all the quantities relating this that batch on the page.

<img class="screenshot" alt="Batch View" src="{{docs_base_url}}/assets/img/stock/batch_view.png">

To move the batch from one warehouse to another, you can click on the move button.

You can also split the batch into smaller one by clicking on "Split". This will create a new Batch based on this Batch and the quantities will be split between the batches.

#### 2.2 Transacting Items with Batches

Batch master is created before creation of Purchase Receipt.
Hence everytime there is Purchase Receipt or Work Order being made for a batch item,
you will first create its Batch No, and then select it in Purchase order or Production Entry.

On every stock transaction (Purchase Receipt, Delivery Note, POS Invoice) made for batch item,
you should provide item's Batch No.

> Note: In stock transactions, Batch IDs will be filtered based on Item Code, Warehouse,
Batch Expiry Date (compared with Posting date of a transaction) and Actual Qty in Warehouse.
While searching for Batch ID  without value in Warehouse field, then Actual Qty filter won't be applied.

#### 3. Related Topics
1. [Serial Number](/docs/user/manual/en/stock/serial-no)
1. [Opening Stock Balance Entry For Serialized And Batch Item](/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Managing Batch Wise Inventory](/docs/user/manual/en/stock/articles/managing-batch-wise-inventory)
