<!-- add-breadcrumbs -->

All GL Entries can easily be exported in DATEV-Format for your tax advisor.

## Prerequisites

To use the DATEV Export, these need to be created first:

- [DATEV Settings](/docs/user/manual/en/regional/germany/datev-settings)

The export assumes that you have created a dedicated receivable **Account** for each **Customer** and a dedicated payable **Account** for each **Supplier**.

## Filters

In the filters section you can choose the company whose **GL Entries** you want to export. You can also set the timeframe for the export. Usually this will be the last month.

![DATEV Export Filters](/docs/assets/img/regional/germany/datev-export-filters.png)

## Menu

From the menu you can open the [DATEV Settings](/docs/user/manual/en/regional/germany/datev-settings) or download the export file. The export file is a ZIP archive that contains the transaction data from the preview as well as master data (**Customers**, **Suppliers**, **Accounts**).

![DATEV Export Menu](/docs/assets/img/regional/germany/datev-export-menu.png)

## Exported Data

Currently, you can export **GL Entries** in the way ERPNext creates them. For example, booking a **Sales Invoice** will result in three **GL Entries** and three rows in the DATEV Export:

1. Debtors against Sales (gross amount),
2. Tax against Customer (tax amount) and
3. Sales against Customer (net amount).

Please consult your tax advisor about if and how you can use this data.
