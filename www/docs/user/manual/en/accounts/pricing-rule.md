<!-- add-breadcrumbs -->
# Pricing Rule

**A Pricing Rule defines the discount/pricing rules that apply based on set conditions.**

A Pricing Rule has many options using which you can control the pricing of an Item. Filters like quantity, date, groups, and other conditions can be set.

A Pricing Rule is somewhat similar to a [Tax Rule](/docs/user/manual/en/accounts/tax-rule).

Following are the few cases which can be addressed using Pricing Rule:

- As per a promotional sale policy, if the Customer purchases more than 10 units of an item, he enjoys 20% discount.
- For Customer "XYZ", the selling price for the specific Item should be updated as ###.
- Items categorized under specific Item Group have same selling or buying price.
- Customers belonging to specific Customer Group should get ### selling price, or % of Discount on Items.
- Supplier categorized under specific Supplier Group should have ### buying rate applied.

To have Discount and Price List Rate for an Item auto-applied, create Pricing Rules for it.

To access the Pricing Rule list, go to:
> Home > Accounting > Pricing Rule

## 1. Prerequisites
Before creating and using a Pricing Rule, it is advisable to create the following first:

1. [Item](/docs/user/manual/en/stock/item)
1. [Item Group](/docs/user/manual/en/stock/item-group)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Supplier](/docs/user/manual/en/buying/supplier)

## 2. How to create a Pricing Rule
1. Go to the Pricing Rule list and click on New.
1. Set a title for the rule.
1. Select what to Apply On from Item Code, Item Group, Brand, or Transaction.
1. Select whether you want to apply Price discount or Product discount. If you want to give free products then select the product discount.
 <img alt="Applicable On" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-on.png">
