 <!-- add-breadcrumbs -->
# Asset Category

**An Asset Category classifies different assets of a Company.**

The first step towards asset management is creating an Asset Category based on the type of assets. For example, all your desktops and laptops can be part of an Asset Category named "Electronic Equipments".

In Asset Category, you can set default a depreciation method, periodicity and depreciation related accounts, which will apply to all the assets under the category.

> **Note:** You can also set default depreciation-related Accounts and Cost Centers in Company master.

To access the Asset Category list, go to:
> Home > Asset > Assets > Asset Category

## 1. How to create an Asset Category
1. Enter a name for the Asset Category.
1. Check 'Enable Capital Work in Progress Accounting' if you want to maintain records of assets under a temporary balance sheet account instead of the corresponding asset account. To know more, [visit this page](/docs/user/manual/en/asset/purchasing-an-asset).
1. Save.

    ![Asset Category](/docs/assets/img/asset/asset-category.png)

### 1.1 Additional options when creating an Asset Category
1. **Enable Capital Work in Progress Accounting**: On enabling this, accounting entry for assets under this category which are not in use are posted in the Capital Work in Progress accounts. This happens when you own the Asset but it isn't being used yet, i.e. 'Available for Use Date' is set at a later date. If you use all your assets immediately, disable this feature. On disabling this, CWIP accounting will be skipped.

## 2. Features
### 2.1 Finance Book details
You can link a Finance Book if you report depreciation in different ways. You can enter the following fields:

* **Depreciation Method**: Choose a depreciated method on which you'll record the depreciation of assets in this category. To know more, [visit this page](/docs/user/manual/en/asset/asset-depreciation).
* **Frequency of Depreciation (Months)**: The number of months within which the depreciation will be booked. The asset may be scrapped after this period.
* **Total Number of Depreciations**: The number of deprecations to be booked in the selected time frame.
* **Rate of Depreciation**: The rate of deprecation applied over the selected period. This will be calculated based on the Depreciation Method selected.

### 2.2 Accounting Details

The following account details can be set to record asset values in the ledger: 

* Company
* Fixed Asset Account
* Accumulated Depreciation Account
* Depreciation Expense Account
* Capital Work In Progress Account

## 3. Related Topics
1. [Asset](/docs/user/manual/en/asset/asset)
