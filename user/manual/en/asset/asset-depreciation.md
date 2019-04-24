
<!-- add breadcrumbs -->
# Asset Depreciation

The system automatically creates a schedule for depreciation based on depreciation method and other related inputs like Available to Use Date in the Asset record. It is also possible to create multiple depreciation schedules for different Finance Books. You need to tick the 'Calculate Depreciation' checkbox while creating an asset for calculating its depreciation and adding entries to the depreciation table in the Asset record.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/depreciation-schedule.png">

### 1. Scheduled depreciation
On the scheduled date, system creates depreciation entry by creating a Journal Entry and the same Journal Entry is updated in the depreciation table for reference. Next Depreciation Date and Current Value are also updated on submission of depreciation entry.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/depreciation-entry.png">

### 2. Accounting entries on depreciation
In the depreciation entry:

- "Accumulated Depreciation Account" is credited and
- "Depreciation Expense Account" is debited.

The related accounts can be set in the Asset Category or Company.

### 3. Automatic depreciation entries
You can enable booking of depreciation entry automatically from **Accounts > Setup > Account Settings**. This will create depreciation entry automatically on scheduled date via scheduler. Otherwise, you have to create Journal Entry manually by clicking "Make > Depreciation Entry" in corresponding Depreciation Schedule row.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/book-asset-depreciation-accounting-automatically.png">

The system will automatically set the fiscal year end date as the next depreciation date and calculate the depreciation amount pro rata temporis based on the Available-for-use Date (IFRS16).

<img class="screenshot" alt="Asset" src="/docs/assets/img/asset/asset_prorated_depreciation.png">

### 4. An example
For better understanding, net value of the asset on different depreciation dates are shown in a line graph.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-graph.png">

#### 5. Related Topics
1. [Asset Maintenance](/docs/user/manual/en/asset/asset-maintenance)
1. [Asset Value Adjustment](/docs/user/manual/en/asset/asset-value-adjustment)
1. [Scrapping an Asset](/docs/user/manual/en/asset/scrapping-an-asset)
