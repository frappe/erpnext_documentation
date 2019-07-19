<!-- add-breadcrumbs -->
# Auto Repeat

Auto Repeat feature helps you create certain documents automatically in a given time period.

From version 12, you can Customize any Form to make the documents **repeatable**.

For Example: Assuming that you follow deferred expense system for some items. It requires you to create same Journal Entry every month to credit Deferred Expense account and debit Expense Account. You can create first Journal Entry manually for it, and then create auto-repeat transaction for it.

To access Auto Repeat, go to:
> Home > Settings > Automation > Auto Repeat

## 1. How to set up Auto Repeat

### 1.1 Customize the Form
1. Go to: **Home > Customization > Form Customization > Customize Form**.
2. Select the form in which you want to allow creation of repeatable documents.
3. Check 'Allow Auto Repeat' to allow the creation of repeatable documents for that Form. This is necessary for the document type to show up in the Reference Document field under the Auto Repeat doctype.

  <img class="screenshot" alt="Allow Auto Repeat" src="/docs/assets/img/setup/automation/allow-auto-repeat.png">

### 1.2 Set up Auto Repeat
1. Go to **Home > Settings > Automation > Auto Repeat > New**.
2. Select the Reference Document Type, like Journal Entry or Sales Invoice, etc.
3. Select the Reference Document. This is the individual document that you want to repeat.
4. Set the Start Date and End Date (optional).
   If End Date is not specified, recurring documents will be created, unless the Auto Repeat is disabled.
5. Set the Frequency for creating repeatable documents
   (Daily, Weekly, Monthly, Quarterly, Half-yearly, Yearly).
6. Save.

### 1.3 Set up Auto Repeat directly from the document
You can also set a document on Auto Repeat by clicking the **Repeat** option from the **Menu** in the Toolbar.

**Note**: If a document is already on Auto Repeat, the Repeat option is not available.

<img class="screenshot" alt="Allow Auto Repeat" src="/docs/assets/img/setup/automation/repeat-option.png">

Once you click on Repeat, a prompt for Auto Repeat will show up. Fill in the details and click on Save.

<img class="screenshot" alt="Auto Repeat Prompt" src="/docs/assets/img/setup/automation/auto-repeat-prompt.png">

## 2. Features

### 2.1 Notify by Email
If you want to notify certain contacts whenever the recurring documents are created, you can check 'Notify by Email' in the Notification section of Auto Repeat. This will send the auto-generated recurring documents to the specified Email Addresses. Fields for the same are explained below:

- **Recipients**: Defines the Email IDs of the recipients for recurring document creation emails.
- **Get Contacts**: This button will fetch the contacts linked to the document that is set on Auto Repeat and fill up the Recipients field with the same.
- **Template**: You can choose an Email Template for the email. This will fill up the Subject and Message fields as well.
- **Subject**: Subject for your Email (example: Recurring ToDo created successfully).
- **Message**: Message to be sent in the Email.
- **Preview Message**: This button will show a preview of the message.
- **Print Format**: Select a print format to define document view which should be emailed to customer.

### 2.2 Repeat on a particular day
If the frequency is set as Monthly, Quarterly, Half-yearly or Yearly, then it will create recurring documents in the respective months on the same day as the 'Start Date' of Auto Repeat. If you want to create recurring documents on some other day then you can set one of the following:

- **Repeat on Day**: Day of the month on which recurring document will be created. For example, if frequency is Monthly and you enter 7 then it will generate recurring document on 7th of the respective month.
- **Repeat on Last Day of the Month**: This option is available as the last day of every month is different. For example, in a leap year last day of Feb is 29th, and it is 28th otherwise. If you check this option, it will create recurring documents on the last day of the respective months.

### 2.3 Dashboard
You can see the Auto Repeat schedule in the Dashboard of Auto Repeat document. If you don't specify the End Date then the schedule will show only the Next Schedule Date.

<img class="screenshot" alt="Allow Auto Dashboard" src="/docs/assets/img/setup/automation/auto-repeat-dashboard.png">

### 2.4 Auto Repeat Frequency on the sidebar
When a document is set on Auto Repeat you can see the Auto Repeat frequency on the sidebar.
You can click on the status to see the linked Auto Repeat document.

<img class="screenshot" alt="Auto Repeat Frequency" src="/docs/assets/img/setup/automation/auto-repeat-frequency.png">

### 2.5 Disable Auto Repeat
If you check this field it will stop creating recurring documents and unlink the Auto Repeat document from the Reference Document.
