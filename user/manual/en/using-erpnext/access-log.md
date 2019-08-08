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

It is a tool for [System Managers](/docs/user/manual/en/setting-up/users-and-permissions/role-and-role-profile) to track which files were accesed or exported by users on the system. This is useful for tracking company sensitive information like transactions or financials.

Access logs are created in the following events:

 - Printing of all Forms and Reports
 - Private file downloading
 - Exporting via XLSX/CSV formats

In ERPNext, Access Log is available to [System Managers](/docs/user/manual/en/setting-up/users-and-permissions/role-and-role-profile), it can be accessed using our favourite [Awesome Bar](https://frappe.io/blog/erpnext-features/erpnext-awesome-bar) or through:
> Home > Users and Permissions > Logs > Access Log

The general List view provided out of the box by [Frappe](https://frappe.io/frappe).

<img class="screenshot" alt="Acess Log: ERPNext List View" src="{{docs_base_url}}/assets/img/collaboration-tools/access-log-002.png">

In case an access log is created on event of exporting a Report, a **Show Report** button will be generated in the respective log. On clicking this button, the exported report can be viewed along with the set filters.

<img class="screenshot" alt="Acess Log: General Ledger Report ERPNext" src="{{docs_base_url}}/assets/img/collaboration-tools/access-log-003.png">

Similarly, a **Show Document** button is generated in case of events related to documents directly such as document Printing and Private File download.

<img class="screenshot" alt="Acess Log: Sales Invoice Frappe Custom Application" src="{{docs_base_url}}/assets/img/collaboration-tools/access-log-001.png">

Events such as [Raw Printing](/docs/user/manual/en/setting-up/print/raw-printing) save information along with the chosen template for the document.

<img class="screenshot" alt="Acess Log: HTML to PDF Printing" src="{{docs_base_url}}/assets/img/collaboration-tools/access-log-004.png">