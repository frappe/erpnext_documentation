<!-- add-breadcrumbs -->
# Recurring Orders and Invoices

If you have a contract with a **Customer** where you bill the Customer on a monthly, quarterly, half-yearly or annual basis, you should use recurring feature in orders and invoices.

## 1. Consider a scenario

Subscription for your hosted ERPNext account requires yearly renewal. We use Sales Order for generating proforma invoices. To automate proforma invoicing for renewal, we set original Sales Order as recurring. Recurring proforma invoice is created automatically just before customer's account is about to expire, and requires renewal. This recurring Proforma Invoice is also emailed automatically to the customer.

Feature of setting document as recurring is available in Sales Order, Sales Invoice, Purchase Order and Purchase Invoice.

## 2. How to create recurring orders/invoices
Option to set document as recurring will be visible only after it's submitted. This is the **Auto Repeat** option.

1. Click on the + button next to Auto Repeat.
1. Select the Reference Doctype.
1. Select the Reference Document.
1. Set the Start Date and End Date(optional).
1. Select the frequency whether daily, weekly, etc,.
1. Save.

Here is a explanation of the fields:

* **From Date and To Date:** This defines contract period with the customer.
* **Repeat on the Day of Month:** If recurring type is set as Monthly, then it will be day of the month on which recurring invoice will be generated.
* **Repeat on Last Day of the Month:** Recurring invoices will be created on the last day of every month.
* **Notify by Email:** Email Addresses (separated by comma) on which recurring invoice will be emailed when auto-generated.

For more details about Auto Repeat [Click Here](/docs/user/manual/en/setting-up/automation/auto-repeat)

## 3. Exception Handling

In a situation where recurring invoice is not created successfully, user with System Manager role is notified about it via email. Failure in creation of recurring invoice could be due to multiple reasons like wrong Email Address mentioned in the Email Notification field in Recurring section etc.

On receipt of notification, if cause of failure is fixed (like correcting Email Address) within 24 hours, then recurring invoice will be generated automatically. If issue is not fixed within the said time, then document should be created for that month/year manually.

### 4. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
