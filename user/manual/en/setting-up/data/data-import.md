<!--add breadcrumbs-->

# Data Import

**Data Import lets you import records from a CSV/Excel file.**

Data Import (formerly known as the Data Import Tool) is a great way to upload (or edit) bulk data (especially master data) into the system.

To begin importing data, go to:

> Home > Settings > Import Data

Or go to the Transaction you want to import and click on Menu > Import:

<img alt="Start Import" class="screenshot" src="{{docs_base_url}}/assets/img/setup/data-import/data-import-1-new.png">

Before using Data Import **ensure** that you have all of your data ready.

## 1. Using Data Import

Data in ERPNext is stored in tables like a spreadsheet with columns and rows of data. Each form likes Sales Order has multiple fields like Customer, Company, etc. It also has tables like the item table, tax table, etc. In Data Import, the set of fields in the Sales Order are treated as the main table and the rows inside the child table (item table) are treated as the child table for data import.

Each form in ERPNext can have multiple child tables associated with it.

The child tables are linked to the parent tables and are implemented where there are multiple values for any property. For example, an Item can have multiple prices, a Sales Invoice has multiple Items, Taxes and so on.

### 1.1 Downloading the Template
Considering the Supplier document type as an example, after clicking on Import:

> A document type (DocType) is a form (master or transaction) in ERPNext. Eg: Item, Sales Order.

1. Select document type for which template should be downloaded (if navigating from Settings).
1. Select action as Insert new records.
1. Click on Download template.
1. Select whether to create a template for all or just the mandatory columns for a supplier.
1. Check fields to be included in the template.
1. Select the file format of the template file.
1. Click on Download.

  For bulk editing, you can check "Download With Data", this will add the existing system data to the template you'll download.
  
  <img alt="Download Template" class="screenshot" src="{{docs_base_url}}/assets/img/setup/data-import/data-import-steps.gif">

### 1.2 Filling the Template

A separate document will be created for each row in the spreadsheet. It is suggested that you create a few document types first to understand the meaning of fields and the values entered.

After downloading the template, open it in a spreadsheet application (like Excel, Numbers, or Libre Office) and fill in the data below the column headings shown as follows:

<img alt="Download Template" class="screenshot" src="{{docs_base_url}}/assets/img/setup/data-import/import-file.png">

Then save your template as an Excel or Comma Separated Values (CSV) file.

### 1.3 Uploading back the Template

1. After making the necessary changes, go back to the data import form and attach the file by clicking on the Attach button.
1. Click on the Upload.
1. Once the upload is successful click on Import.

  <img alt="Upload" class="screenshot" src="{{docs_base_url}}/assets/img/setup/data-import/data-import-4-new.png">

### 1.4 Uploading All Tables (Main + Child)

If you select all tables when downloading the template, you will get columns belonging to all the tables in
one row. The main table and child table will be separated by `~` between the columns.

If you have multiple child rows then you must start a new main item on a new
row. See the example:


    Main Table                          ~   Child Table
    Column 1    Column 2    Column 3    ~   Column 1    Column 2    Column 3
    v11         v12         v13             c11         c12         c13
                                            c14         c15         c17
    v21         v22         v23             c21         c22         c23

> To see how it appears, enter a few records manually using regular forms (like a Sales Order). Then export the data with "All Tables" and "Download with Data" ticked.

### 1.5 Overwriting

ERPNext also allows you to overwrite all/certain fields of a document type. If you want to
update certain fields (columns in the spreadsheet), you can download the template with data. Remember to
select the option as “Update Records” before uploading.

When you create new records in the system, ERPNext assigns an ID to them. This is a unique value for the record as in used to identify it in the system. When you're updating an existing record, the ID field is a must. If not present, the system will create a new record for it.

> Note: For child records, if you select overwrite, it will delete all the
child records of that parent.

### 1.6 Upload Limitations

You can only upload up to 5,000 records in one go. (maybe less in some cases).

Uploading a lot of data can cause a system crash, especially
if other users are using the system in parallel. Hence ERPNext restricts the
number of “writes” you can process in one request.

When uploading a large number of records, it is recommended to do it in batches. That is, select a few thousand records at a time, upload then repeat.

## 2. Import Options

### 2.1 Skip rows with errors
If this is checked, rows with valid data will be imported and rows which encountered errors will be dumped into a new file for you to import later.

### 2.2 Submit after importing
In ERPNext document types are mainly of two types - masters and transactions. The masters are records like Customer, Supplier, etc., they can only be saved not submitted. The transactions like Sales Orders, Purchase Invoices are submittable documents and can be submitted to the system to alter the general ledger. Tick this in case there are submittable transactions which are imported and need to be submitted after importing.

### 2.3 Ignore encoding errors
In case there are any Unicode errors, a new file with the invalid rows will be created to be imported later.

### 2.4 Don't create new records
For 'Update records', ticking this will prevent the creation of new records even if they exist in the template. In other words, new records in the template will not be imported and created in the system, only existing records will be updated. 

### 3. Additional Notes
A CSV (Comma Separated Value) file is a data file that you can upload into
ERPNext to update various data. Any spreadsheet file from popular spreadsheet
applications like MS Excel or Open Office Spreadsheet can be saved as a CSV
file.

If you are using Microsoft Excel and using non-English characters, make sure
to save your file encoded as UTF-8.

For older versions of Excel, there is no
clear way of saving as UTF-8. So save your file as CSV, then open it in
Notepad, then save as “UTF-8”. (Or upgrade your Excel!)

## 4. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Ta2Xx3QoK3E" frameborder="0" allowfullscreen></iframe>
</div>

### 5. Related Topics
1. [Charts Of Accounts Importer](/docs/user/manual/en/setting-up/chart-of-accounts-importer)
1. [Data Export](/docs/user/manual/en/setting-up/data/data-export)

