<!-- add-breadcrumbs -->
<!-- title: HR Settings -->

# HR Settings

**HR Settings allow global settings for HR related documents.**

## 1. Features

The different settings allowed are explained in brief below:

### 1. Employee Settings

1. **Retirement Age:** You can enter the retirement age (in years) for your employees. 

2. **Employee Records to be created by:** This is a select field which allows you to create Employee records such as Attendance records, Leave records, etc. either by Naming series or Employee Number or Full Name.  

<img class="screenshot" alt="Previous Work Experience" src="{{docs_base_url}}/assets/img/human-resources/hr-settings1.png">

3. **Leave Approval Notification Template:** 

 



To access HR Settings, go to:
> Home > Human Resources > Settings > HR Settings

There are various settings available in the HR Settings. Let's learn about each below.

## 1. Employee Settings


### 1.1 Retirement Age
This is used to compute the retirement date of the employees based on their Date of Birth. The age of retirement is taken as '60' if this field is left blank.


### 1.2 Employee Records to be created by
The naming for employee document is based on value selected in this field.

1. **Naming Series** - The employee documents created will be named using the naming series selected in the 'Series' field.
2. **Employee Number** - The Employee Number field becomes visible on selecting this field, and the naming of the employee document happens based on this field.
3. **Full Name** - The employee document is named using the full name of the employee.


### 1.3 Stop Birthday Reminders
An email is sent to all the employees of the company when any employee has a birthday. To stop this email from being sent you can check this option.

### 1.4 Expense Approver Mandatory In Expense Claim
In Expense Claim Document the 'Expense Approver' field is set to mandatory on checking this option.

## 2. Payroll Settings


### 2.1 Include holidays in Total no. of Working Days
If checked, total number of working days will include holidays, and this will reduce the value of salary per day.

### 2.2 Max working hours against Timesheet
For salary slips based on timesheet, you can set the maximum allowed hours against a single timesheet. Set this value to Zero to disable this validation.

### 2.3 Disable Rounded Total
You can enable this to disable rounding of total amount in salary slips.

### 2.4 Email Salary Slip to Employee
An email with the salary slip is sent to the respective employee's preferred email address on submission of the salary slip.

### 2.5 Encrypt Salary Slips in Emails
The salary slip PDF sent to the employee is encrypted using the mentioned Password Policy.

#### Password Policy
This field becomes visible and mandatory on checking the above option for encrypting the salary slip in email.

Here is an example on how to set a Password Policy for the salary slip PDF.

**Example:** `SAL-{first_name}-{date_of_birth.year}`

This will generate a password like SAL-Jane-1972

## 3. Leave Settings

### 3.1 Leave Approval Notification Template
On creation/updation of a leave application with a leave approver, an email is sent to this leave approver notifying about the new leave application. The email template used for this purpose can be selected here.

### 3.2 Leave Status Notification Template
On Submission/Cancellation of a leave application the employee receives an email with the updated status of their leave application. The email template used for this purpose can be selected here.

### 3.3 Leave Approver Mandatory In Leave Application
In Leave Application document the 'Leave Approver' field is set to mandatory on checking this option.

### 3.4 Show Leaves Of All Department Members In Calendar
The approved leaves of all employees in the same department are shown in the calender view on checking this option.

## 4. Hiring Settings

### 4.1 Check Vacancies On Job Offer Creation
On creation of job offer for a particular position, vacancies present in the staffing plan for that position is checked to warn the user from over hiring for a particular position.

{next}
