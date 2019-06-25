<!-- add-breadcrumbs -->
# Tax Category
If you want to apply different kinds of taxes based on Tax Categories, create Tax Categories from:

> Home > Accounting > Taxes > Tax Category

## 1. How does a Tax Category work
- Tax category is linked to [Tax Rule](/docs/user/manual/en/accounts/tax-rule).
- This Tax Category can be assigned to a Customer, so when that customer is selected, the Tax Category will be fetched.
- This will fetch the Sales Tax Template linked to the Tax Rule. Hence, the rows in the Tax table will be automatically filled.
- Tax Category can be used to group customers to whom same tax will be applied. For example, Government, NGO, commercial, etc.

  <img class="screenshot" alt="Tax Category" src="{{docs_base_url}}/assets/img/accounts/tax-category.gif">

## 2. Assigning Tax Category
Tax Category is automatically determined in a transaction by either the Party Address or Party Master.

  * You can assign Tax Category to specific Parties (Customers and Suppliers).
  * You can assign Tax Category to specific Billing or Shipping Address
  * You can select whether Billing Address or Shipping Address gets preference by changing the Accounts Settings.
  * Tax Category is determined from Party Address first. If the Address is not assigned any Tax Category, then the Party's Tax Category is used.
  * You can also manually select the Tax Category in a transaction.
  
## 3. What effect does the Tax Category have in a transaction?

  * Specific Item Tax Templates for that Tax Category are automatically set for items.
  * You can create [Tax Rules]({{docs_base_url}}/user/manual/en/accounts/setup/tax-rule)
  to automatically set a specific Sales / Purchase Taxes and Charges Template based on different Tax Categories
  in transactions.
