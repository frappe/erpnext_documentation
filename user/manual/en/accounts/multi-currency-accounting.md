<!-- add-breadcrumbs -->
# Multi Currency Accounting

In ERPNext, you can make accounting entries in multiple currencies. For example, if you have a bank account in foreign currency, you can make transactions in that currency and system will show bank balance in that specific currency only.

### 1. Setup
#### 1.1 Set currency in Chart of Accounts
To get started with multi-currency accounting, you need to assign accounting currency in Account record. You can define Currency from [Chart of Accounts](/docs/user/manual/en/accounts/chart-of-accounts) while creating Account.

<img class="screenshot" alt="Set Currency from Chart of Accounts"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/chart-of-accounts.png">

#### 1.2 New account with different currency
You can also assign/modify the currency by opening specific Account record for existing Accounts.

<img class="screenshot" alt="Modify Account Currency"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/account.png">

#### 1.3 Currency for Customer/Supplier
For Customer/Supplier (Party), you can also define its billing currency in the Party record. If the Party's accounting currency is different from Company Currency, you should mention Default Receivable/Payable Account in that currency.

<img class="screenshot" alt="Customer Accounting Currency"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/customer.png">

#### 1.4 After set up
Once you define Currency in the Account and select relevant accounts in the Party record, you are ready to make transactions against them. If Party account currency is different from company currency, system will restrict to make transactions for that party. You need to change the currency to party currency in the transaction. If party account currency is same as company currency, you can make transactions for that Party in any currency. But accounting entries (GL Entries) will always be in Party Account Currency.

You can change accounting currency in Party/Account record, until you make any transactions against them. After making accounting entries, system will not allow you to change the currency for both Party/Account record.

In case of multi-company setup, accounting currency of Party must be same for all the companies.

### 2. Exchange Rates
When dealing with multiple currencies, ERPNext has the Currency Exchange page for managing exchange rates. It allows you to save the exchange rate quotes you require. It's available at **Accounts > Setup > Currency Exchange**.

For foreign currency transactions, ERPNext checks Currency Exchange for any matching record. If this fails, ERPNext will attempt to get the exchange rate quote from [Frankfurter](https://www.frankfurter.app). If this still fails, then the exchange rate will have to be entered manually.

ERPNext automatically fetches the latest exchange rate available.


### 3. Transactions

#### 3.1 Sales Invoice

In Sales Invoice, transaction currency must be same as accounting currency of Customer if Customer's accounting currency is different from Company Currency. Otherwise, you can select any currency in Invoice. On selection of Customer, system will fetch Receivable account from Customer/Company. The currency of receivable account must be same as Customer's accounting currency.

Now, in POS, Paid Amount will be entered in transaction currency, instead of earlier Company Currency. Write Off Amount will also be entered in transaction currency.

Outstanding Amount and Advance Amount will always be calculated and shown in Customer's Account Currency.

<img class="screenshot" alt="Sales Invoice Outstanding"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/sales-invoice.png">

#### 3.1 Purchase Invoice

Similarly, in Purchase Invoice, accounting entries will be made based on Supplier's accounting currency. Outstanding Amount and Advance Amount will also be shown in the supplier's accounting currency. Write Off Amount will now be entered in transaction currency.

#### 3.2 Journal Entry

In Journal Entry, you can make transactions in different currencies. There is a checkbox "Multi Currency", to enable multi-currency entries. If "Multi Currency" option selected, you will be able to select accounts with different currencies.

<img class="screenshot" alt="Journal Entry Exchange Rate"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/journal-entry-multi-currency.png">
 
In the Accounts table, on selection of foreign currency account, system will show Currency section and fetch Account Currency and Exchange Rate automatically. You can change / modify the Exchange Rate later manually. Debit / Credit amount should be entered in Account Currency, system will calculate and show the Debit / Credit amount in Company Currency automatically.

<img class="screenshot" alt="Journal Entry in multi currency"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/journal-entry-row.png">

### 4. Reports

#### 4.1 General Ledger

In General Ledger, system shows debit/credit amount in both currency if filtered by an Account and Account Currency is different from Company Currency.

<img class="screenshot" alt="General Ledger Report"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/general-ledger.png">

#### 4.2 Accounts Receivable/Payable

In Accounts Receivable/Payable report, system shows all the amounts in Party/Account Currency.

<img class="screenshot" alt="Accounts Receivable Report"  	src="{{docs_base_url}}/assets/img/accounts/multi-currency/accounts-receivable.png">

#### 5. Related Topics
1. [Exchange Rate Revaluation](/docs/user/manual/en/accounts/exchange-rate-revaluation)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
