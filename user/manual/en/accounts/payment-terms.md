<!-- add-breadcrumbs -->
# Payment Terms

**A Payment Term is an agreement between the buyer and selling on how much money will be paid in what time.**

For example, 50% payment on shipping and 50% on delivery. You can save your business's payment terms on ERPNext and include it in all documents in the sales/purchase cycle. ERPNext will make all the proper general ledger entries accordingly.

You can use Payment Terms in the following documents:

- Sales Invoice
- Purchase Invoice
- Sales Order
- Purchase Order
- Quotation

Note that the introduction of Payment Terms removes "Credit Days" and "Credit Days Based On" fields in Customer/Supplier master. Payment Term contains the same information and makes it more flexible to use.

To access Payment Term go to:
> Home > Accounting > Billing > Payment Term > New

## 1. How to create a Payment Term
1. Click on New.
1. Enter a name for the Payment Term (eg: 50% post shipment).
1. Optionally, enter Invoice portion.
1. Select a due date type.
1. Enter the number of days.
1. Save.

The fields are explained as follows:

* **Payment Term Name:** (optional) The name for this Payment Term.
* **Due Date Based On:** The basis by which the due date for the Payment Term is to be calculated. There are three options:
 - Day(s) after invoice date: Due date should be calculated in days with reference to the posting date of the invoice
 - Day(s) after the end of the invoice month: Due date should be calculated in days with reference to the last day of the month in which the invoice was created
 - Month(s) after the end of the invoice month: Due date should be calculated in months with reference to the last day of the month in which the invoice was created
* **Invoice Portion:** The portion of the total invoice amount for which this Payment Term should be applied. Value given will be regarded as percentage i.e 50 = 50%.
* **Credit Days (optional):** The number of days or month credit is allowed depending on the option chosen in the Due Date Based On field. 0 means no credit allowed.
* **Description:** (optional) A brief description of the Payment Term.

### 1.2 Payment Terms In Converted Documents
When converting or copying documents in the sales/purchase cycle, the attached Payment Term(s) will not be copied. The reason for this is because the copied information might no longer be true. For example, a Quotation is created for a service costing $1000 on January 1 with payment term of "N 30" (Net payable within 30 days) and then sent to a customer. On the quotation, the due date on the invoice will be January 30. Let's say the customer agrees to the quotation of January 20 and you decide to make an invoice from the Quotation. If the Payment Terms from the Quotation is copied, the due date on the invoice will still wrongly read January 30. This issue also applies for recurring documents.

This does not mean you have manually set Payment Terms for every document. If you want the Payment Terms to be copyable, make use of the Payment Terms Template.

### 1.3 Adding Payment Terms To Documents
You can add Payments Terms in the "Payment Terms Schedule" section of the Document. Each row in the table represents a portion of the document's grand total. 

## 2. How to create a Payment Terms Template
A Payment Terms Template tells ERPNext how to populate the table in the Payment Terms Schedule section of the sales/purchase document.
You should use it if you have a set of standard Payment Terms or if you want the Payment Term(s) on a sales/purchase document to be copyable.

To create a new Payment Terms Template, navigate to the Payment Term Template from the awesome bar and click on new.

1. Enter a name for the template.
1. Add payment terms in the table rows.
1. Make sure that the total Invoice Portion adds up to 100.
1. Save.

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Z91oWYJx6yA?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

### 3. Related Topics
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
