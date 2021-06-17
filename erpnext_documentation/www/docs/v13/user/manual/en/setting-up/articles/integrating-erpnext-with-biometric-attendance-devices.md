---
title: Integrating ERPNext With Biometric Attendance Devices
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: ERPNext has the provision to mark attendance from Check-in and Check-out logs from biometric. There are several possible methods to integrate your biometric device based on the vendor and the available features of your device.
 keywords: frappe, erpnext, erpnext attendance, biometric device integration, human resource, auto attendance
---

<!-- add-breadcrumbs -->
# Integrating ERPNext With Biometric Attendance Devices

The Attendance Punch Logs from the biometric device is a type of Check-in and Check-out log of an employee.

ERPNext has a provision to store these logs in a document called Employee Checkin.

Attendance can then be marked based on the Employee Checkin records and the shift [Auto Attendance Settings](/docs/user/manual/en/human-resources/shift-management#25-auto-attendance-settings) of the employee by using [Auto Attendance](/docs/user/manual/en/human-resources/auto-attendance)

Hence, integrating your Biometric Device --or any access control system that collects IN/OUT--, can be done by the following steps:

  1. [Setting up Auto Attendance to mark attendance from the Employee Checkin](#1-setting-up-auto-attendance-to-mark-attendance-from-the-employee-checkin)
  1. [Populating the Biometric Punch Logs into ERPNext's Employee Checkin](#2-populating-the-biometric-punch-logs-into-erpnexts-employee-checkin)

## 1. Setting up Auto Attendance to mark attendance from the Employee Checkin

Before you import employee's Check-in and Check-out logs into your ERPNext system, you would have to set up the employees and their shifts to be able to generate attendance using the Auto Attendance feature in ERPNext.

Please refer to the following link to set up Auto Attendance: [Set up Auto Attendance](/docs/user/manual/en/human-resources/auto-attendance#steps-to-setup-auto-attendance)

Once you have set up the Employee and assigned shifts to the employees, you are now ready to proceed to the next step.

## 2. Populating the Biometric Punch Logs into ERPNext's Employee Checkin
Depending on your biometric system and its features, there can be a lot of ways you can import the Punch logs into ERPNext:

1. Use ERPNext's Data Import Tool:
    - The simplest possible solution (in terms of implementation complexity) would be to generate an Excel/CSV of the Check-in/Check-out and use the built-in data import tool in ERPNext to periodically import to your Employee Checkin Document
    - Please refer to [ERPNext's Documentation on Data Import Tool](/docs/user/manual/en/setting-up/data/data-import) for more on how to do this.

1. API Integration:
    - You can automate the process of importing the Biometric Punch Logs by integrating it with the available API in ERPNext.
    - This API can be accessed at: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
    - This method requires technical knowledge and you should probably get in touch with your ERPNext implementor or Biometric system vendor.

1. Set up a python script on your computer to integrate ZKTeco or similar devices:
    - This method works only for ZKTeco or similar devices that use the ZKProtocol to communicate over TCP/IP.
    - This script is available at: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
    - Please follow the instructions given in the script page to set it up on your computer.
    - This Script pulls biometric logs from a supported device and uses the API mentioned in the above step to push the data into ERPNext.
