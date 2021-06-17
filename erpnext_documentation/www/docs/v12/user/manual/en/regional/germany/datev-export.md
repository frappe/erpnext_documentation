<!-- add-breadcrumbs -->

All **GL Entries** can be exported in DATEV-Format for your tax advisor.

## DATEV-Format

The german DATEV eG is a registered cooperative of the tax, accountancy and legal professions. The DATEV format is a CSV-based file interface for importing data into DATEV Accounting.

## Prerequisites

To use the DATEV Export, these need to be created first:

- [DATEV Settings](/docs/user/manual/en/regional/germany/datev-settings)
- In **Customer** and **Supplier**, in the "Accounting" section, you can set the "Debtor/Creditor Number" of this party (optional).

    1. Add a new row to the table,
    2. Open the row's detail view,
    3. Select your **Company**, and
    4. Set the "Debtor/Creditor Number" of this party.

    The "Debtor/Creditor Number" will be used as the account number of this party in the exported master data. It will also be available as additional information in exported transactions.
- **Customer** and **Supplier** should have zero or one **Address** marked as "Primary Billing Address". You can also specify a billing email and phone number in this address. If available, this will be exported with the master data. 

## Filters

In the filters section you can choose the company whose **GL Entries** you want to export. You can also set the timeframe for the export. Usually this will be the last month.

![DATEV Export Filters](/docs/assets/img/regional/germany/datev-export-filters.png)

## Menu

From the menu you can open the [DATEV Settings](/docs/user/manual/en/regional/germany/datev-settings) or download the export file. The export file is a ZIP archive that contains the transaction data from the preview as well as master data (**Customers**, **Suppliers**, **Accounts**).

![DATEV Export Menu](/docs/assets/img/regional/germany/datev-export-menu.png)

## Exported Data

Currently, you can export **GL Entries** in the way ERPNext creates them. For example, booking a **Sales Invoice** will result in three **GL Entries**:

| Debit amount | Credit amount | Account | Against         |
|--------------|---------------|---------|-----------------|
| Gross amount |               | Debtors | Revenue Account |
|              | Tax amount    | Tax     | Customer        |
|              | Net amount    | Sales   | Customer        |

However, in ERPNext the right side is not necessarily an **Account**. It could also be multiple accounts, a **Customer** or a **Supplier**. Therefore, we use a temporary against account that can be specified in [DATEV Settings](/docs/user/manual/en/regional/germany/datev-settings). All GL Entries are made against this account. The rows in the DATEV Export will look something like this:

| Amount       | Debit or Credit | Account | Against Account |
|--------------|-----------------|---------|-----------------|
| Gross amount | Debit           | Debtors | Temporary       |
| Tax amount   | Credit          | Tax     | Temporary       |
| Net amount   | Credit          | Sales   | Temporary       |

> Please consult your tax advisor about if and how you can use this data.

## Technical Notes

The interface documentation is available in the DATEV developer portal:

- [DATEV format v7.0](https://developer.datev.de/portal/system/files/files/book/datev_format_v7.0.zip).
