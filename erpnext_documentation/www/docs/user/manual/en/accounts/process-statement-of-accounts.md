<!-- add-breadcrumbs -->

# Process Statement Of Accounts

> Introduced in Version 13

**Process Statement Of Accounts is a tool which helps you send Statement Of Account (General Ledger Report) and Ageing (Accounts Receivable Summary) Report as a PDF to your customers in bulk via email either manually or automated periodically.**

<br>
To access *Process Statement Of Accounts* list you can either search in the navbar or go to:

> Home > Accounting > Tools > Process Statement Of Accounts

## 1. Prerequisites

1. The tool needs to use the email-ids of customers to send them the reports. On not finding the below email entries in the Customer contacts the tool won't allow you to select the respective customer, so please make sure the following details are filled in the customer documents.

    - Billing Email of Customer: This is mandatory and can be set within the [customer contact](/docs/user/manual/en/CRM/contact#1-how-to-create-a-contact) with "Is Billing Contact" option checked.
    - Primary Email of Customer: This is not mandatory, unless you select the "Send To Primary Contact" in the form.

2. Email Account setup with outgoing enabled. Learn more about this [here](/docs/user/manual/en/setting-up/email/email-account).


## 2. How to create a Process Statement Account entry

<img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/name_and_filters.png">


1. Go to the "Process Statement Of Account" list view by searching in the navbar and click on "New".

2. Enter a name for the entry, for future reference.

3. Set the General Ledger filters for the statements which will be sent to the customers.

    - "From Date" and "To Date" filters will be hidden and auto-filled dynamically when "Enable Auto Email" option is selected.
    - "Project" and "Cost Center" fields are multi-select.

4. In the "Customers" section you have an option to select customers in the child table and fetch their primary and billing emails. 

    - The "Select Customer By" select field lets you select customers in bulk, by grouping them based on "Customer Group", "Territory", "Sales Partner" and "Sales Person" by entering the selection and clicking on "Fetch Customers". 
    - In tree doctypes like "Territory", "Sales Person", and "Customer Group" on selecting group values, the customers having the child values of these fields will also be fetched. So when you select "India" as territory in the form, all customers with "Territory" values under India in the Territory tree will get selected.
    - The "Send To Primary Contact" option will send the Statement Of Account to the primary contact email-ids of the customers too apart from the billing email.

    <img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/customers.png"><br>

5. In "Print Preferences" section you can select 2 things:

    - Print orientation of the PDF file, either "Landscape" or "Portrait".
    - Whether you want to see the ageing report (Accounts Receivable Summary report), which shows the ageing amount for 30/60/90/120 days for vouchers (like Sales Invoice), based on either "Due Date" or "Posting Date".

    <img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/print.png">

6. The "Email Settings" section lets you configure how you want the emails to be sent. There are two subsections in this:

    <img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/auto-email.png">
    
    - On selecting "Enable Auto Email" you will see the options to send automated periodic reports to the customers in the entry.

        - You can select the "Frequency" at which the emails will be sent after the "Start Date" to the customers.
        - You can also select the "Filter Duration", which is the gap between the "From Date" and "To Date" values in the General Ledger report until the date of sending the report ("To Date").
        - These mails are not sent right away, but at midnight as a background process.
    
    - After this you can select the "Subject", "CC To" and "Body" fields of the email. If you don't set values to this field, default values will be used like shown in the help box below the body field.
    
    <img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/email-content.png">

7. Review your settings and click on "Save"

## 3. Features

<img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/buttons.png">

### 3.1 Option to download consolidated PDF of all customers

On creating an entry, there is a button seen at the top called "Download" which lets you see the consolidated report PDF of all customers for reviewing.

### 3.2 Option to send emails manually

On creating an entry, there is a button seen at the top called "Send Emails" which lets you trigger email sending manually to the customers. The emails are queued via a background job, which you can track in the "Email Queue" doctype with the DocType and Document references.

### 3.3 Using dynamic values in the Email Subject and Body

You can use Jinja tags to enter dynamic values from:

- the customer to which the email will be sent to under the "customer" object 
- any field in the selected Process Statement Of Account document under the "doc" object
- any method in [`frappe.utils`](https://github.com/frappe/frappe/blob/develop/frappe/utils/__init__.py) under the "frappe" object

They can be used as shown below:

<img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/template.png">

Resulting Email:

<img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/email.png">

Report PDF:

<img class="screenshot" src="{{docs_base_url}}/assets/img/accounts/process-statement-of-accounts/report.png">

## 4. Related Topics
1. [Setting up an Email Account](/docs/user/manual/en/setting-up/email/email-account.md)
1. [Creating Customer Contact](/docs/user/manual/en/CRM/contact#1-how-to-create-a-contact)
1. [Contact](/docs/user/manual/en/CRM/contact.md)