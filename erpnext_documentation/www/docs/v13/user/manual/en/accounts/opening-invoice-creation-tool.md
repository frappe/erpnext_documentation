<!-- add-breadcrumbs -->
# Opening Invoice Creation Tool

The Opening Invoice Creation Tool allows importing data of outstanding Purchase or Sales Invoices into ERPNext. This specific tool is used in place of the Data Import Tool for cases where the Item data is irrelevant and outstanding balances against Customers/Suppliers are to be imported into ERPNext.

To access the Opening Invoice Creation Tool, go to:

> Home > Accounting > Opening and Closing > Opening Invoice Creation Tool

## 1: How to import Opening Invoices

1. Select the Company to which you want to import opening balances.

2. Select the Invoice Type. Selecting Sales or Purchase will generate Sales Invoices or Purchase Invoices respectively.

3. Checking the "Create Missing Party" checkbox will automatically create customers or suppliers if missing according to the name provided in the Party column.

    <img class="screenshot" alt="Opening Invoice Creation Tool" src="{{docs_base_url}}/assets/img/setup/opening-invoice-creation-tool.png">

4. Fill up the Invoices table. It consists of the following fields:
    - **Party**: You can select an existing Customer/Supplier or enter the name of a new one which will be automatically created.
    - **Posting Date**: The date at which the invoice will be posted.
    - **Due Date**: The date after which the invoice will be overdue.
    - **Item Name**: (Optional) The item name entered here will be shown in the invoice item table.
    - **Outstanding Amount**: The outstanding amount of the invoice.

> **Tip**: You can click the download button to download an excel sheet that you can fill up easily with appropriate data. If you have downloaded the excel sheet, then use the Upload button to upload it. Once you upload the sheet, the table will be filled with appropriate data rows.
