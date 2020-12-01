# Leave Policy Assignment

> Introduced in Version 13

Leave Policy Assignment in ERPNext is used to grant leaves to employees. To access Leave policy assignment, go to:

> Home > Human Resources > Leaves > Leave Policy Assignment

## 1. Prerequisites

Before creating a Leave Policy Assignment, it is advisable to create the following:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Leave Policy](/docs/user/manual/en/human-resources/leave-policy)

## 2. How to create a Leave Policy Assignment

1. Go to Leave Policy Assignment, click on New.
1. Select Employee and Leave Policy.
1. Select Assignment based on if required.
    * If an assignment is based on Leave period, You need to select Leave period. The Effective From and Effective To will be set automatically.
    * If an assignment is based on Joining Date, The Effective From date will be set to Employee's Date of Joining.
    * If an assignment is based on is blank, You need to set Effective From and Effective To Manually.
1. Save and Submit.

<img class="screenshot" alt="Leave Policy Assignment"
	src="{{docs_base_url}}/assets/img/human-resources/leave-policy-assignment.png">

## 3. Granting Leave

Once the information is saved, the Leave Policy Assignment will also be used as a tool to help you grant leaves for employees. The **Grant Leave** button will appear at the right top corner.


<img class="screenshot" alt="Grant Leaves"
	src="{{docs_base_url}}/assets/img/human-resources/leave-policy-assignment-grant-leave.png">

On click, The Leave allocation will be created automatically based on [Leave Policy](/docs/user/manual/en/human-resources/leave-policy) as shown below.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/granted-leaves.png">

>**Note:** The Grant Leave button will appear only then if, No leaves are granted or there is no allocation against current Leave Policy Assignment.

## 4. Automatic Allocate Leaves Based On Leave Policy

To enable Automatic allocation for your Leave Policy Assignment you need to Enable [Automatic Allocate Leaves Based On Leave Policy ](/docs/user/manual/en/human-resources/hr-settings#37-automatic-allocate-leaves-based-on-leave-policy) checkbox in HR Settings. Our Scheduler Run background Job and check the Effective From Date in Leave Policy Assignment and create Leave allocation automatically.

>**Note:** The Leave will be automatically granted only if, No leave is granted against that Leave Policy Assignment till Effective From date.

## 5. Features
### 5.1 Bulk Leave Policy Assignment

Our System also allow to create multiple Leave Policy Assignment for multiple employees.

1. Go to Leave Policy Assignment list, click on Bulk Leave Policy Assignment.
1. Dialog Will appear, Select Employee. You can filter Employee based on Company and Department or You can also use standard filters on clicking Add Filters.
1. Select Leave Policy and Effective From and Effective To.
1. Click on Assign.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/bulk-leave-policy-assignment.png">

### 5.2 Granting leaves to multiple employees

Our System also allow to Grant Leaves based on multiple Leave Policy Assignment for multiple employees.

1. Go to Leave Policy Assignment list, click on Grant Leaves.
1. Dialog Will appear, Select Leave Policy Assignments. You can filter Assignment based on Company and Employee or You can also use standard filters on clicking Add Filters.
1. Select the Leave Policy Assignments.
1. Click on Grant Leaves.

<img class="screenshot" alt="Leave Allocations"
	src="{{docs_base_url}}/assets/img/human-resources/granting-leave-to-multiple-employee.png">
