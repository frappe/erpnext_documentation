<!-- add-breadcrumbs -->
# Role Permission for Page and Report

**Access to different pages and reports can be controlled in Role Permission for Page and Report.**

Document types are Sales Order, Customer, Supplier, etc. They are a **document type** meaning they can contain multiple documents of that type. A Page is a single page like [Selling Settings](/docs/user/manual/en/selling/selling-settings). You cannot create multiple Selling Settings, but you can create multiple Sales Orders.

In ERPNext, user can make a custom user interface using Page and a custom report using [Report Builder](/docs/user/videos/learn/report-builder.html) or [Query Report](https://frappe.io/docs/user/en/guides/reports-and-printing/how-to-make-query-report). ERPNext has a [role-based permission system](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions) where you can assign roles to the user. The same role can be assigned to the page and report to access them.

If the user has enabled developer mode, then they can add the roles directly in the page and report record. In that case, the permissions will also be reflected in the JSON file for the page/report. Consider you want to restrict the roles that can access certain pages and reports in ERPNext, this can be done via the Role Permission for Page and Report.

To access Role Permission for Page and Report, go to:
> Home > Users and Permissions > Role Permission for Page and Report


## 1. How to use Role Permission for Page and Report Tool

If developer mode is disabled, the user can assign the roles to the page and report, using "Role Permission for Page and Report" page.

<img alt="Tools to assign custom roles to the page" class="screenshot" src="{{docs_base_url}}/assets/img/users-and-permissions/role-permission-for-page-and-report.png">

### 1.1 Reset to defaults

Using the "Reset to Defaults" button, the user can remove the custom permissions applied on a page or report. Then default permissions will be applicable on that page or report.

<img alt="Reset the default roles" class="screenshot" src="{{docs_base_url}}/assets/img/users-and-permissions/reset-roles-permission-for-page-report.png">

## Setting Role Permissions from the Page/Report as a Developer
### Role Permissions For Page
1. Go to: Home > Developer > Page.
1. Add a row and select which other roles can access the Page.

    <img alt="Assign roles to the page" class="screenshot" src="{{docs_base_url}}/assets/img/users-and-permissions/roles-for-page.png">

### Role Permissions For Report
1. Go to: Home > Developer > Report.
1. Add rows with roles who can access the Report.

    <img alt="Assign roles to the report" class="screenshot" src="{{docs_base_url}}/assets/img/users-and-permissions/roles-for-report.png">

### 3. Related Topics
1. [Role and Role Profile](/docs/user/manual/en/setting-up/users-and-permissions/role-and-role-profile)
1. [Role Based Permissions](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
1. [User Permissions](/docs/user/manual/en/setting-up/users-and-permissions/user-permissions)
