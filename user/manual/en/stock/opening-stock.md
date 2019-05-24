<!-- add-breadcrumbs -->
# Opening Stock

**Opening Stock is the amount and value of materials that a company has available for sale or use at the beginning of an accounting period.**

The closing Stock of the previous accounting period becomes the opening Stock of the current accounting period.

* To update opening stock for non-serialized items, use **Stock Reconciliation**.
* To update opening stock for serialized items, use **Stock Entry** with Stock Entry Type as Material Receipt.

##1. Prerequisites

* Enable "Perpetual Inventory" in [Stock Settings](/docs/user/manual/en/stock/stock-settings).
* Create [Items](/docs/user/manual/en/stock/item) for non-serialised, serialised and batched products.
* Create [Warehouses](/docs/user/manual/en/stock/warehouse)
* Link Warehouse to appropriate accounting ledgers.

##2. Opening Stock for Non-serialized Items


To post opening stock for non-serialised items check [Stock Reconciliation](/docs/user/manual/en/setting-up/stock-reconciliation-for-non-serialized-item)


##3. Opening Stock for Serialised and Batched Items

Create the [Batch](/docs/user/manual/en/stock/batch) and [Serial No](/docs/user/manual/en/stock/serial-no) records beforehand. To post opening stock for serialised and batched items:

1. Go to **Stock > Stock Transactions > Stock Entry > New**.
1. Select 'Material Receipt' in 'Stock Entry Type'.
1. Select the warehouse in 'Default Target Warehouse'.
1. In Items table select Item Code, Qty and Basic rate.
1. For batched items select Batch No.
1. For serialised items select Serial No.
1. Save and Submit.

<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/nlHX0ZZ84Lw?end=120" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

### 4. Related Topics
1. [Accounting Of Inventory Stock](/docs/user/manual/en/stock/accounting-of-inventory-stock)
1. [Stock Entry](/docs/user/manual/en/stock/stock-entry)
1. [Stock Reconciliation](/docs/user/manual/en/setting-up/stock-reconciliation-for-non-serialized-item)
