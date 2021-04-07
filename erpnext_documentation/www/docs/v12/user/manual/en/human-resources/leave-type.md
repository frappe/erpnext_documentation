# Leave Type

**Leave Type refers to the types of leaves allocated to an Employee which they can use while making Leave Applications.**


You can create any number of Leave Types based on your company’s requirements.

To access Leave Type, go to:

> Home > Human Resources > Leaves > Leave Type

## 1. How to create a Leave Type

1. Go to Leave Type list, click on New.
1. Enter Leave Type Name.
1. Enter Max Leaves Allowed, Applicable After (Working Days), Maximum Continuous Days Applicable (optional).
1. Save.

    <img class="screenshot" alt="New Leave Type"
    src="{{docs_base_url}}/v12/assets/img/human-resources/new-leave-type.png">

Below is a detailed explanation of all the fields and checkboxes in Leave Type.

* **Max Leaves Allowed:** This field allows you to set the maximum number of the annual allocation of this Leave Type while creating the Leave Policy.

* **Applicable After (Working Days):** Enter the minimum number of working days here. Only the employees who have worked for this number of days or more will be allowed to apply for this particular leave type. Any other leaves (such as Casual Leave, Sick Leave.etc.) availed by the Employees after their joining date will also be considered while calculating working days of the Employee.

* **Maximum Continuous Days Applicable:** It refers to the maximum number of days this particular Leave Type can be availed at a stretch. If an employee exceeds the maximum number of days, their extended leave will be considered as ‘Leave Without Pay'.

* **Is Carry Forward:** If checked, the balance leaves of this Leave Type will be carried forward to the next allocation period.

* **Is Leave Without Pay:** This ensures that the Leave Type will be treated as leaves without pay and salary will get deducted for this Leave Type.

* **Is Optional:** Optional Leaves are holidays that Employees can choose to avail from a list of holidays published by the company. The Holiday List for Optional Leaves can have any number of holidays, but you can restrict the number of such leaves by setting the Max Days Leave Allowed field.

* **Allow Negative Balance:** If checked, the system will always allow to apply and approve [Leave Applications](/docs/user/manual/en/human-resources/leave-application) for the Leave Type, even if there is no leave balance.

* **Include holidays within leaves as leaves:** Check this option if you wish to count holidays within leaves as a ‘leave’. For example, if an Employee has applied for leave on Friday and Monday, and Saturday and Sunday are weekly offs, if the 'Include holidays within leaves as leaves' checkbox for the Leave Type is checked, the system will consider Saturday as Sunday as leaves too. Such holidays will be deducted from the total number of leaves.

* **Is Compensatory:** Compensatory leaves are leaves granted for working overtime or on holidays, normally compensated as an encashable leave. You can check this option to mark the Leave Type as compensatory. An Employee can request for compensatory leaves using [Compensatory Leave Request](/docs/user/manual/en/human-resources/compensatory-leave-request).

> Introduced in version 13

* **Is Partially Paid Leaves:** This checkbox ensures that Leave Type will be treated as partially paid and some part of daily earnings will be paid through salary slip. If this checkbox is enabled then a field "Fraction of Daily Salary Per Leave" appears where you can define the fraction of daily salary paid on the partial leave day.

    <img class="screenshot" alt="New Leave Type"
    src="{{docs_base_url}}/v12/assets/img/human-resources/is-partially-paid-leaves.png">

> **Note:** The Leave Type can be either Leave Without pay or Partially Paid.

## 2. Features

### 2.1 Leave Encashment

It is possible that Employees can receive cash from their Employer for unused leaves granted to them in a Leave Period. Not all Leave Types need to be encashable, so, you should set "Allow Encashment" for only those Leave Types which are encashable.

> **Note:** Leave encashment is allowed only in the last month of the Leave Period.

<img class="screenshot" alt="Leave Encashment"
        src="{{docs_base_url}}/v12/assets/img/human-resources/leave-encashment.png">

**Encashment Threshold Days:**  This field indicates the number of leave days the Employees won't be able to encash. Above the mentioned days, the Employee is eligible to encash leaves.

For example, if there are 10 leaves of a particular Leave Type which is encashable, and the Employee has 8 leaves left. If Encashment Threshold Days = 5, the Employee is given encashment of only 8 - 5 = 3 leaves.

**Earning Component:** This field allows you to specify the Salary Component that will be encashed to Employees as a part of their Salary in the Salary Slip.

> **Note:** On submitting a [Leave Encashment](/docs/user/manual/en/human-resources/leave-encashment) for an Employee, ERPNext automatically creates an [Additional Salary](/docs/user/manual/en/human-resources/additional-salary) which will get added to the Salary Slip of the Employee when processing the next payroll.

### 2.2 Earned Leave

Earned Leaves are leaves earned by an Employee after working with the company for a certain amount of time. Checking "Is Earned Leave" will allot leaves pro-rata basis by automatically updating Leave Allocation for leaves of this type at intervals set by 'Earned Leave Frequency'.


For example, an Employee is allotted 24 Privilege Leaves in a year, wherein the Privilege Leave is set as Earned Leave with Monthly allotment. In this case, the Employee will earn 2 (24 leaves/12 months) Privilege Leaves at the end of every month. The leave allotment process (background job) will only allot leaves considering the max leaves for the leave type and will round to 'Rounding' for fractions.

<img class="screenshot" alt="Earned Leave"
        src="{{docs_base_url}}/v12/assets/img/human-resources/earned-leave.png">

> **Note:** The initial allocation of this Leave Tye will be 0. Leaves will be updated at the end of the Month (or as per the 'Earned Leave Frequency' set).

### 2.3 Default Leave Types

There are some pre-loaded Leave Types in the system, as below:

- **Leave Without Pay:** You can avail these leaves for different purposes, such as extended medical issues, educational purposes, or unavoidable personal reasons. The 'Leave Without Pay' checkbox for this Leave Type is checked by default. The employee does not get paid for such leaves.
- **Privilege leave:** These are like earned leaves that can be availed for travel, family vacation, and so on.
- **Sick leave:** You can avail of these leaves if you are unwell.
- **Compensatory off:** These are compensatory leaves allotted to employees for overtime work. The 'Is Compensatory' checkbox for this Leave Type is checked by default.
- **Casual leave:** You can avail of this leave to take care of urgent and unseen matters.

## 3. Related Topics

1. [Leave Period](/docs/user/manual/en/human-resources/leave-period)
1. [Leave Policy](/docs/user/manual/en/human-resources/leave-policy)
1. [Leave Allocation](/docs/user/manual/en/human-resources/leave-allocation)
1. [Leave Application](/docs/user/manual/en/human-resources/leave-application)
1. [Compensatory Leave Request](/docs/user/manual/en/human-resources/compensatory-leave-request)
1. [Leave Encashment](/docs/user/manual/en/human-resources/leave-encashment)

