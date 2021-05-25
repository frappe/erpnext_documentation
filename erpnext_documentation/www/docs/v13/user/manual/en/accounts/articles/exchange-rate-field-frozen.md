<!-- add-breadcrumbs -->
# Exchange Rate Field Frozen

In ERPNext, you can fetch Exchange Rates between currencies in real-time, or save specific exchange rates as well. In ERPNext, saved exchange rates are also referred as Stale Exchange Rate.

In your sales and purchase transactions, if the field of Currency Exchange Rate is frozen, that is because the feature of allowing stale exchange rates in transactions is enabled. To you wish to make Currency Exchange Rate field editable again, then disable the feature of Stale Exchange Rate from:

* Accounting > Accounting Masters > Accounts Settings
* Uncheck field "Allow Stale Exchange Rates".

    ![Allow Stale Exchange Rates](/docs/v13/assets/img/articles/allow-stale-exchange-rates.png)
    
* Save Account Settings
* Refresh your ERPNext account
* Check Sales / Purchase transaction once again

After this setting, the Exchange Rate field in the transactions should become editable once again.

{next}
