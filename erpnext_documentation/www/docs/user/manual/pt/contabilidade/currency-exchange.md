<!-- add-breadcrumbs -->
# Currency Exchange

The Currency Exchange form in ERPNext stores exchange rates manually stored by the User. By default, ERPNext automatically fetched the current exchange rates for currencies as per the market. However, you can store fixed exchange rates and use them. You need to enable 'Allow Stale Exchange Rates' in Accounts Settings for using the exchange rates stored in the Currency Exchange form.

To access the Currency Exchange list, go to:
> Home > Accounting > Multi Currency > Currency Exchange

## 1. How to create a Currency Exchange
1. Go to the Currency Exchange list and click on New.
1. Enter a date from which this exchange rate will be valid. New Currency Exchange forms saved with newer dates will be used in transactions.
1. Set the From and To currency.
1. Enter the Exchange Rate, for example, 1 USD = 65 INR.
1. Select whether the exchange rate applies to selling, buying, or both transactions.
1. Save.

    ![Currency Exchange](/docs/assets/img/accounts/currency-exchange.png)

## 2. Related Topics
1. [Exchange Rate Revaluation](/docs/user/manual/en/accounts/exchange-rate-revaluation)
1. [Multi Currency Accounting](/docs/user/manual/en/accounts/multi-currency-accounting)