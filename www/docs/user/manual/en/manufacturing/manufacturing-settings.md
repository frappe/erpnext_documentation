<!-- add-breadcrumbs -->
#Manufacturing Settings

Manufacturing Settings can be found at:

> Home > Manufacturing > Settings > Manufacturing Settings

<img class="screenshot" alt="Manufacturing Settings" src="{{docs_base_url}}/assets/img/manufacturing/manufacturing-settings-1.png">

### Capacity Planning
[Capacity planning](/docs/user/manual/en/manufacturing/capacity-planning) is the process in which an organization decides whether or not to accept the new orders based on the resources and existing work orders.

### Over Production Allowance Percentage

While making Work Orders against a Sales Order, the system will only allow production item quantity to be lesser than or equal to the quantity in the Sales Order. In case you wish to allow Work Orders to be raised with greater quantity, you can mention the Over Production Allowance Percentage here.

Example: In certain cases, a Workstation has to manufacture 100 units for cost effectiveness but the Work Order could be for 50 units. In this case, the Over Production Allowance Percentage would be 100.

### Backflush Raw Materials Based On

The Stock Entry of type 'Manufacture' is known as backflush. Raw materials being consumed to manufacture finished goods is known as backflushing.

When creating Manufacture Entry, raw-material items are backflushed based on BOM of production item. If you want raw-material items to be backflushed based on Material Transfer entry made against that Work Order instead, then you can set it under this field.

<img class="screenshot" alt="Manufacturing Settings" src="{{docs_base_url}}/assets/img/articles/manufacturing-settings-4.png">

### Default Work In Progress Warehouse

This Warehouse will be auto-updated in the 'Work In Progress' Warehouse field of Work Orders.

### Default Finished Goods Warehouse

This Warehouse will be auto-updated in the 'Target Warehouse' field of Work Order.

### Allow Multiple Material Consumption
If ticked, multiple materials can be used for a single Work Order. This is useful if one or more time consuming products are being manufactured. For example a single product takes a month to manufacture and the raw materials are consumed daily. In a regular scenario, this won't be feasible with stock entries. Enabling this option will allow you to create stock entries for material consumption without having to create an entry to backflush. End result is that you can see the stock being consumed in the Warehouses and can update the final manufacure entry at a later stage.

### Update BOM Cost Automatically
If ticked, the BOM cost will be automatically updated based on Valuation Rate / Price List Rate / last purchase rate of raw materials.
