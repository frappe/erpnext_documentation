<!-- add-breadcrumbs -->
# Subscription

If you offer a service that requires renewal in a certain time period (yearly, monthly, quarterly, etc.), you can use the Subscription feature in ERPNext to track them. The Subscription master captures all the details required for the auto-creation of Sales Invoice on subscription expiry.

Let's consider a use-case of ERPNext subscription itself. Our hosting plans are available on a yearly basis. Each Customer's account has a subscription expiry date, after which customers must renew their subscription with us.

To manage the client's subscription expiry and auto-generation of Sales Invoice for the renewal, we use the Subscription feature.

To access the Subscription list, go to:
> Home > Accounts > Subscription Management > Subscription

## 1. Prerequisites
Before creating and using a Subscription, it is advisable to create the following first:

1. [Subscription Plan](/docs/user/manual/en/accounts/subscription-plan)

## 2. How to set a Subscription
1. Go to the Subscription list and click on New. 
1. Select a Customer.
1. Set the Start Date from when the subscription will be active.
1. Days Until Due is the number of days within which Customer has to pay a generated Sales Invoice.
1. Select the [Subscription Plans](/docs/user/manual/en/accounts/subscription-plan).
1. Save. 
 ![Subscription](/docs/assets/img/accounts/subscription.png)

Based on the subscription start and end date, actual dates for invoices will be calculated.

## 3. Features
### 3.1 Trial Period
If you're offering a trial period for the subscription, a Trial Period Start Date and a Trial Period End Date can be set. Invoices will not be generated during the trial period and the Subscription status will show 'Trialling'.
![Subscription Trial](/docs/assets/img/accounts/subscription-trial.png)

### 3.2 Cancel Auto Renewal
On enabling the 'Cancel At End Of Period' the Subscription will be canceled at the end of its period. For example, if it is a yearly subscription, the system will stop generating invoices after one year of subscription.

### 3.3 Taxes
You can apply Taxes to a Subscription by using a Sales Taxes and Charges Template. Visit the [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template) page to know more. 

### 3.4 Applying discounts
You can apply additional discounts on the Subscription based on Grand Total (pre tax) or Net Total (post tax). A discount percentage can also be set. For example, a discount of 2% on 12,000 would be 240 in discount.
 ![Subscription Discount](/docs/assets/img/accounts/subscription-discount.png)
Visit the [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) page for more details.

### 3.5 Automatically create invoices
Based on the [Subscription Plans](/docs/user/manual/en/accounts/subscription-plan) interval, invoices will be created automatically. The 'Generate Invoice At Beginning Of Period' needs to be enabled if you want to generate invoices as soon as the subscription is active.
 ![Subscription Invoices](/docs/assets/img/accounts/subscription-invoices.png)

### 3.6 Canceling a Subscription
If the Customer decides to cancel a Subscription, it can be canceled in the system using the **Cancel Subscription**. The system will stop generating invoices when a Subscription is canceled.
 ![Subscription Cancel](/docs/assets/img/accounts/subscription-cancel.png)

### 3.7 Updating a Subscription
Clicking on the **Fetch Subscription Updates** button will update the Subscription with the latest generated invoices.

## 4. Difference Between Subscription and Auto-Repeat

| Auto Repeat | Subscription |
|---------------|---------------|
| Is applicable on transactions | Is applicable on Items |
| Multiple transactions like Sales Order, Purchase Order, Invoices, Journal Entry, etc. are auto created | Only Sales Invoices are auto-created |
| Has only a few controls | Has many control options to define trials, billing due date, and creating Subscription Plans |

### 5. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
1. [Item](/docs/user/manual/en/stock/item)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Subscription Plan](/docs/user/manual/en/accounts/subscription-plan)