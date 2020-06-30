<!-- add-breadcrumbs -->
#Calculation of Valuation Rate as per FIFO and Moving Average method

**Valuation Rate** of an item is calculated based on the total expense incurred to make the product available for sale like freight, labour, cost of raw materials, etc.

In ERPNext, the Valuation Rate is calculated based on the valuation method selected for the particular item.

An item can have either **FIFO** or **Moving Average** selected as a valuation method.

Consider the following example to know how it impacts your stock:

| Date | Transaction | Qty | Unit Cost |
|--|--|--|--|
| 1-4-2020 | Purchase | 10 | 100  |
| 6-4-2020 | Purchase | 20 | 120  |
| 10-4-2020 | Sale | 15 | ? |


## Calculating Valuation Rate at the time of sale:

### As per FIFO:

Since this is FIFO, we will consume quantities from the _earliest_ transactions, therefore, to make a sale of 15 qty, we will take 10 qty from the first transaction and 5 qty from the second one.

(10 * 100) + (5 * 120) = **1600** which leaves us 15 qty in stock at cost of 120 amounting to **1800**.

### As per Moving Average:

In the Moving Average method, the value of an item is _recalculated_  _every time_ when an item is acquired. This is done by adding the cost of the newly acquired items to the existing inventory’s value and then dividing it by the total quantity available.

( (10 * 100) + (20 * 120) ) / 30 = **113.33**

To make a sale of 15 qty, we will directly multiply it by the average value we received just now.

15 * 113.33 = **1700** which leaves us 15 qty in stock amounting to **1700**.

If you check, even though the quantity is same the stock value is different but both amounts to a total of 3400 only.
