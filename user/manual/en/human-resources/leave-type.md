# Leave Type

**Leave Type refers to the types of leaves that an Employee can use while making Leave Applications.** 

To access Leave Type, go to:

> Home > Human Resources > Leaves > Leave Type 

An employee can select a particular Leave Type while requesting for a leave. You can create any number of Leave Types based on your company’s requirement.

## 1. How to create a Leave Type

1. Go to Leave Type list, click on New.
1. Enter Leave Type Name.
1. Enter Max Leaves Allowed, Applicable After (Working Days), Maximum Continuous Days Applicable (optional).
1. Save.

	<img class="screenshot" alt="New Leave Type"
	src="{{docs_base_url}}/assets/img/human-resources/new-leave-type.png">

Below is a detailed explanation of all the fields in Leave Type.

* **Max Leaves Allowed:** This field allows you to set the maximum number of leaves of this Leave Type that Employees can apply within a Leave Period.

* **Applicable After (Working Days):** Employees who have worked with the company for this number of days are only allowed to apply for this Leave Type. Any other leaves availed by the Employees after their joining date is also considered while calculating working days.

* **Maximum Continuous Days Applicable:** It refers to the maximum number of days this particular Leave Type can be availed at a stretch. If an employee exceeds the maximum number of days, their extended leave may be considered as ‘Leave Without Pay'.

* **Is Carry Forward:** If checked, the balance leave will be carried forwarded to the next allocation period.

* **Is Leave Without Pay:** This ensures that the Leave Type will be treated as leaves without pay and salary will get deducted for this Leave Type.

* **Is Optional:** Optional Leaves are holidays which Employees can choose to avail from a list of holidays published by the company. The Holiday List for optional leaves can have any number of holidays but you can restrict the number of such leaves by setting the Max Days Leave Allowed field.

* **Allow Negative Balance:** If checked, system will always allow to approve leave application for the Leave Type, even if there is no leave balance.


* **Include holidays within leaves as leaves:** Check this option if you wish to count holidays within leaves as a ‘leave’. Such holidays will be deducted from the total number of leaves.


* **Is Compensatory:** Compensatory leaves are leaves granted for working overtime or on holidays, normally compensated as an encashable leave. You can check this option to mark the Leave Type as compensatory. An Employee can request for compensatory leaves using [Compensatory Leave Request](/docs/user/manual/en/human-resources/compensatory-leave-request).



## 2. Features

### 2.1 Leave Encashment

It is possible that Employees can receive cash from their Employer for unused leaves granted to them in a Leave Period. Not all Leave Types need to be encashable, so, you should set "Allow Encashment" for Leave Types which are encashable. 

> **Note:** Leave encashment is allowed only in the last month of the Leave Period.

<img class="screenshot" alt="Leave Encashment"
		src="{{docs_base_url}}/assets/img/human-resources/leave-encashment.png">

**Encashment Threshold Days:**  This field indicates the number of leave days the the Employees won't be able to encash. Above the mentioned days, the Employee is eligible to encash leaves. 

For example, if there are 10 leaves of a particular Leave Type which is encashable, and the Employee has 8 leaves left. If Encashment Threshold Days = 5, the Employee is given encashment of ony 8 - 5 = 3 leaves.

**Earning Component:** This field allows you to specify the [Salary Component](/docs/user/manual/en/human-resources/salary-component) that will be encashed to Employees as a part of their Salary in the Salary Slip.

> **Note:** On submitting a [Leave Encashment](/docs/user/manual/en/human-resources/leave-encashment) for an Employee, ERPNext automatically creates an [Additional Salary](/docs/user/manual/en/human-resources/additional-salary) which will get added to the Salary Slip of the Employee when processing the next payroll

### 2.2 Earned Leave

Earned Leaves are leaves earned by an Employee after working with the company for a certain amount of time. Checking "Is Earned Leave" will allot leaves pro rata basis by automatically updating Leave Allocation for leaves of this type at intervals set by 'Earned Leave Frequency'. 


For example, if an Employee earns 2 leaves of Privilege Leaves monthly, ERPNext automatically increments the Leave Allocation for Paid Leave at the end of every month by 2. The leave allotment process (background job) will only allot leaves considering the max leaves for the leave type, and will round to 'Rounding' for fractions.

<img class="screenshot" alt="Earned Leave"
		src="{{docs_base_url}}/assets/img/human-resources/earned-leave.png">

### 2.3 Default Leave Types

There are some pre-loaded Leave Types in the system, as below:

- Leave Without Pay: You can avail these leaves for different purposes, such as, extended medical issues, educational purpose or unavoidable personal reason. Employee does not get paid for such leaves.
- Privilege leave: These are like earned leaves which can be availed for the purpose of travel, family vacation and so on.
- Sick leave: You can avail these leaves if you are unwell.
- Compensatory off: These are compensatory leave allotted to employees for overtime work.
- Casual leave: You can avail this leave to take care of urgent and unseen matters.

## 3. Related Topics

1. [Leave Period](/docs/user/manual/en/human-resources/leave-period)
1. [Leave Policy](/docs/user/manual/en/human-resources/leave-policy)
1. [Leave Allocation](/docs/user/manual/en/human-resources/leave-allocation)
1. [Leave Application](/docs/user/manual/en/human-resources/leave-application)
1. [Compensatory Leave Request](/docs/user/manual/en/human-resources/compensatory-leave-request)
1. [Leave Encashment](/docs/user/manual/en/human-resources/leave-encashment)

