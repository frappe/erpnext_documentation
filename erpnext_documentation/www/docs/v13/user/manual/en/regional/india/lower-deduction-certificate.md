<!-- add-breadcrumbs -->
# Lower Deduction Certificate

According to the tax withholding category, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the government wants the payers to deduct tax beforehand and deposit it with the government. However this scheme of deducting tax at source may cause issues to a few taxpayers who may not have taxable income for that fiscal year.

Therefore, for such taxpayers, the government provides an option to obtain a certificate confirming to either a lower rate or NIL rate of TDS compared to the rate specified in the tax withholding category.

## 1. Prerequisites
Before creating and using a Lower Deduction Certificate, it is advised to create and study the following first:

1. [Supplier](/docs/v13/user/manual/en/buying/supplier)
1. [Tax Withholding Category](/docs/v13/user/manual/en/accounts/tax-withholding-category)

## 2. How to create a Lower Deduction Certificate
1. Go to the Lower Deduction Certificate list and click on New.
1. Enter the Certificate No.
1. Select the Section Code.
1. Enter the [Fiscal Year](/docs/v13/user/manual/en/accounts/fiscal-year).
1. Select the Supplier having a valid PAN number. PAN number will be auto fetched on the selection of Supplier.
1. Enter Valid From and Valid Up To dates.
1. Enter rate of TDS as per the certificate and the certificate limit.
1. Click on Save.

 ![Lower Deduction Certificate](/docs/v13/assets/img/regional/india/lower-deduction-certificate.png)

## 3. Using Lower Deduction Certificate

### 3.1 Use in Purchase Invoice

In the following example, we have selected TDS category as 'TDS - 194D - Individual' which has a rate of 5%.

 ![Tax Withholding Category](/docs/v13/assets/img/regional/india/tax-withholding-category.png)

1. Set the Tax Withholding Category for the Supplier in the supplier master. Then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not and the TDS category will be auto-fetched.

 ![Supplier With Tax Withholding Category](/docs/v13/assets/img/regional/india/supplier-with-tax-withholding-category.png)

1. Let's create an invoice for 20,000. Saving the invoice automatically calculates tax and appends it in the Purchase Taxes and Charges table. Although the tax category assigned to the supplier has a tax rate of 5%, the prevailing tax rate is 1% which is mentioned in the Lower Deduction Certificate.

 ![Lower TDS in Purchase Invoice](/docs/v13/assets/img/regional/india/lower-tax-withholding-in-purchase-invoice.png)

### 4. Related Topics
1. [Tax Withholding Category](/docs/v13/user/manual/en/accounts/tax-withholding-category)

{next}
