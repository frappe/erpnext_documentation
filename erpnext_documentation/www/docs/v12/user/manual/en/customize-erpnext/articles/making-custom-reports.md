<!-- add-breadcrumbs -->
# Making Custom Reports

There are three kind of reports in ERPNext.

### 1. Report Builder

Report Builder is an in-built report customization tool in ERPNext. This allows you to define specific fields of the form which shall be added in the report. Also you can set required filters, sorting and give preferred name to report. 

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/TxJGUNarcQs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 2. Query Report

Query Report is written in SQL which pulls values from account's database and displays the same in the report. Though SQL queries can be written from front end, like HTML, it has been restricted for ERPNext cloud users. This is because it allows users with no access to specific report to fetch data directly from the database.

Check Purchase Order Item to be Received report in Stock module for example of a Query report. [Click here](https://frappe.io/docs/user/en/guides/reports-and-printing/how-to-make-query-report.html) to learn how to create Query Report.

### 3. Script Report

Script Reports are written in Python and stored on server side. These are complex reports which involves logic and calculation. Since these reports are written on server side, customizing it from hosted account is not possible.

Check Financial Analytics report in Accounts module for an example of Script Report. [Click here](https://frappe.io/docs/user/en/guides/reports-and-printing/how-to-make-script-reports.html) to learn how to create Script Report.

> Note: **Dynamic Filter** is available in Script Reports and Query Reports; however, not in the Report Builder.

{next}

<!-- markdown -->
