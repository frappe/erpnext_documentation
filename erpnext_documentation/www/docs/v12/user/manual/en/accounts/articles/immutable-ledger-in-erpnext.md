<!-- add-breadcrumbs -->
# Immutable Ledger In ERPNext

> Introduced in Version 13

A major change has been introduced in ERPNext from version 13 onwards. This changes the way Accounting Ledger (General Ledger) and Stock Ledger works in ERPNext. There are multiple reasons why ledgers should be immutable. To list a few:

* Reposting future entries is computationally expensive. To post a backdated transaction, all future entries need to be reposted.
* In Stock Ledger, where the valuations are based on First-in-first-out (FIFO) method, the entire sequence may get regenerated which may upset valuations and profit for subsequent transactions.
* Taxes paid for a period may also get changed.

## Following are the impacts on day to day transactions

### 1. Reverse Entries on cancellation of transactions

<img alt="General Ledger" class="screenshot" src="{{docs_base_url}}/assets/img/articles/general-ledger.png">

On cancellation of any transaction instead of deleting the GL Entries for that transactions reverse entries will be passed to cancel the effect of that transaction on the date of cancellation.

<img alt="Document Delete" class="screenshot" src="{{docs_base_url}}/assets/img/articles/document-delete.png">

Since GL Entries linked to a transaction will never be deleted this also means that cancelled transactions and their linked documents can no longer be deleted.

### 2. Restriction on posting backdated stock entries

Since the ledgers are immutable now this means future transactions cannot be updated or reposted.
So users will no longer be able to post backdated stock transactions.

<img alt="Back Dated Entry" class="screenshot" src="{{docs_base_url}}/assets/img/articles/backdated-entry.png">

For Eg: Suppose a Stock Transaction has been made for **Item A** with posting time as `19-06-2020 23:00:10` then after this transaction you cannot post a transaction for **Item A** with posting time before this timestamp.
