<!-- add-breadcrumbs -->
# Item

**An Item is a product or a service offered by your company.**

The term Item is also applicable to raw materials or components of products yet to be produced (before they can be sold to customers). ERPNext allows you to manage all sorts of items like raw-materials, sub-assemblies, finished goods, item variants, and service items.

ERPNext is optimized for itemized management of your sales and purchase. If you are in services, you can create an Item for each service that you offer. Completing the Item Master is very essential for the successful implementation of ERPNext.

## 1. How to create an Item
1. Go to  **Stock > Items and Pricing > Item > New**.
2. Enter an Item Code, the name will be autofilled the same as Item Code on clicking inside the Item Name field.
1. Select an Item Group.
1. Enter the opening stock units and standard selling rate.
3. Save.

### 1.1 Item Properties

  * **Item Name:** Item name is the actual name of your product or service.
  * **Item Code:** Item Code is a short-form to denote your Item. If you have very few Items, it is advisable to keep the Item Name and the Item Code same. This helps new users to recognize and update Item details in all transactions. In case you have a lot of Items with long names and the list runs in hundreds, it is advisable to code. To understand naming Item codes see [Item Codification](/docs/user/manual/en/stock/item-codification).
  * **Item Group:** Item Group is used to categorize an Item under various criteria like products, raw materials, services, sub-assemblies, consumables or all Item groups. Create your default Item Group list under Setup > Item Group and pre-select the option while filling your New Item details under [Item Group](/docs/user/manual/en/stock/item-group).
  * **Default Unit of Measure:** This is the default measuring unit that you will use for your product. It could be in nos, kgs, meters, etc. You can store all the UOM’s that your product will require under Set Up> Master Data > UOM. These can be preselected while filling New Item by using % sign to get a pop up of the UOM list.

### 1.2 Options when creating an item
* **Disabled**: The item will be disabled and will not appear in the Item List.
* **Allow Alternative Item**: Sometimes when manufacturing a finished good, specific material may not be available. If you tick this, you can create and select an alternative item from the Item Alternative list.
* **Maintain Stock:** If you are maintaining stock of this Item in your Inventory, ERPNext will make a stock ledger entry for each transaction of this item.
* **Include Item in Manufacturing**: This is for raw material Items that'll be used to create finished goods.
* **Valuation Rate**: There are two options to maintain valuation of stock. FIFO (first in - first out) and Moving Average. To understand this topic in detail please visit [Item Valuation, FIFO and Moving Average](/docs/user/manual/en/stock/articles/item-valuation-fifo-and-moving-average).
* **Standard Selling Rate**: The rate at which you'll sell the item. This will be fetched in Sales Orders and Sales Invoices.
* **Is Fixed Asset**: Tick this checkbox if this item is an Asset. Check out the [Asset Module](/docs/user/manual/en/asset) to know more.

* **Allowance Percentage**: This option will be available only when you create and save the item. This is the percent by which you will be allowed to over-bill or over-deliver this Item. If not set, it will select from the Global Defaults.
* **Uploading an Image**: To upload an image for your icon that will appear in all transactions, save the partially filled form. Only after your file is saved  the 'upload' button will work above the Image icon. Click on this sign and upload the image.

For India:

* **HSN/SAC**: Harmonized System of Nomenclature (HSN) and Service Accounting Code (SAC) for GST.
* **Is nil rated or exempted**: For an item that is under GST, but no tax is applied to it. Eg: Cereals.
* **Is Non GST**: For an item that is not covered under GST. Eg: petrol.

##2. Features

### 2.1 Brand and Description

* **Brand**: If you have more than one brand save them under Selling > Brand and pre-select them while filling a New Item.
* **Description**: Description of the item. The text from the Item Code will be fetched by default.

### 2.3 Inventory

* **Shelf Life In Days**: This is for a product batch. The number of days after which a batch of a product will be unusable. For example: medicines.
* **End of Life**: For a non-serialized single item/product, the date after which it'll be completely unusable. That is, the item will be unusable in transactions and manufacturing.
* **Warranty**: To track a warranty period, it is necessary that the Item be a serialized Item. When this Item is delivered, the delivery date and the expiry period is saved in the Serial Number master. Through the serial number master you can track the warranty status.

  A warranty period is a time period in which a purchased product may be returned or exchanged.

  <img class="screenshot" alt="Item Warranty" src="{{docs_base_url}}/assets/img/stock/item-inventory.png">

