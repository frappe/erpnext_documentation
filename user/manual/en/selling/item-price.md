<!-- add-breadcrumbs -->
# Item Price

**Item Price is the record in which you can log the selling and buying rate of an item.**

## 1. How to create Item Price
1. There are two ways to reach a new Item Price form:

    **Selling/Buying/Stock > Items and Pricing > Item Price > New**.
 
    Or

    **Stock > Item > Click on "+" next to Item Price**.
1. Select the item, the name and description will be fetched.
1. Select the price list whether Selling or Buying price.
1. Enter the actual rate.
1. Save.

### 1.1 Select Price List

You can create multiple Price Lists in ERPNext to track Selling and Buying Price of an item separately. Also if item's selling prices change based on territory or due to other criteria, you can create multiple Selling Price Lists for it.

<img class="screenshot" alt="Item Price list" src="{{docs_base_url}}/assets/img/stock/item-price-1.png">

On selection of Price List, its currency and for selling or buying property will be fetched as well. To have Item Price fetching in the sales or purchase transaction, you should have Price List ID selected in the transaction under Currency and Price List. If you select a Selling Price list, a customer field will appear where you can assign this Item Price to a specific customer.

To check all Item Prices together, go to:

**Stock > Main Report > Itemwise Price List Rate**

## 2. Features
###2.1 Packing Unit
This is the quantity that must be bought or sold per unit of measure. For example if Packing Unit is two, and UOM is one, two items in quantity will be transacted. The default is 0, you can use non-integer UoM like 1.5Kg Oats for 1 Packing Unit. If you leave it as 0, it'll not affect any transaction.

###2.2 Minimum quantity
This is the minimum quantity of items to be transacted for this price to be applicable.

###2.3 Validity
There are two fields here—Valid From and Valid Upto. Valid from is set to the date you created the Price List, you can also set the Valid Upto date for when the Price List will expire.

###2.4 Lead Time in days
Approximate number of days it takes the product to reach the seller's warehouse. You can set different price lists based on how much time a the same product will reach you from different vendors.

###2.5 Note
You can add any note about the Item Price in this field.

Here is a video that shows how to manage item prices:

<div>
    <style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style>
    <div class='embed-container'>
        <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?start=193' frameborder='0' allowfullscreen>
        </iframe>
    </div>
</div>

### 2. Related Topics
1. [Item](/docs/user/manual/en/stock/item)
1. [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount)