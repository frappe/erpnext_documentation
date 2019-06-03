<!-- add-breadcrumbs -->
# Stock Reconciliation

**Stock Reconciliation is the process of counting and evaluating material/products, periodically and at year end in order to:**

* **Keep the actual physical stock count and book stock count in sync**
* **Value the stock for preparation of the accounting statements**

Stock Reconciliation is used for:

* Posting opening stock
* Reconciling book and actual stock

>Stock Reconciliation can be used for above listed purposes only for non-serialized items. For serialized and batched items Stock Entry can be used.

**Difference between Serialized and Non-serialized Items.**

A serial number is a unique, identifying number or group of numbers and
letters assigned to an individual Item. Serialized items are generally high value items for which you need to manage warranty and service agreements. Mostly items like machinery, equipments and high-value electronics (computers, printers etc.) are serialized.

Non Serialized items are generally fast moving and low value item, hence don't need tracking for each unit. Items like screw, cotton waste, other consumables, stationary products can be categorized as non-serialized.


###1. How to Create a Stock Reconciliation to Post Opening Stock for Non-serialized Items

Using stock reconciliation you can update the quantity of specific items in a warehouse as of specific time.

To post opening stock:

1. Go to **Stock > Tools > Stock Reconciliation > New**
1. Set Posting Date.
1. Set Purpose to Opening Stock.
1. Set Item Code, Warehouse, Quantity, and Valuation Rate.
1. Select 'Temporary Opening' in Difference Account.
1. Select Cost Center.
1. Save and Submit.


###2. How to Create a Stock Reconciliation to Reconcile Book and Physical Stock Count

Stock Reconciliation is the process of counting and evaluating stock-in-trade, periodically and at year end in order to value the total stock for preparation of the accounting statements. In this process actual physical stocks are checked and recorded in the system. The actual stocks and the stock in the system should be in agreement and accurate. If they are not, you can use the stock reconciliation tool to reconcile stock balance and value with actuals.

To reconcile the stock:

1. Go to **Stock > Tools > Stock Reconciliation > New**
1. Set Posting Date.
1. Set Purpose to Stock Reconciliation.
1. Set Item Code, Warehouse, Quantity, and Valuation Rate.
1. Select an expense account in Difference Account.
1. Select Cost Center.
1. Save and Submit.

###3. Features

###3.1 Upload Data Through Spreadsheet

If you have lot of items, you can upload the details via a spreadsheet.

1. Download Template

  Open new Stock Reconciliation and click on Download button to download the template in CSV format.

  <img class="screenshot" alt="Stock Reconciliation" src="{{docs_base_url}}/assets/img/setup/stock-recon-1.png">

2. Enter Data in CSV Template.

  The CSV format is case-sensitive. Do not edit the headers which are preset in the template. In the Item Code and Warehouse column, enter exact Item Code and Warehouse as created in your ERPNext account. For quantity, enter stock level you wish to set for that item, in a specific warehouse.

  <img class="screenshot" alt="Stock Reconciliation" src="{{docs_base_url}}/assets/img/setup/stock-reco-data.png">


3. Upload the CSV file with the data by clicking on 'Upload' button.

  <img class="screenshot" alt="Stock Reconciliation" src="{{docs_base_url}}/assets/img/setup/stock-recon-2.png">


4. Review, Save, and Submit.

  <img class="screenshot" alt="Stock Reconciliation" src="{{docs_base_url}}/assets/img/setup/stock-reco-upload.gif">

5. Check Stock Ledger Report for updated stock balance.

  <img class="screenshot" alt="Stock Reconciliation" src="{{docs_base_url}}/assets/img/setup//stock-reco-ledger.png">

###3.2 Get Stock Balance and Valuation as of Specific Date and Time

You can import the stock balance and valuation as of specific date and time by clicking on 'Items' button. You can update the Quantity and Valuation Rate as needed.

<img class="screenshot" alt="Stock Reconciliation Items Button" src="{{docs_base_url}}/assets/img/stock/stock_reconciliation_items_button.gif">

###4 How Stock Reconciliation Works

Once a stock reconciliation is posted to update the quantity on specific date and time for an item in a warehouse, it will not be modified by subsequent stock transactions even if the such transactions have a posting date which is prior to the stock reconciliation date.  

Example:
Consider an item with code 'ABC001' in a 'Mumbai' warehouse.
Let's assume that stock as on 10th January is 100 units.
Stock Reconciliation is made on 12th January to set stock balance to 150 units.

Stock Ledger would look as shown below:
<html>
<style>
    td {
    padding:5px 10px 5px 5px;
    };
    img {
    align:center;
    };
	table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
	}
</style>
 <table border="1" cellspacing="0px">
            <tbody>
                <tr align="center" bgcolor="#EEE">
                    <td><b>Posting Date</b>
                    </td>
                    <td><b>Qty</b>
                    </td>
                    <td><b>Balance Qty</b>
                    </td>
                    <td><b>Voucher Type</b>
                    </td>
                </tr>
                <tr>
                    <td>10/01/2014</td>
                    <td align="center">100</td>
                    <td>100&nbsp;</td>
                    <td>Purchase Receipt</td>
                </tr>
                <tr>
                    <td>12/01/2014</td>
                    <td align="center">50</td>
                    <td>150</td>
                    <td>Stock Reconciliation</td>
                </tr>
            </tbody>
        </table>
</html>

If a new Purchase Receipt entry is made on 5th January, 2014, which is prior to the date of Stock Reconciliation entry, Stock Ledger would look as shown below.
<html>
	<table border="1" cellspacing="0px">
        <tbody>
            <tr align="center" bgcolor="#EEE">
                <td><b>Posting Date</b></td>
                <td><b>Qty</b></td>
                <td><b>Balance Qty</b></td>
                <td><b>Voucher Type</b></td>
            </tr>
            <tr>
                <td>05/01/2014</td>
                <td align="center">20</td>
                <td style="text-align: center;">20</td>
                <td>Purchase Receipt</td>
            </tr>
            <tr>
                <td>10/01/2014</td>
                <td align="center">100</td>
                <td style="text-align: center;">120</td>
                <td>Purchase Receipt</td>
            </tr>
            <tr>
                <td>12/01/2014</td>
                <td align="center"><br></td>
                <td style="text-align: center;"><b>150</b></td>
                <td>Stock Reconciliation<br></td>
            </tr>
        </tbody>
	</table>
</html>

As you can see, the Balance Qty as on 10th January got updated from 100 to 120. But the Balance Qty as on 12th January did not get updated from 150 to 170.

<br>

<div class="embed-container">
	<iframe src="https://www.youtube.com/embed/nlHX0ZZ84Lw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
	</iframe>
</div>

### 5. Related Topics
1. [Stock Entry](/docs/user/manual/en/stock/stock-entry)
1. [Accounting Of Inventory Stock](/docs/user/manual/en/stock/accounting-of-inventory-stock)


{next}
