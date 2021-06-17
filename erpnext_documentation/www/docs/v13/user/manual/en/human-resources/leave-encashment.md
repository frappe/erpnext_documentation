<!-- add-breadcrumbs -->
# Leave Encashment



**Leave Encashment refers to an amount of money received in exchange for Leaves not availed by an Employee. You can submit Leave Encashment for Leave Types which are encashable.**

To access Leave Encashment, go to:

> Home > Human Resources > Leaves > Leave Encashment


## 1. Prerequisites

Before creating Leave Encashment, it is advisable you create the following documents:

1. [Employee](/docs/v13/user/manual/en/human-resources/leave-allocation)
1. [Leave Type](/docs/v13/user/manual/en/human-resources/leave-type)
1. [Leave Policy](/docs/v13/user/manual/en/human-resources/leave-policy)
1. [Leave Period](/docs/v13/user/manual/en/human-resources/leave-period)
1. [Salary Structure](/docs/v13/user/manual/en/human-resources/salary-structure)
1. [Salary Structure Assignment](/docs/v13/user/manual/en/human-resources/salary-structure-assignment)

## 2. How to create a Leave Encashment

1. Go to Leave Encashment list, click on New.
1. Select Leave Period.
1. Select the Employee. Once the Employee is selected, the Employee's Department is automatically fetched.
1. Select Leave Type for which the Leave is encashed. Make sure the Leave Type is encashable (the 'Allow Encashment' checkbox in the Leave Type is checked).
1. Select Encashment Date. Based on the date selected, the amount will be encashed in that particular Payroll Entry.
1. Save and Submit.

	<img class="screenshot" alt="Leave Encashment"
	src="{{docs_base_url}}/v13/assets/img/human-resources/leave-encashment-new.png">


> **Note:** As you select Employee and Leave Type, Leave Balance and Encashable Days (which is total leave balance minus the threshold days set in Leave Type) will be shown along with the Encashment Amount based on the Leave Encashment per day as configured in the Employee's assigned Salary Structure.


On submitting a Leave Encashment for an Employee, ERPNext automatically creates an [Additional Salary](/docs/v13/user/manual/en/human-resources/additional-salary) which will get added to the Salary Slip of the Employee when processing the payroll.



## 3. Related Topics

1. [Payroll Period](/docs/v13/user/manual/en/human-resources/payroll-period)
1. [Payroll Entry](/docs/v13/user/manual/en/human-resources/payroll-entry)
1. [Additional Salary](/docs/v13/user/manual/en/human-resources/additional-salary)


