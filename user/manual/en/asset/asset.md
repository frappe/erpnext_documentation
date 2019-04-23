<!-- add-breadcrumbs -->
# What are Assets?

Asset record is the heart of fixed asset management feature. All the transactions related to an Asset like purchasing, sales, depreciation, scrapping, movement or maintenance will be managed against the Asset record.

### 1. How to create an Asset
Following are the steps to create an existing asset.

1. Before you can create an Asset, you need to create an Item with 'Is Fixed Asset' checkbox ticked.
1. An Asset Category needs to be assigned to that item.
1. Now, go to: **Assets > Asset > New**.
1. Enter a name for the asset.
1. Select the Item Code, the name and category will be fetched automatically.
1. Select who is the Asset Owner.
1. Select the Company/Supplier/Customer.
1. Select a location. Eg: Mumbai Office.
1. Enter the Purchase Date.
1. Enter the gross purchase amount.
1. Enter an Available-for-use Date to indicate the date from which the asset is available for use.
1. Tick the 'Is Existing Asset' checkbox.
1. Save and Submit. 

In case you're purchasing new assets, i.e., new items then assigning them as assets, you need not create an asset as shown in previous steps. When you're buying new assets, an asset ID is created when you make a Purchase Receipt. On submitting the Purchase Receipt for an Asset, you'll see a message like 'Asset AST00003 created'. This will happen only if you've ticked the 'Is Fixed Asset' checkbox when creating the item. An entry for an Asset will be created in Draft stage. You can then go to the Asset and submit it.

> Once you create an Asset, you'll see options to transfer, scrap, or sell the asset. From the Make button, you can adjust it's value and make a depreciation entry.

### 2. Types of Assets
There are two use cases for creating an asset record. The asset can be an existing asset which has been bought earlier and it might have already been depreciated partially. Or the asset is a newly purchased item.

#### 2.1 Existing Asset
For the existing asset, you can create the asset record directly checking "Is Existing Asset" field. In this case, you also need to enter already booked depreciation amount and number of booked depreciation. And based on the input, system will create a schedule for remaining depreciation.

<img class="screenshot" alt="Existing Asset" src="{{docs_base_url}}/assets/img/asset/existing-asset.png">

#### 2.2 New Asset
For new asset, you cannot create the asset record directly from Asset master. Asset record will be created automatically on submission of Purchase Receipt/Purchase Invoice for the Asset. And later you can modify the details of the asset record. Find more details in [Purchasing an Asset](/docs/user/manual/en/asset/purchasing-an-asset).

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset.png">

### 3. Features

### 3.1 The fields explained
1. **Item Code**: An Item for the Asset must be a non-stock item, with "Is Asset" field checked.

	<img class="screenshot" alt="Asset Item" src="{{docs_base_url}}/assets/img/asset/asset-item.png">
1. **Custodian**: The employee you're giving the asset to.
1. **Department**: The department of the Custodian.
3. **Is Existing Asset**: Check if you already have the asset, not purchased recently. The asset could also have been carried forward from the previous Fiscal Year. The existing assets which are partially/fully depreciated can also be created/maintained for the future reference.
7. **Depreciation Start Date**: The date from which booking of depreciation will be started.
8. **Expected Value After Useful Life**: Useful Life is the time period over in which the company expects that the asset will be productive. After that period, either the asset is scrapped or sold. In case it is sold, mention the estimated value here. This value is also known as Salvage Value, Scrap Value or Residual Value.
9. **Opening Accumulated Depreciation**: The accumulated depreciation amount which has already been booked for an existing asset.
10. **Available-for-use Date**: The date from which the asset can be used. The depreciation for the first period will be calculated from this date.
11. **Current Value (After Depreciation)**: In case you are creating record of an existing asset which has already been partially/fully depreciated, mention the current value of the asset. In case of new asset, mention the purchase amount or leave it blank.
12. **Depreciation Method**: There are two options**: Straight Line and Double Declining Balance.
	- **Straight Line**: This method spreads the cost of the fixed asset evenly over its useful life.
	- **Double Declining Method**: An accelerated method of depreciation, it results in higher depreciation expense in the earlier years of ownership.
13. **Total Number of Depreciations**: The total number of depreciations during the useful life. In case of existing assets which are partially depreciated, mention the number of pending depreciations.
14. **Number of Depreciations Booked**: Enter the number of already booked depreciations for an existing asset.
15. **Frequency of Depreciation (Months)**: The number of months between two depreciations.
16. **Next Depreciation Date**: Mention the next depreciation date, even if it is the first one. If the asset is an existing one and depreciation has already been completed, leave it blank.

#### 3.2 Asset Category

First step towards asset management, is creating Asset Category based on the type of assets. For example, all your desktops and laptops can be part of an Asset Category named "Electronic Equipments".

In Asset Category, you can set default depreciation method, periodicity and depreciation related accounts, which will be applicable to all the assets under the category.

<img class="screenshot" alt="Asset Category" src="{{docs_base_url}}/assets/img/asset/asset-category.png">

> **Note:** You can also set default depreciation related Accounts and Cost Centers in Company master.

#### 3.3 Asset Location

The assets that your organisation owns will be located at various facilities like administrative offices, manufacturing plants, warehouses etc. In ERPNext you can create a 'Location' for each of your facilities and track the assets which are present in these locations.

You can also add Latitude and Longitude of the location. When an asset is moved from one location to another you need to create an asset movement record.

Map of the location is also shown:

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset_location.png">

#### 3.4 Accounting Entry

On submission of an asset, "Capital Work in Progress" account will be credited and the asset account related to the asset will be debited. Submission is only possible after entering "Available-to-use Date". If "Available-to-use Date" is a future date, then accounting entry will be booked automatically on that date via scheduler.

#### 4.Related Topics
1. [Asset Maintenance](/docs/user/manual/en/asset/asset-maintenance)
1. [Asset Movement](/docs/user/manual/en/asset/asset-movement)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)