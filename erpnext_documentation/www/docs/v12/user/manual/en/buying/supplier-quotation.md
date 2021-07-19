<!-- add-breadcrumbs -->
# Supplier Quotation

**A Supplier Quotation is document by a potential supplier specifying the cost of goods or services they'll provide within a specified period.**

A Supplier Quotation may also contain terms of sale, terms of payment, and warranties. Acceptance of quotation by the buyer can be considered as an agreement binding on both parties.

![Buying Flow](/docs/v12/assets/img/buying/buying_flow_sq.png)

To access Supplier Quotation, go to:
> Home > Buying > Purchasing > Supplier Quotation

## 1. Prerequisites
Before creating and using a Supplier Quotation, it is advised that you create the following first:

* [Supplier](/docs/user/manual/en/buying/supplier)
* [Item](/docs/user/manual/en/stock/item)

## 2. How to create a Supplier Quotation

### 2.1 Supplier Quotation from Material Request

You can make a supplier quotation from a Material Request:
![Supplier Quotation from Material Receipt]({{docs_base_url}}/v12/assets/img/buying/supplier-quotation-from-mr.png)

Or:

A Supplier Quotation can be created from a [Supplier master](/docs/user/manual/en/buying/supplier).

Or:

The supplier can submit you a quotation himself via ERPNext. To know more about this, see section visit the [Request for Quotation page](/docs/user/manual/en/buying/request-for-quotation#4-creating-a-supplier-quotation-after-rfq).

### 2.2 Creating a Supplier Quotation manually
1. You can also make a Supplier Quotation directly from:

    **Buying > Purchasing > Supplier Quotation > New**.
1. Select the Supplier who sent you the quotation.
1. The Address and Contact will be fetched if you've saved it in the supplier master.
1. Enter the Item code, select the quantity. Rate will be fetched if you've set the Standard Buying rate for the item in [Item Price](/docs/v12/user/manual/en/stock/item-price).
    <img class="screenshot" alt="Supplier Quotation" src="{{docs_base_url}}/v12/assets/img/buying/supplier-quotation.png">

If you have multiple Suppliers who supply you with the same Item, you
usually send out a [Request for Quotation](/docs/user/manual/en/buying/request-for-quotation) to various Suppliers. In
many cases, especially if you have centralized buying, you may want to record all the quotes so that:

  * You can easily compare prices in the future
  * Audit whether all Suppliers were given the opportunity to quote.

Supplier Quotations are not necessary for most small businesses. Always
evaluate the cost of collecting information to the value it really provides!
As a recommendation, you can do this only for high value items.

## 3. Features
### 3.1 Taxes and Charges
If your Supplier is going to charge you additional taxes or charge like a shipping or insurance charge, you can add it here. This will help you accurately track your costs. Also, if some of these charges add to the value of the product you will have to mention them in the Taxes table. You can also use templates for your taxes. For more information on setting up your taxes see the [Purchase Taxes and Charges Template](/docs/user/manual/en/buying/purchase-taxes-and-charges-template).

### 3.2 More
There are fields for Tax Category, Shipping Rule, Purchase Taxes and Charges Template, Discount, Terms and Conditions, Printing Settings. You can fill these fields for your record. Visit the [Quotation](/docs/user/manual/en/selling/quotation) page to know more about these sections. Note that the details you fill here like Shipping Rule, taxes, Discount, Terms and Conditions etc., are from your supplier and can be recorded for accurate tracking.

Note:

- Tax Category will be fetched from supplier master if set
- Print settings is for making changes to the supplier quotation print
- The Terms and Conditions here are your supplier's
- The supplier quotation can be linked to material requests using the 'Link to material requests' button

### 3.3 After Submitting
The following items can be created after submitting a Supplier Quotation:

* Purchase Order - A Purchase Order if you agree with the supplier's quotation.
* Quotation - A quotation to your customer.
* Auto Repeat - Auto Repeat the supplier quotation at specified intervals.

### 4. Related Topics
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Supplier Group](/docs/user/manual/en/buying/supplier-group)
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Request for Quotation](/docs/user/manual/en/buying/request-for-quotation)

{next}