<!-- add-breadcrumbs -->
# Employee Incentive

**Employee Incentives are a way of compensating and motivating employee performance apart from the usual salary.**

When an organization wants to encourage productivity among its employees, one of the options available is rewarding the Employee with an incentive. ERPNext allows you to create Employee Incentives as and when required for a particular payroll entry.


To access Employee Incentive, go to:
> Home > Payroll > Compensation > Employee Incentive

## 1. Prerequisites

Before creating an Employee Incentive, it is advisable to create the following:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Salary Component](/docs/user/manual/en/payroll/salary-component)

## 2. How to create an Employee Incentive

1. Go to Employee Incentive list, click on New.
1. Select the Employee.
1. Enter the Incentive Amount.
1. Select the Payroll Date.
1. Select the [Salary Component](/docs/user/manual/en/payroll/salary-component) under which you want to give the incentive.
1. Save and Submit.
1. On submit, the 'Additional Salary' document of the specified 'Salary Component' is created. This will be fetched while running the Payroll Entry.

 <img class="screenshot" alt="Employee Incentive" src="/docs/assets/img/payroll/employee-incentive.png">

## 3. How Employee Incentive is processed
When Retention Bonus is Submitted, an Additional Salary having reference of Employee Incentive document is created which is fetched in Salary Slip Earnings while payroll process.

 <img class="screenshot" alt="Retention Bonus" src="/docs/assets/img/payroll/employee-incentive-reference.png">


## 4. Related Topics

1. [Retention Bonus](/docs/user/manual/en/payroll/retention-bonus)
1. [Additional Salary](/docs/user/manual/en/payroll/additional-salary)
1. [Salary Component](/docs/user/manual/en/payroll/salary-component)
1. [Salary Structure](/docs/user/manual/en/payroll/salary-structure)
1. [Payroll Entry](/docs/user/manual/en/payroll/payroll-entry)

{next}