* **Weight UOM**: The Unit of Measure for the item. This can be Nos, Kilo, etc.,
* **Weight Per Unit**: The actual weight per unit of the item. Eg: 1 kilo biscuits or 10 biscuits per pack.
* **Default Material Request Type**: When you create a new Material Request for this item, the field set here will be selected by default in the new Material Request.
* **Valuation Method**: Select the Valuation Method whether FIFO or Moving Average. To know more about Valuation Methods, [click here](/docs/user/manual/en/stock/articles/item-valuation-fifo-and-moving-average).

### 2.4 Automatic Reordering
When the stock of an item dips under a certain quantity, you can set an automatic reorder under 'Auto Reorder' section.

* **Check in (group)**: In which group warehouses to check quantity of the item.
* **Request for**: Which warehouse to stock the item reorder.
* **Re-order Level**: When this quantity is reached, the reorder will be triggered. Re-order level can be determined based on the lead time and the average daily consumption. For example, you can set your reorder level of Motherboard at 10. When there are only 10 Motherboards remaining in stock, the system will either automatically create a Material Request in your ERPNext account.
* **Re-order Qty**: The number of units to be reordered so that the sum of ordering cost and holding cost is at its minimum. The re-order quantity is based on the 'Minimum Order Qty' specified by the supplier and many other factors.

  For example, If reorder level is 100 items, your reorder quantity may not necessarily be 100 items. The Reorder quantity can be greater than or equal to the reorder level. It may depend upon lead time, discount, transportation and average daily consumption.

* **Material Request Type**: The [Material Request](/docs/user/manual/en/stock/material-request) type with which the stock will be reordered.

<img alt="Item Reorder" class="screenshot" src="{{docs_base_url}}/assets/img/stock/item-reorder.png">

### 2.5 Multiple Units of Measure
You can add alternate UoMs for an Item. If the default UoM in which you sell is numbers (NoS) but you receive it in Kilos, you can set an additional UoM with an appropriate conversion factor. For example 500 Nos of screws = 1 Kilogram, so select Kilogram/Litre as UOM and set the conversion factor as 500.

### 2.6 Serial Numbers and Batches

These numbers help to track individual units or batches of Items which you sell. It also tracks warranty and returns. In case any individual Item is recalled by the supplier the number system helps to track individual Item. The numbering system also manages expiry dates.

Please note that if you sell your items in thousands, and if the items are very small like pens or erasers, you need not serialize them.

In ERPNext, you will have to mention the serial number in some accounting entries. If your product is not a big consumer durable Item, if it has no warranty and has no chances of being recalled, avoid giving serial numbers.

* **Has Batch No**: Options for batch number, expiry date, and retaining sample stock will be revealed on ticking this checkbox. You cannot activate this if there is any pre-existing transaction for this item.
* **Batch Number Series**: Prefix that'll be applied to batch numbers. If you set 5x1SCR,then the first batch will be named like 5x1SCR00001 on first transaction/manufacture.
* **Automatically Create New Batch**: If the batch number is not mentioned in transactions, then they will be automatically created according to a format like AAAA.00001. If you always want to manually create a batch number for this item, leave this field blank. This setting will override 'Naming Series Prefix' in Stock Settings.
* **Has Expiry Date**: If you tick this, the batch number will be created according to the expiry date. The expiry dates can be set in the 'Batch' master.
* **Retain Sample**: To retain a minimum number of sample stock of the item. You need to set a Sample Retention Warehouse in Stock Settings for this. To know more, [click here](/docs/user/manual/en/stock/retain-sample-stock).
* **Has Serial No**: This is similar to Batch Number Series, it'll be created when you make transactions/manufacture. If you set Serial Number Series as AA, then on the first transaction a serial number like AA00001 wil be created.

> Tip: While entering an item code in an items table, if the table requires inventory details, then depending on whether the entered item is batched or serialized, you can enter serial or batch numbers right away in a pop-up dialog.

<img alt="Serial No modal" class="screenshot" src="{{docs_base_url}}/assets/img/stock/serial_no_modal.gif"><img alt="Batch No modal" class="screenshot" src="{{docs_base_url}}/assets/img/stock/batch_no_modal.png">

> **Note**: Once you mark an item as serialized or batched or neither, you cannot change it after you have made any stock entry.

To know more, read [Stock Reconciliation](/docs/user/manual/en/setting-up/stock-reconciliation).

### 2.7 Variants
An Item Variant is a different version of a Item. To learn more about managing variants see [Item Variants](/docs/user/manual/en/stock/item-variants).

### 2.8 Item Defaults

* **Default Warehouse:** This is the Warehouse that is automatically selected in your transactions with this item.
* **Default Price List:** Whether Standard Selling or Standard Buying. Likewise you can also set the purchasing and selling default accounts
* **Supplier**: If a default supplier is set, this supplier will be selected for new purchase transactions.
* **Default Expense Account:** It is the account in which cost of the Item will be debited.
* **Default Income Account:** It is the account in which income from selling the Item will be credited.
* **Default Cost Center:** It is used for tracking expense for this Item.

