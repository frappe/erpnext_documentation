<!-- add-breadcrumbs -->
# Compensatory Leave Request


**Compensatory Leave is a leave that is granted to an Employee as a compensation for working overtime or on holidays.**



 ERPNext allows Employees to request for Compensatory Leaves through the Compensatory Leave Request document. It is necessary that the dates should be in default Holiday List and also that the Employee should have their attendance marked Present. 
 
 > **Note:** Only Leave Types which are marked are _Is Compensatory_ can be selected in the Compensatory Leave Request.

To access Compensatory Leave Request, go to:

> Home > Human Resources > Leaves > Compensatory Leave Request 


## 1. Prerequisites

Before creating a Compensatory Leave Request, it is necessary to create the following documents:

* [Employee](/docs/user/manual/en/human-resources/employee)
* [Leave Period](/docs/user/manual/en/human-resources/leave-period)
* [Leave Type](/docs/user/manual/en/human-resources/leave-type)
* [Leave Policy](/docs/user/manual/en/human-resources/leave-policy)
* [Leave Allocation](/docs/user/manual/en/human-resources/leave-allocation)
* [Holiday List](/docs/user/manual/en/human-resources/holiday-list)
* [Attendance](/docs/user/manual/en/human-resources/attendance)


## 2. How to create a Compensatory Leave Request

1. Go to Compensatory Leave Request list, click on New.
1. Select the Employee ID. Once selected, The Employee Name and Department will get automatically fetched.
1. Select the Leave Type.
1. Select Work From Date and Work End Date. This is the date of the day(s) you have worked on a Holiday.
1. Enter the Reason.
1. Save and Submit.

	<img class="screenshot" alt="Compensatory Leave Request"
	src="{{docs_base_url}}/assets/img/human-resources/compensatory-leave.png">



On submitting a Compensatory Leave Request, ERPNext updates the Leave Allocation record for the Compensatory leave type,allowing the Employee to apply for leaves of this type later on depending upon the number of leaves left.


## 3. Related Topics

1. [Leave Application](/docs/user/manual/en/human-resources/leave-application)
1. [Leave Encashment](/docs/user/manual/en/human-resources/leave-encashment)
1. [Leave Block List](/docs/user/manual/en/human-resources/leave-block-list)

