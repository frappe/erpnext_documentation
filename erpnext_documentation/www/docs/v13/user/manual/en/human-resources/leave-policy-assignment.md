<!-- add-breadcrumbs -->
# Leave Policy Assignment

> Introduced in Version 13

Leave Policy Assignment in ERPNext is used to assign leaves to employees based on created policies. To access the Leave policy assignment, go to:

> Home > Human Resources > Leaves > Leave Policy Assignment

## 1. Prerequisites

Before creating a Leave Policy Assignment, it is advisable to create the following:

* [Employee](/docs/v13/user/manual/en/human-resources/employee)
* [Leave Policy](/docs/v13/user/manual/en/human-resources/leave-policy)

## 2. How to create a Leave Policy Assignment

1. Go to Leave Policy Assignment, click on New.
1. Select Employee and Leave Policy.
1. Select Assignment based on the following as needed:
    * If "Assignment based on" is set to Leave Period, you need to select the applicable Leave Period. The Effective From and Effective To dates will be set automatically based on the Leave Period selected.
    * If "Assignment based on" is set to Joining Date, the Effective From date will be set to the employee's Date of Joining.
    * If "Assignment based on" is left blank, then you will have to set the Effective From and Effective To date manually.
1. Save and Submit.

<img class="screenshot" alt="Leave Policy Assignment"
    src="{{docs_base_url}}/v13/assets/img/human-resources/leave-policy-assignment.png">

On submit, Leave Allocation will be automatically created based on the [Leave Policy](/docs/user/manual/en/human-resources/leave-policy) as shown below.

<img class="screenshot" alt="Leave Allocations"
    src="{{docs_base_url}}/v13/assets/img/human-resources/granted-leaves.png">

## 5. Features
### 5.1 Bulk Leave Policy Assignment

ERPNext also allows creating multiple Leave Policy Assignment for multiple employees.

1. Go to the Leave Policy Assignment list, click on Bulk Leave Policy Assignment.
1. Dialog Will appear, Select Employee. You can filter employees based on Company and Department or You can also use standard filters by clicking Add Filters.
1. Select Leave Policy and Effective From and Effective To dates.
1. Click on Assign.

<img class="screenshot" alt="Bulk Leave Policy Assignment" src="{{docs_base_url}}/v13/assets/img/human-resources/bulk-leave-policy-assignment.png">

When you click on assign, it will automatically create and submit Leave Policy Assignment and also allocate leave based on Leave Policy.
