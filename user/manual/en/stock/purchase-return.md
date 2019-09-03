<!-- add-breadcrumbs -->
# Purchase Return

**A purchased Item being returned is known as a Purchase Return.**

With the Purchase Return feature, you can return products to the
Supplier. This may be on account of a number of reasons like defects in goods,
quality not matching, the buyer not needing the stock, etc.

## 1. Prerequisites
Before creating and using a Purchase Return, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)
* [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
    
    Or

    [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)


## 1. How to create a Purchase Return
1. First open the original Purchase Receipt, against which supplier delivered the Items.

    <img class="screenshot" alt="Original Purchase Receipt" src="{{docs_base_url}}/assets/img/stock/purchase-return-original-purchase-receipt.png">

1. Click on 'Create > Return', it will open a new Purchase Receipt with 'Is Return' checked. Items, Rate, and taxes will negative numbers.

    <img class="screenshot" alt="Return Against Purchase Receipt" src="{{docs_base_url}}/assets/img/stock/purchase-return-against-purchase-receipt.png">

1. On submission of Return Purchase Return, the system will decrease item quantity from the mentioned Warehouse. To maintain correct stock valuation, stock balance will also go up according to the original purchase rate of the returned items.

    <img class="screenshot" alt="Return Stock Ledger" src="{{docs_base_url}}/assets/img/stock/purchase-return-stock-ledger.png">

1. In the Accounting Ledger, the Stock In Hand account will be credited and the Stock Received but Not Billed account will be debited.

    <img class="screenshot" alt="Return Stock Ledger" src="{{docs_base_url}}/assets/img/stock/purchase-return-general-ledger.png">

If Perpetual Inventory enabled, the system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.

### 2. Related Topics
1. [Sales Return](/docs/user/manual/en/stock/sales-return)
1. [Perpetual Inventory](/docs/user/manual/en/stock/perpetual-inventory)
