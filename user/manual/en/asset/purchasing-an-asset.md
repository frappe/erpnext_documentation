# Purchasing an Asset

For purchasing a new asset:

1. Create an Asset Category
1. Create an related Item with 'Is Fixed Asset' enabled for creating the asset.
1. You may also enable 'Auto Create Assets on Purchase' for creating assets automatically. (Optional)

  <img class="screenshot" alt="Purchasing Asset" src="{{docs_base_url}}/assets/img/asset/asset-purchase-receipt.png">

1. Then, the [purchase cycle](/docs/user/manual/en/buying/purchase-order) should be followed for purchasing an asset.
1. Enter the Asset Location in the Items table of the [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt) or [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice) through which you are receiving the item.
1. On submission of a Purchase Receipt, based on auto creation checkbox, Asset records will be created automatically. You can then enter other details of the Asset manually from the Asset form.

<img class="screenshot" alt="Purchasing Asset" src="{{docs_base_url}}/assets/img/asset/asset-purchase-receipt.png">

Following accounting entries will be posted on submission of the Receipt entry if Capital Work In Progress Accounting is enabled in the Asset Category of the purchased asset.

<img class="screenshot" alt="Asset" src="{{docs_base_url}}/assets/img/asset/asset-purchase-receipt-gl-entries.png">

It is noticeable here that, instead of corresponding asset account, Capital Work in Progress (CWIP) has been debited. It is because, asset has been just purchased and it is still not available for use. Until the asset is available for use, the asset value maintained against this account. On the day when it is available for use, the CWIP account gets credited and corresponding asset account gets debited.

In case of disabled 'Capital Work In Progress Accounting' in the Asset Category, the receipt entry will be made against corresponding asset accounts set in the Asset Category.

ERPNext also uses a temporary account "Asset Received But Not Billed" (a liability account) which gets credited on submission of Purchase Receipt entry. Later, on submission of Purchase Invoice, this account gets debited/reversed.

#### Related Topics
1. [Asset](/docs/user/manual/en/asset/asset)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
