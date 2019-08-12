<!-- add-breadcrumbs -->
# Tax Withholding Category

Tax Withholding Category is simply Tax Deducted at Source. According to this, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the govt wants the payers to deduct tax before hand and deposit it with the government.

### 1. How to create a Tax Withholding Category
1. Go to: **Accounts > Taxes > Tax Withholding Category > New**.
1. Enter a unique name for the doctype (eg: Section 194C Individual).
1. Enter a Category Name (Dividends, Professional Fees etc,.).
1. Enter a Tax Withholding Rate against a Fiscal Year.
1. You can set the threshold for a single invoice or sum of all invoices.
1. Select an account against your company to which tax will be credited.
1. Add more companies and accounts as needed.
1. Save.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-1.png">

#### 1.1 How does the threshold work?
Lets say a rate of 5% will be applicable on invoice where Single threshold is 20,000 and Cumulative threshold is 30,000. If an invoice is created with a grand total of 20,000 then the single threshold will be triggered and a 5% tax would be charged. But if the invoice amount totalled up to be 15,000 then no tax will be charged as it didn't cross the threshold. If again an invoice is created with a total of 15,000 then although it didn't cross the Single threshold, charges will be deducted since the sum of last invoice and this invoice adds up to be 30,000 which is equal to the specified Cumulative threshold.

### 2. Using Tax Withholding
#### 2.1 Enable in Supplier

Select the Tax Category that needs to be applied on the Supplier and Save, shown as follows.

<img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-1.png">

#### 2.2 Use in Purchase Invoice

1. If the **Supplier** has the tax withholding field set, then upon selecting that supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not.

  <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-2.png">

1. Saving the invoice, automatically calculates tax and appends it in the taxes table.

   <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-6.png">

1. In case of Cumulative threshold, let's create an invoice with a total of 15,000 and submit it.

   <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-7.png">

1. Now, lets create another similar invoice. Although the invoice amount didn't cross the Single threshold, we see that tax has been charged. This is because the previous and the current invoice adds up to be 30,000 which exceeds the Cumulative threshold. Hence, tax based on the rate provided in the **Tax Withholding Category** is applied accordingly.

   <img class="screenshot" alt="Tax Withholding Category" src="{{docs_base_url}}/assets/img/accounts/tax-withholding-category-8.png">

> Note: On submitting the invoice, three GL Entries are created:


>1. First for debit from the expense head
>1. Second for credit in Creditors account
>1. Third for credit in the account selected in Tax Withholding Category.

#### 3. Related Topics
1. [Tax Rule](/docs/user/manual/en/accounts/tax-rule)

