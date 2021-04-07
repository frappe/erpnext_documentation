<!-- add-breadcrumbs -->
# Shift Management

Shift Management section of Human Resources helps your Organization manage shifts of your employees.

To use Shift Management in ERPNext,

  1. Set Up a Shift Type.
  2. Enter Shift Request.
  3. View and Manage Shift Assignments.

## 1. Shift Type

The Shift Type document allows you to define the different types of Shifts in your Organization and setup the auto attendance for the shift. Auto attendance marks attendance based on 'Employee Checkin' for Employees assigned to the shift.

To access Shift Type, go to:
> Home > Human Resources > Shift Management > Shift Type

1. Go to Shift Type List, Click on New.
2. Enter Name, Start Time and End Time
3. Save
<img class="screenshot" alt="Shift Type" src="{{docs_base_url}}/v12/assets/img/human-resources/new-shift-type.png">

## 2. Features

In addition to defining the different shifts in your organization, the Shift Type document also has the setting for auto attendance. Auto attendance marks the attendance for the employees assigned to this shift based on records in the 'Employee Checkin' Document. Auto Attendance for all shift type records are attempted to be marked every hour. You can also trigger the auto attendance manually for a single shift type by pressing the 'Mark Attendance' button in the shift type document.
<img class="screenshot" alt="Shift Type" src="{{docs_base_url}}/v12/assets/img/human-resources/shift-type.png">

### 2.1 Start Time
The time of the day when this shift starts. The time is to be entered in 24Hrs format.

### 2.2 End Time
The time of the day when this shift ends. The time is to be entered in 24Hrs format.

> Note: For cases where the 'End Time' is less that 'Start Time', the shift is assumed to be a night shift that starts on one calendar date and end on the next calendar date.

### 2.3 Holiday List
The Applicable Holidays for this shift can be selected here. If left blank then the default holiday list from the employee or the company document is taken in to account.

### 2.4 Enable Auto Attendance
You can use this option to enable marking attendance for the employees assigned to this shift based on their 'Employee Checkin' records.

### 2.5 Auto Attendance Settings
You can use the following settings to configure the Auto Attendance as per your requirements.

### Determine Check-in and Check-out
Employee Check-in may not always have an IN/OUT log type. For, such scenarios you could use this option to get appropriate results from the auto attendance system.

1. Alternating entries as IN and OUT during the same shift:
	- The first entry is taken as IN followed by the next entry as OUT and the following entry as IN and so on.
2. Strictly based on Log Type in Employee Checkin:
	- The check-in is determined as IN or OUT strictly based on the 'Log Type' in the Employee Checkin record.

### Working Hours Calculation Based On
Working hours can be calculated either by including the breaks in between the shift or by excluding the breaks.

This can be configured using the following options:

1. First Check-in and Last Check-out:
	- Selecting this option calculates the working hours by considering the first IN and last OUT Employee Checkin during the shift.
	- In case the IN/OUT is determined by alternating entries then the first Employee Checkin is considered as IN and the last Employee Checkin is considered as OUT for the purpose of working hours calculation.
2. Every Valid Check-in and Check-out:
	- Selecting this option excludes the time during which the Employee is checked out.
	- i.e. Only the time during which the employee is checked in is calculated as working hours.

### Begin check-in before shift start time
Often employees would check-in a few minutes before the shift start time. To consider these check-ins as part of the shift during the calculation of attendance, you could setup this value accordingly.

### Allow check-out after shift end time
Often employees would check-out after the shift end time. To consider these check-outs as part of the shift during the calculation of attendance, you could setup this value accordingly.

### Working Hours Threshold for Half Day
If the actual number of working hours is less than the given value in this field then the employee attendance is marked as 'Half Day'. If you never want to mark Half Day based on working hours, you should set this value to zero.

### Working Hours Threshold for Absent
If the actual number of working hours is less than the given value in this field then the employee attendance is marked as 'Absent'. If you never want to mark Absent based on working hours, you should set this value to zero.

### Process Attendance After
The date from which 'Auto Attendance' should start marking attendance. You should set it to a date after which you have Employee Checkin Records for this shift.

### Last Sync of Checkin
This is the time upto which attendance is marked based on the Employee Checkin records. You should set this to a date and time upto which the Employee Checkin has been synced. Otherwise an employee might be marked as absent due to the lack of check-in records.

# Shift Request


## 1. Prerequisites
To create a Shift Request, these need to be created first:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Shift Type](docs/user/manual/en/human-resources/shift-management#1-shift-type)

Shift Request is used by an employee to request for a particular Shift Type.

To create a new Shift Request go to:
> Human Resources > Shift Management > Shift Request


1. Go to Shift Request List, Click on New.
1. Select Employee and Shift Type.
1. Set the Shift duration using From Date and To Date.
1. Select the Approver. If the selected approver does not have access to the Shift Request document, it is shared with the approver with "submit" permission.
1. Save.

	<img class="screenshot" alt="Shift Request" src="{{docs_base_url}}/v12/assets/img/human-resources/shift-request.png">

# Shift Assignment

* Once the Shift Request is Approved and submitted it automatically creates the Shift Assignments for an Employee.

	<img class="screenshot" alt="Shift Assignment" src="{{docs_base_url}}/v12/assets/img/human-resources/shift-assignment.png">

> Note: The Assignment for active shift-type will be for a fixed period if there is an End Date otherwise, it will be treated as an ongoing shift with no End Date. Users can update End Date and status even after submitting the document.

### 3.1 Setting Shift Request Approver

A Shift Request Approver is a user who can approve a Shift Request of an Employee. In ERPNext version 13, Shift Request Approver can be set at two levels:

* **Department Level:** Shift Request Approvers for each department can be configured in the [Department](/docs/user/manual/en/human-resources/department) master. Multiple Shift Request Approver can be set in a Department.


    <img class="screenshot" alt="Shift Request Approvers" src="{{docs_base_url}}/v12/assets/img/human-resources/shift-request-approvers.png">

    When an Employee belonging to a particular department request for Shift Type, the Shift Request Approver set in that Employee's department master will be considered as his Shift Type Approvers.


* **Employee Level:**
Shift Request Approver can also be set Employee-wise in the employee master.


 <img class="screenshot" alt="Shift Request Approvers" src="{{docs_base_url}}/v12/assets/img/human-resources/employee-level-approvers.png">


If Shift Request Approver are set at both Employee-level and Department-level, the Employee-level Shift Request Approver will be considered as the default Leave Approver in this case.

{next}
