---
title: Access log
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Access Log is a security feature that logs all data exports in the form of printing of Forms and reports, private file downloading and exporting reports in excel/csv formats.
 keywords: frappe, access log, erpnext v12, erpnext release notes, erpnext new features, erp, open source erp, free erp, security
---

# Access Log

> Introduced in Version 13

**Access Log is a security feature that logs all data exports by all users in the system.**

It is a tool for System Managers to track which files were accessed or exported by users on the system. This is useful for tracking your company's sensitive information like transactions or financials.

Access logs are created in the following events:

 - Printing of all Forms and Reports
 - Private file downloading
 - Exporting via XLSX/CSV formats

In ERPNext, Access Log is available to System Managers, it can be accessed using the Global Search or through:

> Home > Users and Permissions > Logs > Access Log

![Access Log](/docs/assets/img/using-erpnext/using-access-log-3.png)

In case an access log is created on event of exporting a Report, a **Show Report** button will be generated in the respective log. On clicking this button, the exported report can be viewed along with the set filters.

![Access Log](/docs/assets/img/using-erpnext/using-access-log-1.png)

Similarly, a **Show Document** button is generated in case of events related to documents directly such as document Printing and Private File download.

![Access Log](/docs/assets/img/using-erpnext/using-access-log-2.png)

Events such as [Raw Printing](/docs/user/manual/en/setting-up/print/raw-printing) save information along with the chosen template for the document.

![Access Log](/docs/assets/img/using-erpnext/using-acces-log-4.png)