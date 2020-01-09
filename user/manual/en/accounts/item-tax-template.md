<!-- add-breadcrumbs -->
# Item Tax Template

**Item Tax Template is useful for item wise taxation.**

If some of your Items have tax rates different from the standard tax rate assigned in the Taxes and Charges table, then you can create an Item Tax Template and assign it to an [Item](/docs/user/manual/en/stock/item) or [Item Group](/docs/user/manual/en/stock/item-group). The rate assigned in the Item Tax Template will get preference over the standard tax rate assigned in the Taxes and Charges table.

For example, if tax GST 18% is added in the Taxes and Charges table in Sales Order, then it will be applied on all the items in that Sales Order. However, if you need to have different tax rate applied on some of the items, the steps are given below

To access the Item Tax Template list, go to
> Home > Accounting > Taxes > Item Tax Template

Let's assume that we are creating a Sales Order. We have the [Sales Taxes and Charges Template](/docs/user/manual/en/selling/sales-taxes-and-charges-template) master for GST 9%. Out of all the Sales Items, on one Item, only 5% GST will be applied, while another item is exempted from tax (non taxable). You need to select the Account Head of the tax and set its overriding rate.

## 1. Prerequisites
Before creating and using an Item Tax Template, it is advised to create the following first:

1. [Item](/docs/user/manual/en/stock/item)
1. Enable 'Automatically add Taxes and Charges from Item Tax Template' in [Account Settings](/docs/user/manual/en/accounts/accounts-settings)

## 2. How to create an Item Tax Template
1. Go to the Item Tax Template list and click on New.
1. Enter a title for the Item Tax Template.
1. Select an account and set the overriding rate. Add more rows if required.
1. Save.

Now the Item Tax Template is ready to be assigned to an Item. To do this, go the Item, Item Tax section and select an Item Tax Template:

![Item Tax In Item](/docs/assets/img/accounts/item-tax-in-item.png)

> Note: It is advised to not use the Sales/Purchase Template selected here in [Tax Rule](/docs/user/manual/en/accounts/tax-rule), it may cause interference. If you want to use same tax rates for Tax Rule and Item Tax Template, use a different name for the Sales/Purchase Tax Templates.

### 2.1 Mention Tax Applicable in the Item master

Tax templates are preset with values. For items which have a different tax rate than the others, you need to change it in the Item master. Go to the tax table in the Item, add a row, select the tax type and change the rate. Now, this new rate will over ride the template when creating an order/invoice. For example, in the below screenshot you can see that the tax rate is set as 5 and that's the rate which will be applied in transactions.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/item-wise-tax.png">

For the Item which is exempted from tax entirely, mention 0% as tax rate in the Item master.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/exempted-item.png">

> Note: For Item Tax Template to work, you need to ensure that the tax types (accounts) set in Item Tax Template (with changed tax rates) are present in the Sales Taxes and Charges Template.

> If you want to include multiple items with different tax rates, you need to have record them under different tax heads. For example, VAT 14%, VAT 5% etc.

### 2.2 Tax Calculation in transaction

For example, in the following screenshot, the Item has an Item Tax Template assigned to it with 5% on two tax heads.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation.png">

The tax is fetched from the Item Tax Template and calculated:
<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation1.png">

### 2.3 Item Tax Template for each Items
You can also manually select a different Item Tax Template for each Item in a transaction:

![Item Tax individual](/docs/assets/img/accounts/item-tax-each.png)


### 2.4 Item wise tax on an Item Group
You can assign the Item Tax Template to an Item Group by modifying the Item Tax table in the Item Tax section within the Item Group document.
<img class="screenshot" alt="Item Tax in Item Group" src="{{docs_base_url}}/assets/img/accounts/item-group-tax.png">

Item Tax Template applied on an Item Group will apply to all Items in that group unless an individual Item in the Item Group has its own Item Tax Template assigned to it.


### 2.5 Validity of Item Taxes

<img class="screenshot" alt="Item Tax in Item Group" src="{{docs_base_url}}/assets/img/accounts/item-tax-in-item.png">

You can also assign validity to tax templates as shown in the image above.

* Based on the posting date of the transaction, a valid tax template will be automatically fetched.
* If there are more than one valid tax templates then the first valid tax template from Item Tax table will be fetched.
* In case when there are no valid tax templates then the first tax template with no 'Valid From' date in the Item Tax table will be fetched.

> Note: While adding items in Purchase Invoice first preference will be given to 'Supplier Invoice Date' instead of 'Posting Date' for fetching valid Item Tax Template.

### 2.6 Some points to note

- If you set the Tax Category as empty, the default Item Tax Template will be applied to Items in transactions.

- You can apply different Item Tax Templates for different Tax Categories.

- For an Item Tax Template to override taxes, there must be a row in the Taxes and Charges table with the same tax Account Head with a standard tax rate.

- If you wish to apply taxes only on the Items with an Item Tax Template then you can set the standard tax rate as 0.

### 3. Related Topics
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
