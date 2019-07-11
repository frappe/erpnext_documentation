# Promotional Scheme

> Introduced in v12

Promotional schemes help retail stores become successful. They can be easily configure in ERPNnext. A Promotional scheme is linked to a pricing rule, against each slab system will generate the pricing rule.

## 1. How to create a Promotional Scheme

1. Go to: **Selling > Items and Pricing > Promotional Scheme > New**.
1. Set a title for the rule.
1. Select what to Apply On like Item Code, Item Group, Brand etc.
1. Based on the 'Apply On', system will give you the provision to select the Item Code / Item Group / Brand in the table.
1. Then configure the party information.
1. Set promotional schemes for price dicsount, product discount.
1. User can also apply the discount on the other Item Code / Item Group / Brand by selcting the value for Apply Rule On Other field.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/promotional-schemes/promotional-schemes.png">

### 1.1 Price Discount

In this type of promotional schemes, the user gets an option to set the discount in terms of percentage or amount based on the min quantity, max quantity, min amount and max amount on the products. User can also configure the scheme where they can set the flat rate for the product based on the quantity or the amount of the product.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/promotional-schemes/promotional-schemes-price-discount.png">

### 1.2 Product Discount

In this type of promotional schemes, the user gets an option to give the free product on purchase of the same or different product with conditions like min quantity, max quantity, min amount, max amount.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/promotional-schemes/promotional-schemes-product-discount.png">

## 2. How to configure a Promotional Scheme

Lets understand how to configure a promotional scheme in ERPNext using some examples.

### 2.1 Mixed Conditions Schemes

Customer A has purchased 10 quantities of Britannia Cake 5 Rs packet and 5 quantities of Britannia Cake 10 Rs packet. Now shopkeeper wants to give the discount of 10% to customer A. This shopkeeper also wants to give 10 % discount to customer B who has purchased 15 quantities of Britannia Cake 5 Rs packet. So basically user wants to apply the discount on products Britannia Cake 5 Rs, Britannia Cake 10 Rs only if his clients have purchased 15 quantities of any product or sum of both product.

To configure this in ERPNext the stpes are as follows:
1. Set Apply On as Item Code.
1. Set the item code Britannia Cake 5 Rs, Britannia Cake 10 Rs in the Pricing Rule Item Code table.
1. Enable "Mixed Conditions" field.
1. In price discount table, set the min qty, max qty as 15.
1. Set the discount type as Discount Percentage and rate as 10.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/promotional-schemes/promotional-schemes-mixed-conditions.png">

### 2.2 To apply discount on other item

Customer A has purchased 30 quantities of Britannia Cake 5 Rs packet and 2 quantities of the product Britannia Cake 15 Rs then the user wants to sell the product Britannia Cake 15 Rs at the flat rate 12. Here the original price for the product Britannia Cake 15 Rs is 15.
The user wants to apply the rule only if the customer has purchased min 30 quantities of the product Britannia Cake 5 Rs or Britannia Cake 10 Rs.

To configure this in ERPNext the stpes are as follows:
1. Set Apply On as Item Code.
1. Set the item code Britannia Cake 5 Rs, Britannia Cake 10 Rs in the Pricing Rule Item Code table.
1. Apply Rule On Other as Item Code and set Item Code as Britannia Cake 15 Rs.
1. In price discount table, set the min qty as 30.
1. Set the discount type as Rate and rate as 12.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/promotional-schemes/promotional-schemes-discount-on-other.png">

#### 4. Related Topics
1. [Pricing Rule](/docs/user/manual/en/accounts/pricing-rule)
1. [Customer](/docs/user/manual/en/crm/customer)
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Item](/docs/user/manual/en/stock/item)
