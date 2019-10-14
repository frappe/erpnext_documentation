<!-- add-breadcrumbs -->
# Accounts Settings

There are various account settings in ERPNext to restrict and configure actions in the Accounting module.

![Account Settings]({{docs_base_url}}/assets/img/accounts/account-settings.png)

## 1. Accounts Frozen Up to
Freeze accounting transactions up to specified date, nobody can make/modify entry except the specified Role.

## 2. Role Allowed to Set Frozen Accounts & Edit Frozen Entries
Users with this Role are allowed to set frozen accounts and create/modify accounting entries against frozen accounts.

## 3. Determine Address Tax Category From
[Tax category](/docs/user/manual/en/accounts/tax-category) can be set on Addresses. An address can be Shipping or Billing address. Set which addres to select when applying Tax Category.

## 4. Over Billing Allowance Percentage
The percentage by which you can overbill transactions. For example, if the order value is $100 for an Item and percentage here is set as 10% then you are allowed to bill for $110.

## 5. Credit Controller
Select the role that is allowed to submit transactions that exceed credit limits set. The credit limit can be set in the Customer form.

## 6. Check Supplier Invoice Number Uniqueness
When checked, Purchase Invoices with same 'Supplier Invoice No' will not be allowed. This is useful to avoid duplicate entries. 

## 7. Make Payment via Journal Entry
When checked, if user proceeds to make payment from an invoice, the system will open a Journal Entry instead of a Payment Entry.

## 8. Unlink Payment on Cancellation of Invoice
If checked, system will unlink the payment against the respective invoice. By default, if a Payment Entry is submitted, the linked invoice cannot be canceled until the Payment Entry is also canceled. On unlinking, you can now cancel and amend the invoices. But the payments not be linked and considered as advance payments.

## 9. Unlink Advance Payment on Cancellation of Order
Similar to the previous option, this unlinks any advance payments made against Purchase/Sales Orders. 


## 10. Book Asset Depreciation Entry Automatically
When checked, an automatic entry for an asset depreciation will be created based on the first date set. For example, yearly depreciation for an item will be scheduled for the next 3/4 years based on the Number of Depreciations Booked set in the Asset master. For more details, visit the [Asset Depreciation](/docs/user/manual/en/asset/asset-depreciation) page.

## 11. Allow Cost Center in Entry of Balance Sheet Account
If checked, system will allow user to tag entries in Balance Sheet Accounts against a Cost Center. By default Cost Center is available only for Profit/Loss account.

## 12. Automatically Add Taxes and Charges from Item Tax Template
Enabling this will populate the Taxes table in transactions if an [Item Tax Template](/docs/user/manual/en/accounts/item-tax-template) is set for an Item and that Item is selected in the transaction.

## 13. Automatically Fetch Payment Terms
Enabling this will automatically fetch the Payment Terms based on the Supplier. 

## 14. Print Settings

![Account Settings]({{docs_base_url}}/assets/img/accounts/account-settings-1.png)

* **Show Inclusive Tax In Print**: The applied taxes will be shown in the print view.
* **Show Payment Schedule in Print**: The Payment Schedule table is visible on using [Payment Terms](/docs/user/manual/en/accounts/payment-terms). Enabling this will show this table in print view.

## 15. Allow Stale Exchange Rate
This should be unchecked if you want ERPNext to check the age of records fetched from Currency Exchange in foreign currency transactions. If it is unchecked, the exchange rate field will be read-only in documents.

Stale Days is the number of days to use when deciding if a Currency Exchange record is stale. This is valid when 'Allow Stale Rates' is **disabled**. So, if the Stale Days is set as 10, stale rates that are 10 days will be allowed. If Allow Stale Rates is enabled, there is no time limit on the age of stale rates.

If stale rates are enabled, the order of fetching is:

* Latest rate from Currency Exchange form
* If no Currency Exchange is found latest rate as per market is fetched automatically

If stale rates are disabled, the order of fetching is:

* Latest rate from Currency Exchange form upto number of days set in 'Stale Days'
* If no Currency Exchange is found Latest rate as per market is fetched automatically


## 16. Use Custom Cash Flow Format
You may choose to use Custom Cash Flow Formats to customize what the Cash Flow report looks like. To know more, [visit this page](/docs/user/manual/en/accounts/articles/how-to-customise-cash-flow-report).