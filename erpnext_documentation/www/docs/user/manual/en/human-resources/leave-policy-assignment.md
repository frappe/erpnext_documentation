# Leave Policy Assignment

> Introduced in Version 13

Leave Policy Assignment in ERPNext is used to assign leaves to employees based on created policies. To access Leave policy assignment, go to:

> Home > Human Resources > Leaves > Leave Policy Assignment

## 1. Prerequisites

Before creating a Leave Policy Assignment, it is advisable to create the following:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Leave Policy](/docs/user/manual/en/human-resources/leave-policy)

## 2. How to create a Leave Policy Assignment

1. Go to Leave Policy Assignment, click on New.
1. Select Employee and Leave Policy.
1. Select Assignment based on the following as needed:
    * If "Assignment based on" is set to Leave Period, you need to select the applicable Leave Period. The Effective From and Effective To dates will be set automatically based on the Leave Period selected.
    * If "Assignment based on" is set to Joining Date, the Effective From date will be set to the employee's Date of Joining.
    * If "Assignment based on" is left blank, then you will have to set the Effective From and Effective To date manually.
1. Save and Submit.

<img class="screenshot" alt="Leave Policy Assignment"
	src="{{docs_base_url}}/assets/img/human-resources/leave-policy-assignment.png">

## 3. Granting Leaves

Once the information is saved, the Leave Policy Assignment will also be used as a tool to help you grant leaves to employees. The **Grant Leave** button will appear at the right top corner.


<img class="screenshot" alt="Grant Leaves"
	src="{{docs_base_url}}/assets/img/human-resources/leave-policy-assignment-grant-leave.png">

On clicking the "Grant Leave" button, Leave Allocation will be automatically created based on the [Leave Policy](/docs/user/manual/en/human-resources/leave-policy) as shown below.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/granted-leaves.png">

>**Note:** The Grant Leave button will appear only if there are no leaves granted or there is no allocation against a current Leave Policy Assignment.

## 4. Automatically Allocate Leaves Based On Leave Policy

To enable automatic allocation of leaves based on the Leave Policy Assignment, enable [Automatic Allocate Leaves Based On Leave Policy ](/docs/user/manual/en/human-resources/hr-settings#37-automatic-allocate-leaves-based-on-leave-policy) checkbox in HR Settings. The scheduler then runs a background job and checks the Effective From date in the Leave Policy Assignment to create leave allocations automatically.

>**Note:** Leaves will be automatically granted only if, there are no leaves granted against that Leave Policy Assignment till Effective From date.

## 5. Features
### 5.1 Bulk Leave Policy Assignment

ERPNext also allows creating multiple Leave Policy Assignment for multiple employees.

1. Go to Leave Policy Assignment list, click on Bulk Leave Policy Assignment.
1. Dialog Will appear, Select Employee. You can filter Employee based on Company and Department or You can also use standard filters by clicking Add Filters.
1. Select Leave Policy and Effective From and Effective To dates.
1. Click on Assign.

<img class="screenshot" alt="Bulk Leave Policy Assignment" src="{{docs_base_url}}/assets/img/human-resources/bulk-leave-policy-assignment.png">
	src="{{docs_base_url}}/assets/img/human-resources/bulk-leave-policy-assignment.png">

### 5.2 Granting leaves to multiple employees

Leaves can be granted based on multiple Leave Policy Assignments to multiple employees.

1. Go to Leave Policy Assignment list, click on Grant Leaves.
1. A dialog will be shown. Select the Leave Policy Assignments. You can filter the assignments based on Company and Employee or you can also use standard filters by clicking on the Add Filters button.
1. Select the Leave Policy Assignments.
1. Click on Grant Leaves.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/granting-leave-to-multiple-employee.png">
