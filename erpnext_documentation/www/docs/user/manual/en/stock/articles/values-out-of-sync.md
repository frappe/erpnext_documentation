<!-- add-breadcrumbs -->

# Values Out Of Sync - Validation Message

While creating a Stock Transaction, you can get this validation message: 
<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/value-out-of-sync.png">

Since [Perpetual inventory](https://erpnext.com/docs/user/manual/en/stock/perpetual-inventory) is enabled in your Company master, it requires the syncing of Stock Ledger and Stock Accounts (ledger) balance.

The message indicates that there is a mismatch in Stock and Accounts balance due to previous entries.

To proceed forward, sync the Stock Balance and Stock Accounts balance by creating a Journal Entry. Click on **“Make JV“** in the validation message, update relevant accounts, and submit the Journal Entry.

<img class="screenshot" alt="Unselectable Serial and Batch" src="{{docs_base_url}}/assets/img/articles/values-out-of-sync.gif">
Once done, you can proceed with the previous stock transaction.