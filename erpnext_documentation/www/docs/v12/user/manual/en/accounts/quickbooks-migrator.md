# ERPNext QuickBooks Migrator

##  How to Setup QuickBooks Migrator?

### Create a QuickBooks Online App

1. From Awesome-bar, Go to "QuickBooks Migrator" DocType.
1. Go to [Inuit Developer Portal](https://developer.intuit.com)
1. Sign In with your existing account or Sign Up.
1. Go to "My Apps" page.
1. Click on "Select APIs".
1. Under "QuickBooks API" Check "Accounting".
1. Click on "Create App".
    - You'll be taken to the Dashboard of your App.

1. Go to "Keys" tab.
1. Go to "Production Keys" Section.
    - Complete requirements.

1. In "QuickBooks Migrator" DocType a "Redirect URL" will be generated for you and add it in the list of "Redirect URIs" of your Inuit App  (under "Production Keys" section). Click Save.

    - Make sure that the Redirect URL starts with `https`.

1. From "Production Keys" section copy "Client ID" and "Client Secret" to "QuickBooks Migrator" DocType.
1. Save "QuickBooks Migrator".


### Connect to QuickBooks Online API

1. Click "Connect to QuickBooks".
1. A new tab will open in your browser and You'll be asked to Log In.
1. If you have more than one companies then Select the company you want to migrate.
1. Click "Connect".
1. Upon successful authorization, the tab will close.
1. The indicator will be set to "Connected to QuickBooks".
1. In "QuickBooks Migrator" select "Company" where you want to migrate your data.
1. Save "QuickBooks Migrator".


### Migrate Data

1. Click the "Fetch Data" button.
1. The indicator will change from "Connected to QuickBooks" to "In Progress".
1. Progress bars will show the status of migration.
1. This will take a few minutes depending on the size of data.
1. After migration is complete, the indicator will change to "Complete" or "Failed".


## What Will Happen when I Click Fetch Data?


## Account

### Existing Chart of Accounts
    Upon creation of a Company ERPNext creates a chart of accounts for that company, these accounts will be kept.

### Account Naming
    To avoid name collision with existing accounts, all accounts from QuickBooks will be assigned "- QB" suffix.

    e.g. `Job Expense` will become  `Job Expense - QB`.

    **Note**: ERPNext also encodes account names with Company abbreviation. Taking this into account `Job Expense` will become  `Job Expense - QB - AZ` (assuming `AZ` is the company abbreviation).

### Root Accounts
    Five root accounts, namely `Asset`, `Equity`, `Expense`, `Liability`, `Income` will be created and all accounts (depending on the account type) will become children of these accounts.

### Group Accounts
    QuickBooks allows transactions on group accounts, which is not allowed in ERPNext, to handle this, every group account will have a child with a hyphenated name.

    e.g.

    ```
        Job Expenses
            Job Materials
    ```
    will become
    ```
        Job Expenses
            Job Expenses - 1
            Job Materials
    ```

### Name Collisions
    QuickBooks allows multiple accounts to have the same name, which is not allowed in ERPNext, to handle this, every duplicate account will have a hyphenated name.

    e.g.
    ```
        Insurance
            Job Materials
        Job Expenses
            Job Materials
    ```
    will become
    ```
        Insurance
            Job Materials
        Job Expenses
            Job Materials - 1
    ```



## Item

### Naming
    All Items will have company encoded names.

    e.g. `Pen` will become  `Pen - AZ` (assuming `AZ` is the company abbreviation).

### UOM
    All Items will be assigned `Unit` as the default UOM.

### Fractional UOM
    `Unit` will be allowed to have fractional value.

### Inventory
    Irrespective of whether Item is an Inventory or Non-Inventory Item in QuickBooks, No Inventory related information will be kept.

## Customer and Supplier
### Naming
    All Customer and Suppliers will have company encoded names.

    e.g. `Pen` will become  `Pen - AZ` (assuming `AZ` is the company abbreviation).



## Invoice

### Variants
    QuickBooks has four transactional variants of Invoice, all of these will be saved as Sales Invoice.

    - **Invoice** is equivalent to a Sales Invoice.
    - **Sales Receipt** is equivalent to a POS Sales Invoice.
    - **Credit Memo** is equivalent to a return Sales Invoice (Credit Note).
    - **Refund Receipt** is equivalent to a return POS Sales Invoice.

### Discount and Markup
    QuickBooks uses special accounts for both Markup and Discount, ERPNext doesn't handle the discount expense and markup this way, instead, all Item's will see the change in their Income accounts.

### Shipping
    For Invoices with Shipping, an Item with name Shipping will be added in the Item table.

### Round off
    ERPNext uses different rounding method than QuickBooks, because of this, in Invoices with Tax and with a currency different than company currency, Sales Invoice will have different grand total than that of the QuickBooks Invoice.

### Special Case
    If a QuickBooks Invoice is linked to a `Delayed Charge` or `Statement Charge` then an equivalent `Journal Entry` is created for this Invoice.



## Bill

### Variants
    QuickBooks has two transactional variants of Bill, all of these will be saved as Purchase Invoice.

    - **Bill** is equivalent to a Purchase Invoice.
    - **Supplier Credit** is equivalent to a return Purchase Invoice.



## Other

Following transactions will be saved as Journal Entry

- Advance Payment
- Bill Payment
- Cheque
- Credit Card Credit
- Expense
- Inventory Qty Adjustment
- Journal Entry
- Payment
- Tax Payment



## Tax

For every QuickBooks Tax Rate an ERPNext account will be created.

## Custom Fields

QuickBooks Migrator will add following Custom Fields

- Company field
    - Customer
    - Item
    - Supplier

- QuickBooks ID field
    - Customer
    - Item
    - Journal Entry
    - Purchase Invoice
    - Sales Invoice
    - Supplier