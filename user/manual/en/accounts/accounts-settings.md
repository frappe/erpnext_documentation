<!-- add-breadcrumbs -->
# Accounts Settings

There are various account settings in ERPNext to restrict and configure actions in the Accounting module.

<img class="screenshot" alt="Account Settings" src="{{docs_base_url}}/assets/img/accounts/account-settings.png">

#### 1. Accounts Frozen Up to
Freeze accounting transactions up to specified date, nobody can make/modify entry except specified role.

#### 2. Role Allowed to Set Frozen Accounts & Edit Frozen Entries
Users with this role are allowed to set frozen accounts and create / modify accounting entries against frozen accounts.

#### 3. Credit Controller
Select the role that is allowed to submit transactions that exceed credit limits set.

#### 4. Check Supplier Invoice Number Uniqueness
When checked, Purchase Invoices with same Supplier Invoice No will not be allowed.

#### 5. Make Payment via Journal Entry
When checked, if user chooses to make payment from invoice, this will open the journal entry instead of payment entry.

#### 6. Unlink Payment on Cancellation of Invoice
If checked, system will unlink the payment against the invoice. Otherwise, it will show the link error.

#### 7. Book Asset Depreciation Entry Automatically
When checked, an automatic entry for an asset depreciation will be created based on the first date set. For example, yearly depreciation for an item will be scheduled for the next 3/4 years based on the Number of Depreciations Booked set in the Asset master.

#### 8. Allow Cost Center in Entry of Balance Sheet Account
If checked, system will allow user to tag entry in Balance Sheet Account against a Cost Center.

#### 9. Allow Stale Exchange Rate
This should be unchecked if you want ERPNext to check the age of records fetched from Currency Exchange in foreign currency transactions. If it is unchecked, the exchange rate field will be read-only in documents. Stale Days is the number of days to use when deciding if a Currency Exchange record is stale. For example, if Currency Exchange records are to be updated every day, the Stale Days should be set as 1. 
