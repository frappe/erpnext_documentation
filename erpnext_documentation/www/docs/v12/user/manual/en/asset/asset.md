<!-- add-breadcrumbs -->
# Assets

**An Asset is any valuable Item owned by a Company.**

Examples of Assets include furniture, computers, mobile phones, printers, cars, etc. Assets may be leased to be used by the employees of a Company.

In ERPNext, the Asset record is the heart of fixed asset management. All the transactions related to an Asset like purchasing, sales, depreciation, scrapping, movement, or maintenance will be managed against the Asset record.

To access the Asset list, go to:
> Home > Assets > Assets > Asset

## 1. Prerequisites
Before creating and using Asset, it is advised to create the following first:

* [Item](/docs/user/manual/en/stock/item) with 'Is fixed Asset' enabled
* [Asset Category](/docs/user/manual/en/asset/asset-category)

## 2. Types of Assets
Before creating an Asset, the types of Assets in ERPNext need to be understood.

There are two use cases for creating an asset record. The asset can be an existing asset which has been bought earlier and it might have already been depreciated partially. Or the asset is a newly purchased item.

### 2.1 Existing Asset
For an existing asset, you can create the asset record directly checking "Is Existing Asset" field. In this case, you also need to enter already booked depreciation amount and number of booked depreciation. And based on the input, the system will create a schedule for remaining depreciation.

<img class="screenshot" alt="Existing Asset" src="{{docs_base_url}}/assets/img/asset/existing-asset.png">

### 2.2 New Asset

For new assets, you cannot create the asset record directly from the Asset form. You need to create a Purchase Receipt/Invoice for it.

When you're buying new assets, an asset ID is created when you make a Purchase Receipt. On submitting the Purchase Receipt for an Asset, you'll see a message like 'Asset AST00003 created'. This will happen only if you've ticked the 'Is Fixed Asset' checkbox when creating the Item.

When you're buying new assets, assets can be created automatically when you make a Purchase Receipt, if you have 'Auto Create Assets on Purchase' ticked in the Item master of the Asset. On submitting the Purchase Receipt for an Asset, you'll see a message like '5 Assets created for Office Phone'. If you don't want to auto create assets, after Purchase Receipt submission you will have to manually create assets and link the Purchase Receipt to the Asset.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset.png">

After submitting a Purchase Receipt/Invoice for such an Item, in case of asset auto creation, a number of Asset records will be created in the Draft stage. You can then go to these Assets and submit them.

To know more, visit the [Purchasing an Asset](/docs/user/manual/en/asset/purchasing-an-asset) page.

## 3. How to manually create an Asset

Before you can create an Asset, you need to create an Item with 'Is Fixed Asset' checkbox ticked and create a Purchase Receipt/Invoice against that Item. Note that you will have to create a number of Assets based on the quantity specified in the Purchase Document.

An Asset Category needs to be assigned to that Item. Now the Asset can be created.

1. Go to the Assets list, click on New.
1. Enter a name for the asset.
1. Select the Item Code, the Item Name and Asset Category will be fetched automatically.
1. Select who is the Asset Owner, i.e. Company, Supplier, or Customer.
1. Select the Company/Supplier/Customer.
1. Select the Purchase Receipt/Invoice. Purchase Date and Gross Purchase Amount will be fetched automatically.
1. Select a Location. Eg: Mumbai Office. This will be fetched automatically if specified in Purchase Receipt items table
1. Enter an Available for use Date to set the date from which the Asset is available for use. The depreciation amount for the first period will be calculated from this date.
1. Tick the 'Is Existing Asset' checkbox if you're recording an existing Asset.
1. Save and Submit. 

### 3.1 Additional options when creating an Asset

1. **Item Code**: An Item for the Asset must be a non-stock item, with "Is Asset" field checked.
    <img class="screenshot" alt="Asset Item" src="{{docs_base_url}}/assets/img/asset/asset-item.png">
