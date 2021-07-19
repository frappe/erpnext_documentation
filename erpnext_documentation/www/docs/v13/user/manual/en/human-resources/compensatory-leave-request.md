<!-- add-breadcrumbs -->
# Compensatory Leave Request


**Compensatory Leave is a leave that is granted to an Employee as compensation for working overtime or on holidays.**

 ERPNext allows Employees to request for Compensatory Leaves through the Compensatory Leave Request document. It is necessary that the dates mentioned in the Compensatory Leave Request should be in default Holiday List and also that the Employee should have their attendance marked Present.

 > **Note:** Only Leave Types which are marked as 'Is Compensatory' can be selected in the Compensatory Leave Request.

To access Compensatory Leave Request, go to:

> Home > Human Resources > Leaves > Compensatory Leave Request


## 1. Prerequisites

Before creating a Compensatory Leave Request, it is necessary to create the following documents:

* [Employee](/docs/v13/user/manual/en/human-resources/employee)
* [Leave Period](/docs/v13/user/manual/en/human-resources/leave-period)
* [Leave Type](/docs/v13/user/manual/en/human-resources/leave-type)
* [Leave Policy](/docs/v13/user/manual/en/human-resources/leave-policy)
* [Leave Allocation](/docs/v13/user/manual/en/human-resources/leave-allocation)
* [Holiday List](/docs/v13/user/manual/en/human-resources/holiday-list)
* [Attendance](/docs/v13/user/manual/en/human-resources/attendance)


## 2. How to create a Compensatory Leave Request

1. Go to Compensatory Leave Request list, click on New.
1. Select the Employee ID. Once selected, The Employee Name and Department will get automatically fetched.
1. Select Leave Type.
1. Select Work From Date and Work End Date. This is the date of the day(s) the Employee has worked on, during a Holiday.
1. Enter the Reason.
1. Save and Submit.

    <img class="screenshot" alt="Compensatory Leave Request"
    src="{{docs_base_url}}/v13/assets/img/human-resources/compensatory-leave.png">



On submitting the Compensatory Leave Request, ERPNext updates the Leave Allocation record for the Compensatory leave type, allowing the Employee to apply for leaves of this type later on depending upon the number of leaves left.


## 3. Related Topics

1. [Leave Application](/docs/v13/user/manual/en/human-resources/leave-application)
1. [Leave Encashment](/docs/v13/user/manual/en/human-resources/leave-encashment)
1. [Leave Block List](/docs/v13/user/manual/en/human-resources/leave-block-list)

