<!-- add-breadcrumbs -->
# Tax Rule

**A Tax Rule automatically applies taxes to transactions based on preset rules.**

You can define which [Tax Template](/docs/user/manual/en/setting-up/setting-up-taxes.html) must be applied on a Sales / Purchase transaction using Tax Rule. This is decided by various factors like Customer, Customer Group, Supplier, Supplier Group, Item, Item Group or a combination of these.

To access the Tax Rule list, go to:
> Home > Accounting > Taxes > Tax Rule

## 1. Prerequisites
Before creating and using a Tax Rule, it is advised to create the following first:

1. [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template)
    
    Or

1. [Purchase Taxes and Charges Template](/docs/user/manual/en/buying/purchase-taxes-and-charges-template)

## 2. How to create a Tax Rule
1. Go to the Tax Rule list and click on New.
1. Under Tax Type select whether the tax will be applied at Sales or Purchase. 
1. Select the Tax Template to be applied.
1. Save.
 <img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule.png">

You can list Items online using the Website module. Selecting 'Use for Shopping Cart' will use this Tax Rule for Shopping Cart transactions also. To know more, visit the [Shopping Cart](/docs/user/manual/en/website/shopping-cart) page.

> Note: It is advised to not use the Sales/Purchase Template selected here in [Item Tax Template](/docs/user/manual/en/accounts/item-tax-template), it may cause interference. If you want to use same tax rates for Tax Rule and Item Tax Template, use a different name for the Sales/Purchase Tax Templates.

## 3. Features
### 3.1 Auto applying Tax Rule based on Customer/Supplier
Select a Customer/Supplier if tax is to be applied for a specific party. Leave it as All Customer Groups/All Supplier Groups if this Tax Rule is applicable to all Customers/Suppliers.

On selecting a Customer/Supplier their Billing and Shipping addresses will be fetched if saved in the Customer/Supplier master.

### 3.2 Auto applying Tax Rule based on Item / Item Group

On setting an Item or Item group in the Tax Rule, this Tax Rule will automatically be applied to new transactions that have the selected Item/Item Group.

### 3.3 Setting a Tax Category
Setting a Tax Category allows applying multiple Tax Rules to a transaction based on different factors. To know more, visit the [Tax Category](/docs/user/manual/en/accounts/tax-category) page.

### 3.4 Validity
Set a Start and End Date if the tax is to be applied only for a specified period. Leaving both dates blank will result in the Tax Rule to have no time limits.

### 3.5 Priority
Setting a priority number here will decide on which order a Tax Rule will be applied in case multiple Tax Rules have similar criteria. '1' is the highest priority, '2' has lesser priority and so on.

## 4. How does Tax Rule Work?
It works like a filter to automatically apply tax templates:

1. Set a Customer or a specific region
1. The selected tax template will be applied according to the conditions set in the Tax Rule
1. It will be applied to new Sales/Purchase transactions based on the type selected in the Tax Rule

For example, selecting 'Nitin' as the Customer and 'All Item Groups' will cause the Tax Rule to be applied to all sales transactions with the Customer Nitin. Likewise, selecting a 'Plastic Crystal A' and 'All Customer Groups' will cause the Tax Rule to be applied to all Customers but only when the Item is 'Plastic Crystal A'. 

While creating a new transaction the system will select and apply tax template based on the tax rule defined.

Let us consider a scenario to understand Tax Rule Better. Suppose we define two Tax Rules as below.

<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule-1.png">

<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule-2.png">

Here In State GST has Billing Country as India and VAT 14% has Billing Country as Germany.

Now suppose we try to create a Sales Order for a Customer whose default Billing Country is India, system will select In State GST.
In case the Customer's Billing Country was Germany, the system will select VAT 14%.

### 5. Related Topics
1. [Pricing Rule](/docs/user/manual/en/accounts/pricing-rule)
1. [Item Tax Template](/docs/user/manual/en/accounts/item-tax-template)
1. [Tax Category](/docs/user/manual/en/accounts/tax-category)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Supplier](/docs/user/manual/en/buying/supplier)