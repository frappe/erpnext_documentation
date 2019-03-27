<!-- add-breadcrumbs -->
# Item

An Item is your company's product or a service. The term Item is applicable to things (products or services) you sell as well as raw materials or components of products yet to be produced (before they can be sold to customers). An Item can be a physical product or a service that you buy/sell from your customers/suppliers. ERPNext allows you to manage all sorts of items like raw-materials, sub-assemblies, finished goods, item variants and service items.

ERPNext is optimized for itemized management of your sales and purchase. If you are in services, you can create an Item for each services that your offer. Completing the Item Master is very essential for successful implementation of ERPNext.

### 1. How to create an Item
1. Go to  **Stock > Items and Pricing > Item > New**
2. Enter an item code, name, group and other details as needed.
3. Save.

#### 1.2 Options when creating an item

  * **Maintain Stock:** If you are maintaining stock of this Item in your Inventory, ERPNext will make a stock ledger entry for each transaction of this item.
  * **Default Warehouse:** This is the Warehouse that is automatically selected in your transactions.
  * **Valuation Rate:** There are two options to maintain valuation of stock. FIFO (first in - first out) and Moving Average. To understand this topic in detail please visit [Item Valuation, FIFO and Moving Average](/docs/user/manual/en/stock/item-valuation-fifo-and-moving-average).
  * **Allowance Percentage:** This is the percent by which you will be allowed to over-bill or over-deliver this Item. If not set, it will select from the Global Defaults. This option will be available once you create and save the item.
  

###2. Features
#### 2.1 Item Properties

  * **Item Name:** Item name is the actual name of your product or service.
  * **Item Code:** Item Code is a short-form to denote your Item. If you have very few Items, it is advisable to keep the Item Name and the Item Code same. This helps new users to recognize and update Item details in all transactions. In case you have lot of Items with long names and the list runs in hundreds, it is advisable to code. To understand naming Item codes see [Item Codification](/docs/user/manual/en/stock/item/item-codification)
  * **Item Group:** Item Group is used to categorize an Item under various criteria like products, raw materials, services, sub-assemblies, consumables or all Item groups. Create your default Item Group list under Setup> Item Group and pre-select the option while filling your New Item details under [Item Group](/docs/user/manual/en/stock/setup/item-group)
  * **Default Unit of Measure:** This is the default measuring unit that you will use for your product. It could be in nos, kgs, meters, etc. You can store all the UOM’s that your product will require under Set Up> Master Data > UOM. These can be preselected while filling New Item by using % sign to get a pop up of the UOM list.
  * **Brand:** If you have more than one brand save them under Set Up> Master Data> Brand and pre-select them while filling a New Item.
  * **Variant:** A Item Variant is a different version of a Item.To learn more about managing variants see [Item Variants](/docs/user/manual/en/stock/item/item-variants)

#### 2.2 Upload an Image

To upload an image for your icon that will appear in all transactions, save the partially filled form. Only after your file is saved  the 'upload' button will work above the Image icon. Click on this sign and upload the image.

#### 2.3 Item Warranty
To track a warranty period, it is necessary that the Item is a serialized Item. When this Item is delivered, the delivery date and the expiry period is saved in the serial number master. Through the serial number master you can track the warranty status.

A warranty means a guarantee or a promise which provides assurance by one party to the other party which allows for a legal remedy if that promise is not true or followed. A warranty period is a time period in which a purchased product may be returned or exchanged.

<img class="screenshot" alt="Item Warranty" src="{{docs_base_url}}/assets/img/stock/item-warranty.png">

#### 2.4 Serialized and Batched Inventory

These numbers help to track individual units or batches of Items which you sell. It also tracks warranty and returns. In case any individual Item is recalled by the supplier the number system helps to track individual Item. The numbering system also manages expiry dates. Please note that if you sell your items in thousands, and if the items are very small like pens or erasers, you need not serialize them. In ERPNext, you will have to mention the serial number in some accounting entries. To create serial numbers you will have to manually create all the numbers in your entries. If your product is not a big consumer durable Item, if it has no warranty and has no chances of being recalled, avoid giving serial numbers.

> Tip: While entering an item code in an items table, if the table requires inventory details, then depending on whether the entered item is batched or serialized, you can enter serial or batch numbers right away in a pop-up dialog.
<img alt="Serial No modal" class="screenshot" src="{{docs_base_url}}/assets/img/stock/serial_no_modal.gif"><img alt="Batch No modal" class="screenshot" src="{{docs_base_url}}/assets/img/stock/batch_no_modal.png">

> Important: Once you mark an item as serialized or batched or neither, you cannot change it after you have made any stock entry.

  * [Discussion on Serialized Inventory](/docs/user/manual/en/setting-up/stock-reconciliation-for-non-serialized-item)

#### 2.5  Re-Ordering

  ***Re-order level** suggests the amount of stock balance in the Warehouse.
  ***Re-order Qty** suggests the amount of stock to be ordered to maintain minimum stock levels.
  ***Minimum Order Qty** is the minimum quantity for which a Material Request / Purchase Order must be made.

