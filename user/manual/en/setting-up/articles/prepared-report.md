---
title: Using Prepared Reports in ERPNext
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: ERPNext allows report generation in background so users can continue with their usual tasks while the report is being generated for them.
 keywords: frappe, erpnext, erpnext reports, mis, prepared report, background reports
---

<!-- add-breadcrumbs -->
# Using Prepared Report

Many times when generating a report that deals with large volume of data, say, a GL report for the entire year, you may end up getting the following error message: **Request Timed Out**. This occurs as there is a lot of data to be processed and presented on the report page, but not enough server resource hence resulting in a time out.

For better processing of such reports, ERPNext offers Prepared Reports (since v11). When a report is set as a Prepared Report, it is generated through a [background job](https://frappe.io/docs/user/en/guides/app-development/running-background-jobs), and once ready, is available for users to view.

## Steps to Enable Background Reports

1. Go to [Role Permission for Page and Report](/docs/user/en/setting-up/role-permission-for-page-and-report)
