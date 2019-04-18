<!-- add-breadcrumbs -->
# Exchange Rate Revaluation

In ERPNext, you can make accounting entries in multiple currencies. For example, if you have a bank account in foreign currency, you can make transactions in that currency and system will show bank balance in that specific currency.

### 1. How to set up currency in an account

1. To get started with multi-currency accounting, you need to assign accounting currency in Account record.
1. You can define Currency from Chart of Accounts while creating Account.

    <img class="screenshot" alt="Set Currency from Chart of Accounts"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/chart-of-accounts.png">

1. You can also assign/modify the currency for existing accounts by opening the specific Account record.
1. Click on the Account and Click on Edit.

   <img class="screenshot" alt="Modify Account Currency"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/account.png">

### 2. How to enable Exchange Rate Revaluation

Exchange Rate Revaluation feature is for dealing the situation when you have a multiple currency accounts in one company's chart of accounts

1. Go to: **Setup > Company > *select the company***.
1. Set the 'Unrealized Exchange Gain/Loss Account' field in Company DocType. This account is to balance the difference of total credit and total debit.
    <img class="screenshot" alt="Field Set for Company"  	src="{{docs_base_url}}/assets/img/accounts/exchange-rate-revaluation/field_set_company.png">
1. Go to **Exchange Rate Revaluation** by searching from the awesome bar.
1. Select the Company.
1. Click the Get Entries button. It'll fetch the accounts which have different currency as compared to 'Default Currency' in Company DocType.
1. This will fetch the new exchange rate automatically if not set in Currency Exchange DocType for that currency else it will fetch the 'Exchange Rate' set in the Currency Exchange DocType.
    <img class="screenshot" alt="Exchange Rate Revaluation"  	src="{{docs_base_url}}/assets/img/accounts/exchange-rate-revaluation/exchange-rate-revaluation.png">

1. On Submitting, 'Make Journal Entry' button will appear.
1. Clicking on this button will create a journal entry for the Exchange Rate Revaluation.

<img class="screenshot" alt="Exchange Rate Revaluation Submitting"  	src="{{docs_base_url}}/assets/img/accounts/exchange-rate-revaluation/exchange-rate-revaluation-submit.png">

<img class="screenshot" alt="Journal Entry"  	src="{{docs_base_url}}/assets/img/accounts/exchange-rate-revaluation/journal-entry.png">

#### 3. Related Topics
1. [Inter Company Journal Entry](/docs/user/manual/en/accounts/inter-company-journal-entry)
1. [Inter Company Invoices](/docs/user/manual/en/accounts/inter-company-invoices)
