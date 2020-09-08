<!-- add-breadcrumbs -->
# Asset Maintenance

**Asset Maintenance refers to any activity done on Assets to maintain their performance or condition.**

ERPNext provides features to track the details of individual maintenance/calibration tasks for an asset by date, the person responsible for the maintenance, and future maintenance due date.

To perform Asset Maintenance in ERPNext:

1. Enable 'Maintenance Required' from the Asset master.
2. Create an Asset Maintenance Team.
3. Create the Asset Maintenance.
4. An Asset Maintenance Log is created.
5. Create Asset Repair Log.

To access the Asset Maintenance list, go to:
> Home > Asset > Maintenance > Asset Maintenance

## 1. Prerequisites
Before creating and using Asset Maintenance, it is advised to create the following first:


1. [Asset](/docs/user/manual/en/asset/asset)
1. Go to an Asset master and check the 'Maintenance Required' checkbox in Asset to enable Asset Maintenance.
<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/maintenance_required.png">
1. [Asset Maintenance Team](/docs/user/manual/en/asset/asset-maintenance-team)

## 2. How to create Asset Maintenance
For each asset, create an Asset Maintenance record listing all the associated maintenance tasks, maintenance type (Preventive Maintenance or Calibration), periodicity, assign to and start and end date of maintenance. Based on start date and periodicity the next due date is auto-calculated and a ToDo is created for the Assignee.

1. Go to the Asset Maintenance list, click on New.
1. Select the Asset.
1. Select the Asset Maintenance Team.
1. Add Maintenance Tasks in the table.
  1. Set the Maintenance Status whether 'Planned', 'Overdue', or 'Canceled'.
  1. Select a periodicity for which the task needs to be carried out. The next due date will be calculated.
1. Save.
1. After saving, you can assign the task to a user.
  <img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset_maintenance.png">

If the Item is serialized, the Serial Number can be entered.

## 3. Features
### 3.1 Maintenance Tasks

* **Maintenance Type**: Whether this is a 'Preventive' maintenance activity or 'Calibration' to restore accurate functioning.
* **Start and End Date**: Set the start date and end date when the maintenance is supposed to begin and end.
* **Last Completion Date**: If the maintenance was not carried out on or before the scheduled date, the actual date of maintenance can be recorded here.

### 3.2 Asset Maintenance in ToDo

On assigning the maintenance to a user, it will appear in the User's ToDo list.

![Asset Maintenance](/docs/assets/img/asset/asset-maintenance-todo.png)


## 4. Related Topics
1. [Asset Value Adjustment](/docs/user/manual/en/asset/asset-value-adjustment)
1. [Asset Depreciation](/docs/user/manual/en/asset/asset-depreciation)
1. [Scrapping an Asset](/docs/user/manual/en/asset/scrapping-an-asset)
