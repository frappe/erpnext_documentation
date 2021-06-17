<!-- add-breadcrumbs -->
# Subscription

If you offer a service that requires renewal in a certain time period or you pay some monthly expenses like rent (yearly, monthly, quarterly, etc.), you can use the Subscription feature in ERPNext to track them. The Subscription master captures all the details required for the auto-creation of Sales or Purchase Invoices.

Let's consider a use-case of ERPNext subscription itself. Our hosting plans are available on a yearly basis. Each Customer's account has a subscription expiry date, after which customers must renew their subscription with us.

To manage the client's subscription expiry and auto-generation of Sales Invoice for the renewal, we use the Subscription feature.

To access the Subscription list, go to:
> Home > Accounting > Subscription Management > Subscription

## 1. Prerequisites
Before creating and using a Subscription, it is advisable to create the following first:

1. [Subscription Plan](/docs/user/manual/en/accounts/subscription-plan)

## 2. How to set a Subscription
1. Go to the Subscription list and click on New.
1. Select Party Type as 'Customer' or 'Supplier' and select the party.
1. Set the Start Date from when the subscription will be active.
1. Optionally you can also enter the subscription end date if you know it before hand.
1. Days Until Due is the number of days within which Customer has to pay a generated Sales Invoice.
1. Select the [Subscription Plans](/docs/user/manual/en/accounts/subscription-plan).
1. Save.
 ![Subscription](/docs/v12/assets/img/accounts/subscription.png)

Based on the subscription start and end date, actual dates for invoices will be calculated.

## 3. Features
### 3.1 Trial Period
If you're offering a trial period for the subscription, a Trial Period Start Date and a Trial Period End Date can be set. Invoices will not be generated during the trial period and the Subscription status will show 'Trialling'.
![Subscription Trial](/docs/v12/assets/img/accounts/subscription-trial.png)

### 3.2 Cancel Auto Renewal
On enabling the 'Cancel At End Of Period' the Subscription will be canceled at the end of its period. For example, if it is a yearly subscription, the system will stop generating invoices after one year of subscription.

### 3.3 Taxes
You can apply Taxes to a Subscription by using a Sales Taxes and Charges Template. Visit the [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template) page to know more.

### 3.4 Applying discounts
You can apply additional discounts on the Subscription based on Grand Total (pre tax) or Net Total (post tax). A discount percentage can also be set. For example, a discount of 2% on 12,000 would be 240 in discount.
 ![Subscription Discount](/docs/v12/assets/img/accounts/subscription-discount.png)
Visit the [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) page for more details.

### 3.5 Automatically create invoices
Based on the [Subscription Plans](/docs/user/manual/en/accounts/subscription-plan) interval, invoices will be created automatically. The 'Generate Invoice At Beginning Of Period' needs to be enabled if you want to generate invoices as soon as the subscription is active. If "Generate New Invoices Past Due Date" is enabled then new invoices will keep on generating even though current invoice is unpaid or past due date. If "Generate Invoice Early" is enabled, an invoice will be generated before the end of the period by the number of days entered in "Generate Invoice Days Early."
 ![Subscription Invoices](/docs/v12/assets/img/accounts/subscription-invoices.png)

### 3.6 Follow Calendar Months
If 'Follow Calendar Months' is enabled then proper calendar months will be followed even if the Subscription Start Date is in the middle of the month. For Eg: Suppose billing interval is 'Month' and billing interval count is 3 in subscription plan and Subscription Start Date is '15-04-2020' then if 'Follow Calendar Months' is checked then first invoice will be generated for '15-04-2020' to '30-06-2020' rather than '15-04-2020' to '14-07-2020'

### 3.8 Canceling a Subscription
If the Customer decides to cancel a Subscription, it can be canceled in the system using the **Cancel Subscription**. The system will stop generating invoices when a Subscription is canceled.
 ![Subscription Cancel](/docs/v12/assets/img/accounts/subscription-cancel.png)

### 3.9 Updating a Subscription
Clicking on the **Fetch Subscription Updates** button will update the Subscription with the latest generated invoices.

## 4. Difference Between Subscription and Auto-Repeat

| Auto Repeat | Subscription |
|---------------|---------------|
| Is applicable on transactions | Is applicable on Items |
| Multiple transactions like Sales Order, Purchase Order, Invoices, Journal Entry, etc. are auto created | Only Sales Invoices and Purchase  Invoices are auto-created |
| Has only a few controls | Has many control options to define trials, billing due date, and creating Subscription Plans |

### 5. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
1. [Item](/docs/user/manual/en/stock/item)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Subscription Plan](/docs/user/manual/en/accounts/subscription-plan)
