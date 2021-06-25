<!-- add-breadcrumbs -->
# Asset Repair

**Asset Repair refers to any activity carried to repair a broken Asset to restore full functionality.**

You can also maintain the records of Repair/Failures of Assets which are not listed in Asset Maintenance.

To access the Asset Repair list, go to:
> Home > Assets > Maintenance > Asset Repair

## 1. Prerequisites
Before creating and using Asset Repair, it is advised to create the following first:

* [Asset](/docs/v13/user/manual/en/asset/asset)

## 2. How to create an Asset Repair

1. Go to the Asset Repair list, click on New. 
1. Select the Asset. 

    Alternatively, you could open the record for the Asset in question and click on the **Repair Asset** button under **Manage**.
    <img class="screenshot" alt="Create Asset" src="{{docs_base_url}}/v13/assets/img/asset/create-asset-repair.png">

1. Select the Failure Date.
1. Enter the Repair Cost.
1. Save.
1. Change the Repair Status from 'Pending' to 'Completed', or 'Canceled'.
1. Select a Purchase Invoice if Repair Cost is greater than zero.
1. Save and Submit.

<img class="screenshot" alt="Asset Repair" src="{{docs_base_url}}/v13/assets/img/asset/asset-repair-basic.png">

### 2.1 Additional options when creating an Asset Repair 

* **Capitalize Repair Cost**: If checked, the Repair Cost will be added to the Asset's value. This could also allow you to increase the Asset's life.
* **Increase In Asset Life(Months)**: The number of months by which the Asset's life might be extended by the repair can be added here. This will modify the Depreciation Schedule of the Asset. This field will only be visible if Capitalize Repair Cost is checked.

<img class="screenshot" alt="Asset Repair with Capitalize Repair Cost checked" src="{{docs_base_url}}/v13/assets/img/asset/asset-repair-capitalize-repair-cost.png">

* **Stock Consumed During Repair**: Checking this will allow you to make a note of all the Stock Items consumed during the repair.
* **Warehouse**: The Warehouse from which the Stock Items consumed during the repair were taken should be entered here, if Stock Consumed During Repair is checked.
* **Stock Items**: Entering Stock Items consumed during the repair here will create a Stock Entry record of type Material Issue for them, thereby decreasing their quantity. GL Entries will also be created for each Item in the table. This table will only be visible if Stock Consumed During Repair is checked.

<img class="screenshot" alt="Asset Repair with Stock Consumed During Repair checked" src="{{docs_base_url}}/v13/assets/img/asset/asset-repair-stock-consumption.png">

* **Error Description**: A detailed descripton of the problem can be entered here.
* **Actions Performed**: A sequence of actions performed to carry out the repair can be noted down here.

<img class="screenshot" alt="Asset Repair Description section" src="{{docs_base_url}}/v13/assets/img/asset/asset-repair-description.png">

## 3. Features

### 3.1 Accounting Dimensions
Accounting Dimensions let you tag transactions based on a specific Territory, Branch, Customer, etc. This helps in viewing accounting statements separately based on the selected dimension(s). To know more, check help on [Accounting Dimensions](/docs/user/manual/en/accounts/accounting-dimensions) feature.

> Note: Project and Cost Center are treated as dimensions by default.

### 3.2 Purchase Invoice
A Purchase Invoice can be linked with the Asset Repair, to account for any Items that need to be purchased to carry out the repair or the repair service offered.

### 3.3 Total Repair Cost
If Stock Consumed During Repair is checked, the Total Repair Cost will be computed based on the value of the consumed Stock Items and the Repair Cost entered.


## 4. Related Topics
1. [Asset Maintenance](/docs/v13/user/manual/en/asset/asset-maintenance)
1. [Asset Value Adjustment](/docs/v13/user/manual/en/asset/asset-value-adjustment)

{next}