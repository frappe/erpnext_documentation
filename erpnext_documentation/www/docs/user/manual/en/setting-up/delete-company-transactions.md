<!-- add-breadcrumbs -->
# Delete Company Transactions

**You can delete all the transaction data like Sales Invoices, Sales Orders associated with a company and start afresh, while keeping the other master data like Customers, Items, BOMs intact.**

Often, users setup all the master data and then create a few dummy records. Then they want to delete the dummy records and the company and start over again. This can be done in two ways:

## 1. Transaction Deletion Tool

This feature allows you to delete all the records associated with the specified company, except for the ones belonging to the DocTypes listed in the **Excluded DocTypes** table. 

To access Transaction Deletion Tool, go to:
> Home > Setup > Transaction Deletion Tool

Tread with caution while using this- records once deleted using this can never be recovered. But if you're certain you want to start over, follow these steps:

1. Go to Transaction Deletion Tool.
1. Create a new doc by clicking on New.
1. Enter the name of the Company whose records you wish to delete.
1. Save and Submit.

And voila, your Company's as good as new.

![Transaction Deletion Tool](/docs/assets/img/setup/transaction-deletion-tool.png)

The **Summary** table displays the names of the DocTypes whose records were deleted as well as the number of records that were deleted.

## 2. Delete Transactions

1. Go to **Home > Accounting > Company** and find your company.
1. On the top right, you'll find the **Delete Transactions** button under **Manage**.
1. Enter your password.
1. Enter the company name to confirm. 

![Delete Transactions](/docs/assets/img/setup/delete-transactions-button.png)

This will submit a record in the [Transaction Deletion Tool](/docs/user/manual/en/setting-up/delete-company-transactions#1-transaction-deletion-tool) DocType.

![Successful Deletion Message](/docs/assets/img/setup/successful-deletion.png)

### Note: 

To perform this action, the user must at least be one of these:

* The creator of the company 
* The administrator