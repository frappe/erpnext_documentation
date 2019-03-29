<!-- add-breadcrumbs -->
# Purchase Order

A Purchase Order usually a binding contract with your Supplier that you promise to buy a set of Items under the given conditions. It is analogous to a Sales Order. 

### 1. How to create a Purchase Order

A Purchase Order can be automatically created from a Material Request or
Supplier Quotation.
![Purchase Order]({{docs_base_url}}/assets/img/buying/buying_flow.png)

1. In ERPNext, you can also make a Purchase Order directly by going to:

    **Buying > Purchasing > Purchase Order > New Purchase Order**
1. Select the Supplier, required by date.
1. Set the target Warehouse where the items will be delivered.
1. In the items table, select the item by code, you can change the required by date.
1. Set the quantity and the price will be fetched automatically.
1. Set taxes.
1. Save and Submit.
    <img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/purchase-order.png">

Entering a Purchase Order is very similar to a Purchase Request, the additional fields
you will have to set are:

  1. Supplier.
  1. A “Required By” date on each Item: If you are expecting part delivery, your Supplier will know how much quantity to deliver at which date. This will help you from preventing over-supply. It will also help you to track how well your Supplier is doing on timeliness.

### 2. Features

#### 2.1 Taxes and Charges

If your Supplier is going to charge you additional taxes or charge like a
shipping or insurance charge, you can add it here. It will help you to
accurately track your costs. Also, if some of these charges add to the value
of the product you will have to mention them in the Taxes table. You can also
use templates for your taxes. For more information on setting up your taxes
see the Purchase Taxes and Charges Template.

#### 2.2 Value Added Taxes (VAT)

Many a times, the tax paid by you to a Supplier, for an Item, is the same tax
which you collect from your Customer. In many regions, what you pay to your
government is only the difference between what you collect from your Customer
and what you pay to your Supplier. This is called Value Added Tax (VAT).

#### 2.3 Add Taxes in Purchase Order
Add the tax rate:
<img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/add_taxes_to_doc.png">

The following screenshot shows Tax break-up:
<img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/show_tax_breakup.png">

For example you buy Items worth X and sell them for 1.3X. So your Customer
pays 1.3 times the tax you pay your Supplier. Since you have already paid tax
to your Supplier for X, what you owe your government is only the tax on 0.3X.

This is very easy to track in ERPNext since each tax head is also an Account.
Ideally you must create two Accounts for each type of VAT you pay and collect,
“Purchase VAT-X” (asset) and “Sales VAT-X” (liability), or something to that
effect. Please contact your accountant if you need more help or post a query
on our forums!

#### 2.4 Purchase UOM and Stock UOM Conversion

You can change your UOM as per your stock requirements in the Purchase Order
form.

For example, If you have bought your raw material in large quantities with UOM
-boxes, and wish to stock them in UOM- Nos; you can do so while making your
Purchase Order.

1. Store UOM as Nos in the Item form. Note that the UOM in the Item form is the stock UOM.

2. In the Purchase Order mention UOM as Box. (Since material arrives in
Boxes)

3. In the Warehouse and Reference section, the UOM will be pulled in as
Nos (from the Item form):

    <img class="screenshot" alt="Purchase Order - UOM" src="{{docs_base_url}}/assets/img/buying/purchase-order-uom.png">

4. Mention the UOM conversion factor. For example, (100); If one box has
100 pieces.  

5. Notice that the stock quantity will be updated accordingly.

6. Save and Submit the Form.

#### 3. Related Topics
1. [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation)
1. [Purchase Taxes](/docs/user/manual/en/buying/purchase-taxes)
1. [Purchasing In Different Unit](/docs/user/manual/en/buying/articles/purchasing-in-different-unit)
1. [Amending Purchase Order After Submit](/docs/user/manual/en/buying/articles/amending-purchase-order-after-submit)