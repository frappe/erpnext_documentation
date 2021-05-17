<!-- add-breadcrumbs -->
# Employee Grievance

> Introduced in version-13

**An employee grievance is a concern, problem, or complaint raised by an employee with what he expects from the company(or their individuals) and its management. Something has made them feel dissatisfied, and they believe it is unfair and/or unjust on them. It may or may not be justified but needs to be tackled very carefully.**

In ERPNext, you can handle these Employee Grievances to make your employees happy.

To access Employee Grievance, go to:

> Home > Human Resources > Employee Grievance

## 1. Prerequisites

Before creating an Attendance record, it is advised that you create the following first:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Grievance Type](/docs/user/manual/en/human-resources/grievance-type)

## 2. How to create Employee Grievance

1. Go to Employee Grievance List, click on Add Employee Grievance.
1. Select Raised by, date, etc.
1. Fill Grievance Details like Grievance Against Party, Grievance Against, Grievance Type, etc.
1. Enter Description.
1. Save your document.

<img class="screenshot" alt="Employee Grievance" src="{{docs_base_url}}/assets/img/human-resources/employee-grievance.png">

> Note: Employee can also link Documents related to the grievance.




## 3. Workflow

1. The Employee creates an Employee Grievance document for their complaint or problem against Company, Employee, Department, etc.
1. The HR manager will investigate and he will fill the cause of the grievance and after that, he can change the status to Investigated. You can not set the status to **Investigated** without cause of grievance.
1. After that, the Hr manager will fill in resolution detail, and now he can and save the Employee grievance. You can not mark Grievance as **Resolved** without Resolution details.
1. So, Now the cause of grievance and Resolution details are filled and the status is resolved which allows you to submit the document.

> Note: You can only submit a document with **Resolved** status.

## 4 Action
Some cases like Employee Abuse, Bullying, harassment may require some action like Suspension or Pay-cut for an employee. ERPNext also allows you to perform such kinds of actions when need to be done.

### 4.1 Employee Suspension:
Suspension of an employee means keeping an employee away from the workplace temporarily for reasons of discipline.

> Note: For taking such action first you need to check *"Is Applicable for Suspension"* checkbox and fill *"Number of days for suspension"* in respective [Grievance Type](/docs/user/manual/en/human-resources/employee-grievance) and need to fill *"Employee Responsible"*.

When Employee Grievance is Investigated and resolved now it time to take action. Click on suspend button on the right top corner and refresh the page. The "Suspended from" And "Suspended to" will be automatically updated in the actions section.


<img class="screenshot" alt="Employee Grievance" src="{{docs_base_url}}/assets/img/human-resources/grievance-action.png">

An employee will be unsuspended automatically after the "Suspended to" date or you can do it manually by clicking on unsuspend Employee on the top right corner

<img class="screenshot" alt="Employee Grievance" src="{{docs_base_url}}/assets/img/human-resources/unsuspend-employee.png">

### 4.2 Employee pay-cut

> Note: For taking such action first you need to check *"Is Applicable for Pay-cut"* checkbox in respective [Grievance Type](/docs/user/manual/en/human-resources/employee-grievance).

When Employee Grievance is Investigated and resolved You can Apply Pay-cut by clicking on Apply Pay-cut at Top right corner.

<img class="screenshot" alt="Employee Grievance" src="{{docs_base_url}}/assets/img/human-resources/apply-pay-cut.png">

On click, It will redirect you to the Additional salary form with the type Deduction select component and fill amount. Save and Submit the document.