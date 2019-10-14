<!-- add-breadcrumbs -->
# Payment Terms

**A Payment Term is an agreement between the buyer and seller on how much money will be paid in what time.**

For example, 50% payment on shipping and 50% on delivery of the item. You can save your business's payment terms on ERPNext and include it in all documents in the sales/purchase cycle. ERPNext will make all the General Ledger entries accordingly.

In ERPNext, the Payment Terms form only defines portion percentages, the actual Payment Terms can easily applied using the Payment Terms Template.

You can use Payment Terms in the following documents:

- Sales Invoice
- Purchase Invoice
- Sales Order
- Purchase Order
- Quotation

To access Payment Term go to:
> Home > Accounting > Accounting Masters > Payment Term

Note that the introduction of Payment Terms removes "Credit Days" and "Credit Days Based On" fields in Customer/Supplier master. Payment Term contains the same information and makes it more flexible to use.

![Payment Terms]({{docs_base_url}}/assets/img/accounts/payment-terms.png)

## 1. How to create a Payment Term
1. Go to the Payment Term list and click on New.
1. Enter a name for the Payment Term (eg: 50% post shipment).
1. Enter the Invoice portion. If you enter 30, the portions will be 30 and 70 percent of the Invoice amount.
1. Select a Due Date type.
1. Under Credit Days enter the number of days after which the remaining amount has to be paid.
1. Save.

The fields are explained as follows:

* **Payment Term Name:** The name for this Payment Term.
* **Due Date Based On:** The basis by which the due date for the Payment Term is to be calculated. This is calculates X number of days from the **posting date** of the invoice/order. There are three options:
 - Day(s) after invoice date: Due date should be calculated in days with reference to the posting date of the invoice
 - Day(s) after the end of the invoice month: Due date should be calculated in days with reference to the last day of the month in which the invoice was created
 - Month(s) after the end of the invoice month: Due date should be calculated in months with reference to the last day of the month in which the invoice was created
* **Invoice Portion:** The portion of the total invoice amount for which this Payment Term should be applied. Value given will be regarded as percentage i.e 50 = 50%.
* **Credit Days (optional):** The number of days or month credit is allowed depending on the option chosen in the Due Date Based On field. 0 means no credit allowed.
* **Description:** (optional) A brief description of the Payment Term.

### 1.2 Payment Terms in Converted Documents
When converting or copying documents in the sales/purchase cycle, the attached Payment Term(s) will be copied. When creating a Sales Order from a Quotation, the Due Date in the Payment Terms will be according to the Quotation, this needs to be updated.

For ease of use, you can also set a Payment Terms Template and simply reselect it.

### 1.3 Adding Payment Terms To Documents
You can add Payments Terms in the "Payment Terms Schedule" section of the Document. Each row in the table represents a portion of the document's grand total. 

### 2. Related Topics
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
