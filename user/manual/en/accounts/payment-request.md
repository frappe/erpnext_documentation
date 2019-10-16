<!-- add-breadcrumbs -->
# Payment Request

**A Payment Request is used to request payment for an order or an invoice.**

Payment Request is sent via email and will contain a link to a Payment Gateway if set up. You can create a payment request via Sales Order or Sales Invoice. A Payment Request can also be set up against a Purchase Order or a Purchase Invoice for internal records. Then, payments can be processed in bulk using a [Payment Order](/docs/user/manual/en/accounts/payment-order).

To access Payment Term go to:
> Home > Accounting > Accounts Receivable > Payment Term

## 1. Prerequisites
Before creating and using Payment Request, it is advisable to create the following first:

1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)

## 2. How to create a Payment Request
A Payment Request cannot be created manually, it is created from a Sales/Purchase Order or Invoice.

### 2.1 Creating Payment Request via Sales Order
<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-from-so.png">

### 2.2 Creating payment Request via Sales Invoice
<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-from-si.png">

Select appropriate Payment Gateway Account on Payment Request. Account head specified on payment gateway will 
be considered to create a Journal Entry.

> Note: Invoice/Order currency and 'Payment Gateway Account' currency should be the same.

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-details-1.png">

### 2.3 Notifying the Customer
You can notify customer from Payment Request using [Print Format](/docs/user/manual/en/setting-up/print/print-format). If the customer contact email is set, it will be fetched automatically. If not so you can set an email address in Payment Request. 

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-details-2.png">

### 2.4 Request Mail
Here is an example request email. The URL is generated automatically if you've set up the respective payment integration. To know more about integrations, [visit this page](/docs/user/manual/en/erpnext_integration).

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-email.png">

### 2.5 Payment Request without using any Gateway

In case you don't want to use any integration or payment gateway, simply set the Bank Account. You'll have to compose the message accordingly with bank details. The party can then transfer the amount to the mentioned bank account.

## 3. Related Topics
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payment Terms](/docs/user/manual/en/accounts/payment-terms)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)