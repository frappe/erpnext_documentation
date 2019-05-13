<!-- add-breadcrumbs -->
# Tax Rule

You can define which [Tax Template](/docs/user/manual/en/setting-up/setting-up-taxes.html) must be applied on a Sales / Purchase transaction using Tax Rule. 

### 1. How to create a Tax Rule
1. Go to: **Accounts > Taxes > Tax Rule > New**.
1. Select whether the tax will be applied at Sales or Purchase.
1. Select the Sales Tax Template from the ones available.
1. Enter the a customer if tax is to be applied for a specific customer.
1. Leave it as All Customer Groups to be applied for all customers.
1. Set other fields for which you want to activate the Tax Rule.
1. This works like a filter, so if you set a customer or a specific region, then the tax template set will be applied to the conditions set in the Tax Rule.
1. Set a start and end date if the tax is to be applied only for a specified period.
1. Save.
<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule.png">

### 2. Example
While making a Transaction the system will select and apply tax template based on the tax rule defined.
The system selects Tax Rule with maximum matching Filters.
Let us consider a scenario to understand Tax Rule Better.
Suppose we define two Tax Rules as below.

<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule-1.png">

<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule-2.png">

Here Tax Rule 1 has Billing Country as India and Tax Rule 2 has Billing Country as United Kingdom.

Now suppose we try to create a Sales Order for a customer whose default Billing Country is India, system shall select Tax Rule 1.
In case the customers Billing Country was United Kingdom, the system would have selected Tax Rule 2.

#### 3. Related Topics
1. [Pricing Rule](/docs/user/manual/en/accounts/pricing-rule)
1. [Itemized Taxation](/docs/user/manual/en/accounts/item-wise-taxation)
