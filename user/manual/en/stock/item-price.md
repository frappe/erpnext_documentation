<!-- add-breadcrumbs -->
# Item Price

Item Price is the record in which you can log selling and buying rate of an item.

### 1. How to set Item Price

There are two ways to reach to new Item Price form.

1. **Selling/Buying/Stock > Items and Pricing > Item Price > New**.
2. Enter the price list whether its the standard selling or buying rate.
3. Enter the actual price rate.
4. Save.

Or

1. **Selling/Buying/Stock > Items and Pricing > Item > Select the Item > Item Price**.
2. Click on the item and change the price or create a new item price as above.

### 2. How to create a new Price List.

1. Go to **Selling/Buying/Stock > Items and Pricing > Price List**. You can create multiple Price List in ERPNext to track Selling and Buying Price List of an item separtely. Also if item's selling prices id changing based on territory, or due to other criteria, you can create multiple selling Price List for it.

    ![Item Price list]({{docs_base_url}}/assets/img/stock/item-price-1.png)

    On selection of Price List, its currency and for selling or buying property will be fetched as well. To have Item Price fetching in the sales or purchase transaction, you should have Price List id selected in the transaction, just above Item table.

2. Select Item. Select item for which Item Price record is to be created. On selection of Item Code, Item Name and Description will be fetched as well.

    ![Item Price Item]({{docs_base_url}}/assets/img/stock/item-price-2.png)

3. Enter Rate. Enter selling/buying rate of an item in Price List currency.

    ![Item Price Rate]({{docs_base_url}}/assets/img/stock/item-price-3.png)

4. Save Item Price. To check all Item Price together, go to:

    **Stock > Analytics > Item-wise Price List Rate**

You will find option to create new Item Price record (+) in this report as well.

<div>
    <div class="embed-container">
        <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?start=193' frameborder='0' frameborder='0' allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

#### 3. Related Topics
1. [Item Valuation Transactions](/docs/user/manual/en/stock/articles/item-valuation-transactions)
1. [Item Warranty](/docs/user/manual/en/stock/item-warranty)
