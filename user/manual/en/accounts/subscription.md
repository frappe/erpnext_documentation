# Subscription

If you offer a service which requires renewal in the certain time period (yearly, monthly, quarterly etc.), you can use Subscription feature to track them. Subscription master captures all the details required for the auto-creation of Sales Invoice on subscription expiry.

Let's consider a use-case of ERPNext subscription itself. Our hosting plans are available on yearly basis. Each customer's account has subscription expiry date, after which customer must renew their subscription with us.

To manage client's subscription expiry and auto-generation of Sales Invoice for the renewal, we use Subscription feature.

### 1. How to create a Subscription Plan
Before you can set a Subscription, you need a Subscription Plan.

1. Go to: **Accounts > Subscription Management > Subscription Plan > New**. 
1. Enter a name for the plan.
1. Select the item that will be subscribed.
1. Select a Price Determination whether fixed or based on a Price List.
1. Set a Billing Interval.
1. Set a Billing Interval Count. If you select Day as your interval and count as 5, the billing will be done for every 5 days.
1. You can also set up payment details.
1. Save.
The subscription plan is linked to an Item, for which Sales Invoice is created.

### 2. How to set a Subscription
1. Go to: **Accounts > Subscription Management > Subscription > New**. 
1. Select a Customer.
1. Set the start date from when the subscription will be active.
1. Days Until Due is the validity of the subscription.
1. Set applicable taxes and discounts.
1. Save. 

Based on the subscription start and end date, actual dates for invoices will be calculated.

### 3. Difference Between Subscription and Auto-Repeat

Before Subscription feature was added in ERPNext, the current Auto-Repeat feature was present to be used as a Subscription.

The Auto-Repeat feature which is applicable for multiple transactions like Sales Order, Purchase Order, Invoices, Journal Entry etc. Whereas based on Subscription, only Sales Invoices are auto-created.

**Disabled**: It will stop to make auto recurring documents against the subscription

#### Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
1. [Item](/docs/user/manual/en/stock/item)
1. [Customer](/docs/user/manual/en/crm/customer)
