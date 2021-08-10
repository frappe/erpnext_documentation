<!-- add-breadcrumbs -->
# Tax Withholding Category

**Tax Withholding Category is Tax Deducted at Source.**

According to this, a person responsible for making payments is required to deduct tax at source at prescribed rates. Instead of receiving tax on your income from you at a later date, the govt wants the payers to deduct tax beforehand and deposit it with the government.

To access the Tax Withholding Category list, go to:
> Home > Accounting > Taxes > Tax Withholding Category

## 1. Prerequisites
Before creating and using a Tax Withholding Category, it is advised to create the following first:

1. [Supplier](/docs/v13/user/manual/en/buying/supplier)
1. [Customer](/docs/v13/user/manual/en/CRM/customer)

## 2. How to create a Tax Withholding Category
In ERPNext, Tax Withholding Categories for most cases are available by default, however, you can create more if needed.

1. Go to the Tax Withholding Category list and click on New.
1. Enter a unique name, eg: Section 194C Individual.
1. Enter a Category Name (Dividends, Professional Fees, etc,.).
1. Enter a Tax Withholding Rate against a [Fiscal Year](/docs/v13/user/manual/en/accounts/fiscal-year).
1. You can set the threshold for a single invoice or sum of all invoices.
1. Select an account against your Company to which tax will be credited.
1. Add more companies and accounts as needed.
1. Save.

 ![Tax withholding Category](/docs/v13/assets/img/accounts/tax-withholding-category.png)

Under accounting details, the TDS account is added for each Company in the system.

### 2.1 Assigning Tax Withholding to Supplier

After saving, it can be assigned to a Supplier:

 ![Tax withholding Category in Supplier](/docs/v13/assets/img/accounts/tax-withholding-category-in-supplier.png)

### 2.2 How does the threshold work?
Consider a Supplier on whom a Tax Withholding Category is applied.

For example, let's say a rate of 5% will be applicable on invoice where Single threshold is 20,000 and the Cumulative threshold is 30,000. If an invoice is created with a grand total of 20,000 then the single threshold will be triggered and a 5% tax would be charged.

But if the invoice amount totaled up to be 15,000 then no tax will be charged as it didn't cross the threshold. If again another invoice is created against the same supplier with a total of 15,000 then although it didn't cross the Single threshold, charges will be deducted since the sum of the last invoice and this invoice adds up to be 30,000 which is equal to the specified Cumulative threshold.

## 3. Using Tax Withholding
### 3.1 Use in Purchase Invoice
In the following example, we have selected 'TDS - 194C - Individual' which has a single threshold of 30,000, cumulative threshold of 1,00,000 and rate of 1%.

1. If the **Supplier** has the tax withholding field set, then upon selecting that Supplier, a checkbox will become visible in the Purchase Invoice to select whether to apply tax or not.

![Tax Withholding Category in Purchase Invoice](/docs/v13/assets/img/accounts/tax-withholding-category-in-purchase-invoice.png)

1. Let's create an invoice for 90,000. Saving the invoice automatically calculates tax and appends it in the taxes table.

 ![Tax Withholding Category in Purchase Invoice](/docs/v13/assets/img/accounts/withheld-tax-calculation-in-purchase-invoice.png)

1. To see the effect of Cumulative threshold, let's create an invoice with of amount 10,000 and submit it.

  ![Tax Withholding Category Cumulative Threshhold](/docs/v13/assets/img/accounts/tax-withholding-category-cumulative-threshold.png)

 Although the invoice amount didn't cross the Single threshold (30,000), we see that tax has been charged. This is because the previous and the current invoice adds up to be 1,10,000 which exceeds the Cumulative threshold. Hence, tax based on the rate provided in the **Tax Withholding Category** is applied accordingly.

> Note: On submitting the invoice, three GL Entries are created:

>1. First for debit from the expense head
>1. Second for credit in Creditors account
>1. Third for credit in the account selected in Tax Withholding Category.

### 3.2 Deducting TDS on Advances
#### 3.2.1 Deduction Advance TDS against Purchase Order
1. Set up Tax Withholding Category against supplier and follow the same steps required to apply TDS in a Purchase Invoice as shown in the image below

![TDS Purchase Order](/docs/v13/assets/img/accounts/tds-purchase-order.png)

2. Create Payment Entry against that Purchase Order, all the relevant details required to apply TDS will be pulled.

![TDS Payment Entry](/docs/v13/assets/img/accounts/tds-po-payment-entry.png)

3. Update Advance Tax Account or add "Unrealized Profit and Loss Account" in company master which will be used as the default Advance Tax Account if not specific in the transaction

![Advance Tax Account](/docs/v13/assets/img/accounts/advance-tax-account.png)

4. Once a Purchase Invoice is created against this order, TDS will still be applied but the new effect of TDS will be zero, hence no TDS payable. In a way the Advance TDS Paid will be allocated against the invoice.

![TDS Purchase Invoice](/docs/v13/assets/img/accounts/tds-purchase-invoice.png)

### 3.2.2 Deducting TDS against advances paid (Using Payment Entry)
1. Select "Payment Type" as "Pay"
2. Select "Party Type" as "Supplier" and the appropriate supplier
3. Enter paid amount, paid can be before of after TDS deduction
4. Under the Taxes and Charges section check "Apply Tax Withholding Amount" and select Tax Withholding Category
5. Click on Save. TDS will be auto applied
6. Submit the entry
7. Same will also be visible in TDS payable monthly report

![Advance Tax Account](/docs/v13/assets/img/accounts/advance-tax-account.png)

![TDS Payable Monthly Report](/docs/v13/assets/img/accounts/advance-tds-payable-monthly.png)

### 3.3 Setting up TCS - Section 20C(1H) for eligible customers
In the following example, we have create a Tax Withholding Category for [TCS - Section 20C(1H)](https://taxguru.in/income-tax/faqs-tcs-sales-goods-section-206c1h.html) and set it up against an eligible customer.

1. We will first create a Tax Withholding Category named **TCS - Section 20C(1H)** and we set cumulative threshold to 50 Lakhs as per the scheme.

![Tax Withholding Category For TCS](/docs/v13/assets/img/accounts/tax-withholding-category-for-tcs.png)

1. If a **Customer** is expected to crosses the sales threshold of 50 Lakh in current Fiscal Year, then we can set the Tax Withholding Category of the customer to TCS - Section 20C(1H) for automatically calculation TCS on sale of goods against the customer's invoices.

 ![TCS in Customer](/docs/v13/assets/img/accounts/tcs-eligible-customer.png)

1. Let's create an invoice for 50 Lakhs against the eligible customer. Saving the invoice automatically calculates tax and appends it in the taxes table.

 ![TCS Calculation in Sales Invoice](/docs/v13/assets/img/accounts/tcs-invoice.png)

 Since the invoice cross the Cumulative threshold (50 Lakhs), we see that tax has been charged. Hence, tax based on the rate provided in the **Tax Withholding Category** is applied accordingly. Note that, as per the scheme, the TCS is calculated on the amount exceeding the threshold i.e 0.075 % of 10 Lakhs.

### 4. Related Topics
1. [Tax Rule](/docs/v13/user/manual/en/accounts/tax-rule)
1. [Supplier](/docs/v13/user/manual/en/buying/supplier)
1. [Customer](/docs/v13/user/manual/en/CRM/customer)

{next}
