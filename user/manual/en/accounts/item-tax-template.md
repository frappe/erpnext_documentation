<!-- add-breadcrumbs -->
# Item Tax Template

**Item Tax Template it for item wise taxation.**

If some of your Items require tax rates different from the standard tax rate assigned in the Taxes and Charges table, then you can create an Item Tax Template and assign it to an Item or Item Group. The rate assigned in the Item Tax Template will get preference over the standard tax rate assigned in the Taxes and Charges table.

For example, if tax GST 16% is added in the Taxes and Charges table in Sales Order, then it will be applied on all the items in that Sales Order. However, if you need to have different tax rate applied on some of the items, the steps are given below to setup Items and Sales Taxes and Charges Template master in your ERPNext account. 

To create an Item Tax Template, go to
> Home > Accounting > Taxes > Item Tax Template

## 1. How to use Item Tax Template
Let's assume that we are creating a Sales Order. We have Sales Taxes and Charges Template master for GST 16%. Out of all the Sales Items, on one item, only 5% GST will be applied, while another item is exempted from any tax. You need to select the Account Head of the tax and set its overriding rate.

###1.1 Mention Tax Applicable in the Item master

Tax templates are preset with values. For items which have a different tax rate than the others, you need to change it in the Item master. Go to the tax table in the Item, add a row, select the tax type and change the rate. Now, this new rate will over ride the template when creating an order/invoice. For example, in the below screenshot you can see that the tax rate is set as 5 and that's the rate which will be applied in transactions.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/item-wise-tax.png">

For the item which is exempted from tax totally, mention 0% as tax rate in the Item master. 

> Note: For Item Tax to work, you need to ensure that the tax types set in Item Tax table (with changed tax rates) in Item master are present in the Sales Taxes and Charges Template.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/exempted-item.png">

###1.2 Setup Taxes and Other Charges

In Sales Taxes and Charges Template master, select GST 16% account and mention Tax Rate as 16. This tax rate will be applied on all the Items selected in the Sales Order, unless specific Tax Rate is defined in the Item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-master.png">

If you want tax rates always to be applied from the Item master, you should update the rate for the tax account as zero in the Sales Taxes and Charges Template.

###1.3 Tax Calculation in transaction	

In the Sales Order, we have selected many Items. For the items shown in blue, tax rate is applied based on tax rate mentioned in the taxes table. For the items highlighted in red, tax rates were fetched from the respective item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation.png">

Please note that an item's tax rate will be pulled from the item master only if you have selected same tax account (GST 16% in this case) in both Item master and in Sales Order under Taxes and Charges section.

###1.4 Item wise tax on an Item Group
You can assign the Item Tax Template to an Item Group by modifying the Item Tax table in the Item Tax section within the Item Group document.
<img class="screenshot" alt="Item Tax in Item Group" src="{{docs_base_url}}/assets/img/accounts/item-group-tax.png">

###1.5 Some points to note
- If you set the Tax Category as empty, it will be considered the default Item Tax Template will be applied to items in transactions by default.

- You can apply different Item Tax Templates for different Tax Categories.

- For an Item Tax Template to override taxes, there must be a row in the Taxes and Charges table with the same tax Account Head with a standard tax rate.

- If you wish to apply taxes only on the items with an Item Tax Template then you can set the standard tax rate as 0.
By default ERPNext will automatically set the Taxes and Charges table for you. However, you can change this by changing the Accounts Settings:

    > Accounting > Setup > Accounts Settings > Automatically Add Taxes and Charges from Item Tax Template

### 2. Related Topics
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
