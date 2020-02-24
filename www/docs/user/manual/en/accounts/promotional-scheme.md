# Promotional Scheme

> Introduced in version 12

**A Promotional Scheme is a temporary discount on one or more products.**

Promotional schemes help businesses become successful as lower prices for a limited period of time to attract more Customers. They can be easily configured in ERPNnext. A Promotional scheme is linked to a pricing rule, against each slab system that will generate the pricing rule.

On creating a Promotional Scheme, the system creates a [Pricing Rule](/docs/user/manual/en/accounts/pricing-rule). A Promotional Scheme can have multiple Pricing Rules associated with it. In ERPNext, a Promotional Scheme is an easier way to manage pricing on multiple Item/Groups based on different parties and conditions.

To access the Promotional Scheme list, go to:
> Home > Selling > Items and Pricing > Promotional Scheme

## 1. Prerequisites
Before creating and using a Promotional Scheme, it is advisable to create the following first:

1. [Item](/docs/user/manual/en/stock/item)
1. [Item Group](/docs/user/manual/en/stock/item-group)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Supplier](/docs/user/manual/en/buying/supplier)

## 2. How to create a Promotional Scheme

1. Go to the Promotional Scheme list and click on New.
1. Enter a title for the rule.
1. Select what to Apply On like Item Code, Item Group, Brand, or Transaction. Selecting Transaction will apply the scheme on the total amount of the transaction.
1. Based on the 'Apply On', system will give you the provision to select the Item Code / Item Group / Brand in the table.
1. Select whether the scheme is for Selling, Buying, or both and set the part information.
1. In the Price Discount Slabs table, set the price discount, product discount.
1. Users can also apply the discount on the other Item Code / Item Group / Brand by selecting the value for Apply Rule On Other field.

 <img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes.png">
1. Save.

> Note: On saving a Promotional Scheme, a new Pricing Rule is created.

### 2.1 Additional fields when creating a Promotional Scheme

#### Mixed Conditions
If you select two or more Items and set the Min and Max Quantity. The Promotional Scheme will be applied only if the total sum of Items matches the set quantities. For example, you create a Promotional Scheme on Item 1 and Item 2 and set the Min and Max Quantity as 30, the Promotional Scheme will apply only if the total quantity is 30.

#### Is Cumulative
Enabling this options allows the Promotional Scheme to be applied cumulatively. You need to set the 'Min Amt' and 'Max Amt' for this.

Consider a scenario where the Min Amt is 1,500 and Max Amt is 2,000. Now, if one transaction is created for 1,400 then the Promotional Scheme will not be applied. However, on creating a second invoice of amount 600, Promotional Scheme will be applied. This happened since the total (cumulative) amount of the invoices added up to 2,000. Note that the discount will be applied only to the latest transaction that crosses the cumulative limit.

This can be useful to give discounts if a Customer buys an Item multiple times and you want to reward him with discounts/special prices.

## 3. Features

### 3.1 Apply Scheme On Other Item
This feature checks condition on the first Item but applies scheme/discount/rate on another Item.

For example, set Item1 and Item2 in the 'Apply Rule On' table and set 'Apply Rule On Other' on Item3. Now, if the transaction has Item1, Item2, and Item3, the Pricing Rule will apply on Item3 since the first two Items were present in the transaction.

### 3.2 Party Information

Set whether the Promotional Scheme is for Selling of Buying the Item.

Based on your selection you can set applicability to one of the following masters.

* [Customer](/docs/user/manual/en/CRM/customer)
* [Customer Group](/docs/user/manual/en/CRM/customer-group)
* [Territory](/docs/user/manual/en/selling/territory)
* [Sales Partner](/docs/user/manual/en/selling/sales-partner)
* [Campaign](/docs/user/manual/en/CRM/campaign)
* [Supplier](/docs/user/manual/en/buying/supplier)
* Supplier Group

### 3.3 Validity 
You can also set a date interval for when the Promotional Scheme will be valid. This is useful for a sales promotion. On leaving the dates blank the Promotional Scheme will not have any time frame limit. 

**Currency**: Setting a Currency here will cause the Promotional Scheme to be applied only when the Currency is the same in the transaction.

### 3.4 Price Discount Slabs

**Rule Description**: Enter a description to keep a not of what this Promotional Scheme entails.

#### Quantity and Amount
Specify minimum qty, maximum qty, minimum amount, or maximum amount of an Item when this Promotional Scheme should be applicable.

Note that if the quantity or amount falls short or exceeds the limits set here, the Promotional Scheme will not be applied at all. However, it will be applied if you have enabled the options Mixed Conditions or Cumulative.

