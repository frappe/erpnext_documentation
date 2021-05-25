<!-- add-breadcrumbs -->
# Fixing Fiscal Year Error

While creating any entry, system validates if dates (like Posting Date, Transaction Date etc.) belong to Fiscal Year selected. If not, system through an error message saying:

`Date ##-##-#### not in fiscal year`

You are more likely to receive this error message if your Fiscal Year has changes, but new Fiscal Year still not set a default. To ensure new Fiscal Year is auto updated in the transactions, you should setup your master as instructed below.

#### Create New Fiscal Year

Only User with System Manager's Role Assigned has permission to create new Fiscal Year. To create new Fiscal Year, go to:

`Accounting > Accounting Masters > Fiscal Year`

Read [Fiscal Year](/docs/v13/user/manual/en/accounts/fiscal-year) to learn more.

#### Set Fiscal Year as Default

After Fiscal Year is saved, you will find option to set that Fiscal year as Default.

![Set Fiscal Year as Default](/docs/v13/assets/img/articles/set-fiscal-year-as-default.png)

Default Fiscal Year will be updated in the Global Default setting as well. You can manually update Default Fiscal Year from:

`Settings > Core > Global Default`

![Current Fiscal Year Setting in Global Defaults](/docs/v13/assets/img/articles/current-fiscal-year-in-global-defaults.png)

Save Global Default, and Reload your ERPNext account. Then, default Fiscal Year will be auto-updated in your transactions.

Note: In transactions, you can manually select required Fiscal Year, from More Info section.

{next}
