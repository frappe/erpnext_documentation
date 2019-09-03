<!-- add-breadcrumbs -->
# Sales Return

**A sold Item being returned is known as a Sales Return.**

Goods sold being returned happens commonly in business. They could be returned by the customer due to quality issues, non-delivery on the agreed date, or any other reason. 

## 1. Prerequisites
Before creating and using a Sales Return, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)
* [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
    
    Or

    [Delivery Note](/docs/user/manual/en/stock/delivery-note)

## 2. How to create a Sales Return

1. First open the original Delivery Note / Sales Invoice, against which Customer returned the Items.

    <img class="screenshot" alt="Original Delivery Note" src="{{docs_base_url}}/assets/img/stock/sales-return-original-delivery-note.png">

1. Then click on 'Create > Sales Return', it will open a new Delivery Note with 'Is Return' checked, Items, Rate, and taxes will negative numbers.

    <img class="screenshot" alt="Return Against Delivery Note" src="{{docs_base_url}}/assets/img/stock/sales-return-against-delivery-note.png">

1. You can also create the return entry against the original Sales Invoice, to return stock along with credit note, check "Update Stock" option in Return Sales Invoice.

    <img class="screenshot" alt="Return Against Sales Invoice" src="{{docs_base_url}}/assets/img/stock/sales-return-against-sales-invoice.png">

1. On submission of Return Delivery Note / Sales Invoice, the system will increase stock balance in the mentioned Warehouse. To maintain correct stock valuation, stock balance will go up according to the original purchase rate of the returned items.

    <img class="screenshot" alt="Return Stock Ledger" src="{{docs_base_url}}/assets/img/stock/sales-return-stock-ledger.png">

1. In case of Return Sales Invoice, Customer account will be credited and associated income and tax account will be debited as shown in the Accounting Ledger.

    <img class="screenshot" alt="Return Stock Ledger" src="{{docs_base_url}}/assets/img/stock/sales-return-general-ledger.png">

If Perpetual Inventory is enabled, the system will also post accounting entry against warehouse account to sync warehouse account balance with stock balance as per Stock Ledger.

## 3. Related Topics
1. [Purchase Return](/docs/user/manual/en/stock/purchase-return)
1. [Perpetual Inventory](/docs/user/manual/en/stock/perpetual-inventory)
