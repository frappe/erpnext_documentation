<!-- add-breadcrumbs -->
#Product Bundle

Product Bundle can be seen as something like a "Bill-of-Material" on the Sales side. It's a master where you can list existing items which are bundled together and sold as a set (or bundle). For instance, when you sell a laptop, you need to ensure that charger, mouse and laptop bag are delivered with it and stock levels of these items get affected. 
To address this scenario, you can set create a Product Bundle for the main item, i.e. laptop, and list deliverable items i.e. laptop + charger + mouse + laptop bag as so-called "Child Items".
  
Following are the steps on how to setup Product Bundle master, and how is it used in the sales transactions.

### 1. How to create a Product Bundle
1. Go to: **Selling > Items and Pricing > Product Bundle > New**.
2. Enter Parent Item, create one if not already created. Make sure Maintain Stock in unchecked when creating a Parent Item.
3. Enter the products to be bundled in the Items table and enter their quantities.
4. Save.
<img class="screenshot" alt="Product Bundle" src="{{docs_base_url}}/assets/img/selling/product-bundle.png">

#### 1.1 Selecting Parent Item

In Product Bundle master, there are two sections. The "Parent Item" and a List of items to be shipped (Child Items).

The "Parent Item" must be a so called <b>non-stock item</b>. The "Parent Item" is to be seen more like a vessel or virtual item and not a physical product.
To create a <b>non-stock item</b> you have to unmark "Maintain Stock" in the Item Form.
This is non-stock item because there is no stock maintained for it but only for the "Child Items". 
If you want to maintain stock for the Parent Item, then you must create a regular Bill of Material (BOM) 
and package them using a Stock Entry Transactions.

#### 1.2 Selecting Child Items

In Package Item section, you will list all the child items for which we maintain stock and is delivered to customer.
Remember: The "Parent Item" is just virtual, so your main product (a laptop in our example here) also has to be listed on the List of Child (or Package) Items

### 2. Features
#### 2.1 Product Bundle in the Sales Transactions

When making Sales transactions (Sales Invoice, Sales Order, Delivery Note) 
the Parent Item will be selected in the main item table.

<img class="screenshot" alt="Product Bundle" src="{{docs_base_url}}/assets/img/selling/product-bundle.gif">

On selection of a Parent Item in the main item table, its child items will be fetched in Packing List 
table of the transaction. If child item is the serialized item, you will be able to specify its Serial Mo. 
in packing List table itself. On submission of transaction, system will reduce the stock level of child items from 
warehouse specified in Packing List table.

<div class="well"><b>Use Product Bundle to Manage Schemes:</b>
<br>
This work-around in Product Bundle was discovered when a customer dealing into nutrition product asked for feature to manage schemes like "Buy One Get One Free". To manage the same, he created a non-stock item which was used as Parent Item. In description of item, he entered scheme details with items image indicating the offer. The sellable product was selected in Package Item where qty was two. Hence every time they sold one qty of Parent item under scheme, system deducted two quantities of product from Warehouse.</div>

#### 3. Related Topics
1. [Item](http://frappe.local:8000/docs/user/manual/en/stock/item)