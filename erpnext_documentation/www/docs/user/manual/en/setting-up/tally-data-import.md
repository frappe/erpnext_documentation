<!--add breadcrumbs-->

# Tally Migrator

> Introduced in Version 13

Tally Migrator in ERPNext helps migrating masters and transactions from Tally.

Any existing Chart Of Accounts against that company will be overwritten. Make sure the company you are selecting doesn't have any pre-existing transactions otherwise you'll receive a validation error.

To access the tool, go to:
> Home > Integrations > Tally Migration

## 1. Prerequisites
To migrate data to ERPNext you need to fetch following data from Tally:

1. Masters Data
1. Trial Balance Report before date of migration
1. Day Book Data from date of migration

## 2. Importing Master Data

1. Create a new Tally Migration document.

    <img class="screenshot" alt="New Tally Migration" src="{{docs_base_url}}/assets/img/setup/tally-migrator/new-tally-migration.png">

1. Select **ERPNext Company** to which you want to import masters and transactions. Selected company will have its Chart of Accounts **overwritten** with new one.
1. Now click on **Attach** and select Tally Masters file. Make sure the file is compressed with .zip extension
1. After attaching the file, document will be saved and **Process Master Data** button will be visible.

    <img class="screenshot" alt="Attached Master Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/masters-attached.png">

1. Click on **Process Master Data** button.

    <img class="screenshot" alt="Processing Master Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/processing-masters.png">

1. Any error occurred while processing master will be saved as **Error Log** document. This will be helpful for troubleshooting errors.
1. Once processing is done without any errors, **Import Master Data** button will be visible.
1. Clicking on **Import Master Data** will start importing following documents in order:
  - Chart of Accounts
  - UOMs
  - Item Groups
  - Items
  - Customers
  - Suppliers
  - Addresses

    <img class="screenshot" alt="Importing Master Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/importing-masters.png">

1. If there are errors while importing any of the document, it will be saved in the Tally Migration document itself. You will have to check errored documents and resolve / skip them manually one by one.

    <img class="screenshot" alt="Failed Master Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/failed-masters.png">

1. Master Data import will be completed once you have resolved all the errors by creating or skipping the document.

## 3. Importing Day Book Data

1. Select default warehouse, default cost center and round off account. These will be needed to set default values while importing transactions

1. Now **Attach** Tally Day Book Data file and Trial Balance Report file. Make sure both of these are compressed with .zip extension

    <img class="screenshot" alt="Attached Day Book Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/transactions-attached.png">

1. Click on **Process Day Book Data** button.

    <img class="screenshot" alt="Processing Day Book Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/processing-transactions.png">

1. Any error occurred while processing transactions will be saved as **Error Log** document. If you have such documents then you might have to manually import these transactions into ERPNext with Journal Entries.

    <img class="screenshot" alt="Errored Transactions" src="{{docs_base_url}}/assets/img/setup/tally-migrator/error_log.png">

1. Once processing is done, **Import Day Book Data** button will be visible.
1. Clicking on **Import Day Book Data** will start importing following documents in order:
  - Opening Entry - Imports opening balances of all ledgers from Tally
  - Journal Entry - Journals, Receipts, Payments, Contra will be imported as Journal Entry in ERPNext
  - Sales Invoice - Sales Transactions will be imported as Sales Invoice
  - Purchase Invoice - Purchase Transactions will be imported as Purchase Invoice

    <img class="screenshot" alt="Importing Day Book Data" src="{{docs_base_url}}/assets/img/setup/tally-migrator/importing-vouchers.png">

1. If there are errors while importing any of the document, it will be saved in the Tally Migration document itself. You will have to check errored documents and resolve / skip them manually one by one.

    <img class="screenshot" alt="Failed Vouchers" src="{{docs_base_url}}/assets/img/setup/tally-migrator/failed-transactions.png">

1. Day Book Data import will be completed once you have resolved all the errors by creating or skipping the document.