You can add more rows for multiple companies.

### 2.9 Purchase, Replenishment Details

* **Default Purchase Unit of Measure**: The default UoM that will be used in transactions.
* **Minimum Order Qty**: The minimum quantity required for purchase transactions/Material Requests. This quantity also applied to auto reordering items as explained in section _2.4_.
* **Safety Stock**: “Safety Stock” is used in the report “Itemwise Recommended Reorder Level”. Based on Safety Stock, average daily consumption and the lead time, the system suggests Reorder Level of an item.

  Reorder Level = Safety Stock + (Average Daily Consumption * Lead Time)
* **Last Purchase Rate**: The rate at which you last purchased this item will be displayed here.
* **Is Purchase Item:** If unticked, you won't be able to use this item in purchase transactions.
* **Is Customer Provided Item:** Checked if Item is provided by a customer and received through **Stock Entry > Material Receipt**. If Checked, **Customer** field is Mandatory as the default customer for **Material Request**.
* **Lead time days:** Lead time days are the number of days required for the Item to reach the warehouse.

  <img class="screenshot" alt="Purchase details" src="{{docs_base_url}}/assets/img/stock/item-purchase-details.png">

### 2.10 Supplier Details

* **Delivered by Supplier (Drop Ship)**: If the item is delivered directly by the supplier to the customer, tick this checkbox. If ticked here, it'll be automatically selected in sales transactions. Read more [here](/docs/user/manual/en/selling/articles/drop-shipping).
* **Manufacturer:** Select the Manufacturer who manufactured this item.
* **Manufacturer Part Number:** Enter the manufacturer part number that the manufacturer has assigned to this item.
* **Supplier Codes:** Track Item Code defined by the Suppliers for this Item. In the Purchase transactions, on selection and Supplier, Supplier Part No. will be fetched as well for the Supplier's reference. You can read more about it [here](/docs/user/manual/en/buying/articles/maintaining-suppliers-part-no-in-item).

<img alt="Item Supplier Details" class="screenshot" src="{{docs_base_url}}/assets/img/stock/item-supplier.png">

### 2.11 Foreign Trade Details
If you're sourcing the item from another country, you can set the details here.

* **Country of Origin**: The country from which you're sourcing the item.
* **Customs Tariff Number**: You can create a customs tariff number with a description and use it for reference here to share with custom agencies. Later it can be used to add in Delivery Notes.

### 2.12 Sales Details

* **Default Sales Unit of Measure**: The default UoM that'll be selected for sales transactions.
* **Max Discount (%)**: You can define the maximum discount in % to be applied to an item. Eg: if you set 20%, you cannot sell this item with a discount greater than 20%.
* **Is Sales Item**: If unticked, you won't be able to use this item in sales transactions.

  <img alt="Item Sales Details" class="screenshot" src="{{docs_base_url}}/assets/img/stock/item-sales.png">

### 2.13 Deferred Revenue and Deferred Expense
You can enable deferred revenue or expense from the item. Once you tick the checkbox, you'll see options to set the Deferred Expense Account and the number of months through which the revenue/expense is deferred. 

For example, consider a yearly gym membership, you pay the money upfront at once but the service is given throughout the year. For the gym owner this is deferred revenue and for the customer it is a deferred expense.

### 2.14 Customer Details

* **Customer Name**: Select a customer here 
* **Customer Group**: This will be fetched based on the customer you selected in the previous field.
* **Ref Code:** A customer can identify this item with a different number. You can track Item Code assigned by the Customer for this Item. This will help you in searching this item in the Customer's Purchase Order while creating a Sales Order based on the Item Code.

### 2.15 Item Tax

Go to [Setting Up Taxes](/docs/user/manual/en/setting-up/setting-up-taxes) to understand taxes better.

These settings are required only if a particular Item has a different tax rate than the rate defined in the standard tax Account.

You need to create a new 'Item Tax Template' or choose an existing one. For example, if you have a tax Account, “VAT 14%” and this particular Item is exempted from tax, then you select “VAT 14%” in the first column, and set “0” as the tax rate in the second column.

![Item tax template](/docs/assets/img/stock/item-tax-template.png)

You can also set a Tax Category, visit [Quotation](/docs/user/manual/en/selling/quotation) to know more about Tax Category.

### 2.16 Inspection Criteria

