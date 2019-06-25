<!-- add-breadcrumbs -->
#Managing Transactions In Multiple Currency

In ERPNext, transactions can be created in the base currency as well as in parties' (customer or supplier) currency. If the transaction is created in the parties' currency, their currency symbol is updated in the print format as well.

If you are quoting to a Customer in a different currency, you will have to update the conversion rates to enable ERPNext to save the information in your standard currency. This will help you to analyze the value of your Quotations in your currency.

Let's consider a Sales Invoice, where your base currency is USD and party currency is EUR.

1. Create a new Sales Invoice: **Home > Accounting > Billing > Sales Invoice > New**.

1. Select Customer from the Customer master. If default Currency is updated in the Customer master, it'll be fetched here.

1. Currency Exchange between base currency and customer currency will auto-fetched.

    <img alt="Accounts Frozen Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/multiple-currency-1.png">

1. Update other details like Item, Taxes, Terms. In the Taxes and other Charges table. Charges of type Actual should be updated in the Customer's currency.

1. Save Sales Invoice and then check Print Format. For all the Currency field (rate, amount, totals) Customer's Currency symbol will be updated as well.

    <img alt="Accounts Frozen Date" class="screenshot" src="{{docs_base_url}}/assets/img/articles/multiple-currency-2.png">

## Currency Exchange Masters

If you have come to terms with party to follow standard exchange rate throughout, you can capture it by creating a Currency Exchange master. To create one, go to:

> Home > Accounting > Settings > Currency Exchange

In ERPNext, real-time exchange rates are fetched.

**Note**: If you create a Currency Exchange master with a specific rate, it will be given preference over real-time exchange rates. For example, if you set $1 = ₹65 in Currency Exchange, then even if live rate is ₹69, ₹65 will be used in transactions.

{next}
