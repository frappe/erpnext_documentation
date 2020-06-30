<!-- add-breadcrumbs -->

# How is Valuation Rate of Serialised Item calculated in ERPNext?

In ERPNext, Item's Valuation Rate is updated based on the following transaction:

1.  **Purchase Receipt**
    
2.  **Stock Entry of type Material Receipt**
    
3.  **Stock Reconciliation made for updating the stock’s opening balance**

ERPNext supports two valuation methods: **FIFO** & **Moving Average**.

*Learn more about the working of these methods [here.](https://erpnext.com/docs/user/manual/en/stock/articles/item-valuation-fifo-and-moving-average)*

You can select a valuation method based on which item's value will be calculated. It can be set as per individual item as well as globally for all the items from Stock Settings.

<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/stock-settings-1.png">

Item valuation rates are calculated as per the valuation method set for them. 

However, in the case of serialized Item, these settings are ignored. The Item, "*Macbook Pro*" is a serialized Item and its valuation rate is not fetched from Item master, instead, the valuation rate is updated from the first incoming stock entry rate, Rs.199.80. Consequently, it is updated as per the other transactions carried out on this Item.  

**In Item Master:**
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/serail-no-enabled.png">
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/valuation-rate-1.png">

**In Stock Ledger:**
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/stock-ledger-2.png">

To learn more about **ERPNext's Stock module**, [click here](https://erpnext.com/docs/user/manual/en/stock)