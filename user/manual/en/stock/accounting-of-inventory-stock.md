<!-- add-breadcrumbs -->
# Accounting Of Inventory Stock

The value of available inventory is treated as an Asset in the company's [Chart of
Accounts](/docs/user/manual/en/accounts/chart-of-accounts). To prepare a Balance Sheet, you should make the accounting entries for those assets. There are generally two different methods of
accounting for inventory.

## 1. Auto/Perpetual Inventory

In this process, for each stock transaction, the system posts relevant
accounting entries to sync stock balance and accounting balance. This is the
default setting in ERPNext for new accounts.

When you buy and receive items, those items are booked as the company’s assets
(stock-in-hand). When you sell and deliver those items, an
expense (Cost of Goods Sold) equal to the landed cost of the items is booked.
General Ledger entries are created after every stock transaction. As a result,
the value as per Stock Ledger always remains the same with the relevant account
balance. This improves the accuracy of the Balance Sheet and the Profit and Loss
statement.

To check accounting entries for a particular stock transaction,
[click here](/docs/user/manual/en/stock/perpetual-inventory)

### 1.2 Advantages of Perpetual Inventory

Perpetual Inventory system will make it easier for you to maintain the accuracy of the company's asset and expense values. Stock balances will always be synced with relevant account balances, so no more periodic manual entry needs to be done to balance them.

In case of new back-dated stock transactions or cancellation/amendment of an existing transaction, all the future Stock Ledger entries and GL Entries will
be recalculated for all items of that transaction. The same is applicable if
any cost is added to the submitted Purchase Receipt later through the Landed
Cost Voucher.

> Note: Perpetual Inventory completely depends upon the item valuation rate.
Hence, you have to be more careful entering the valuation rate while making any
incoming stock transactions like Purchase Receipt, Material Receipt, or
Manufacturing/Repack.

* * *

## 2. Periodic Inventory

In this method, accounting entries need to be created manually in order to sync stock balance and relevant account balance. The system does not create
accounting entries automatically for assets at the time of material purchases
or sales.

In an accounting period, when you buy and receive items, an expense is booked
in your accounting system. You sell and deliver some of these items.

At the end of an accounting period, the total value of items to be sold, need
to be booked as the company’s assets, often known as stock-in-hand.

The difference between the value of the items remaining to be sold and the
previous period’s stock-in-hand value can be positive or negative. If
positive, this value is removed from expenses (Cost of Goods Sold) and is
added to assets (stock-in-hand). If negative, a reverse entry
is passed.

This complete process is called **Periodic Inventory**.

If you are an existing user using Periodic Inventory and want to use Perpetual
Inventory, you need to follow [a few steps](/docs/user/manual/en/stock/migrate-to-perpetual-inventory) to migrate. 

### 3. Related Topics
1. [Perpetual Inventory](/docs/user/manual/en/stock/perpetual-inventory)
1. [Migrate to Perpetual Inventory](/docs/user/manual/en/stock/migrate-to-perpetual-inventory)