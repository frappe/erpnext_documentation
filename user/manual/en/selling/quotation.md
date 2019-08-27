<!-- add-breadcrumbs -->
# Quotation

**A quotation is an estimated cost of the products/services you're selling to your future/present customer.** 

During a sale, a customer may request for a note about the products
or services you are planning to offer along with the prices and other terms
of engagement. This has many names like "Proposal", Estimate", "Pro Forma
Invoice" or a **Quotation**.

To access the Quotation list, go to:
> Home > Selling > Sales > Quotation

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


## 1. Prerequisites
Before creating and using a Quotation, it is advised that you create the following first:

* [Customer](/docs/user/manual/en/CRM/customer)
* [Lead](/docs/user/manual/en/CRM/lead)
* [Item](/docs/user/manual/en/stock/item)

## 2. How to create a Quotation
1. Go to the Quotation list, click on New.
2. Select if the Quotation is to a Customer or a Lead from the 'Quotation To' field.
3. Enter Customer/Lead name.
1. Enter a Valid till date after which the quoted amount will be considered invalid.
1. Order Type can be Sales, Maintenance, or Shopping Cart. Shopping Cart is for website shopping cart and is not intended to be created from here.
4. Add the Items and their quantities in the items table, the prices will be fetched automatically from Item Price. You can also fetch items from an Opportunity by clicking on Get Items from > Opportunity.
5. Add additional taxes and charges as applicable.
6. Save.

You can also create a Quotation from an Opportunity shown as follows.

<img class="screenshot" alt="Make Quotation from Opportunity" src="{{docs_base_url}}/assets/img/selling/make-quote-from-opp.png">

## 3. Features

### 3.1 Address and Contact
In this section there are four fields:

* **Customer Address:** This is the Billing address of the customer.
* **Shipping Address:** Address where the items will be shipped to.
* **Contact Person:** If your customer is an organization, then you can add the person to contact in this field.
* **Territory:** Region where the customer belongs to. Default is All Territories. 

### 3.2 Currency and Price List
You can set the currency in which the quotation/sales order is to be sent. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

To know about Price Lists, [click here](/docs/user/manual/en/setting-up/price-lists).

To know about managing transactions in multiple currencies, [click here](/docs/user/manual/en/accounts/articles/managing-transactions-in-multiple-currency).

### 3.3 The Items Table
This table can be expanded by clicking on the inverted triangle present rightmost of the table.

* On selecting Item Code, the following will be fetched automatically: item name, description, any image if set, quantity default as 1, the rates. You can add discounts in the Discounts and Margin section. 
* **Under Discount and Margin** you can add extra margin for profit or give a discount. Both can be set based on either amount or percentage. The final rate will be shown below in the Rate section. You can assign an Item Tax Template created specifically for an item.
* **Item weights** will be fetched if set in the Item master.
* In **Warehouse and Reference**, the warehouse will be fetched from the Item master, this is the warehouse where your stock is present.
* Under **Planning** you can see the Projected quantity and the actual quantity present. To know more about these fields, [click here](/docs/user/manual/en/stock/projected-quantity). If you click on the 'Stock Balance' button, it'll take you to a doctype where you can generate a stock report for the item.
* **Shopping cart**, additional notes is for website transactions. Notes about the item will be fetched here when added via a shopping cart. For example: make food extra spicy. *Introduced in v12*
* **Page Break** Will create a page break just before this item when printing.

* You can insert rows below/above, duplicate, move, or delete rows in this table.

* Tip: You can also Download the items table in CSV format and Upload it to another transaction.

The total quantity, rate, and net weight of all items will be shown below the item table. The rate shown here is pre-tax.

### 3.4 Taxes and Charges
To add taxes to your Quotation, you can select a [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template) or add the taxes manually in the Sales Taxes and Charges table.

The total taxes and charges will be displayed below the table. Clicking on Tax Breakup will show all the components and amounts.

<img class="screenshot" alt="Taxes in Quotation" src="{{docs_base_url}}/assets/img/selling/quotation-taxes.png">

You can add a [Shipping Rule](/docs/user/manual/en/selling/shipping-rule) here for the items in the quotation.

To add taxes automatically via a Tax Category, visit [this page](/docs/user/manual/en/accounts/tax-category).

### 3.5 Additional Discount
To know about Additional Discount, [click here](/docs/user/manual/en/selling/articles/additional-discount)

### 3.6 Payment Terms
Sometimes payment is not done all at once. Depending on the agreement, half of the payment may be made before shipment and the other half after receiving the goods/services. You can add a Payment Terms template or add the terms manually in this section.

<img class="screenshot" alt="Payment Terms in Quotation" src="{{docs_base_url}}/assets/img/selling/quotation-payment-terms.png">

To know more about Payment Terms, [click here](/docs/user/manual/en/accounts/payment-terms).

### 3.7 Terms and Conditions
To know about Terms and Conditions, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions).

### 3.8 Print Settings
#### Letterhead
You can print your quotation/sales order on your company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when your print.

#### Print Headings
Quotations can also be titled as “Proforma Invoice” or “Proposal”.
You can do this by selecting a **Print Heading**. To create new Print Headings go to: Home > Settings > Printing > Print Heading. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

### 3.9 More Information
* **Campaign:** A Sales campaign can be associated with the quotation. A set of quotations can be part of a sales campaign.
* **Source:** A Lead Source type can be linked if quoting to a lead, whether from a campaign, from a supplier, an exhibition etc,. Select Existing Customer if quoting to a customer.
* **Supplier Quotation:** A Supplier Quotation can be linked for comparing with your current quotation to a buyer. You can get an idea of profit/loss by comparing the two.

### 3.10 Submitting the Quotation
Quotation is a “Submittable” transaction. When you click on Save, a draft is saved, on submitting, it is submitted permanently. Since you send this Quotation to
your Customer or Lead, you must freeze it so that changes are not made after
you send the Quotation.

On submitting, you can create a Sales Order or a Subscription from the Quotation using the Create button. In the Dashboard present on the top, you can go to the Sales Order linked with this Quotation. In case it didn't work out, you can set the Quotation as lost by clicking on the 'Set as Lost button'.

<img class="screenshot" alt="Submitted Quotation" src="{{docs_base_url}}/assets/img/selling/submitted-quotation.png">

### 4. Related Topics
1. [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount)

{next}
