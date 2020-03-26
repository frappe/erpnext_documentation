<!-- add-breadcrumbs -->
# Auto Attendance

> Introduced in Version 12

Auto attendance marks the attendance for the Employees assigned to a shift based on records in the 'Employee Checkin' Document and the [Auto Attendance Settings](/docs/user/manual/en/human-resources/shift-management#25-auto-attendance-settings) of that shift.

Auto Attendance for every 'Shift Type' record is attempted to be marked every hour. You can also trigger the auto attendance manually for a single shift type by pressing the 'Mark Auto Attendance' button in the Shift Type document. 

> Note: [Shift Type](/docs/user/manual/en/human-resources/shift-management#shift-type) needs to be set up and assigned to Employees before creating 'Employee Checkin' records. Attendance will be marked by Auto Attendance only for check-in records that are created after setting up and assigning an Employee to their shift type.

## Steps to Setup Auto Attendance
You can set up Auto Attendance by following the steps mentioned below:

1. [Define Shift Type with Auto Attendance Enabled](#1-define-shift-type-with-auto-attendance-enabled)
1. [Assign these shifts to Employees](#2-assign-these-shifts-to-employees)
1. [Setup Attendance Device ID field in Employee](#3-setup-attendance-device-id-field-in-employee)

### 1. Define Shift Type with Auto Attendance Enabled
To be able to mark attendance from a list of Check-in/Check-out logs, you need to set up shifts that have the "Enable Auto Attendance" field enabled. Once you enable this option, you will be able to see an "Auto Attendance Settings" section. Please fill this section as per your requirements for that shift.

Please refer to the following link to know more about each field in the Auto Attendance settings section: [Auto Attendance Settings](/docs/user/manual/en/human-resources/shift-management#25-auto-attendance-settings)

### 2. Assign these shifts to Employees
Once you have set up a shift, you will have to assign this to the employees. 

You can assign this to an employee by either of the two methods:

1. Using the Shift Assignment

    You can use the [Shift Assignment](/docs/user/manual/en/human-resources/shift-management#shift-assignment) to assign shifts to employees on a date to date basis.

1. Using the Default Shift field in the employee

    Sometimes you would want to assign a shift for an employee for all the days.

    You can do this by setting the following field in the Employee: `Employee > ATTENDANCE AND LEAVE DETAILS > Default Shift`

> Note: Setting Shift Assignment takes precedence over the default shift. i.e. When the default shift is set, that shift is taken as the employee shift for all days without a Shift Assignment.


### 3. Setup Attendance Device ID field in Employee
Biometric systems usually have their own IDs for employees. But, the Employee Checkin in ERPNext needs to be mapped to an employee.

To map the employee to their IDs in the Biometric system you need to set the following field with the appropriate value: `Employee > ATTENDANCE AND LEAVE DETAILS > Attendance Device ID (Biometric/RF tag ID)`

Once you are done with the above steps you can now import the Employee Checkin and start generating attendance automatically.

Please refer to this article to know more about importing Employee Checkin from an external system: [Integrating ERPNext With Biometric Attendance Devices](/docs/user/manual/en/setting-up/articles/integrating-erpnext-with-biometric-attendance-devices)

## Following are some frequently asked questions regarding Auto Attendance.

### How does Auto Attendance determine shift for an Employee?
Shift of an Employee on a particular date is determined by the following steps:

- Shift assigned to an Employee on the given date in the 'Shift Assignment' document.
- If the above is not found, the shift is picked up from the 'Default Shift' field of the 'Employee' document.
- Finally, if a shift is not found in 'Employee' document also, then it is assumed that the Employee does not belong to any shift on the given date and no attendance is attempted to be marked by the Auto Attendance.

### How does Auto Attendance determine Holiday List for an Employee?
Holiday List of an Employee is determined by the following steps:

- If the Employee's determined 'Shift Type' has a holiday list, then this is taken.
- Otherwise, the holiday list is taken from either the 'Holiday List' field in the Employee Document or from 'Default Holiday List' field of the Company Document, in that order.

Note: The Holiday List is important to be determined correctly by the Auto Attendance to not mark Absents for Employees on holidays.
