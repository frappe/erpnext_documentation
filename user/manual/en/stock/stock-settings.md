<!-- add-breadcrumbs -->
# Stock Settings

You can set default settings for your stock related transactions here.

## 1. Item Naming By
To choose if items should be named by Item Codes or be a set [Naming Series](/docs/user/manual/en/setting-up/settings/naming-series).

## 2. Defaults

### 2.1 Default Item Group
This will be the default item group allocated to a newly created item.

### 2.2 Default Stock UOM
The default unit of measure for stock is set as numbers, it can be changed from here.

### 2.3 Default Warehouse
Select the default warehouse from which the stock transactions are done.

### 2.4 Sample Retention Warehouse
This is the warehouse where sample retentions are stored.

### 2.5 Default Valuation method
FIFO - first in first out or moving average valuation for your items. Read more [here](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average).

### 3. Limit Percent
This is the percentage you are allowed to receive or deliver more against the quantity ordered. For example: If you have ordered 100 units, Supplier sends 120 units and percentage is set to 10% then you are allowed to receive 110 units. By default this is set to 0.

## 4. Show Barcode Field
A field to enter Barcode details for an item. If unticked, the field won't be visible in the item DocType.

## 5. Convert Item Description to Clean HTML
Usually descriptions are copy-pasted from a website or Word/PDF file and they contain a lot of embedded style. This messes up the Print view of your invoices or quotes.

To fix this, you can check "Convert Item Description to Clean HTML" in Stock Settings. This will ensure that when you save the Items, their descriptions will be cleaned up.

If you want to control your description, views, and allow any HTML to be embedded, you can uncheck this property.

## 6. Auto insert
### 6.1 Auto insert Price List rate if missing
Will insert a Price List rate to the item automatically if it's missing.

## 6.2 Automatically Set Serial Nos based on FIFO
Serial numbers for stock will be set automatically based on the items entered FIFO.

## 7. Allow Negative Stock
This will allow stock items to be displayed in negative values.

## 8. Set Qty in Transactions based on Serial No Input
The quantity of items will be set according to the serial numbers. For example if the user has added serial nos like A001, A002, and A003 then the system will set the quantities as 3 in the transaction.

## 9. Automatic Material Request
## 9.1 Raise Material Request when stock reaches re-order level
A material request will be raised automatically when stock reached the re-order level defined in the item master.

## 9.2 Notify by Email on creation of automatic Material Request
An email will be sent to notify you when an automatic Material Request is created. 

## 10. Freeze Stock Entries

* **Stock Frozen Upto**: A threshold date till which stocks will be frozen.
* **Freeze Stocks Older Than [Days]**: Stocks older than x days will be frozen. This is calculated based on creation date of the item.
* **Role Allowed to edit frozen stock**: The role you choose here will be allowed to edit frozen stock.

## 11. Batch identification
Global setting for batches of stocks to be identified by a naming series. You can override this in the Item DocType.

Here is a screenshot of the Stock Settings page.

<img class="screenshot" alt="Stock Settings" src="{{docs_base_url}}/assets/img/stock/stock-settings.png">
