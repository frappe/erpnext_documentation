<!-- add breadcrumbs -->
# Asset Depreciation

The system automatically creates a schedule for depreciation based on depreciation method and other related inputs like 'Available to Use Date' in the Asset record. It is also possible to create multiple depreciation schedules for different Finance Books. You need to tick the 'Calculate Depreciation' checkbox while creating an asset for calculating its depreciation and adding entries to the depreciation table in the Asset record.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/depreciation-schedule.png">

Types of depreciations in ERPNext:

* **Straight line**: The depreciation is calculate in a straight line and is _distributed evenly_ over the selected frequency in months. For example, current asset value is 1000, post depreciation value is 500 after 5 years, straight line would set 100 as depreciated amount for each year. This method is useful when there is no particular pattern to how the depreciation takes place over a period of time.

* **Double Declining Balance**: This is also known as 200% declining balance. In this method, 20% is depreciated from the existing value each time. For example, if asset is worth 1000, it'll be worth 800 in the next period, then 20% of 800 would be 160 so now the asset is worth 640, and so on till the end value is reached. If you start at the middle of the year, 10% depreciation will be calculated. This method is useful when the asset depreciates fast in the beginning and slows down later.

* **Written Down Value**: A fixed depreciation percentage is set and the asset value depreciates by that percentage over lifespan of the asset. This fixed percentage is always calculated on the current existing value of the asset. For example if the value is 1000 and 'Written Down Value' is 10% over 5 years, 10% will be depreciated every year to get the expected value of 600 at the end of life. Useful for vehicles where the depreciation is higher in later years.

    | Current Value | Depreciation | Booked Value |
    | -------------- | ----------- | ------------ |
    | 1000 | 100 | 900 |
    | 900 | 90 | 810 |
    | 810 | 80 | 730 |
    | 730 | 70 | 660 |
    | 660 | 60 | 600 |
    | 600 | 50 | 550 |


* **Manual**: In this method, you can define the Schedule Date and Depreciation Amount for each period. 

## 1. Scheduled depreciation
On the scheduled date, system creates a depreciation entry by creating a Journal Entry and the same Journal Entry is shown in the depreciation table for reference. Next Depreciation Date and Current Value are also updated on submission of depreciation entry.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/depreciation-entry.png">

## 2. Accounting entries on depreciation
In the depreciation entry:

- "Accumulated Depreciation Account" is credited and
- "Depreciation Expense Account" is debited.

The related accounts can be set in the Asset Category or Company.

## 3. Automatic depreciation entries
You can enable booking of depreciation entry automatically from [Accounts Settings](/docs/user/manual/en/accounts/accounts-settings). This will create depreciation entry automatically on scheduled date via scheduler. Otherwise, you have to create Journal Entry manually by clicking "Make > Depreciation Entry" in corresponding Depreciation Schedule row.

The system will automatically set the Fiscal Year end date as the next depreciation date and calculate the depreciation amount *pro rata temporis* based on the Available-for-use Date (IFRS16).

<img class="screenshot" alt="Asset" src="/docs/assets/img/asset/asset_prorated_depreciation.png">

## 4. An example
For better understanding, net value of the asset on different depreciation dates are shown in a line graph.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-graph.png">

### 5. Related Topics
1. [Asset Maintenance](/docs/user/manual/en/asset/asset-maintenance)
1. [Asset Value Adjustment](/docs/user/manual/en/asset/asset-value-adjustment)
1. [Scrapping an Asset](/docs/user/manual/en/asset/scrapping-an-asset)