#### 2.6  Item Tax

These settings are required only if a particular Item has a different tax rate than the rate defined in the standard tax Account. For example, If you have a tax Account, “VAT 10%” and this particular Item is exempted from tax, then you select “VAT 10%” in the first column, and set “0” as the tax rate in the second column.

Go to [Setting Up Taxes](/docs/user/manual/en/setting-up/setting-up-taxes) to understand this topic in detail.

#### 2.7  Inspection

Inspection Required: If an incoming inspection (at the time of delivery from the Supplier) is mandatory for this Item, mention “Inspection Required” as “Yes”. The system will ensure that a Quality Inspection will be prepared and approved before a Purchase Receipt is submitted.

Inspection Criteria: If a Quality Inspection is prepared for this Item, then this template of criteria will automatically be updated in the Quality Inspection table of the Quality Inspection. Examples of Criteria are: Weight, Length, Finish etc.

#### 2.8  Purchase, Replenishment Details

<img alt="Item Purchase Details" class="screenshot" src="{{docs_base_url}}/assets/img/stock/item-purchase.png">

<img class="screenshot" alt="Purchase details" src="{{docs_base_url}}/assets/img/stock/item-purchase.png">

* **Is Purchase Item:** Checked if Item is purchased through a supplier and follows **Buying Cycle**.
* **Is Customer Provided Item:** Checked if Item is provided by a customer and received through **Stock Entry - Material Receipt**. If Checked, **Customer** field is Mandatory as the default customer for **Material Request**.
* **Lead time days:** Lead time days are the number of days required for the Item to reach the warehouse.
* **Default Expense Account:** It is the account in which cost of the Item will be debited.
* **Default Cost Centre:** It is used for tracking expense for this Item.

#### 2.9 Supplier Details

<img alt="Item Supplier Details" class="screenshot" src="{{docs_base_url}}/assets/img/stock/item-supplier.png">

* **Default Supplier:** Supplier from whom you generally purchase this item.

* **Manufacturer Details:** Select Manufacturer and Part No. assigned by the Manufacturer for this item.

* **Supplier Codes:** Track Item Code defined by the Suppliers for this Item. In the Purchase transactions, on selection and Supplier, Supplier Part No. will be fetched as well for the Supplier's reference.

#### 2.10  Sales Details

<img alt="Item Sales Details" class="screenshot" src="{{docs_base_url}}/assets/img/stock/item-sales.png">

* **Default Income Account:** Income account selected here will be fetched automatically in sales invoice for this item.

* **Cost Centre:** Cost center selected here will be fetched automatically in sales invoice for this item.

* **Customer Codes:** Track Item Code assigned by the Customers for this Item. This will help you in searching item while creating Sales Order based on the Item Code in the Customer's Purchase Order.

#### 2.11  Manufacturing nd Website

<img class="screenshot" alt="Manufaturing details" src="{{docs_base_url}}/assets/img/stock/item-manufacturing-website.png">

Visit [Manufacturing](/docs/user/manual/en/manufacturing) and [Website ](/docs/user/manual/en/website)to understand these topics in detail.

Here is a video for demonstrating item management:
<div>
  <div class='embed-container'>
    <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?end=192' frameborder='0' allowfullscreen>
    </iframe>
  </div>
</div>


#### Related Topics
1. [Item Price](/docs/user/manual/en/stock/item-price)
1. [Item Codification](/docs/user/manual/en/stock/item-codification)
1. [Item Variants](/docs/user/manual/en/stock/item-variants)
1. [Item Warranty](/docs/user/manual/en/stock/item-warranty)
1. [Reorder Item](/docs/user/manual/en/stock/reorder-item)
1. [Item Group](/docs/user/manual/en/stock/item-group)
1. [Item Attribute](/docs/user/manual/en/stock/item-attribute)
1. [Item Valuation FIFO And Moving Average](/docs/user/manual/en/stock/item-valuation-fifo-and-moving-average)
1. [Item Valuation Transactions](/docs/user/manual/en/stock/articles/item-valuation-transactions)
- [Maintain Stock Field Frozen In Item Master](/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master)
- [Managing Rejected Finished Goods Items](/docs/user/manual/en/stock/articles/managing-rejected-finished-goods-items)
- [Return Rejected Item](/docs/user/manual/en/stock/articles/return-rejected-item)
- [Track Items Using Barcode](/docs/user/manual/en/stock/articles/track-items-using-barcode)
- [Creating Depreciation For Item](/docs/user/manual/en/stock/articles/creating-depreciation-for-item)
1. [Serial Number Naming](/docs/user/manual/en/stock/articles/serial-no-naming)
- [Opening Stock Balance Entry For Serialized And Batch Item](/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Serial Number](/docs/user/manual/en/stock/serial-no)
1. [Serial Number Naming](/docs/user/manual/en/stock/articles/serial-no-naming)