### Setting the Discount/Rate
* **Rate**: This will be the new rate for an Item. For example, if you sell an Item for 100 and want to sell it for 112 for a specific party, then select Rate and set the Rate as 112.
* **Discount Percentage**: A specific discount percentage can be set. For example, a 10% discount on an Item worth 500 would result in a price of 450.
* **Discount Amount**: A fixed discount amount will be applied. For example if you sell an Item for 100 and want to sell it with a discount of 7, then this condition can be set using the Discount Amount option.

#### Filters for setting discount

* **Warehouse**: Setting a Warehouse here will cause the Promotional Scheme to be applied only if the Item is selected from the Warehouse specified here.

* **Priority**: Consider an Item Group, you want to set specific rules on one Item from the group. This can be done by creating a new Promotional Scheme and setting a higher priority. 

* **Threshold for Suggestion**: This is the threshold based on which the system will notify you to adjust Item Quantity for discount. For example, if the Min Quantity is 10 and the Threshold is 9, the system will notify to add 1 more Item for the discount to be applicable. This also applies to the amount set.

* **Validate Applied Rule**: If the entered price is not valid for the Item, the system will not allow you to apply a different rate/discount.

### 3.5 Product Discount Slabs
A Product Discount is applicable when one or more Items are free on the purchase of other Items. Most fields in this table are the same as the previous section.

The additional options are:
* **Same Item**: If you want to give the same Item as free (product discount) on purchase of an Item, enable this checkbox. If you want to give another Item, untick and select the Item to be given as free.

* **Apply Multiple Pricing Rules**: To understand this, consider an Item of Rate 500. There are two Pricing Rules on it P1 and P2. P1 applies 10% discount and P2 applies 5%. Enabling this option will apply a total of 15% on the Item Rate which gives 425.

* **UoM**: The Promotional Scheme will apply only if the UoM set here matches with the transaction.

* **Rate**: An Item may be offered free of cost by the Supplier but there may be some tax applicable. Entering a Rate here means that the Customer will have to pay the applicable taxes.


## 4. Promotional Scheme types
### 4.1 Price Discount

In this type of promotional scheme, the user gets an option to set the discount in terms of percentage or amount based on the min quantity, max quantity, min amount and max amount on the products. Users can also configure the scheme where they can set the flat rate for the product based on the quantity or the amount of the product.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-price-discount.png">

### 4.2 Product Discount

In this type of promotional scheme, the user gets an option to give a free product on purchase of the same or different product with conditions like min quantity, max quantity, min amount, max amount.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-product-discount.png">

## 5. How to configure a Promotional Scheme (Examples)

Let's understand how to configure a promotional scheme in ERPNext using some examples.

### 5.1 Mixed Conditions Schemes

Customer A has purchased 10 quantities of Britannia Cake 5 Rs packet and 5 quantities of Britannia Cake 10 Rs packet. Now, the Supplier wants to give a discount of 10% to Customer A. This Supplier also wants to give a 10 % discount to Customer B who has purchased 15 quantities of Britannia Cake 5 Rs packet.

So, the Supplier wants to apply the discount on products Britannia Cake 5 Rs, Britannia Cake 10 Rs only if his Customers have purchased 15 quantities of any product or sum of both products.

To configure this in ERPNext the steps are as follows:

1. Set Apply On as Item Code.
1. Set the Item Code Britannia Cake 5 Rs, Britannia Cake 10 Rs in the Pricing Rule Item Code table.
1. Enable the "Mixed Conditions" field.
1. In the price discount table, set the min qty, max qty as 15.
1. Set the discount type as Discount Percentage and rate as 10.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-mixed-conditions.png">

### 5.2 To apply a discount on other Item

Customer A has purchased 30 quantities of Britannia Cake 5 Rs packet and 2 quantities of Britannia Cake 15 Rs. The Supplier wants to sell the product Britannia Cake 15 Rs at the flat rate 12. Here the original price for the product Britannia Cake 15 Rs is 15.

The Supplier wants to apply the rule only if the Customer has purchased min 30 quantities of the product Britannia Cake 5 Rs or Britannia Cake 10 Rs.

To configure this in ERPNext the steps are as follows

1. Set Apply On as Item Code.
1. Set the item code Britannia Cake 5 Rs, Britannia Cake 10 Rs in the Pricing Rule Item Code table.
1. Apply Rule On Other as Item Code and set Item Code as Britannia Cake 15 Rs.
1. In the price discount table, set the min qty as 30.
1. Set the discount type as Rate and rate as 12.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-discount-on-other.png">

## 6. Related Topics
1. [Pricing Rule](/docs/user/manual/en/accounts/pricing-rule)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Item](/docs/user/manual/en/stock/item)
