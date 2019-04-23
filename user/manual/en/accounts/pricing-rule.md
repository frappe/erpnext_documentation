<!-- add-breadcrumbs -->
#Pricing Rule

Pricing Rule is a master where you can define rules based on which discount is applied to specific Customer or Supplier.

Following are the few cases which can be addressed using Pricing Rule.

- As per a promotional sale policy, if customer purchases more than 10 units of an item, he enjoys 20% discount. 
- For Customer "XYZ", selling price for the specific Item should be updated as ###.
- Items categorized under specific Item Group has same selling or buying price.
- Customers belonging to specific Customer Group should get ### selling price, or % of Discount on Items.
- Supplier categorized under specific Supplier Group should have ### buying rate applied.

To have Discount and Price List Rate for an Item auto-applied, create Pricing Rules for it.

### 1. How to create a Pricing Rule
1. Go to Pricing Rule via searching.
1. Set a title for the rule.
1. Select what to Apply On.

    <img alt="Applicable On" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-on.png">
1. For a single item, select Item Code and select the item.
1. If you want Pricing Rule to be applied on all the items, select 'Item Group' and select **All Item Group** (parent Item Group).
1. If you have multiple price lists, you can set the priority from 0 to 20.
1. Set whether the Pricing Rule is for Selling of Buying the item.
1. Set what type is this applicable for and select the record. You can set applicability to one of the following masters.

    <img alt="Applicable for" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-for.png">

1. Specify minimum and maximum qty of an item when this Pricing Rule should be applicable.

    <img alt="Applicable Qty" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-qty.png">
1. You can also set a date interval for when the Pricing Rule will be valid. This is useful for a sales promotion.

###2. How to apply the Pricing Rule

1. Under the Margin Type, you can set whether the margin is calculated as a percentage or an amount. Eg: 10% margin on supplier price list at the time of sales.

1. Rate or Discount specified in the Pricing Rule will be applied only if above applicability rules are matched with values in the transaction. Rate mentioned in Pricing Rule will be given priority over item's Price List rate.

   <img alt="Applicable Rate" class="screenshot" src="/docs/assets/img/articles/pricing-rule-price.png">

1. Discount Percentage can be applied for a specific Price List (Selling or Buying). To apply it for both, leave the 'For Price List' field blank.

    <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount.png">

### 3. Scenarios with Pricing Rule
#### 3.1 Make Price List
1. Create a new Pricing List by going to **Stock > Price List > New**.
1. Go to **Buying > Supplier** and set the new Price List.
1. Go to **Stock > Item Price** and set a newly created Price List here.
1. Also set the supplier who has the new Price List set.

<img alt="Disable" class="screenshot" src="{{docs_base_url}}/assets/img/articles/price-list.png">

#### 3.2 Make Pricing Rule 
1. Create a new Pricing Rule.
1. Select the item which has the new Price List set.
1. Tick the Selling checkbox.
1. Save.

<img alt="Disable" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-margin.png">

#### 3.2 Make Invoice
When you make an invoice, the system applies the margin rate on the item price on selection of the specific item.

<img alt="Disable" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-invoice.png">

For more details about adding margins [Click Here](/docs/user/manual/en/selling/articles/adding-margin.html)

#### 4. Related Topics
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Item](/docs/user/manual/en/stock/item)