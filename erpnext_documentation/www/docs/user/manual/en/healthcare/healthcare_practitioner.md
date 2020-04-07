<!-- add-breadcrumbs -->
# Healthcare Practitioner

Healthcare Practitioners are the doctors, nurses, ward boys, lab technicians, etc. who are serving the hospital unit in one way or another. ERPNext Healthcare allows you to create multiple practitioners and link to a User with appropriate Roles. You can also link a Healthcare Practitioner to an [Employee](/docs/user/manual/en/human-resources/employee) to track Payroll, Attendance or other Human Resource Management activities.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_1.png">

To create a Practitioner, go to,

> Home > Healthcare > Masters > Healthcare Practitioner

## 1. How to Create a Healthcare Practitioner

1. Go to the Healthcare Practitioner list and click on New.
2. Select the Naming Series.
3. Enter basic details like First Name, Last Name, Gender, Mobile number.
4. Optionally, select a Medical Department.
4. Save.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner.png">

## 2. Features

### 2.1 Track Payroll, Attendance, Roles and Permissions

In order to track all Human Resource Management activities for the Practitioner, you need to create and select the [Employee](/docs/user/manual/en/human-resources/employee) in the "Employee" field in practitioner. This will help run [Payroll](/docs/user/manual/en/human-resources/payroll-intro) and also track availability and attendance for booking appointments by setting appropriate [Holiday List](/docs/user/manual/en/human-resources/holiday-list) and [Practitioner Schedule](/docs/user/manual/en/Healthcare/practitioner_schedule). You can then create an ERPNext User linked to the Employee document. This will help track permissions for the Practitioner.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner-employee.png">

> Note: Selecting the Employee field will fetch in all relevant fields as configured in the Employee document to help you easily setup the Practitioner

If the Healthcare Practitioners are not employees in your Healthcare Units you can link User to the Practitioner and assign them the required roles.

### 2.2 Practitioner Availability

You can select multiple [Practitioner Schedule](/docs/user/manual/en/Healthcare/practitioner_schedule) for each practitioner and optionally set a service unit at which the practitioner will be available.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_availability.png">

### 2.3 Healthcare Practitioner Charges

You can select or create the service items for consulting charges and set them in "Out Patient Consulting Charge Item" and "In Patient Consulting Charge Item". These will be fetched in Sales Invoices. You can set the consultation charges which are applicable to the practitioner. If required, you can also select an Income Account for a Physician to book all Consultation charges into separate accounts.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/practitioner_charges.png">

> Note: Make sure that the Items you create for services have "Maintain Stock" and "Include Items in Manufacturing" unchecked since they are service items.

### 2.4 Referring Physicians

You may also want to manage a list of Doctors who refers Patients to your facility. You can manage such data in the Healthcare Practitioner document itself by leaving out the Employee and User links.

### 2.5 Link Multiple Addresses and Contacts

Suppose the Practitioner works at various hospitals, you can link multiple contacts and addresses for that Practitioner.

## 3. Related Topics

1. [Users and Permissions](/docs/user/manual/en/setting-up/users-and-permissions)
2. [Employee](/docs/user/manual/en/human-resources/employee)
3. [Practitioner Schedule](/docs/user/manual/en/Healthcare/practitioner_schedule)

{next}