1. For a single item, select Item Code and select the items.
1. If you want Pricing Rule to be applied on all the items, select 'Item Group' and select **All Item Group** (parent Item Group).
1. Set the discount/price to be applied. To know more, [go to this section](/docs/user/manual/en/accounts/pricing-rule#35-price-discount-scheme).
1. Save. 

### 2.1 Additional options when creating a Pricing Rule

#### Warehouse
Setting a Warehouse here will cause the Pricing Rule to be applied only if the Item is selected from the Warehouse specified here.

#### Apply Rule On
Based on the attribute selected in the 'Apply On' field, you can set the Pricing Rule based on one of these:

* [Item](/docs/user/manual/en/stock/item)
* [Item Group](/docs/user/manual/en/stock/item-group)
* Brand
* Transaction (on the total amount of the transaction)

In this table, you can select the specific Item/Item Group/Brand. For example, if you select Apply On 'Item Group' and select 'Raw Materials' in the table, this Pricing Rule will be applied only on Items that belong to the Group 'Raw Materials'.

**UoM**: The Pricing Rule will apply only if the UoM set here matches with the transaction.

#### Mixed Conditions
If you select two or more Items and set the Min and Max Quantity. The Pricing Rule will be applied only if the total sum of Items matches the set quantities. For example, you create a Pricing Rule on Item 1 and Item 2 and set the Min and Max Quantity as 30, the Pricing Rule will apply only if the total quantity is 30.

#### Is Cumulative
Enabling this options allows the Pricing Rule to be applied cumulatively. You need to set the 'Min Amt' and 'Max Amt' for this.

Consider a scenario where the Min Amt is 1,500 and Max Amt is 2,000. Now, if one transaction is created for 1,400 then Pricing Rule will not be applied. However, on creating a second invoice of amount 600, Pricing Rule will be applied. This happened since the total (cumulative) amount of the invoices added up to 2,000. Note that the discount will be applied only to the latest transaction that crosses the cumulative limit.

This can be useful to give discounts if a Customer buys an Item multiple times and you want to reward him with discounts/special prices.

## 3. Features

### 3.1 Apply Rule On Other
This feature checks condition on first Item but applies rule on another Item.

![Apply rule on other](/docs/assets/img/articles/pricing-rule-other.png)

For example, set Item1 and Item2 in the 'Apply Rule On' table and set 'Apply Rule On Other' on Item3. Now, if the transaction has Item1, Item2, and Item3, the Pricing Rule will apply on Item3 since the first two Items were present in the transaction.

### 3.2 Party Information

Set whether the Pricing Rule is for Selling of Buying the Item.

Based on your selection you can set applicability to one of the following masters.

* [Customer](/docs/user/manual/en/CRM/customer)
* [Customer Group](/docs/user/manual/en/CRM/customer-group)
* [Territory](/docs/user/manual/en/selling/territory)
* [Sales Partner](/docs/user/manual/en/selling/sales-partner)
* [Campaign](/docs/user/manual/en/CRM/campaign)
* [Supplier](/docs/user/manual/en/buying/supplier)
* Supplier Group

### 3.3 Quantity and Amount
Specify minimum qty, maximum qty, minimum amount, or maximum amount of an Item when this Pricing Rule should be applied.

Note that if the quantity or amount falls short or exceeds the limits set here, the Pricing Rule will not be applied at all. However, it will be applied if you have enabled the options Mixed Conditions or Cumulative.

<img alt="Applicable Qty" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-qty-amt.png">

### 3.4 Validity 
You can also set a date interval for when the Pricing Rule will be valid. This is useful for a sales promotion. On leaving the dates blank the Pricing Rule will not have any time frame limit. 

<img alt="Period" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-period.png">

### 3.5 Margin

![Pricing Rule Margin](/docs/assets/img/articles/pricing-rule-margin1.png)

* **Margin Type**: When selling an Item, you may sell it for a certain margin. If you don't want to add selling prices to Items every time and would like to automatically set a margin, it can be done with this feature. 

* **Margin Rate or Amount**: The margin set can be based on Percentage or Amount, eg: 5% margin or $50 fixed margin.

For more details about adding margins [Click Here](/docs/user/manual/en/selling/articles/adding-margin)

### 3.6 Price Discount Scheme
The actual rule to be applied is set in this section.

![Pricing Rule](/docs/assets/img/articles/pricing-rule-rule.png)

* **Rate**: This will be the new rate for an Item. For example, if you sell an Item for 100 and want to sell it for 112 for a specific party, then select Rate and set the Rate as 112.
* **Discount Percentage**: A specific discount percentage can be set. The discount percentage can be set to a specific [Price List](/docs/user/manual/en/stock/price-lists). Leaving the 'For Price List' blank will apply the Pricing Rule to all Price Lists.
* **Discount Amount**: A fixed discount amount will be applied. For example if you sell an Item for 100 and want to sell it with a discount of 7, then this condition can be set using the Discount Amount option.

### 3.7 Advanced Settings

![Pricing Rule Advance](/docs/assets/img/articles/pricing-rule-adv.png)

* **Threshold for Suggestion**: This is the threshold based on which the system will notify you to adjust Item Quantity for discount. For example, if the Min Quantity is 10 and the Threshold is 9, the system will notify to add 1 more Item for the discount to be applicable. This also applies to the amount set.

* **Priority**: Consider an Item Group, you want to set specific rules on one Item from the group. This can be done by creating a new Pricing Rule and setting a higher priority. This can also apply to Customer Group and Supplier Group.

* **Apply Multiple Pricing Rules**: To understand this, consider an Item of Rate 500. There are two Pricing Rules on it P1 and P2. P1 applies 10% discount and P2 applies 5%. Enabling this option will apply a total of 15% on the Item Rate which gives 425.

* **Apply Discount on Rate**: The discount will be compounded. Consider the same scenario as above. On enabling this option, 10% will be applied on 500 which will give 450, then 5% will be applied on 450 which will give 427.5. 

* **Validate Applied Rule**: Shows the entered validation message if the discount/rate set manually by you in a transaction does not match the Pricing Rule.

 This is useful when the top distributor in the hierarchy decides the discount/rate to be applied and you are only validating if the Pricing Rule is applied correctly.

## 4. Pricing Rule discount types
### 4.1 Price Discount

1. Under the Margin Type, you can set whether the margin is calculated as a percentage or an amount. Eg: 10% margin on supplier price list at the time of sales.

1. Rate mentioned in Pricing Rule will be given priority over Item's Price List (Item Price) rate.

 <img alt="Applicable Rate" class="screenshot" src="/docs/assets/img/articles/pricing-rule-price.png">

1. Discount Percentage can be applied for a specific Price List (Selling or Buying). To apply it for both, leave the 'For Price List' field blank.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount.png">

1. Discount can also be set in terms of amount.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount-amt.png">

### 4.2 Product Discount

1. "Buy 2 quantities get 1 free quantity of the same item." To configure such type of rules, set the Price or Product Discount as 'Product discount', tick the Same Item checkbox, and set the quantity.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-same-product-free.png">

1. "Buy 2 quantities get 1 free quantity of the another item." To configure such type of rules. Set the Price or Product Discount as Product discount, untick the 'Same Item' checkbox and set the 'Free Item' and quantity.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-other-product-free.png">

### 5. Related Topics
1. [Promotional Scheme](/docs/user/manual/en/accounts/promotional-scheme)
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Item](/docs/user/manual/en/stock/item)