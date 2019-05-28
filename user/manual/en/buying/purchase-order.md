<!-- add-breadcrumbs -->
# Purchase Order

**A Purchase Order is a binding contract with your Supplier that you promise to buy a set of items under given conditions.**

It is similar to a Sales Order but instead of sending it to an external party, you keep it for internal records.

## 1. How to create a Purchase Order

A Purchase Order can be automatically created from a Material Request or
Supplier Quotation.
![Purchase Order]({{docs_base_url}}/assets/img/buying/buying_flow.png)

1. In ERPNext, you can also make a Purchase Order directly by going to:

    **Buying > Purchasing > Purchase Order > New Purchase Order**
1. Select the Supplier, required by date.
1. Set the target Warehouse where the items will be delivered (optional).
1. In the items table, select the item by code, you can change the required by date for each item.
1. Set the quantity and the price will be fetched automatically if set in the Item master.
1. Set taxes.
1. Save and Submit.
    <img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/purchase-order.png">

## 2. Features

### 2.1 Address and Contact

* **Select Supplier Address**: The Supplier's billing address.
* **Select Shipping Address**: The Supplier's shipping warehouse from which they'll be sending the items.
* **Supplier and Company GSTIN**: The GST Identification Number of your Supplier and your company.
* **Place of Supply**: For GST(India), Place of Supply is necessary. It consists of the state's name and number.
* Address, Shipping Address, Contact, Contact Email will be fetched if saved in the Supplier master.

### 2.2 The Items table
* **Quantity and Rate**: When you select the Item code, it's name, description, and UOM will be fetched. The 'UOM Conversion Factor' is set to 1 by default, you can change it depending on the UOM received from the seller, more in the next section.

    'Price List Rate' will be fetched if a Standard Buying rate is set. 'Last Purchase Rate' shows the rate of the item from your last Purchase Order. Rate is fetched if set in the item master. You can attach an Item Tax Template to apply a specific tax rate to the item.

* **Item weights** will be fetched if set in the Item master else enter manually.

* **Warehouse**: The warehouse where the items will be delivered, will be auto-filled if 'Set Target Warehouse' was set in the Purchase Order. Via Blanket Order, a Blanket Order can be linked, to know more [click here](/docs/user/manual/en/selling/blanket-order). A 'Project' can be linked to track progress. A 'BOM' or Bill of Materials can also be linked to track progress.

* 'Qty as per Stock UOM' will show the current stock as per the UOM set in the Item master. 'Received Qty' will be updated when the items are billed.

* **Accounting Details**: This section is autofilled for a Purchase Order. 'Expense Account' is the account against which the PO is billed and Cost Center is the CC against which the PO is charged.

A “Required By” date on each Item: If you are expecting part delivery, your Supplier will know how much quantity to deliver at which date. This will help you from preventing over-supply. It will also help you to track how well your Supplier is doing on timeliness.

### 2.3 Purchase UOM and Stock UOM Conversion

You can change your UOM as per your stock requirements in the Purchase Order.

For example, If you have bought your raw material in large quantities with UOM - boxes, and wish to stock them in UOM - Nos; you can do so while making your Purchase Order.

1. Store UOM as Nos in the Item master. Note that the UOM in the Item master is the stock UOM.

2. In the Purchase Order mention UOM as Box. (Since material arrives in Boxes)

3. In the Warehouse and Reference section, the UOM will be pulled in as Nos (from the Item form):

 <img class="screenshot" alt="Purchase Order - UOM" src="{{docs_base_url}}/assets/img/buying/purchase-order-uom.png">

4. Mention the UOM conversion factor. For example, (1); If one box has 1 kilo.

5. Notice that the stock quantity will be updated accordingly.

 <img class="screenshot" alt="Purchase Order - UOM" src="{{docs_base_url}}/assets/img/buying/po-stock-uom.png">

### 2.4 Taxes and Charges

If your Supplier is going to charge you additional taxes or charge like a
shipping or insurance charge, you can add it here. It will help you to
accurately track your costs. Also, if some of these charges add to the value
of the product you will have to mention them in the Taxes table.

A Shipping Rule can be assigned if you know how the Supplier is shipping your order, to know more, [click here](/docs/user/manual/en/selling/shipping-rule).

You can also use templates for your taxes by selecting one under 'Taxes and Charges'. The Tax Breakup will be shown below the Purchase Taxes and Charges table.

<img class="screenshot" alt="Purchase Order Taxes" src="{{docs_base_url}}/assets/img/buying/po-taxes.png">

For example, you buy Items worth X and sell them for 1.3X. So your Customer
pays 1.3 times the tax you pay your Supplier. Since you have already paid tax
to your Supplier for X, what you owe your government is only the tax on 0.3X.

This is very easy to track in ERPNext since each tax head is also an Account.
Ideally you must create two Accounts for each type of VAT you pay and collect,
“Purchase VAT-X” (asset) and “Sales VAT-X” (liability), or something to that
effect. 

For more information on setting up your taxes see the [Purchase Taxes and Charges Template](/docs/user/manual/en/buying/purchase-taxes-template).

### 2.5 More Information
This section shows the status of the Purchase Order, percentage of items received, and percentage of items billed. If this is an Inter Company Order, the Sales Order can be linked here.

<!-- ### 2.5 Subscription
A start and end date can be selected to repeat a Purchase Order. -->

### 2.6 More
For Currency and Price List, Additional Discount, Payment Terms, Terms and Conditions, Printing Settings visit [Quotation](/docs/user/manual/en/selling/quotation). The seller's Additional Discount, Payment Terms, Terms and Conditions can be recorded in your Purchase Order.

### 3. Related Topics
1. [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation)
1. [Purchase Taxes and Charges Template](/docs/user/manual/en/buying/purchase-taxes-template)
1. [Purchase Taxes](/docs/user/manual/en/buying/purchase-taxes)
1. [Purchasing In Different Unit](/docs/user/manual/en/buying/articles/purchasing-in-different-unit)
1. [Amending Purchase Order After Submit](/docs/user/manual/en/buying/articles/amending-purchase-order-after-submit)