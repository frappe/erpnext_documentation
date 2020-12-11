<!-- add-breadcrumbs -->
# Retention Bonus


**Retention bonus is a payment or reward outside of an employee's regular salary that is offered as an incentive to keep a key employee on the job.**

 ERPNext allows you to configure Retention Bonus for an Employee for a particular period.

To access Retention Bonus, go to:
> Home > Payroll > Compensation > Retention Bonus

## 1. Prerequisites

Before creating a Retention Bonus, it is advisable to create the following:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Salary Component](/docs/user/manual/en/payroll/salary-component)

## 2. How to create a Retention Bonus
1. Go to Retention Bonus list, click on New.
1. Select Employee and Bonus Payment Date.
1. Enter the Bonus Amount.
1. Select the [Salary Component](/docs/user/manual/en/payroll/salary-component) under which you want to give the bonus.
1. Save and Submit.
1. On submit, 'Additional Salary' document of the specified 'Salary Component' is created. This will be fetched while running Payroll Entry.

 <img class="screenshot" alt="Retention Bonus" src="/docs/assets/img/payroll/retention-bonus.png">

## 3. How Retention Bonus is processed
When Retention Bonus is Submitted, an Additional Salary having reference of Retention Bonus document is created which is fetched in Salary Slip Earnings while payroll process.

 <img class="screenshot" alt="Retention Bonus" src="/docs/assets/img/payroll/retention-bonus-reference.png">


## 4. Related Topics

1. [Employee Incentive](/docs/user/manual/en/payroll/employee-incentive)
1. [Additional Salary](/docs/user/manual/en/payroll/additional-salary)
1. [Salary Component](/docs/user/manual/en/payroll/salary-component)
1. [Salary Structure](/docs/user/manual/en/payroll/salary-structure)
1. [Payroll Entry](/docs/user/manual/en/payroll/payroll-entry)

{next}