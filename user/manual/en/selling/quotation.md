<!-- add-breadcrumbs -->
# Quotation

**A quotation is an estimated cost of the products/services you're selling to your future/present customer.** 

During a sale, a customer may request for a note about the products
or services you are planning to offer along with the prices and other terms
of engagement. This has many names like "Proposal", Estimate", "Pro Forma
Invoice" or a **Quotation**.

A typical sales flow looks like:

<img class="screenshot" alt="Make Quotation from Opportunity" src="{{docs_base_url}}/assets/img/selling/selling-flow-quo.png">

A Quotation contains details about:

  * The recipient of the Quotation
  * The Items and quantities you are offering.
  * The rates at which they are offered.
  * The taxes applicable.
  * Other charges (like shipping, insurance) if applicable.
  * The validity of contract.
  * The time of delivery.
  * Other conditions.

> Tip: Images look great on Quotations. Make sure your items have an image attached.


## 1. How to create a Quotation
1. Go to **Selling > Sales > Quotation > New Quotation**.
2. Select if the Quotation is to a Customer or a Lead from the 'Quotation To' field.
3. Enter Customer/Lead name.
1. Enter a Valid till date after which the quoted amount will be considered invalid.
1. Order Type can be Sales, Maintenance, or Shopping Cart. Shopping Cart is for website shopping cart and is not intended to be created from here.
4. Add the Items and their quantities in the items table, the prices will be fetched automatically from Item Price. You can also fetch items from an Opportunity by clicking on Get Items from > Opportunity.
5. Add additional taxes and charges as applicable.
6. Save.

You can also create a Quotation from an Opportunity shown as follows.

<img class="screenshot" alt="Make Quotation from Opportunity" src="{{docs_base_url}}/assets/img/selling/make-quote-from-opp.png">

## 2. Features

### 2.1 Address and Contact
In this section there are four fields:

* **Customer Address:** This is the Billing address of the customer.
* **Shipping Address:** Address where the items will be shipped to.
* **Contact Person:** If your customer is an organization, then you can add the person to contact in this field.
* **Territory:** Region where the customer belongs to. Default is All Territories. 

### 2.2 Currency and Price List
To know about Currency and Price List, [click here](/docs/user/manual/en/selling/articles/currency-and-price-list)

### 2.3 The Items Table
This table can be expanded by clicking on the inverted triangle present rightmost of the table.

* On selecting Item Code, the following will be fetched automatically: item name, description, any image if set, quantity default as 1, the rates. You can add discounts in the Discounts and Margin section. 
* **Under Discount and Margin** you can add extra margin for profit or give a discount. Both can be set based on either amount or percentage. The final rate will be shown below in the Rate section. You can assign an Item Tax Template created specifically for an item.
* **Item weights** will be fetched if set in the Item master.
* In **Warehouse and Reference**, the warehouse will be fetched from the Item master, this is the warehouse where your stock is present.
* Under **Planning** you can see the Projected quantity and the actual quantity present. To know more about these fields, [click here](/docs/user/manual/en/stock/projected-quantity). If you click on the 'Stock Balance' button, it'll take you to a doctype where you can generate a stock report for the item.
* **Shopping cart**, additional notes is for website transactions. Notes about the item will be fetched here when added via a shopping cart. For example: make food extra spicy. *Introduced in v12*
* **Page Break** will be useful when printing, it's present in the Print Format section.

* You can insert rows below/above, duplicate, move, or delete rows in this table.

* Tip: You can also Download the items table in CSV format and Upload it to another transaction.

The total quantity, rate, and net weight of all items will be shown below the item table. The rate shown here is pre-tax.

### 2.4 Taxes and Charges
To know about setting up taxes visit [this page](/docs/user/manual/en/setting-up/setting-up-taxes).
To know about Taxes and Charges in a quotation, [click here](/docs/user/manual/en/selling/articles/taxes-and-charges)

### 2.5 Additional Discount
To know about Additional Discount, [click here](/docs/user/manual/en/selling/articles/additional-discount)

### 2.6 Payment Terms
To know about Payment Terms, [click here](/docs/user/manual/en/selling/articles/payment-terms)

### 2.7 Terms and Conditions
To know about Terms and Conditions, [click here](/docs/user/manual/en/selling/articles/terms-and-conditions)

### 2.8 Print Settings
To know about Print Settings, [click here](/docs/user/manual/en/selling/articles/print-settings)

### 2.9 More Information
* **Campaign:** A Sales campaign can be associated with the quotation. A set of quotations can be part of a sales campaign.
* **Source:** A Lead Source type can be linked if quoting to a lead, whether from a campaign, from a supplier, an exhibition etc,. Select Existing Customer if quoting to a customer.
* **Supplier Quotation:** A Supplier Quotation can be linked for comparing with your current quotation to a buyer. You can get an idea of profit/loss by comparing the two.

### 2.10 Submitting the Quotation
Quotation is a “Submittable” transaction. When you click on Save, a draft is saved, on submitting, it is submitted permanently. Since you send this Quotation to
your Customer or Lead, you must freeze it so that changes are not made after
you send the Quotation.

On submitting, you can create a Sales Order or a Subscription from the Quotation using the Create button. In the Dashboard present on the top, you can go to the Sales Order linked with this Quotation. In case it didn't work out, you can set the Quotation as lost by clicking on the 'Set as Lost button'.

<img class="screenshot" alt="Submitted Quotation" src="{{docs_base_url}}/assets/img/selling/submitted-quotation.png">

### 3. Related Topics
1. [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Lead](/docs/user/manual/en/CRM/lead)

{next}
