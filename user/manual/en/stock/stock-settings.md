<!-- add-breadcrumbs -->
# Stock Settings

You can set default settings for your stock related transactions here.

<img class="screenshot" alt="Stock Settings" src="{{docs_base_url}}/assets/img/stock/stock-settings.png">

#### 1. Item Naming By
To choose if items should be named by Item Codes or be a set Naming Series.

#### 2. Default Item Group
Select a group that an item would belong to.

#### 3. Default Stock UOM
The default unit of measure for stock is set as numbers, it can be changed from here.

#### 4. Default Warehouse
Select the default warehouse from which the stock transactions are done.

#### 5. Sample Retention Warehouse
This is the warehouse where sample retentions are stored.

#### 6. Default Valuation method
FIFO - first in first out or moving average valuation for your items. Read more [here](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average).

#### 7. Convert Item Description to Clean HTML

Usually descriptions are copy-pasted from a website or Word / PDF file and they contain a lot of embedded style. This messes up the Print view of your invoices or quotes.

To fix this, you can check "Convert Item Description to Clean HTML" in Stock Settings. This will ensure that when you save your Items, their descriptions will be cleaned up.

If you want control your description views and low any HTML to be embedded, you can uncheck this property.

#### 8. Limit Percent
Limit the additional stock you can deliver.

#### 9. Show Barcode Field
A field to enter Barcode details for an item.

#### 10. Auto insert Price List rate if missing
Will insert a Price List rate automatically if it's missing.

#### 11. Allow Negative Stock
Stock items will be displayed in negative values.

#### 12. Automatically Set Serial Nos based on FIFO
Serial numbers for stock will be set automatically based on the items entered FIFO.

#### 13. Set Qty in Transactions based on Serial No Input
The quantity of items will be set according to the serial numbers.

#### 14. Raise Material Request when stock reaches re-order level
A material request will be raised automatically when stock reached the re-order level.

#### 15. Notify by Email on creation of automatic Material Request
An email will be send when an automatic Material Request is created. 

#### 16. Freeze Stock Entries
You can set a threshold date for freezing stocks then set number of days after which a stock will be frozen. You can also set who can edit the frozen stock.

#### 17. Batch identification
Batches of stocks can be identified by a naming series.