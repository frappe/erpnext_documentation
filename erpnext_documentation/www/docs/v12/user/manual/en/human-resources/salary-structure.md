<!-- add-breadcrumbs -->
# Salary Structure

**Salary Structure is the details of the salary being offered to an Employee, in terms of the breakup of the different components constituting the compensation.**

Any changes to the Salary Structure i.e. among the components can have a major impact on what the Employee does, such as the kind of tax exemptions claimed.

ERPNext allows you to define the Earnings and Deductions of a Salary Structure, Payroll frequency, and Payment Mode among other features.

To access Salary Structure, go to:
> Home > Human Resources > Payroll > Salary Structure


## 1. Prerequisites

Before you create a Salary Structure, it is advisable you have the following:

* [Salary Component](/docs/user/manual/en/human-resources/salary-component)


## 2. How to create a Salary Structure

1. Go to the Salary Structure list, click on New.
2. Enter the Salary Structure Name.
3. Select the Company Name and Payroll Frequency.
3. Save and Submit.


## 2. Features

### 2.1 Earnings and Deductions

Earnings specify the Salary Components that are earned by an Employee. These components typically include basic, allowances, bonuses, and incentives that are added to the employee's Total Salary. On the other hand, Deductions specify the Salary Components that are deducted from the employee's Total Salary. These typically include the taxes.

>**Note:** Only Salary Components set as 'Earnings' will be shown in the Earnings table and components set as 'Deductions' will be shown in the Deductions table.


To create Earnings and Deductions, select the Salary Component in the Component column. Enter the Formula/Condition if not previously specified while creating the [Salary Component](/docs/user/manual/en/human-resources/salary-component). Additionally, you can also enter a pre-defined amount in the Amount column.



<img class="screenshot" alt="Salary Structure" src="{{docs_base_url}}/v12/assets/img/human-resources/salary-structure.png">


> **Note:** Make sure to click on the downward arrow and enable the 'Amount based on formula' checkbox in case the Salary Component is calculated using a formula.


### 2.2 Account

In this section, the [Mode of Payment](/docs/user/manual/en/accounts/mode-of-payment) and the [Payment Account](/docs/user/manual/en/accounts/chart-of-accounts) that is used to pay the salary can be specified.

### 2.3 Salary Structure for Salary based on Timesheets

In ERPNext you can also define the Salary Structure for Salary Slip based on Timesheet, which allows the Company to pay there Employee as per working hours.

Steps for creating Salary Structure based on Timesheets:

1. Go to Salary Structure List, click on New.
1. Select checkbox **Salary Slip Based on Timesheet**.
1. Select the Salary Component. 
1. Enter the Hour Rate. Based on the Rate entered, the amount for Working hours for the selected Salary Component will be calculated accordingly.
1. Save and Submit.

 <img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/v12/assets/img/human-resources/salary-structure-for-salary-based-on-timesheets.png">


### 2.4 Leave Encashment Amount Per Day 

In case there are encashable leaves for an Employee, you can define the leave encashment amount per day in this field for this particular Salary Structure. Based on the 'Earning Component' set in the encashed [Leave Type](/docs/user/manual/en/human-resources/leave-type) and the amount per day, the value for the Salary component will be calculated accordingly in the Salary Slip.


### 2.5 Max Benefits (Amount)

In this field, the Max Benefits Amount for the Salary Structure can be specified. If this field is filled, make sure the Salary Structure has a [Salary Component](/docs/user/manual/en/human-resources/salary-component) with the "Is Flexible Benefits" checked, against which this amount will be paid.



Once all the information is saved and submitted, you can assign the Salary Structure to an Employee either through the **Assign Salary Structure** button or by creating a new [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment) through the dashboard.

You can also assign the created Salary Structure to several employees based on the [Employee Grade](/docs/user/manual/en/human-resources/employee-grade), [Department](/docs/user/manual/en/human-resources/department), [Designation](/docs/user/manual/en/human-resources/designation), etc. through the 'Assign to Employees' button.
Additionally, Salary Slip can also be directly created through the dashboard.

## 3. Related Topics

1. [Salary Component](/docs/user/manual/en/human-resources/salary-component)
1. [Salary Structure Assignment](/docs/user/manual/en/human-resources/salary-structure-assignment)
1. [Payroll Entry](/docs/user/manual/en/human-resources/payroll-entry)
