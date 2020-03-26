<!-- add-breadcrumbs -->

> Introduced in Version 13

# Capacity Planning

Capacity planning is the process in which an organization decides whether or not to accept the new orders based on the resources and existing work orders.

Capacity planning has been enabled by default in your account, to know more go to:

> Home > Manufacturing > Settings > Manufacturing Settings

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/capacity_planning_settings.png">

## 1. Prerequisites
Before creating and using a Work Order, it is advised that you create the following first:

* [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials)
* [Operation](/docs/user/manual/en/manufacturing/operation)
* [Workstation](/docs/user/manual/en/manufacturing/workstation)
* [Work Order](/docs/user/manual/en/manufacturing/work-order)

## 2. How Capacity Planning Works in ERPNext
The user has to define the number of days in the "Capacity Planning For" field under manufacturing settings to plan the upcoming work orders. For example, if you have kept the Capacity Planning For 30 days and to make 1 finished good it requires 5 days then on the current date user can only accept the 6 work orders (30/5 = 6). You can take the next Work Order when your [Workstation](/docs/user/manual/en/manufacturing/workstation) gets free.

### 2.1 Create Work Order With Operations
User needs to create the Work Orders with Operations so that the system will track the [Job Card](/docs/user/manual/en/manufacturing/job-card) timings against the Work Order.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/work_order_with_operations.png">

Once the user submits the Work Order, system will generate the Job Card with the available Workstation's time details. If 'Allow Overtime' is disabled in Manufacturing Settings then the system schedules the job as per the timings defined in the Workstation. If "Allow Production on Holidays" is disabled then the system schedules job only on working days.

### 2.2 Workstation's Production Capacity

In the Workstation, the user can set the 'Production Capacity'. This is the number of Operations the system will allow you work on in this Workstation. For example, if a certain Workstation can handle 10 operations at the same time, enter the 'Production Capacity' as 10.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/work_station_capacity.png">

### 2.3 Job Card With Timing
The system will auto-create the Job Card with timing against each operation based upon the time required to complete that operation and Workstation's availability. The user has to set the planned start date and based on the operation time, system calculates the planned end date.

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/job_card_timing.png">

### 2.4 Work Order Planned Start Date and End Date
Based on the planned start date and end date, users can calculate the capacity of their work stations. Also, they can track the status of the work order using the [Calendar](/docs/user/manual/en/using-erpnext/calendar).

To view calendar, goto:

> Work Order List > Calendar > Default

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/work_order_calendar.png">

### 2.5 Capacity Planning Error
If the Production Capacity days is less than time required to complete the operation then system throws a capacity planning error. In this case, user has to increase the number under "Production Capacity" days in the Manufacturing Settings or reduce the number of finished goods as per the capacity of the Workstations

<img class="screenshot" alt="Work Order" src="{{docs_base_url}}/assets/img/manufacturing/capacity_planning_error.png">
