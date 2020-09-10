<!-- add-breadcrumbs -->
# Update Fixed Assets

To import all the existing fixed assets first create the asset record and then create a Journal Entry to update the General Ledger.

## 1. Create Asset Records

Create Asset record for each asset that your company owns which is not fully depreciated.

To create a new Asset:

1. Create an [Item](/docs/user/manual/en/stock/item) with 'Is fixed Asset' enabled.
1. Go to **Assets > Assets > New**.
1. Enter Asset Name.
1. Enter Item Code.
1. Enter Location.
1. Enter the Purchase Date.
1. Enter Gross Amount.
1. Tick **Is Existing Asset.**
1. Save.

    <img class="screenshot" alt="Stock Asset Ledger" src="{{docs_base_url}}/assets/img/accounts/asset_opening_balance.png">

> To know about Assets in detail, [visit this page](/docs/user/manual/en/asset/asset).

## 2. Create Journal Entry to Update the Ledgers

When you create an Asset with 'Is Existing Asset' checkbox ticked, the General Ledger is not updated. You will have to update the value via a Journal Entry.

To create a new Journal Entry:

1. Go to: **Accounting > Masters and Accounts > Journal Entry > New.**
1. Enter Posting Date.
1. Select the appropriate fixed asset ledgers in Account column and enter the value in Debit column.
1. Select 'Temporary Opening' ledger in Account column and enter the balancing amount in Credit column.
1. Set 'Is Opening' to Yes.

<img class="screenshot" alt="Stock Asset Ledger" src="{{docs_base_url}}/assets/img/accounts/journal_entry_for_fixed_asset_opening_balance.png">

{next}
