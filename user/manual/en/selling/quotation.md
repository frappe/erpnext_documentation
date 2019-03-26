<!-- add-breadcrumbs -->
# Quotation

During a sale, the customer may request for a note about the products
or services you are planning to offer, along with the prices and other terms
of engagement. This is called a "Proposal" or an "Estimate" or a "Pro Forma
Invoice" or a **Quotation**.

A typical Selling flow looks like:

<img class="screenshot" alt="Make Quotation from Opportunity" src="{{docs_base_url}}/assets/img/selling/selling-flow.png">

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


### 1. How to create a Quotation
1. Go to **Selling > Sales > Quotation > New Quotation**.
2. Select if the Quotation is to a Lead or a Customer.
3. Enter Customer name.
4. Add the Items in the CURRENCY AND PRICE LIST table.
5. Modify the details as needed.
6. Save.
You can also create a Quotation from an Opportunity.

<img class="screenshot" alt="Make Quotation from Opportunity" src="{{docs_base_url}}/assets/img/selling/make-quote-from-opp.png">

### 2. Features
#### 2.1 Rates

The rates you quote may depend on two things.

  * The Price List: If you have multiple Price Lists, you can select a Price List or tag it to the Customer (so that it is auto-selected). Your Item prices will automatically be updated from the Price List. For details refer [Price List](/docs/user/manual/en/setting-up/price-lists)

  * The Currency: If you are quoting to a Customer in a different currency, you will have to update the conversion rates to enable ERPNext to save the information in your standard Currency. This will help you to analyze the value of your Quotations in standard Currency.

#### 2.2 Taxes

To add taxes to your Quotation, you can select a **Sales Taxes and Charges Template** or add the taxes on your own.

For example:

<img class="screenshot" alt="Taxes and Charges" src="{{docs_base_url}}/assets/img/selling/taxes-and-charges.gif">

To understand taxes in detail visit [Taxes](/docs/user/manual/en/setting-up/setting-up-taxes).

#### 2.3 Terms and Conditions

Each Quotation must ideally contain a set of terms, of your contract. It is
usually a good idea to make templates of your Terms and Conditions, so that
you have a standard set of terms. You can do this by going to:

**Selling > Terms and Conditions**

#### 2.4 What should Terms and Conditions Contain?

  * Validity of the offer.
  * Payment Terms (In Advance, On Credit, part advance etc).
  * What is extra (or payable by the Customer).
  * Safety / usage warning.
  * Warranty if any.
  * Returns Policy.
  * Terms of shipping, if applicable.
  * Ways of addressing disputes, indemnity, liability, etc.
  * Address and Contact of your Company.

#### 2.5 Submission

Quotation is a “Submittable” transaction. Since you send this Quotation to
your Customer or Lead, you must freeze it so that changes are not made after
you send the Quotation.

> Tip: Quotations can also be titled as “Proforma Invoice” or “Proposal”.
You can do this by selecting a **Print Heading** in the **Print Settings**
section. To create new Print Headings go to Setup > Printing >
Print Heading.

#### 2.6 Discount

While making your sales transactions like a Quotation (or Sales Order) you
can also give discounts to your customers. In the Discount section, add
the discount in percentage or fixed amount. Read [Discount](https://erpnext.org/docs/user/manual/en/selling/articles/applying-discount) for more explanation.

#### 3. Related Topics
1. [Applying Discount](/docs/user/manual/en/selling/articles/applying-discount)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Lead](/docs/user/manual/en/CRM/lead)