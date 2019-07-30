<!-- add-breadcrumbs -->
# User Permissions

**User permissions is a way of restricting user access to particular documents.**

Role based permissions allow setting complete (by default) access to a document type (doctype) like Sales Invoice, Orders, Quotation, etc. This means that when you assign a Sales User role to a user, they can access all the Sales Orders and Quotations.

User Permissions can be used to restrict access to select documents based on the link fields in the document. For example, consider that you do business with multiple territories and you want to restrict access of certain Sales Users to Quotations/Sales Order belonging to a particular territory. This can be done via User Permissions. The restrictions can be set on Customer, Supplier, Customer Group, Supplier Group, etc.

Setting User Permissions are particularly useful when you want to restrict based on:

1. Allowing user to access data belonging to one Company
2. Allowing user to access data related to a specific Customer or Territory

To access User Permissions, go to:
> Home > User and Permissions > User Permissions


## 1. How to create User Permissions

1. Go to the User Permissions list, click on New.
1. Select the user for which the rule has to be applied.
2. Select the type of document to be allowed (for example "Company").
3. Under For Value, select the specific item that you want to allow (the name of the "Company).
4. If you check 'Is Default', the value selected in 'For Value' will be used as default for any future transactions by this user. That is, if company Unico Plastics Inc. is selected as 'For Value', this Company will be set as default for all future transactions by this user.

    <img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/new-user-permission.png" class="screenshot" alt="Creating a new user permission">

    > Note: Only a single user permission can be set as default for a particular document type for a specific user.

## 2. More User Permission actions
### 2.1 Advanced control

You can optionally apply user permissions only for specific document type by setting the Document Type after unticking the Apply To All Document Types checkbox.
Setting **Applicable For** option will make the current user permission applicable only under the selected Document Type master.

<img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/advanced-control.png" class="screenshot" alt="Advance control">

In the above User Permission, the user will be able to access only Sales Orders of the selected company.

**Note:** If **Applicable For** is not set, User Permission will apply across all related Document Types.

### 2.2 Ignoring User Permissions on Certain Fields

Another way of allowing documents to be seen by everyone that have been restricted by User Permissions is to tick "Ignore User Permissions" on a particular field by going to **Customize Form**.

For example, you don't want Assets to be restricted for any user, then select **Asset** in form type. Under the fields table, expand the Company field and tick on "Ignore User Permissions".

<img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/ignore-user-permissions.png" class="screenshot" alt="Ignore User Permissions on specific properties">


### 2.3 Strict Permissions

This restricts user access to documents in a stricter way.

To know more, go to the [System Settings page](/docs/user/manual/en/setting-up/settings/system-settings#14-permissions).

### 2.4 Checking How User Permissions are Applied

Finally, once you have created your air-tight permission model, and you want to check how it applies to various users. You can see it via the **Permitted Documents for User** report. Using this report, you can select the **User** and document type and view which documents a particular user can access.

Ticking on the Show Permissions checkbox will show the read/write/submit and other access levels.

<img src="{{docs_base_url}}/assets/img/users-and-permissions/user-perms/permitted-documents.png" class="screenshot" alt="Permitted Documents for User report">

Note: If you cannot access Sales Order or any other document type in this list, make sure you've set the [roles](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions) correctly.

For example, User Bruce is restricted to Company Unico Plastics Inc.
![User restricted to Company](/docs/assets/img/users-and-permissions/user-perms/user-restricted-to-company.png)

### 3. Related Topics
1. [Adding Users](/docs/user/manual/en/setting-up/users-and-permissions/adding-users)
1. [Role and Role Profile](/docs/user/manual/en/setting-up/users-and-permissions/role-and-role-profile)
1. [Role Based Permissions](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
1. [Role Permission For Page And Report](/docs/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report)
