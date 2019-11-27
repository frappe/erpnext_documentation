<!-- add-breadcrumbs -->
# Payment Terms

**A Payment Term helps to set a schedule according to which payments will be made.**

A Payment Term defines a specific payment slab. For example, 50% payment on shipping and 50% on delivery of the item. You can save your business's payment terms on ERPNext and include it in all documents in the sales/purchase cycle. ERPNext will make all the General Ledger entries accordingly.

In ERPNext, the Payment Terms form only defines portion percentages. The actual payment schedule can easily be applied using the Payment Terms Template.

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
1. Enter the Invoice portion. If you enter 50, the portion will be 50 percent of the Invoice amount.
1. Select a Due Date type.
1. Under Credit Days enter the number of days after which the remaining amount has to be paid.
1. Save.

The fields are explained as follows:

* **Payment Term Name:** The name for this Payment Term.
* **Due Date Based On:** The basis by which the due date for the Payment Term is to be calculated. This is calculated X number of days from the **posting date** of the invoice/order. There are three options:
 - **Day(s) after invoice date**: Due date should be calculated in days with reference to the posting date of the invoice. For example, if 7 is entered on date 20th, the due date will be 27.
 - **Day(s) after the end of the invoice month**: Due date should be calculated in days with reference to the last day of the month in which the invoice was created. For example, if 7 is entered in the current month and the last day of the month is 30th, the due date will be the 7th of the next month.
 - **Month(s) after the end of the invoice month**: Due date should be calculated in months with reference to the last day of the month in which the invoice was created. For example, if 3 is entered on 20th of January, the due date will be on 20th March.
* **Invoice Portion:** The portion of the total invoice amount for which this Payment Term should be applied. Value given will be regarded as percentage i.e 50 = 50% of the invoice/orders Grand Total
* **Credit Days (optional):** The number of days or month credit is allowed depending on the option chosen in the Due Date Based On the field. 0 means no credit allowed.
* **Description:** (optional) A brief description of the Payment Term.

### 1.2 Payment Terms in Converted Documents
When converting or copying documents in the sales/purchase cycle, the attached Payment Term(s) will be copied. When creating a Sales Order from a Quotation, the Due Date in the Payment Terms will be according to the Quotation, this needs to be updated.

For ease of use, you can also set a Payment Terms Template and simply reselect it.

### 1.3 Adding Payment Terms To Documents

Once you have composed Payment Terms Template, you can use them in sales and purchase transactions. Based on the value defined for Payment Terms and transaction value, the payment schedule will be defined, with Due Date for each payment slab.

![Payment Schedule]({{docs_base_url}}/assets/img/accounts/payment-term-table.png)

Note: The Payment Schedule can be shown in the Print View using the [Print Format Builder](/docs/user/manual/en/setting-up/print/print-format-builder).

### 2. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
