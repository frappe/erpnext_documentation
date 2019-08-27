<!-- add-breadcrumbs -->
# Item Alternative

**An Item Alternative is an Item similar to the original one and can be used instead of the original Item in manufacturing.**

If the raw material defined in the BOM is not available during the production process then their respective available alternative Item can be used to complete the production process.

First you need to enable the "Allow Alternative Item" in the Item.
<img class="screenshot" alt="Item" src="{{docs_base_url}}/assets/img/manufacturing/allow-alternative-item.png">

To access the Item alternative list, go to:
> Home > Stock > Items and Pricing > Item Alternative

This can also be done by clicking the plus sign next to 'Item Alternative' from the Item master dashboard.
You can enable Two-Way replacement between an Item and their alternative item if both can be used as an alternative to each other.

<img class="screenshot" alt="Item Alternative" src="{{docs_base_url}}/assets/img/manufacturing/item-alternative.png">

## 1. Prerequisites
Before creating and using an Item Alternative, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)

## 2. Item Alternative for Work Order

To allow to using alternative Items in the manufacturing process, the user can configure to 'Allow Alternative Item' in the BOM/Work Order

### 2.1 Provision to allow the alternative item in the BOM
You can enable 'Allow Alternative Item' in a BOM then select the alternative item in the Stock Entry. This can also be done with a Work Order.
<img class="screenshot" alt="Item" src="{{docs_base_url}}/assets/img/manufacturing/allow-alternative-item-bom.png">


### 2.2 Provision to Allow Alternative Item in the Work Order
User can also enable/disable allow alternative item for individual Work Orders.
<img class="screenshot" alt="Item" src="{{docs_base_url}}/assets/img/manufacturing/allow-alternative-item-wo.png">


Ticking on the 'Allow Alternative Item' checkbox will show a button named 'Alternate Item'. You can click on this to set the Item Alternative in the Work Order. This is how you use Item Alternative in a Work Order:
<img class="screenshot" alt="Item" src="{{docs_base_url}}/assets/img/manufacturing/work_order_item_alternative.gif">

This is how you use Item Alternative with a Stock Entry:
<img class="screenshot" alt="Item" src="{{docs_base_url}}/assets/img/manufacturing/se_item_alternative.gif">

If the 'Allow Alternative Item' checkbox in the Item table is disabled, you cannot set an Alternate Item for this Item.

### 2.3 Item Alternative for subcontract
In subcontract, the user has to transfer raw materials to the subcontracted supplier to get finished good from them. If the raw material is not available in the stock, with this feature, the user can transfer the alternate item of the subcontracted raw material to the supplier. This is done in the Stock Entry.

<img class="screenshot" alt="Item" src="{{docs_base_url}}/assets/img/manufacturing/purchase_order_item_alternative.gif">

After this, when you create a Purchase Receipt from the Work Order, the alternate item will be shown.

### 3. Related Topics
1. [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials)
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)

{next}