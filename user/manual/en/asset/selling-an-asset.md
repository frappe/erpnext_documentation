<!-- add breadcrumbs -->
# Selling an Asset

To sell an asset, open the asset record and clicking on the "Sell Asset" button. This will lead you to a [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice). Enter details like Customer, Payment Due Date, and Debit To account in the Sales invoice and submit it.

On submission of the Sales Invoice, following accounting entries will take place:

- "Receivable Account" (Debtors) will be debited by the sales amount.
- "Fixed Asset Account" will be credited by the purchase amount of asset.
- "Accumulated Depreciation Account" will be debited by the total depreciated amount till now.
- "Gain/Loss Account on Asset Disposal" will be credited/debited based on gain/loss amount. The Gain/Loss account can be set in Company record.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-sales.png">

#### Related Topics
1. [Asset Value Adjustment](/docs/user/manual/en/asset/asset-value-adjustment)
1. [Purchasing an Asset](/docs/user/manual/en/asset/purchasing-an-asset) 
