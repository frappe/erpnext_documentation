<!-- add-breadcrumbs -->
# Manage Foreign Exchange Difference

In ERPNext, you can create transactions in the foriegn currency as well. When creating transaction in the foreign currency, system updates current exchanage rate with respect to customer/supplier's currency and base currency on your Company. Since Exchange Rate is always flucuating, on might receive payment from the client on exchange rate different from one mentioned in the Sales/Purchase Invoice. Following is the intruction on how to manage different amount avail in payment entry due to exchange rate change.

## Add Expense Account

To mange currency difference, create Account **Exchange Gain/Loss**. This account is generally created on the Expense side of P&L statement. However, you can place it under another group as per your accounting requirement.

![Exchange Gain/Loss Ledger](/docs/v13/assets/img/articles/exchange-gain-loss-ledger.png)

## Book Payment Entry

![Auto Calculate Exchange Gain Loss](/docs/v13/assets/img/articles/exchange-gain-loss-auto-calculation.gif)

{next}
