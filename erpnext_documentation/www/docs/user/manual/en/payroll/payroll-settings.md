# Payroll Settings

**Payroll Settings allow global settings for Payroll-related documents.**

To access Payroll Settings, go to:

> Home > Payroll > Settings > Payroll Settings

There are various settings available in the Payroll Settings.

<img class="screenshot" alt="Previous Work Experience" src="{{docs_base_url}}/assets/img/payroll/payroll-settings.png">

## 1. Calculate Payroll Working Days Based On
Working Days in Salary Slip can be calculated based on Leave Application or Attendance records. You can select the option based on what you want to calculate working days.

## 2. Consider Unmarked Attendance as
This field becomes visible if payroll Working Days are based on Attendance. Users select whether Unmarked days will be considered as absent or present.

## 3. Max working hours against Timesheet
For salary slips based on the timesheet, you can set the maximum allowed hours against a single timesheet. Set this value to zero to disable this validation.

## 4. Include holidays in Total no. of Working Days
If checked, the total number of working days will include holidays, and this will reduce the value of salary per day.

## 5. Disable Rounded Total
You can enable this to disable rounding off the total amount in salary slips.

## 6. Daily Wages Fraction for Half Day
Based on this fraction, the salary for Half Day will be calculated. For example, if the value is set as 0.75, the three-fourth salary will be given for half-day attendance.

## 7. Email Salary Slip to Employee
An email with the salary slip is sent to the respective employee's preferred email address on submission of the salary slip.

## 8. Encrypt Salary Slips in Emails
The salary slip PDF sent to the employee is encrypted using the mentioned Password Policy.

## 9. Password Policy
This field becomes visible and mandatory on checking the above option for encrypting the salary slip in email.

Here is an example of how to set a Password Policy for the salary slip PDF.

**Example:**

```
SAL-{first_name}-{date_of_birth.year}
```

This will generate a password like SAL-Jane-1972