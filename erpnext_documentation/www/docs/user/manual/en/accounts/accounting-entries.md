<!-- add-breadcrumbs -->
# Accounting Entries

The concept of accounting is explained with an example given below: We will
take a "Tea Stall" as a company and see how to book accounting entries for the
business.

Mama (The Tea-stall owner) invests Rs. 25000 to start the business.
![JE](/docs/assets/img/accounts/je-1.png)

## 1. Investment
Mama invested Rs. 25000 in Company, hoping to get some profit. In other
words, company is liable to pay Rs. 25000 to Mama in the future. So, account
"Mama" is a liability account and it is credited. Company's cash balance will
be increased due to the investment. "Cash" is an asset to the company and it
will be debited.

  The company needs equipments (stove, teapot, cups, etc.) and raw materials (tea, sugar, milk, etc.) immediately. He decides to buy them from the nearest general store, "Super Bazaar" whose owner is a friend, so that he gets some credit. Equipments cost him Rs. 2800 and raw materials Rs. 2200. He pays Rs. 2000 out of the total cost which is Rs. 5000. This can be recorded in ERPNext using a [Payment Entry](/docs/user/manual/en/accounts/payment-entry).

![JE](/docs/assets/img/accounts/je-2.png)

## 2. Assets
Equipments are "Fixed Assets" (because they have a long life) and raw materials are "Current Assets" (since they are used for day-to-day
business), of the company. So, "Equipments" and "Stock in Hand" accounts have
been debited to increase the value. He pays 2000, so "Cash" account will be
reduced by that amount, hence credited and he is liable to pay Rs. 3000 to "Super
Bazaar" later, so Super Bazaar will be credited by Rs. 3000.

  Mama (who takes care of all entries) decides to book sales at the end of every day, so that he can analyze daily sales. At the end of the very first day, the tea stall sells 325 cups of tea, which gives net sales of Rs. 1625. The owner happily books his first day sales.

![JE](/docs/assets/img/accounts/si-1.png)

## 3. Income
Income has been booked in "Sales of Tea" account which has been
credited to increase the value and the same amount will be debited to "Cash"
account. Lets say, to make 325 cups of tea, it costs Rs. 800, so "Stock in
Hand" will be reduced (Cr) by Rs. 800 and expense will be booked in "Cost of goods
sold" account by same amount.

At the end of the month, the company paid the rent amount of stall (Rs. 5000) and
salary of one employee (Rs. 8000), who joined from the very first day.

![JE](/docs/assets/img/accounts/je-3.png)

## 4. Booking Profit

As month progress, company purchased more raw materials for the business.
After a month he books profit to balance the "Balance Sheet" and "Profit and
Loss Statements" statements. Profit belongs to Mama and not the company hence
its a liability for the company (it has to pay it to Mama). When the Balance
Sheet is not balanced i.e. Debit is not equal to Credit, the profit has not
yet been booked. To book profit, the profit and loss accounts have to be reset. The profit/loss is transfered to the Liability account and the profit/loss statement starts fresh. This is done using a [Period Closing Voucher](/docs/user/manual/en/accounts/period-closing-voucher).

**Explanation**: Company's net sales and expenses are Rs. 40000 and Rs. 20000
respectively. So, company made a profit of Rs. 20000. To make the profit booking
entry, "Profit or Loss" account has been debited and "Capital Account" has
been credited. Company's net cash balance is Rs. 44000 and there are some raw
materials available worth Rs. 1000.

### Related Topics
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Advance Payment Entry](/docs/user/manual/en/accounts/advance-payment-entry)
1. [Freeze Accounting Entries](/docs/user/manual/en/accounts/articles/freeze-accounting-entries)
1. [Post Dated Cheque Entry](/docs/user/manual/en/accounts/articles/post-dated-cheque-entry)
1. [Adjust Withhold Amount Payment Entry](/docs/user/manual/en/accounts/articles/adjust-withhold-amount-payment-entry)
1. [Bulk Payment Entry](/docs/user/manual/en/accounts/articles/bulk-payment-entry)
1. [Difference Entry Button](/docs/user/manual/en/accounts/articles/difference-entry-button)
