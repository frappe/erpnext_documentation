<!-- add-breadcrumbs -->
# Setting Up Pharmacy
ERPNext Healthcare do not have a Pharmacy module as such. However, [ERPNext Stock](/docs/v13/user/manual/en/.html), [Buying](/docs/v13/user/manual/en/buying.html) and [Accounts](/docs/v13/user/manual/en/accounts.html) Module will do all that's needed to seamlessly manage your Pharmacy Stock as well as other supplies, their billing and purchases.

You can also consider creating multiple POS Profiles for each Pharmacy user. ERPNext Stock module features like [Items](/docs/v13/user/manual/en/stock/item.html) with Reorder Levels and Auto Reordering, [Batch Number and Expiry Dates](/docs/v13/user/manual/en/stock/batch.html) etc. will be worth looking at.

ERPNext Healthcare adds a few custom fields to `Item` document so that you can effectively configure medicines. Also read [Healthcare Settings](/docs/v13/user/manual/en/healthcare/healthcare_settings) for setting up default Items, Accounts etc.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/item_custom_fields.png">

>Note that these fields are made available only if your setup has Healthcare domain enabled.

Furthermore, all the three modules comes with exhaustive reporting and you can also configure auto email to have reports emailed automatically to you.

{next}
