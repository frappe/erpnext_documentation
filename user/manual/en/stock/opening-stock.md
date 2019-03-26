<!-- add-breadcrumbs -->
# Opening Stock

Opening Stock is the Stock quantity in the beginning of every accounting year of an organization. The closing Stock with the prior accounting year becomes the opening Stock with the existing accounting year.

Opening Stock can be done for serialized Items as well as non-serialized Items. To update opening stock for non-serialized Item, you should perform Stock Reconciliation. For serialized Item, you can make Stock Entry of type Material Receipt.

In both cases, you should enter "Difference/Expense Account" as **Temporary Opening** account. On submission of the document, system will debit Warehouse account which is an asset account and credit difference/expense account. Before making these entries, make sure you have enabled "Perpetual Inventory" by checking Stock Settings page.

If you are not making opening Stock Entry, you can select "Stock Adjustment" account in Difference/Expense Account field which is an expense account.

To understand Opening Stock for serialized Items visit [Stock Reconciliation](/docs/user/manual/en/setting-up/stock-reconciliation-for-non-serialized-item)

### 1. How to create a new Stock Reconciliation
1. Go to **Stock > Tools > Stock Reconciliation > New**.
2. Add the items and necessary details.
3. Save and Submit.

<div>
    <div class="embed-container">
        <iframe src="https://www.youtube.com/embed/nlHX0ZZ84Lw?end=120" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>
    </div>
</div>

#### 2. Related Topics
1. [Accounting Of Inventory Stock](/docs/user/manual/en/stock/accounting-of-inventory-stock)
1. [Stock Entry](/docs/user/manual/en/stock/stock-entry)