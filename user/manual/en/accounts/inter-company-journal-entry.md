<!-- add-breadcrumbs -->
# Inter Company Journal Entry

**An Inter Company Journal Entry is done between organizations that belong to the same group.**

You can create Inter Company Journal Entry if you are making transactions with multiple Companies.
You can select the Accounts which you wish to use in the Inter Company transactions. A possible use case would be a company buying goods on behalf of another company.

Before creating an Inter Company Journal Entry, you need to set up your Chart of accounts.

1. Go to: **Accounts > Company and Accounts > Chart Of Accounts**.
1. Select the Account which you would like to set as an Internal Account for the transaction, and check the 'Inter Company Account' checkbox. This account can now be used for Inter Company Journal Entry transactions. It is recommended to create a new account for inter company transactions.
    <img class="screenshot" alt="Internal Account" src="{{docs_base_url}}/assets/img/accounts/internal-account.png">
You need to do the same for all the Companies' Accounts which you want to use for Inter Company Journal Entry transactions.

In case of parent-child companies, when an account is created in the parent company, it gets added in the child company. This works only if you've selected the option to create Chart of Accounts for child Company based on the parent Company.

Inter company Journal Entries are created using the Journal Entry form in ERPNext. To access the Journal Entry list, go to:

> Home > Accounts > Company and Accounts > Journal Entry

## 1. Prerequisites
Before creating an Inter Company Journal Entry, you need the following:

* At least two [Companies](/docs/user/manual/en/setting-up/company-setup)
* Setting inter company accounts in [Chart of Accounts](/docs/user/manual/en/accounts/chart-of-accounts)

## 2. How to create an Inter Company Journal Entry
1. Go to the Journal Entry list, and click on New.
1. Select Entry Type as 'Inter Company Journal Entry'.
1. Set the Company that is buying Items on behalf of another company.
1. Add rows for the individual accounting entries. Only inter company accounts can be fetched here.
1. In each row, you must specify:
  * The Internal account that will be affected. 
  * The amount to Debit or Credit.
  * The Cost Center (If it is an Income or Expense).
1. On submitting the Journal Entry, you will find a button on the top right corner, **Make Inter Company Journal Entry**.

   <img class="screenshot" alt="Submitted Inter Company Journal Entry" src="{{docs_base_url}}/assets/img/accounts/inter-company-jv-submit.png">

1. Click on the button. Now, you will be asked to select the Company against which you wish to create the linked Journal Entry.

    <img class="screenshot" alt="Select Company" src="{{docs_base_url}}/assets/img/accounts/select-company-jv.png">

1. On selecting the Company, you will be routed to another Journal Entry where the relevant fields will be mapped, i.e. Company, Voucher Type, Inter Company Journal Entry Reference etc. 

    <img class="screenshot" alt="Linked Journal Entry" src="{{docs_base_url}}/assets/img/accounts/linked-jv.png">

1. Select the Internal accounts for the second Company in the table.
1. Submit the Journal Entry.
1. Make sure the total Debit and Credit Amounts are same as the previously created Journal Entry's total Credit and Debit Amounts respectively but the debits and credits will be opposite.

**Note:** The accounts in second Journal Entry should be the opposite of what you did in the first Journal Entry.
For example, Company A is buying something from Company B. This is how the payment cycle between the two companies will look like using Inter Company Journal Entry.

1. Debit Bank Account by 500 and credit Debtors account of Company B by 500.
1. Now, in the Inter Company Journal Entry, debit Creditors account of Company A by 500 and credit Bank Account by 500. 
1. You also need to select the parties for Creditors and Debtors account before proceeding with the Journal Entry.

You can also find the reference link at the bottom, which will be added in both the linked Journal Entries and will be removed if any of the Journal Entries are cancelled.

### 3. Related Topics
1. [Journal Entry](/docs/user/manual/en/accounts/journal-entry)
1. [Inter Company Invoices](/docs/user/manual/en/accounts/inter-company-invoices)
