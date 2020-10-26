<!-- add-breadcrumbs -->
# Attendance Status

The Attendance Status of an employee conveys whether the employee is Present, Absent, or is on leave on a particular day.

In ERPNext, you can create multiple statuses for attendance. Suppose, an employee is on a visit to another place or working remotely, then you can create a custom status for tracking Attendance.

To access Attendance Status, go to:

> Home > Human Resources > Attendance

## 1. How to Create Attendance status:

1. Go to the Attendance Status list, click on New.
1. Name your Attendance Status.
1. Write Abbreviation for your status. Which is used in Monthly Attendance Sheet.
1. Click on save.

> Note: if None of the property Is Half Day, Is Leave or Is Present is checked status will be treated as Absent

<img class="screenshot" alt="Attendance" src="{{docs_base_url}}/assets/img/human-resources/attendance-status.png">

Below are detailed explanation of all checkbox in Attendance Status.

* **IS Half Day:** If Checked, The Attendance Status will represent Half Day Status During Attendance Creation.

* **IS Leave:** In ensure that Attendance Status will treated as leave Status.

* **Is Present:** If Checked, The Attendance Status will be treated as present.

* **Applicable for Leave Application**: This checkbox is visible only if **Is Half Day** or **Is leave** property for Attendance Status is enable. If this property is enabled then it will be taken as default Leave or Half Day Status for Attendance created while Leave approval.

>Note: Only one Half Day and Leave Status with property Applicable for Leave Application is allowed at a time.

* **Applicable for Employee Checkins**: This Property works for Auto Attendance Creation through Employee Checkin. If Checked the status will be taken as default status for Present, Half day, or Leave during automatic attendance creation.

>Note:
It is mandatory to create the Attendance Status wil this property to make Auto Attendance Functional.
Only one Half day, Present, and Absent with property Applicable for Employee Checkins ia allowed at a time.

* **Applicable for Attendance Request:** This checkbox is visible if **Is Half Day** for Attendance Status is enable. If Checked, Status will Be treated as default Half day status while Attendance Request Approval.

>Note: Only one Half Day  with property Applicable for Attendance Request is allowed at a time.
