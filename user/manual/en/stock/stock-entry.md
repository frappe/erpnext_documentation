<!-- add-breadcrumbs -->
# Stock Entry

A Stock Entry is a simple document that lets you record Item movement from a
Warehouse, to a Warehouse and between Warehouses.

Stock Entries can be made for the following purposes:

* **Material Issue**: If the material is being issued. (Outgoing Material).
* **Material Receipt**: If the material is being received. (Incoming Material).
* **Material Transfer**: If the material is being moved from one warehouse to another.
* **Material Transfer for Manufacturing**: If the material being transfered is for Manufacturing Process.
* **Manufacture**: If the Material is being received from a Manufacturing/Production Operation.
* **Repack**: If the Original item/items is being repacked into new item/items.
* **Subcontract**: If the Material is being issued for a sub-contract activity.

### 1. How to create a Stock Entry
1. Go to **Stock > Stock Transactions > Stock Entry > New**.

    <img class="screenshot" alt="Stock Entry" src="{{docs_base_url}}/assets/img/stock/stock-entry.png">
1. Select the Stock Entry Purpose from the ones listed above.
1. If you set the Default Source or Target Warehouses, they'll be automatically filled for the rows in the Items table.
1. Source/Target Warehouse will be available as per the Stock Entry Purpose you selected.
1. Select Item, quantity.
1. The basic rate will be fetched and the amount will be calculated automatically.
1. Save and Submit.

Usually, "Source Warehouse" and "Target Warehouse" both are set for recording a movement.

### 2. Features

#### 2.1 Additional Costs

If the stock entry is an incoming entry i.e any item is receiving at a target warehouse, you can add related additional costs (like Shipping Charges, Customs Duty, Operating Costs etc) associated with the process. The additional costs will be considered to calculate valuation rate of the items.

To add additional costs, enter the description and amount of the cost in the Additional Costs table.

<img class="screenshot" alt="Stock Entry Additional Costs" src="{{docs_base_url}}/assets/img/stock/additional-costs-table.png">

The added additional costs will be distributed among the receiving items (where the target warehouse mentioned) proportionately based on Basic Amount of the items. And the distributed additional cost will be added to the basic rate of the item, to calculate valuation rate.

Quantity and Rate is shown as follows when you expand the Items table.
<img class="screenshot" alt="Stock Entry Item Valuation Rate" src="{{docs_base_url}}/assets/img/stock/stock-entry-item-valuation-rate.png">

#### 2.2 Perpetual Inventory

If perpetual inventory system is enabled, additional costs will be booked in "Expense Included In Valuation" account.

<img class="screenshot" alt="Additional Costs General Ledger" src="{{docs_base_url}}/assets/img/stock/additional-costs-general-ledger.png">

The following video shows a demonstration of Stock Entry:
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Njt107hlY3I?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

#### 3. Related Topics
1. [Stock Entry Purpose](/docs/user/manual/en/stock/articles/stock-entry-purpose)
1. [Opening Stock Balance Entry For Serialized And Batch Item](/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Stock Reconciliation](/docs/user/manual/en/setting-up/stock-reconciliation-for-non-serialized-item)
