<!-- add-breadcrumbs -->
# Limited User

**The user will get limited access to the system.**

Limited users can access only specific documents of the specific modules. Certain users don't use all the modules and need only specific modules. For example, in the company, to record the daily attendance or leave application every employee was given required system access. But assume 500 people are working in the company out of which only 100 use all documents and the remaining 400 need only documents for daily attendance or leave applications. Such users are limited users.

The User Type document plays an important role to handle this use case. There are default User Types, "System User" and "Website User",  the System User can access the desk and website portal whereas the Website User can only access the website portal. To handle the case of limited access of documents for the employees by default ERPNext has added a new user type 'Employee Self Service'.

## User Type

To access the User Type document, go to:

> Users > User Type

<img class="screenshot" alt="User Type" src="{{docs_base_url}}/v12/assets/img/users-and-permissions/user-type.png">

Website User and System User will be standard user types and these cannot be deleted or edited. However, non-standard (Custom) user types can be deleted, created, edited. By default, delete rights are not given to any user.

## Non-Standard User Type

1) For the non standard user type, user has to select the Custom Role, document on which they want to apply the user permission, and the fieldname of the user.

<img class="screenshot" alt="User Type" src="{{docs_base_url}}/v12/assets/img/users-and-permissions/user-type-role.png">

In the above image, Employee has the link field User ID which is linked to the User document. As the "Apply User Permission on" has been set as "Employee", then the respective employee's user can only view the documents in which the respective employee field is linked. For example, the employee can only able to view the salary slip which has been created against their employee id.

2) Document Types:

The non-standard user type users can only access the documents which have been mentioned in the user type.

<img class="screenshot" alt="User Type" src="{{docs_base_url}}/v12/assets/img/users-and-permissions/user-type-document-type.png">

The above table also acts as the Role Permission Manager for this particular User Type (Employee Self Service in our case). Employee Self Service as a role won't be accessible in the general Role Permission Manager.

3) Document Types (Select Permissions Only):

In this table, you need to list down all the doctypes that you want the Employee Self Service User to have SELECT access to. There is no limit to the number of doctypes you can add here. Users will not be able to create the records for the documents to which they have Select perm access.

<img class="screenshot" alt="User Type" src="{{docs_base_url}}/v12/assets/img/users-and-permissions/user-type-select-perm.png">

## Adding non-standard User

While adding the new user, the user needs to select the user type. In case of a non-standard user type, the respective user should be linked to the document which has been set in the field "Apply User Permission On".


<img class="screenshot" alt="User Type" src="{{docs_base_url}}/v12/assets/img/users-and-permissions/limited-access-user.png">
