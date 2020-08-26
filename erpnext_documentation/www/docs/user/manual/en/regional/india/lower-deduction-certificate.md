<!-- add-breadcrumbs -->
# Lower Deduction Certificate

According to tax withholding category, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the govt wants the payers to deduct tax beforehand and deposit it with the government. However this scheme of deducting tax at source may cause hardship to few taxpayers who may not have taxable income for that fiscal year.

Therefore to remove hardship for such taxpayers the government provides an option to obtain a certificate confirming to either a lower rate or NIL rate of TDS compared to the rate specified in the tax withholding category.

## 1. Prerequisites
Before creating and using a Lower Deduction Certificate, it is advised to create and study the following first:
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Tax Withholding Category](/docs/user/manual/en/accounts/tax-withholding-category)

## 2. How to create a Lower Deduction Certificate
1. Go to the Lower Deduction Certificate list and click on New.
1. Enter the Certificate No.
1. Select the Section Code.
1. Enter the [Fiscal Year](/docs/user/manual/en/accounts/fiscal-year).
1. Select supplier having a valid PAN number. PAN number will auto fetched on selection of Supplier.
1. Enter Valid From and Valid Upto dates.
1. Enter rate of TDS as per the certificate and the certificate limit.
1. Click on Save.

![Lower Deduction Certificate](/docs/assets/img/regional/india/lower-deduction-certificate.png)

## 3. Using Lower Deduction Certificate
### 3.1 Use in Purchase Invoice
In the following example, we have selected TDS category as 'TDS - 194D - Individual' which has a rate of 5%.
<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/regional/india/tds-rate.png">

1. **Supplier** has the tax withholding field set, then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not and TDS category will be auto-fetched.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/regional/india/tds-supplier-master.png">

1. Let's create an invoice for 20,000. Saving the invoice automatically calculates tax and appends it in the taxes table. Although the tax category assigned to the supplier has a tax rate of 5% the prevailing tax rate is 1% which is mentioned in the Lower Deduction Certificate.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/regional/india/ltds-purchase-invoice.png">

### 4. Related Topics
1. [Tax Withholding Category](/docs/user/manual/en/accounts/tax-withholding-category)