1. **Custodian**: The employee you're giving/assigning the asset to.
1. **Department**: The department of the Custodian.
1. **Is Existing Asset**: Check if you already own the asset, not purchased recently. The asset could also have been carried forward from the previous Fiscal Year. The existing assets which are partially/fully depreciated can also be created/maintained for future reference.
1. **Opening Accumulated Depreciation**: The accumulated depreciation amount which has already been booked for an existing asset.
1. **Number of Depreciations Booked**: Enter the number of already booked depreciations for an existing asset.
1. **Current Value (After Depreciation)**: In case you are creating a record of an existing asset which has already been partially/fully depreciated, mention the current value of the asset. In case of a new asset, mention the purchase amount or leave it blank.
1. **Next Depreciation Date**: Mention the next depreciation date, even if it is the first one. If the asset is an existing one and depreciation has already been completed, leave it blank.
1. **Calculate Depreciation**: Enable this checkbox to calculate depreciation of Assets.
1. **Allow Monthly Depreciation**: Enable this checkbox to distribute depreciation amount of an asset into 12 months of the year. Depreciation entries will be made every month on the date provided as Depreciation Start Date. For example, if Available for Use date is 22nd Nov 2019 and depreciation Start Date is 31st March 2020, first depreciation will be done on 30th Nov 2019 second on 31st Dec 2019 and so on. Amount will be distributed based on days left until next depreciation. 

## 4. Features

### 4.1 Depreciation

* **Frequency of Depreciation (Months)**: The number of months between depreciations.
* **Total Number of Depreciations**: The total number of depreciations during the useful life of the Asset. In case of existing assets which are partially depreciated, mention the number of pending depreciations. For example, if you set frequency as 12 months and no. of depreciations as 3, 1 depreciation will be booked every 12 months for 3 years.
* **Depreciation Method**: There are two options, Straight Line and Double Declining Balance.
    - **Straight Line**: This method spreads the cost of the fixed asset evenly over its useful life.
    - **Double Declining Method**: An accelerated method of depreciation, it results in higher depreciation expense in the earlier years of ownership.
    - **Written Down Value**: In this method, the depreciation percentage is fixed but it is applied on the current value of the asset which we get after each depreciation.
    To know about Asset Depreciation in detail, [visit this page](/docs/user/manual/en/asset/asset-depreciation).
* **Depreciation Start Date**: The date from which booking of depreciation will be started.
* **Expected Value After Useful Life**: Useful Life is the time period over in which the company expects that the asset will be productive. After that period, either the asset is scrapped or sold. In case it is sold, mention the estimated value here. This value is also known as Salvage Value, Scrap Value, or Residual Value.
* **Rate of Depreciation**: This will be calculated based on the amount entered in expected value after useful life.


### 4.2 Depreciation Schedule

On booking depreciations against this Asset, the Depreciation Schedule section will be visible.
This table has columns for Finance Book, Schedule Date, Depreciation Amount, Amount Deprecated, and Journal Entry.

![Depreciation Schedule](/docs/assets/img/asset/asset-depreciation.png)

### 4.3 Insurance Details
If Insurance has been taken for the Asset you're recording, you can store the following Insurance details:

* Policy number
* Insurer
* Insured value
* Insurance Start Date
* Insurance End Date
* Comprehensive Insurance

### 4.4 Accounting Entries
On submission of an asset, "Capital Work in Progress" account will be credited and the asset account related to the asset will be debited. Submission is only possible after entering "Available-to-use Date". If "Available-to-use Date" is a future date, then accounting entry will be booked automatically on that date via the scheduler.

### 4.5 Maintenance
Ticking on Maintenance Required allows recording Asset Maintenance entries for this Asset. To know more, visit the [Asset Maintenance](/docs/user/manual/en/asset/asset-maintenance) page.

### 4.6 After Submitting
Once you create an Asset, you'll see options to transfer, scrap, or sell the asset. From the Make button, you can adjust its value and make a depreciation entry.

![Asset Submit](/docs/assets/img/asset/asset-submit.png)

### 5. Related Topics
1. [Asset Maintenance](/docs/user/manual/en/asset/asset-maintenance)
1. [Asset Movement](/docs/user/manual/en/asset/asset-movement)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
