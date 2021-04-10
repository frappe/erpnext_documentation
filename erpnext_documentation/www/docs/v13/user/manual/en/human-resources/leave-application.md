<!-- add-breadcrumbs -->
# Leave Application

**Leave Application is a formal document created by an Employee to apply for Leaves for a particular time period.**

ERPNext allows your employees to apply for leaves via Leave Applications and get them approved by the Leave Approvers.

To access Leave Application, go to:

> Home > Human Resources > Leaves > Leave Application

## 1. Prerequisites

Before you create a Leave Application, it is advisable you have the following documents:

* [Department](/docs/v13/user/manual/en/human-resources/department)
* [Leave Period](/docs/v13/user/manual/en/human-resources/leave-period)
* [Holiday List](/docs/v13/user/manual/en/human-resources/holiday-list)
* [Leave Type](/docs/v13/user/manual/en/human-resources/leave-type)
* [Leave Policy](/docs/v13/user/manual/en/human-resources/leave-policy)
* [Leave Allocation](/docs/v13/user/manual/en/human-resources/leave-allocation)

## 2. How to create a Leave Application

1. Go to Leave Application list, click on New.
1. A table of Allocated Leaves will be shown. Based on the Leaves taken, the available leaves are displayed for each Leave Type.

     <img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/v13/assets/img/human-resources/leave-app.png">


1. Select the Employee Name and Leave Type.
1. Set the Leave duration using From Date and To Date. Based on the dates selected, the 'Total Leave Days' and the 'Leave Balance Before Application' fields will be displayed.
1. If the Leave applied is for a half-day, select the 'Half Day' checkbox.
1. Enter the Reason for Leave.

    <img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/v13/assets/img/human-resources/leave-app1.png">


1. Select Leave Approver.
1. Select the Posting Date of the Leave Application.
1. Check the 'Follow via Email' checkbox to send notification of the Leave Application to the Leave Approver.
1. You can also link the Salary Slip of the Employee in the Leave Application for the record.

    <img class="screenshot" alt="Leave Application" src="{{docs_base_url}}/v13/assets/img/human-resources/leave-app3.png">

1. Click on Save. Once the Employee saves the Leave Application, the status of the Leave Application changes to 'Open', and an email is sent to the Leave Approver for approval. The Leave Approval Notification Template can be configured in [HR Settings](/docs/v13/user/manual/en/human-resources/hr-settings) under the Leave Settings section.
1. Once the Leave Approver receives the email, they can Approve, Reject, or Cancel the Leave Application. Once this is done, the Leave Approver can submit the Leave Application. On submission, the status of the document changes accordingly, and an email is sent to the Employee notifying them the same.


> **Note:** Leave Application cannot be submitted if the Salary is already processed for the leave period.

The Leave Application process flow is summarized below:

- The employee applies for leave through Leave Application.
- Approver gets notification via email. For this, the "Follow via Email" checkbox should be checked.
- Approver reviews Leave Application.
- Approver approves/rejects/cancels Leave Application
- The employee gets the notification on the status of his/her Leave Application

## 3. Features

### 3.1 Setting Leave Approver

A leave approver is a user who can approve a Leave Application of an Employee. In ERPNext version 12, Leave Approvers can be set at two levels:

* **Department Level:** Leave Approvers for each department can be configured in the [Department](/docs/v13/user/manual/en/human-resources/department) master. Multiple Leave Approvers can be set in a Department. The first Leave Approver in the list will be considered as the default Leave Approver.


    <img class="screenshot" alt="Leave Application - Leave Approvers" src="{{docs_base_url}}/v13/assets/img/human-resources/leave-app4.png">

    When an Employee belonging to a particular department applies for leave, the Leave Approvers set in that Employee's department master will be considered as his Leave Approvers.


* **Employee Level:**
Leave Approvers can also be set Employee-wise in the employee master.


 <img class="screenshot" alt="Leave Application - Leave Approvers" src="{{docs_base_url}}/v13/assets/img/human-resources/employee-level-approvers.png">


If Leave Approvers are set at both Employee-level and Department-level, the Employee-level Leave Approver will be considered as the default Leave Approver in this case.

When a new Leave Application is created, if the selected leave approver does not have access to it, the document is shared with the approver with "submit" permission.

 **Tip:** If you want all users to create their own Leave Applications, you can set
their “Employee ID” as a match rule in the Leave Application Permission
settings. Check [Setting Up Permissions](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions.html)
for more information.

> **Additional Notes:**

>* Leave Application period must be within a single Leave Allocation period. In case, you are applying for leave across the leave allocation period, you have to create two Leave Application records.
>* Leave Application period must be in the latest Leave Allocation period.
>* Employee cannot apply for leave on the dates which are added in the [Leave Block List](/docs/v13/user/manual/en/human-resources/leave-block-list).

To understand how ERPNext allows you configure leaves for employees, check [Leaves](/docs/v13/user/manual/en/human-resources/leave-management-intro/).


## 3. Related Topics

1. [Leave Type](/docs/v13/user/manual/en/human-resources/leave-type)
1. [Leave Period](/docs/v13/user/manual/en/human-resources/leave-period)
1. [Leave Policy](/docs/v13/user/manual/en/human-resources/leave-policy)
1. [Leave Allocation](/docs/v13/user/manual/en/human-resources/leave-allocation)
1. [Leave Block List](/docs/v13/user/manual/en/human-resources/leave-block-list)



<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/fc0p_AXebc8?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

{next}
