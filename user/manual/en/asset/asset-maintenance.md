<!-- add-breadcrumbs -->
# Asset Maintenance
ERPNext provides features to track the details of individual maintenance/calibration tasks for an asset by date, the person responsible for the maintenance and future maintenance due date.

To perform Asset Maintenance in ERPNext:

  1. Enable Asset Maintenance from the Asset master.
  2. Create Asset Maintenance Team.
  3. Create Asset Maintenance.
  4. Create Asset Maintenance Log.
  5. Create Asset Repair Log.

### 1. Enable Asset Maintenance
Go to an Asset master and check the 'Maintenance Required' checkbox in Asset to enable Asset Maintenance.
<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/maintenance_required.png">

### 2. Asset Maintenance Team
Create Asset Maintenance Team.

1. Go to: **Asset > Maintenance > Asset Maintenance Team > New**.
1. Enter a name for the team.
1. Select a manager for the team.
1. Add the team members in the table and select their maintenance roles.
1. Save.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset_maintenance_team.png">


### 3. Asset Maintenance
For each asset create an Asset Maintenance record listing all the associated maintenance tasks, maintenance type (Preventive Maintenance or Calibration), periodicity, assign to and start and end date of maintenance. Based on start date and periodicity the next due date is auto-calculated and a ToDo is created for the Assignee.

1. Go to: **Asset > Maintenance > Asset Maintenance > New**.
1. Select the Asset.
1. Select the Maintenance Team.
1. Add Maintenance Tasks in the table. 
1. Select a period of time for which the task needs to be carried out.
1. Set a start and end date.
1. Save.
1. After saving, you can assign the task to a user.
<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset_maintenance.png">

### 4. Asset Maintenance Log
For each task in Asset Maintenance, Asset Maintenance Log is auto created to keep track of the upcoming Maintenances. It will have status, completion date and actions performed. Based on completion date here, next due date is calculated automatically and new Asset Maintenance Log is created. You can access it from **Asset > Maintenance > Asset Maintenance Log**.
<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset_maintenance_log.png">

### 5. Asset Repair
You can also maintain the records of Repair/Failures of your asset which are not listed in Asset Maintenance.

1. Go to: **Asset > Maintenance > Asset Repair**.
1. Select the asset.
1. Select the failure date.
1. Enter an error description.
1. You can also assign it to someone if to be repaired.
1. Add actions performed if repaired, enter the Repair Cost.
1. Change the Repair Status as applicable.
1. Save and Submit.
<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset_repair.png">

#### 6. Related Topics
1. [Asset Value Adjustment](/docs/user/manual/en/asset/asset-value-adjustment)
1. [Asset Depreciation](/docs/user/manual/en/asset/asset-depreciation)
1. [Scrapping an Asset](/docs/user/manual/en/asset/scrapping-an-asset)
