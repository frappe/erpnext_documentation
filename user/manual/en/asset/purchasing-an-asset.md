# Purchasing an Asset

For purchasing a new asset, first you have to create Asset Category and related Item record for the asset. Then the normal purchase cycle should be followed for purchasing an asset. In [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt) or [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice) through which you are receiving the item, you have to enter "Asset Location". And on submission of a Purchase Receipt, an asset record will be created automatically. You can then enter other details of the asset manually from the Asset record.

<img class="screenshot" alt="Purchasing Asset" src="{{docs_base_url}}/assets/img/asset/asset-purchase-receipt.png">

Following accounting entries will be posted on submission of the Receipt entry.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-purchase-receipt-gl-entries.png">

It is noticeable here that, instead of corresponding asset account, Capital Work in Progress (CWIP) has been debited. It is because, asset has been just purchased and it is still not available for use. Until the asset is available for use, the asset value maintained against this account. On the day when it is available for use, the CWIP account gets credited and corresponding asset account gets debited.

We also use a temporary account "Asset Received But Not Billed" (a liability account) which gets credited on submission of Purchase Receipt entry. Later, on submission of Purchase Invoice, this account gets debited / reversed.

#### Related Topics
1. [Asset](/docs/user/manual/en/asset/asset)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)