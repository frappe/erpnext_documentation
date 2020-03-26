<!-- add-breadcrumbs -->
# Batch

**Batch feature in ERPNext allows you to group multiple units of an Item and assign them a unique value/number/tag called Batch No.**

This is done based on the Item. If the Item is batched, then a Batch number must be mentioned in every stock transaction. Batch numbers can be maintained manually or automatically. This feature is useful to set the expiry date of multiple Items or move them together to different Warehouses.

To access the Batch No list, go to:
> Home > Stock > Serial No and Batch > Batch


## 1. Prerequisites
Before creating and using a Batch, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)
* Enable 'Has Batch No' in the Item master
    ![Batch No Enabled](/docs/assets/img/stock/batch-no-enabled.png)


## 2. How to create a new Batch

To set item as a batch item, "Has Batch No" field should be checked in the Item master. If you have not selected "Automatically Create New Batch" when creating an Item, you will have to make Batches Manually as you go along. 

To create new Batch No. master for an item, go to:

1. Go to the Batch list, click on New.
1. Set the Batch ID.
1. Select the Item.
1. If any transaction is done with an item, the batch cannot be set or unset.
1. Save.

When Batches are enabled for an Item, the option to [retain sample stock](/docs/user/manual/en/stock/retain-sample-stock) also becomes available. 

### 2.1 Batch Auto Creation
If you want automatic batch creation at the time of Purchase Receipt, you must tick 'Automatically Create New Batch' in the Item master:

<img class="screenshot" alt="Item Setup for Batches" src="{{docs_base_url}}/assets/img/stock/item_setup_for_batch.png">

## 3. Features
### 3.1 Splitting and Moving Batches

When you open a batch, you will see all the quantities that belong to that batch on the page.

<img class="screenshot" alt="Batch View" src="{{docs_base_url}}/assets/img/stock/batch_view.png">

* To move the batch from one Warehouse to another, you can click on the **Move** button.

* You can also split the batch into smaller one by clicking on the **Split** button. This will create a new Batch based on this Batch and the quantities will be split between the batches.

    ![Split Batch](/docs/assets/img/stock/batch_split.png)

* If you set expiry date, the Batch will show 'Not Expired' until the expiry date, after which it'll show 'Expired'. If a date is not set, the Batch will show 'Not Set'.

### 3.2 Transacting Items with Batches

A Batch master should be created before the creation of Purchase Receipt.
Hence, every time a Purchase Receipt or Work Order is being made for a batch item,
you will first create its Batch No, and then select it in the Purchase order or Stock Entry.

On every stock transaction (Purchase Receipt, Delivery Note, Invoice) with a batch item,
you should provide the Item's Batch No.

> Note: In stock transactions, Batch IDs will be filtered based on Item Code, Warehouse,
Batch Expiry Date (compared with a Posting date of a transaction) and Actual Qty in Warehouse.
While searching for Batch ID  without value in the Warehouse field, Actual Qty filter won't be applied.

### 4. Related Topics
1. [Serial Number](/docs/user/manual/en/stock/serial-no)
1. [Opening Stock Balance Entry For Serialized And Batch Item](/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Managing Batch Wise Inventory](/docs/user/manual/en/stock/articles/managing-batch-wise-inventory)
