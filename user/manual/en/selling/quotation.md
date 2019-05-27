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
You can set the currency in which the quotation is to be sent. If you set a Pricing List, then the item prices will be fetched from that list. Ticking on Ignore Pricing Rule will ignore the Pricing Rules set in Accounts > Pricing Rule.

The rates you quote may depend on two things.

  * **The Price List**: If you have multiple Price Lists, you can select a Price List or tag it to the Customer (so that it is auto-selected). Your Item prices will automatically be updated from the Price List. For details refer [Price List](/docs/user/manual/en/setting-up/price-lists)

  * **The Currency**: If you are quoting to a Customer in a different currency, you will have to update the conversion rates to enable ERPNext to save the information in your standard Currency. This will help you to analyze the value of your Quotations in standard Currency.

### 2.3 The Items Table
This table can be expanded by clicking on the inverted triangle present rightmost of the table.

* On selecting Item Code, the following will be fetched automatically: item name, description, any image if set, quantity default as 1, the rates. You can add discounts in the Discounts and Margin section. 
* You can add extra margin for profit or give a discount. Both can be set based on either amount or percentage. The final rate will be shown below in the Rate section. You can assign an Item Tax Template created specifically for an item.
* Item weights will be fetched if set in the Item master.
* The warehouse will be fetched from the Item master, this is the warehouse where your stock is present.
* Under Planning you can see the Projected quantity and the actual quantity present. To know more about these fields, [click here](/docs/user/manual/en/stock/projected-quantity). If you click on the 'Stock Balance' button, it'll take you to a doctype where you can generate a stock report for the item.
* Shopping cart, additional notes is for website transactions. Notes about the item will be fetched here when added via a shopping cart. For example: make food extra spicy. *Introduced in v12*
* Page Break will be useful when printing, it's present in the Print Format section.

* You can insert rows below/above, duplicate, move, or delete rows in this table.

* Tip: You can also Download the items table in CSV format and Upload it to another transaction.

The total quantity, rate, and net weight of all items will be shown below the item table. The rate shown here is pre-tax.

### 2.4 Taxes and Charges
Tax category is linked to [Tax Rule](/docs/user/manual/en/accounts/tax-rule). This Tax Category can be assigned to a Customer, so when that customer is selected, the Tax Category will be fetched. This will fetch the Sales Tax Template linked to the Tax Rule. Hence, the rows in the Tax table will be automatically filled. Tax Category can be used to group customers to whom same tax will be applied. For example: Government, NGO, commercial, etc,.

<img class="screenshot" alt="Tax Category" src="{{docs_base_url}}/assets/img/selling/tax-category.gif">

You can add a [Shipping Rule](/docs/user/manual/en/selling/shipping-rule) here for the items in the quotation. To add taxes to your Quotation, you can select a **Sales Taxes and Charges Template** or add the taxes manually in the Sales Taxes and Charges table. The total taxes and charges will be displayed below the table. Clicking on Tax Breakup will show all the components and amounts.

<img class="screenshot" alt="Taxes in Quotation" src="{{docs_base_url}}/assets/img/selling/quotation-taxes.png">

To understand taxes in detail visit [this page](/docs/user/manual/en/setting-up/setting-up-taxes).

### 2.5 Additional Discount
Other than offering discount per item, you can add a discount to the whole quotation in this section. This discount could be based on the Grand Total i.e., post tax/charges or Net total i.e., pre tax/charges. The additional discount can be applied as a percentage or an amount.

Read [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount) for more details.

### 2.6 Payment Terms
Sometimes payment is not done all at once. Depending on the agreement, half of the payment may be made before shipment and the other half after receiving the goods/services. You can add a Payment Terms template or add the terms manually in this section. To know more about Payment Terms, [click here](/docs/user/manual/en/accounts/payment-terms).

<img class="screenshot" alt="Payment Terms in Quotation" src="{{docs_base_url}}/assets/img/selling/quotation-payment-terms.png">


### 2.7 Terms and Conditions

Each Quotation must ideally contain a set of terms of your contract. Terms and conditions are usually included to define terms of service, conditions for using any service or to even limit responsibilities of the seller in case any harm is caused to the buyer due to using the provided goods or services.  It is
usually a good idea to make template(s) of your Terms and Conditions, so that
you have a standard set of terms. You can do this by going to:

**Selling > Terms and Conditions**

#### 2.7.1 What should Terms and Conditions contain?
Here are a some common topics that Terms and Conditions should contain:

  * Validity of the offer.
  * Payment Terms (In Advance, On Credit, part advance etc).
  * What is extra (or payable by the Customer).
  * Safety / usage warning.
  * Warranty if any.
  * Return Policy.
  * Terms of shipping, if applicable.
  * Ways of addressing disputes, indemnity, liability, etc.
  * Address and Contact of your Company.

### 2.8 Print Settings
You can print your quotation on your company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when your print.

Quotations can also be titled as “Proforma Invoice” or “Proposal”.
You can do this by selecting a **Print Heading**. To create new Print Headings go to **Setup > Printing > Print Heading**. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).


### 2.8 More Information
* **Campaign:** A Sales campaign can be associated with the quotation. A set of quotations can be part of a sales campaign.
* **Source:** A Lead Source type can be linked if quoting to a lead, whether from a campaign, from a supplier, an exhibition etc,. Select Existing Customer if quoting to a customer.
* **Supplier Quotation:** A Supplier Quotation can be linked for comparing with your current quotation to a buyer. You can get an idea of profit/loss by comparing the two.

### 2.9 Submitting the Quotation
Quotation is a “Submittable” transaction. When you click on Save, a draft is saved, on submitting, it is submitted permanently. Since you send this Quotation to
your Customer or Lead, you must freeze it so that changes are not made after
you send the Quotation.

On submitting, you can create a Sales Order or a Subscription from the Quotation using the Create button. In the Dashboard present on the top, you can go to the Sales Order linked with this Quotation. In case it didn't work out, you can set the Quotation as lost by clicking on the 'Set as Lost button'.

<img class="screenshot" alt="Submitted Quotation" src="{{docs_base_url}}/assets/img/selling/submitted-quotation.png">

### 3. Related Topics
1. [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Lead](/docs/user/manual/en/CRM/lead)