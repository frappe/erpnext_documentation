<!-- add-breadcrumbs -->
# Itemized Taxation

In sales and purchase transactions, you can apply taxes and other charges on the items. For the ease of applying taxes, you can fetch values from the [Sales Taxes and Charges master](/docs/user/manual/en/setting-up/setting-up-taxes). Taxes and charges are applied equally on all the items.

For example, if tax GST 16% is added in the Taxes and Charges table in Sales Order, then it will be applied on all the items in that Sales Order. However, if you need to have different tax rate applied on some of the items, the steps are given below to setup Items and Sales Taxes and Charges Template master in your ERPNext account. 

### 1. Steps for Itemized Taxation
Let's assume that we are creating a Sales Order. We have Sales Taxes and Charges Template master for GST 16%. Out of all the Sales Items, on one item, only 5% GST will be applied, while another item is exempted from any tax.

####1.1 Mention Tax Applicable in the Item master

Tax templates are preset with values. For items which have a different tax rate than the others, you need to change it in the Item master. Go to the tax table in the Item, add a row, select the tax type and change the rate. Now, this new rate will over ride the template when creating an order/invoice. For example, in the below screenshot you can see that the tax rate is set as 5 and that's the rate which will be applied in transactions.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/item-wise-tax.png">

For the item which is exempted from tax totally, mention 0% as tax rate in the Item master. 

> Note: For Item Tax to work, you need to ensure that the tax types set in Item Tax table (with changed tax rates) in Item master are present in the Sales Taxes and Charges Template.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/exempted-item.png">

####1.2 Setup Taxes and Other Charges

In Sales Taxes and Charges Template master, select GST 16% account and mention Tax Rate as 16. This tax rate will be applied on all the Items selected in the Sales Order, unless specific Tax Rate is defined in the Item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-master.png">

If you want tax rates always to be applied from the Item master, you should update the rate for the tax account as zero in the Sales Taxes and Charges Template.

####1.3 Tax Calculation in transaction	

In the Sales Order, we have selected many Items. For the items shown in blue, tax rate is applied based on tax rate mentioned in the taxes table. For the items highlighted in red, tax rates were fetched from the respective item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation.png">

Please note that an item's tax rate will be pulled from the item master only if you have selected same tax account (GST 16% in this case) in both Item master and in Sales Order under Taxes and Charges section.

#### 2. Related Topics
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
