<!-- add-breadcrumbs -->
# Role Based Permissions

**Permission to different documents can be controlled using Role Based Permissions.**

ERPNext has a role-based permission system. It means that you can assign Roles to Users, and Permissions can be set on Roles. The Role Permissions Manager allows you to set which roles can access which documents and with what permissions (read, write, submit, etc.).

Once roles are assigned to a user, their access can be limited to specific documents. The permission structure allows you to define different permission rules for different fields using a concept called **Permission Level** of a field. 

To start using the Role Permission Manager, go to:
> Home > Users and Permissions > Role Permissions Manager

<img alt="Manage Read, Write, Create, Submit, Amend access using the Role Permissions Manager" class="screenshot" src="{{docs_base_url}}/assets/img/users-and-permissions/setting-up-permissions-leave-application.png">

Permissions are applied on a combination of:

  * **Roles:** As we saw earlier, Users are assigned Roles and it is on these Roles that permission rules are applied. For example, a sales user may be given the roles of an Employee and a Sales User.

  Examples of Roles include Accounts Manager, Employee, HR User, etc.

  * **Document Types:** Each type of document, master or transaction, has a separate list of role-based permissions as seen in the preceding screenshot.

  Examples of Document Types are Sales Invoice, Leave Application, Stock Entry, etc.

  * **Permission Levels:** In each document, you can group fields by "levels". Each group of fields is denoted by a unique number (0 to 9). A separate set of permission rules can be applied to each field group. By default, all fields are of level 0.

    Permission "Level" connects fields with level X to a permission rule with level X. To know more click [here](/docs/user/manual/en/setting-up/articles/managing-perm-level).

  * **Document Stages:** Permissions are applied on each stage of the document like Creation, Saving, Submission, Cancellation, and Amendment. A role can be permitted to Print, Email, Import or Export data, access Reports, or define User Permissions.

  * **User Permissions:** Using User Permissions in ERPNext a user can be restricted to access only specific Documents for that Document Type. Eg: Only one Territory from all Territories. User Permissions defined for other Document Types also get applied if they are related to the current Document Type through Link Fields.
  
    For example, a Customer is a link field in a Sales Order or Quotation. In the Role Permissions Manager, User Permissions can be set using the 'Set User Permissions' button.

    To set User Permissions based on documents/fields go to:
    > Home > Users and Permissions > Permissions > [User Permissions](/docs/user/manual/en/setting-up/users-and-permissions/user-permissions)

  * **Add a New Rule**: In the Role Permissions Manager, to add a new rule, click on the **Add a New Rule** button and a pop-up box will ask you to select a Role and a Permission Level. Once you select this and click on 'Add', this will add a new row to your rules table.

##2. How Role Based Permissions Work

Leave Application is a good example that encompasses all areas of a Permission System.

* It should be created by an Employee.
  For this, Employee Role should be given Read, Write, Create permissions.

  <img class="screenshot" alt="Giving Read, Write and Create Permissions to Employee for Leave Application"  src="{{docs_base_url}}/assets/img/users-and-permissions/setting-up-permissions-employee-role.png">

* An **Employee** should only be able to access his/her Leave Application.
  Hence, User Permissions record should be created for each User-Employee combination.

  <img class="screenshot" alt="Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager" src="/docs/assets/img/users-and-permissions/setting-up-permissions-employee-user-permissions.png">
  
* **HR Manager** should be able to see all Leave Applications.
  Create a Permission Rule for HR Manager at Level 0, with Read permissions. Apply User Permissions should be disabled.

  <img class="screenshot" alt="Giving Submit and Cancel permissions to HR Manager for Leave Applications. 'Apply User Permissions' is unchecked to give full access." src="{{docs_base_url}}/assets/img/users-and-permissions/setting-up-permissions-hr-manager-role.png">

* **Leave Approver** should be able to see and update Leave Applications of employees under him/her.
  Leave Approver is given Read and Write access at Level 0. Relevant Employee Documents should be enlisted in the User Permissions of Leave Approvers. (This effort is reduced for Leave Approvers mentioned in Employee Documents, by programmatically creating User Permission records).

  <img class="screenshot" alt="Giving Read, Write and Submit permissions to Leave Approver for Leave Applications.'Apply User Permissions' is checked to limit access based on Employee." src="{{docs_base_url}}/assets/img/users-and-permissions/setting-up-permissions-leave-approver-role.png">

* It should be Approved/Rejected only by HR User or Leave Approver.
  The Status field of a Leave Application is set at Level 1. HR User and Leave Approver are given Read and Write permissions for Level 0, while everyone else (All) are given Read permission for Level 1.

  <img class="screenshot" alt="Limiting read access for a set of fields to certain Roles" src="/docs/assets/img/users-and-permissions/setting-up-permissions-level-1.png">

* **HR User** should be able to delegate Leave Applications to his/her subordinates.
  HR User is given the right to Set User Permissions. A User with HR User role would be able to define User Permissions on Leave Application for other users.

  <img class="screenshot" alt="Let HR User delegate access to Leave Applications by checking 'Set User Permissions'. This will allow HR User to access User Permissions Manager for 'Leave Application'" src="{{docs_base_url}}/assets/img/users-and-permissions/setting-up-permissions-hr-user-role.png">

In case you have correctly assigned the roles but still you're getting errors when accessing documents, refer [this page](/docs/user/manual/en/setting-up/articles/report-permission-error).

### 3. Related Topics
1. [Role Based Permissions](/docs/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
1. [User Permissions](/docs/user/manual/en/setting-up/users-and-permissions/user-permissions)
1. [Role Permission For Page And Report](/docs/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report)

