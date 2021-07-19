<!-- add-breadcrumbs -->
# Sales Taxes and Charges Template

**Sales Taxes and Charges may be applied to any item you sell.**

The templates created from this form can be used in Sales Orders and Sales Invoices.

For Tax Accounts that you want to use in the tax templates, you must set the Account Type field as 'Tax' for that particular account. The way ERPNext sets up taxes is via templates. Other types of charges that
may apply to your invoices (like shipping, insurance etc.) can also be configured as taxes.

To know about setting up taxes visit [this page](/docs/user/manual/en/setting-up/setting-up-taxes).

To access Sales Taxes and Charges Template, go to:
> Home > Selling > Settings > Sales Taxes and Charges Template

To know about setting up taxes visit [this page](/docs/user/manual/en/setting-up/setting-up-taxes)

## 1. How to add Sales Taxes/Charges via a template
Before creating a new template, note that templates are already created for many of the commonly used taxes.

1. Go to the Sales Taxes and Charges Template list, click on New.
2. Enter a title name for the Tax.
3. Under type, set on what the tax will be calculated and the tax rate. There are five options under type for which tax will be calculated.
  1. Actual: You can directly enter the amount for the expense.
  1. On Net Total: On the net total of all the items.
  1. On Previous Row Amount: This is for compounding the charges. For example, cess charges over the amount to which tax was already applied in the previous row.
  1. On Previous Row Total: Same as above but applied on the total bill and not just the amount of an item.
  1. On Item Quantity: Tax will be calculated as Tax Rate * Item Quantity. For example, if Tax Rate is 2% and number of Items is 1, then Tax Rate will be 4, if number of Items are 5, Tax Rate will be 10, and so on.
4. Select an account head which has pre set tax rates or create your own.
1. Selecting default will apply this template by default for new Sales transactions.
5. Save.
  ![Sales taxes](/docs/v12/assets/img/selling/sales-taxes.png)

**Is Inter State**: For India. On selection of a customer in Sales Invoice or Delivery Note, if the GST codes of place of supply and customer shipping address don't match, the template with 'Is Inter State' ticked will be set as the taxes template. If the place of supply and shipping address are the same, the default taxes template will be applied. This also applies to Purchase Invoice, on selection of Supplier, the templates are set depending on the addresses. For example, IGST.

## 2. Features
### 2.1 Sales Taxes and Charges table

* **Consider Tax or Charge for**: Total - for the total of all items. Valuation - for each item. Valuation and total - apply tax/charge to both. [Check out this article](/docs/user/manual/en/accounts/articles/what-is-the-differences-of-total-and-valuation-in-tax-and-charges) to know the difference.

* **Reference Row #**: If tax is based on "Previous Row Total" you can select the row number which will be taken as a base for this calculation (default is the previous row).
    ![Sales taxes table](/docs/v12/assets/img/selling/sales-taxes-table.png)

* **Is this Tax included in Basic Rate?**: If checked, the tax amount will be considered as already included in the Print Rate / Print Amount in the Item table of a transaction. This is useful when you want to give tax inclusive price to your customers. To account for tax inclusive rates, the system calculates the Net Amount by deducting the amount of tax to be applied then calculates the tax on it.
* **Account Head:** The Account ledger under which this tax will be booked. If you select VAT or any other preset heads, the rate will be automatically filled.
* **Cost Center:** If the tax/charge is an income (like shipping) or expense it needs to be booked against a Cost Center.
* **Description:** Description of the tax (that will be printed in invoices/quotes).
* **Rate:** The Tax rate, eg: 14 = 14% tax.
* **Amount:** The Tax amount to be applied, eg: 100.00 = ₹100 tax.

The tax rates you define in the template be the standard tax rate for all Items. If there are Items that are supposed have different rates, you can override the standard tax rate by setting an Item Tax Template to the Item or Item Group.

### 3. Related Topics
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
1. [Selling Settings](/docs/user/manual/en/selling/selling-settings)

{next}