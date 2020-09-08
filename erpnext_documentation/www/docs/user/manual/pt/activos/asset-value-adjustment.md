<!-- add breadcrumbs -->
# Asset Value Adjustment

**If the value of an Asset changed suddenly due to any damages, it can be recorded using Asset Value Adjustment.**

In case of fixed asset management, sometimes the value of an asset needs some adjustment. For example, if a laptop gets damaged for some reason, and its value will be dropped instantly. And in that case, we have to readjust the value of the asset.

To access the Asset Value Adjustment, go to:
> Home > Assets > Maintenance > Asset Value Adjustment

## 1. Prerequisites
Before creating and using Asset Value Adjustment, it is advised to create the following first:

1. [Asset](/docs/user/manual/en/asset/asset)
1. Enable 'Calculate Depreciation' in the Asset form

## 2. How to create an Asset Value Adjustment

1. Go to the Asset Value Adjustment list, click on New.
1. Select an Asset whose value is to be adjusted.
1. Select a date.
1. Enter the current and new value of the asset.
1. Save and Submit.
    <img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-value-adjustment.png">


On saving the system will book a "Gain/Loss on asset revaluation" and adjust the valuation of the asset.
You can change the cost center and add a finance book.

On submitting, a Journal Entry is created under the 'Accumulated Depreciations' account.

### 3. Related Topics
1. [Asset Depreciation](/docs/user/manual/en/asset/asset-depreciation)
1. [Scrapping an Asset](/docs/user/manual/en/asset/scrapping-an-asset)
