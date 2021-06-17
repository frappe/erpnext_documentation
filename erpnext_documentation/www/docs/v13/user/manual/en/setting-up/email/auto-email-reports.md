<!-- add-breadcrumbs -->
# Auto Email Reports

**Auto Email Reports automatically sends reports for the selected document.**

You can setup **Auto Email Report** to send reports at regular intervals. These must be saved reports of any type (Report Builder, Script or Query Report).

You can find Auto Email Report at:

> Home > Settings > Auto Email Report

## 1. How to create an Auto Email Report
1. Go to the Auto Email Report list, click on New.
1. Select the Report for which you want to generate emails.
1. Select the user for which you want to create this report (permissions will apply for this user).
1. Set the Email Addresses to which you want this report to be emailed and the frequency of the report. Emails will be sent at midnight. The date will be repeated in case of weekly/monthly/yearly frequency. For example, if the selected date is 7 and the frequency is monthly, the email will be sent on the 7th of each month.

 <img class="screenshot" alt="With Filters" src="{{docs_base_url}}/assets/img/setup/email/auto-email-2.png">
1. Save.

You can test the report by clicking on "Download" or "Send Now". Here is an example of the email you will receive for a general ledger report:

<img class="screenshot" alt="Report by Email" src="{{docs_base_url}}/assets/img/setup/email/auto-email-4.png">

## 2. Features

### 2.1 Filter Data

* **Send only if there is any data**: If enabled, emails will not be sent if there is no data in the report.
* **Only Send Records Updated in Last X Hours**: If set to 24, an email will contain only records updated in the last 24 hours. 
* **No of Rows**: The number of rows to be sent in the email. The maximum is 500.

### 2.2 Report Filters
If your report has filters, you will be able to see them. Click on the table to edit it:

<img class="screenshot" alt="Edit Filters" src="{{docs_base_url}}/assets/img/setup/email/auto-email-3.png">

For example, if the email is on the report 'Project Billing Summary' select the Project. The date range here is the date range of the 'Project Billing Summary'.

### 2.3 Message

A message can also be added to be sent with the email report. For example, 'This is your monthly Project Billing Summary Report:'

You can also change the file format in which the report is created. The available options are HTML, XLSX, and CSV.

### 2. Related Topics
1. [Email Digest](/docs/user/manual/en/setting-up/email/email-digest)
1. [Document Follow](/docs/user/manual/en/setting-up/email/document-follow)
