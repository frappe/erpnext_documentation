<!-- add-breadcrumbs -->
# Purchase Taxes and Charges Template

**Purchase Taxes and Charges may be applied to any item you buy.**

The Purchase Taxes and Charges Template is similar to the Sales Taxes and Charges Template. The templates created from this form can be used in Purchase Orders and Purchase Invoices for internal records.

For Tax Accounts that you want to use in the tax templates, you must set the Account Type field as 'Tax' for that particular account.

## 1. How to add Purchase Taxes/Charges via a template
Before creating a new template, note that templates are already created for many of the commonly used taxes.

1. Go to **Buying > Settings > Purchase Taxes and Charges Template > New**.
2. Enter a title name for the Tax.
3. Under type, set on what the tax will be calculated and the tax rate. There are four options under type for which tax will be calculated.
  1. Actual: On the actual amount of each item.
  1. On Net Total: On the grand total of all the items.
  1. On Previous Row Amount: This is for compounding the charges. For example, cess charges over the tax already applied in the previous row.
  1. On Previous Row Total: Same as above but applied on the total and not just the amount.
4. Select an account head which has pre set tax rates or create your own.
1. Selecting default will apply this template by default for new Purchase transactions.
1. 
5. Save.
<img class="screenshot" alt="Purchase taxes" src="{{docs_base_url}}/assets/img/buying/purchase-taxes.png">

You can specify if the tax/charge is only applicable for valuation (not a part of total) or only for total (does not add value to the item), or if the tax/charge is applicable for both. [Check out this article](/docs/user/manual/en/accounts/articles/what-is-the-differences-of-total-and-valuation-in-tax-and-charges) to know the difference.

If you select a particular tax as your Default tax, this
tax will be applied to all the purchase transactions by default. 

## 2. Features
### 2.1 Purchase Taxes and Charges table
Consider Tax or Charge for:

### 2.1 Calculation Type

This can be on Net Total (that is the sum of basic amount). On Previous Row
Total / Amount (for cumulative taxes or charges). If you select this option,
the tax will be applied as a percentage of the previous row (in the tax table)
amount or total. Actual (as mentioned). To see some of the following options, expand the row by clicking on the downward facing triangle.

  * **Account Head:** The Account ledger under which this tax will be booked.
  * **Cost Center:** If the tax / charge is an income (like shipping) or expense it needs to be booked against a Cost Center.
  * **Description:** Description of the tax (that will be printed in invoices / quotes).
  * **Rate:** Tax rate.
  * **Amount:** Tax amount.
  * **Total:** Cumulative total to this point.
  * **Enter Row:** If based on "Previous Row Total" you can select the row number which will be taken as a base for this calculation (default is the previous row).
  * **Consider Tax or Charge for:** In this section you can specify if the tax/charge is only for valuation (not a part of total) or only for total (does not add value to the item) or for both.
  * **Add or Deduct:** Whether you want to add or deduct the tax.

### 3. Related Topics
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Buying Settings](/docs/user/manual/en/buying/setup/buying-settings)