<!-- add-breadcrumbs -->
#Manufacturing Settings

Manufacturing Settings can be found at:

> Home > Manufacturing > Settings > Manufacturing Settings

<!-- <img class="screenshot" alt="Manufacturing Settings" src="{{docs_base_url}}/assets/img/manufacturing/manufacturing-settings-1.png">

## 1. Capacity and Planning
### Disable Capacity Planning and Time Tracking

As per Capacity Planning feature, when a [Work Order](/docs/user/manual/en/manufacturing/work-order) is created for an Item then a Time Log is created for each Operation. Based on actual Operation Time, Time Logs are updated. This also provides total Operations Cost against a specific Work Order.

If you don't track actual operations time, and want to disable the creation of Time Log based on Operations, tick the "Disable Capacity Planning and Time Tracking" checkbox in Manufacturing Settings.

### Allow Overtime

In the Workstation master, actual working hours are defined (say 10 pm to 6 pm). As per the Capacity Planning, Time Logs are created against Workstation, for tracking actual operations hour. It also considers working hours of a Workstation when scheduling a job (via Time Log). 

<img class="screenshot" alt="Manufacturing Settings" src="{{docs_base_url}}/assets/img/articles/manufacturing-settings-2.png">

As per the standard validation, if an operation cannot be completed within working hours of a Workstation, then the user is asked to divide the Operation into multiple smaller Operations. However, if the 'Allow Overtime' field is checked while creating Time Logs for an Operation, the working hours of Workstation will not be validated. In this case, Time Logs for the Operation will be created beyond working hours of the Workstation as well.

### Allow Production on Holidays

Holiday of a company can be recorded in the [Holiday List](/docs/user/manual/en/human-resources/) master. While scheduling production job on a workstation, the system doesn't consider a day listed in the Holiday list. If you want a production job to be scheduled on holidays as well, tick the 'Allow Production on Holidays' checkbox.

<img class="screenshot" alt="Manufacturing Settings" src="{{docs_base_url}}/assets/img/articles/manufacturing-settings-3.png">

### Capacity Planning For (Days)

Define no. of days for which the system will do production job allocation in advance.

### Time Between Operations (in mins)

The time gap between two production operations in minutes. The default is 10 minutes.
 -->

### Over Production Allowance Percentage

While making Work Orders against a Sales Order, the system will only allow production item quantity to be lesser than or equal to the quantity in the Sales Order. In case you wish to allow Work Orders to be raised with greater quantity, you can mention the Over Production Allowance Percentage here.

Example: In certain cases, a Workstation has to manufacture 100 units for cost effectiveness but the Work Order could be for 50 units. In this case, the Over Production Allowance Percentage would be 100.

### Back-flush Raw Materials Based On

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
