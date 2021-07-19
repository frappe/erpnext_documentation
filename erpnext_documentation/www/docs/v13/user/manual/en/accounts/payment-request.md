<!-- add-breadcrumbs -->
# Payment Request

**A Payment Request is used to request payment from a Customer for a Sales Order or Invoice.**

Payment Request is sent via email and will contain a link to a Payment Gateway if set up. You can create a payment request via a Sales Order or a Sales Invoice. A Payment Request can also be set up against a Purchase Order or a Purchase Invoice for internal records. Then, payments can be processed in bulk using a [Payment Order](/docs/v13/user/manual/en/accounts/payment-order).

To access Payment Term go to:
> Home > Accounting > Accounts Receivable > Payment Term

## 1. Prerequisites
Before creating and using Payment Request, it is advisable to create the following first:

1. [Sales Invoice](/docs/v13/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/v13/user/manual/en/accounts/purchase-invoice)
1. [Sales Order](/docs/v13/user/manual/en/selling/sales-order)
1. [Purchase Order](/docs/v13/user/manual/en/buying/purchase-order)

## 2. How to create a Payment Request
A Payment Request cannot be created manually, it is created from a Sales/Purchase Order or Invoice.

### 2.1 Creating Payment Request via Sales Order
In a Sales Order, click on Create and then click on Payment to make an advance payment. To know more about advance payment, visit the [Advance Payment Entry](/docs/v13/user/manual/en/accounts/advance-payment-entry) page.

![Payment Request From Sales Order](/docs/v13/assets/img/accounts/payment-request-from-sales-order.png)

### 2.2 Creating payment Request via Sales Invoice
In a Sales Invoice, click on Create and then click on Payment to make payment against the invoice.

![Payment Request From Sales Invoice](/docs/v13/assets/img/accounts/payment-request-from-sales-invoice.png)

Select appropriate Payment Gateway Account on Payment Request for accounts posting. Account head specified on payment gateway will
be considered to create a Journal Entry.

> Note: Invoice/Order currency and 'Payment Gateway Account' currency should be the same.

![Payment Request Details](/docs/v13/assets/img/accounts/payment-request-details.png)

### 2.3 Notifying the Customer
You can notify customer from Payment Request using [Print Format](/docs/v13/user/manual/en/setting-up/print/print-format). If the customer contact email is set, it will be fetched automatically. If not so you can set an email address in Payment Request.

![Payment Request Details](/docs/v13/assets/img/accounts/payment-request-recipient-details.png)

### 2.4 Request Mail
Here is an example request email. The URL is generated automatically if you've set up the respective payment integration. To know more about integrations, [visit this page](/docs/v13/user/manual/en/erpnext_integration).

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/v13/assets/img/accounts/pr-email.png">

### 2.5 Payment Request without using any Gateway

In case you don't want to use any integration or payment gateway and only want to send a notification, simply set the Bank Account. You'll have to compose the message accordingly with bank details. The party can then transfer the amount to the mentioned bank account.

## 3. Related Topics
1. [Payment Entry](/docs/v13/user/manual/en/accounts/payment-entry)
1. [Payment Terms](/docs/v13/user/manual/en/accounts/payment-terms)
1. [Sales Invoice](/docs/v13/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/v13/user/manual/en/accounts/purchase-invoice)

{next}