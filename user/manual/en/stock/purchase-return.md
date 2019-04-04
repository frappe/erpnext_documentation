<!-- add-breadcrumbs -->
# Purchase Return

ERPNext has an option for products that are need to be returned to the
supplier. This may be on account of a number of reasons like defects in goods,
quality not matching, the buyer not needing the stock, etc.

### 1. How to create a Purchase Return
A Purchase Return can be created by simply making a Purchase Receipt with negative quantity.

1. First open the original Purchase Receipt, against which supplier delivered the items.

    <img class="screenshot" alt="Original Purchase Receipt" src="{{docs_base_url}}/assets/img/stock/purchase-return-original-purchase-receipt.png">

1. Click on "Make Purchase Return", it will open a new Purchase Receipt with "Is Return" checked, items and taxes with negative amount.

    <img class="screenshot" alt="Return Against Purchase Receipt" src="{{docs_base_url}}/assets/img/stock/purchase-return-against-purchase-receipt.png">

On submission of Return Purchase Return, system will decrease item quantity from the mentioned warehouse. To maintain correct stock valuation, stock balance will also go up according to the original purchase rate of the returned items.

<img class="screenshot" alt="Return Stock Ledger" src="{{docs_base_url}}/assets/img/stock/purchase-return-stock-ledger.png">

If Perpetual Inventory enabled, system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.

<img class="screenshot" alt="Return Stock Ledger" src="{{docs_base_url}}/assets/img/stock/purchase-return-general-ledger.png">

#### 2. Related Topics
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Perpetual Inventory](/docs/user/manual/en/stock/perpetual-inventory)
1. [Sales Return](/docs/user/manual/en/stock/sales-return)