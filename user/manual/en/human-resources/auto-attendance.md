<!-- add-breadcrumbs -->
# Auto Attendance

> Introduced in Version 12

Auto attendance marks the attendance for the Employees assigned to a shift based on records in the 'Employee Checkin' Document and the [Auto Attendance Settings](/docs/user/manual/en/human-resources/shift-management#25-auto-attendance-settings) of that shift.

Auto Attendance for every 'Shift Type' record is attempted to be marked every hour. You can also trigger the auto attendance manually for a single shift type by pressing the 'Mark Auto Attendance' button in the Shift Type document. 

> Note: [Shift Type](/docs/user/manual/en/human-resources/shift-management#shift-type) needs to be set up and assigned to Employees before creating 'Employee Checkin' records. Attendance will be marked by Auto Attendance only for check-in records that are created after setting up and assigning an Employee to their shift type.

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
- Note: The Holiday List is important to be determined correctly by the Auto Attendance to not mark Absents for Employees on holidays.
