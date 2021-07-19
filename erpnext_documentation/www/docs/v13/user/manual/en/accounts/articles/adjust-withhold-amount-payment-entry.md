<!-- add-breadcrumbs -->

# Adjust Withhold Amount in the Payment Entry

Let's assume that outstanding against a Sales Invoice is 20,000. When client makes payment, they will only pay 19,600. Rest 400 needs to be booked under tax withhold account. You can manage this scenario as described below.

## Step 1: Setup Withhold Account

[Create a Withhold Account](/docs/v13/user/manual/en/accounts/chart-of-accounts#1-how-to-createedit-accounts) in your Chart of Accounts.

## Step 2: Payment Entry

To create Payment Entry, go to unpaid Sales Invoice and create click on Make Payment button.

### Step 2.1: Enter Payment Amount

Enter Payment Amount as 19,600.

![Paid Amount in Payment Entry](/docs/v13/assets/img/articles/paid-amount-in-payment-entry.png)

### Step 2.2: Allocate Against Sales Invoice

Against Sales Invoice, allocate 20,000 (explained in GIF below).

### Step 2.3: Add Deduction/Loss Account

You can notice that there is a difference of 400 in the Payment Amount and the Amount Allocated against Sales Invoice. You can book this difference account under Withhold Account.

![Tax Withheld Adjustment in Payment Entry](/docs/v13/assets/img/articles/tax-withheld-adjustment-in-payment-entry.gif)

 Following same steps, you can also manage difference availed due to Currency Exchange Gain/Loss.

{next}