* **Inspection Required before Purchase**: If an inspection is mandatory before the item is purchased, i.e., before you generate Purchase Receipt, tick this checkbox.
* **Inspection Required before Delivery**: If an inspection is required at the time of delivery from your Supplier is mandatory for this Item, tick this checkbox. That is, before you generate a Delivery Note. 
* **Quality Inspection Template**: If a Quality Inspection is prepared for this Item, then this template of criteria will automatically be updated in the Quality Inspection table of the Quality Inspection. Examples of Criteria are: Weight, Length, Finish etc.

To know more about Quality Inspection, [click here](/docs/user/manual/en/stock/quality-inspection).

### 2.17  Manufacturing and Website

* **Supply Raw Materials for Purchase**:  If you're subcontracting to a vendor, you can choose to provide him with the raw materials to manufacture the item.

* **Show in Website**: Choose if you want to show this item on your website. Once you tick this, additional options will be visible to configure the item on your website. To view the item on the website click on the 'See on Website' link on the top left just above the item image.

  <img class="screenshot" alt="Manufaturing details" src="{{docs_base_url}}/assets/img/stock/item-manufacturing-website.png">

* **Weightage**: Items with higher weight will be displayed first on the website. The limit for the number you can enter here is very high. 

* **Slideshow**: A slideshow can be displayed at the top of the page. Visit the [Homepage](/docs/user/manual/en/website/homepage) page in Website module to know more.
* **Image**: You can attach an image instead of a Slideshow. 
* **Website Warehouse**: Select an existing or create a new warehouse for transactions via your website.
* **Website Item Groups**: In this table you can select existing or create new [Item Groups](/docs/user/manual/en/stock/item-group) to classify items on your website.
* **Set Meta Tags**: Meta tags help with SEO. See [Web Page](/docs/user/manual/en/website/web-page) to know how to add them.

Visit [Manufacturing](/docs/user/manual/en/manufacturing) and [Website](/docs/user/manual/en/website) to understand these topics in detail.

### 2.18 Website Specifications
This section is for configuring other details about the item.

* **Copy from Item Group:** The 'Website Specifications' details will be fetched as set in a specific Item Group chosen on the previous section (2.17).
* **Website Specifications**: Label and its description for the item. For example, 'Warranty: 1 year'.
* **Website Description**: This will appear on the item page.
* **Website Content**: (*Introduced in v12*) You can create additional styling etc., use Bootstrap 4 markup to display on the item page.

### 2.19 Hub Publishing Details

* **Publish in Hub**: Choose if you want to publish your item on https://hubmarket.org/. It is a free marketplace. If your supplier/customer is also on ERPNext, the transactions will be seamless. For example, on creating a Purchase Order from your end, a Sales Order will be created on the Supplier's end.
* **Hub Warehouse**: This is a separate Warehouse to maintain the stock for your hub transactions.
* **Synced With Hub**: Sync item and other details with the hub when transactions take place.

Here is a video for demonstrating item management:

<div>
  <div class='embed-container'>
    <iframe src='https://www.youtube.com/embed/FcOsV-e8ymE?end=192' frameborder='0' allowfullscreen>
    </iframe>
  </div>
</div>

### 3. Related Topics
1. [Item Price](/docs/user/manual/en/stock/item-price)
1. [Item Codification](/docs/user/manual/en/stock/item-codification)
1. [Item Variants](/docs/user/manual/en/stock/item-variants)
1. [Item Warranty](/docs/user/manual/en/stock/item-warranty)
1. [Reorder Item](/docs/user/manual/en/stock/reorder-item)
1. [Item Group](/docs/user/manual/en/stock/item-group)
1. [Item Attribute](/docs/user/manual/en/stock/item-attribute)
1. [Item Valuation FIFO And Moving Average](/docs/user/manual/en/stock/item-valuation-fifo-and-moving-average)
1. [Item Valuation Transactions](/docs/user/manual/en/stock/articles/item-valuation-transactions)
1. [Maintain Stock Field Frozen In Item Master](/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master)
1. [Managing Rejected Finished Goods Items](/docs/user/manual/en/stock/articles/managing-rejected-finished-goods-items)
1. [Return Rejected Item](/docs/user/manual/en/stock/articles/return-rejected-item)
1. [Track Items Using Barcode](/docs/user/manual/en/stock/articles/track-items-using-barcode)
1. [Creating Depreciation For Item](/docs/user/manual/en/stock/articles/creating-depreciation-for-item)
1. [Serial Number Naming](/docs/user/manual/en/stock/articles/serial-no-naming)
1. [Opening Stock Balance Entry For Serialized And Batch Item](/docs/user/manual/en/stock/articles/opening-stock-balance-entry-for-serialized-and-batch-item)
1. [Serial Number](/docs/user/manual/en/stock/serial-no)
1. [Serial Number Naming](/docs/user/manual/en/stock/articles/serial-no-naming)
