<!-- add-breadcrumbs -->
# Salary Slip

**A salary slip is a document issued to an employee. It contains a detailed description of the employee’s salary components and amounts.**

To access Salary Slip, go to:
> Home > Payroll > Salary Slip

## 1. Prerequisites
Before creating Salary Slip, it is advised that you create the following first:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Salary Structure](/docs/user/manual/en/payroll/salary-structure)
* [Salary Structure Assignment](/docs/user/manual/en/payroll/salary-structure-assignment)

## 2. How to create a Salary Slip

1. Go to Salary Slip, Click on New.
1. Select Employee. On selecting Employee all details of the Employee will be fetched from Salary Structure which is assigned to that Employee. This includes details such as Currency, Payroll Frequency, Earnings, Deductions, etc.
1. If Currency is different than Company's Default Currency, then Exchange Rate field gets visible with default exchange rate on the day. However, user can change this value as per their requirements.
1. Select Start Date and End Date.
1. Save.

<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/payroll/salary-slip-top.png">

<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/payroll/salary-slip-bottom.png">

>Note: If Currency is different than Company's Default Currency, then all the totals are shown in both selected Currency and Company's Currency.

## 3. Feature

### 3.1. Salary Slip based on Attendance/Leave

HR users can create Salary Slip based on Attendance or leave.
The Working days will calculated on basis of leave/Attendance, depending on the field **Calculate Payroll Working Days Based On** in [Payroll Settings](/docs/user/manual/en/payroll/hr-settings). If Payroll is based on Attendance then, the **Leave without pay** will be considered as absent and **half-day** will be considered as half-day absent.

### 3.2 Salary Slip based on Timesheet
For creating Salary Slip based on timesheet you need to [create Salary Structure for Timesheets](/docs/user/manual/en/payroll/salary-structure#23-salary-structure-for-salary-based-on-timesheets).

On selecting employee all the timesheet between the start date and end date will be fetched in the timesheets child table. The amount will be calculated on Total Working hours and Hour rate. The amount is shown in the Earnings table, under the component selected in the Salary Structure.


<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/payroll/salary-timesheet.png">

### 3.3. Creating Salary Slip directly from Timesheet

ERPNext also provides an option to create Salary slip based on working hours based on [Timesheet](/docs/user/manual/en/projects/timesheets).
You can create Salary Slip after submitting the Timesheet by clicking directly on **Create Salary Slip** button on the top right.

<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="{{docs_base_url}}/assets/img/payroll/create-salary-slip-based-on-timesheets.png">

The Payment Amount is calculated based on Hour Rate defined in Salary Structure and is reflected in the Earnings table.

### 3.3 Year to Date and Month to Date

For every salary slip, 'Year to Date' and 'Month to Date' are computed.

<img class="screenshot" alt="Year to Date and Month to Date" src="{{docs_base_url}}/assets/img/human-resources/ytd-and-mtd.png">

- **Year to Date**: Total salary booked for that particular employee from the beginning of the year (payroll period or fiscal year) up to the current salary slip's end date.
- **Month to Date**: Total salary booked for a particular employee from the beginning of the month (for which the payroll entry is created) up to the current salary slip's end date.

Year to Date is also computed for every component in the earnings and deduction tables. The "Salary Slip with Year to Date" print format is available with Year to Date and Month to Date computations.

<img class="screenshot" alt="Year to Date for Salary Slip Components" src="{{docs_base_url}}/assets/img/human-resources/ytd-component.png">