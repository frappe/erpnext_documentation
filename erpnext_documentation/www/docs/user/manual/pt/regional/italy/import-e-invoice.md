<!-- add-breadcrumbs -->

# Importing e-Invoice from Supplier

> Introduced in Version 13

As of January 1, 2019, electronic Invoicing is mandatory for domestic businesses operating with domestic B2B and B2C transactions in Italy. ERPNext has a feature to import supplier invoices from XML files provided by suppliers to the government.

ERPNext has a feature to import supplier invoices from XML files provided by suppliers to the government. Using this you can import Supplier e-invoices into ERPNext. The supplier details like supplier names, addresses and purchase invoices will get created automatically in the system from the XML files.

## 1. Prerequisites
- Default Stock UOM should be specified in the Stock Settings Doctype.
- Enable Check Supplier Invoice Uniqueness in the Accounts Settings Doctype.
- Create a Zip file with all your supplier invoice XML files.

### 2. How to use Import Supplier Invoice

1. Navigate to Import Supplier Invoice doctype from the global search bar and enter the Invoice Series, Company, Supplier Group, Tax Account, Item Code and Default Buying Price List.
    <img class="screenshot" src="/docs/assets/img/regional/italy/import_einvoice.png">

   - Invoice Series - The series with which the new Purchase Invoices will be created.
   - Company - The company for which the new Purchase Invoices will be created.
   - Supplier Group - The supplier group under which the new suppliers will be created.
   - Tax Account - The account under which the taxes would be entered for the Purchase Invoices created.
   - Item Code - The item code which would be used for Purchase Invoice creation.
   - Default Buying Price list - The default buying price list to be used for the Purchase Invoice.

2. After entering the above details click on Save.

3. Attach the zip file with XML invoices.

4. Click on Import invoices and the Purchase Invoices will be created. Suppliers would be created if they do not exist in the system already.
    <img class="screenshot" src="/docs/assets/img/regional/italy/purchase_invoices_created.png">

5. If the file import completes successfully you would see a status of File Import Completed. If there are any errors you can view them from the Error Log.
    <img class="screenshot" src="/docs/assets/img/regional/italy/file_import_completed.png">
