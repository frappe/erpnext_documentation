# Appointment

```
---
title: Appointment
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Appointment Schedulling for CRM in ERPNext
 keywords: Appointment Schedulling , CRM, frappe, erpnext new features, erp, open source erp, free erp, security
---
```

**An appointment is a prearranged meeting between a lead and an employee.**

Appointment document type can be used to schedule and manage interaction with a lead or opportunity. 

To access Appointment list, go to:
> Home > CRM > Appointment 

## 1. Prerequisites

1. [Appointment Booking Settings](/docs/user/manual/en/CRM/appointment_booking_settings)
2. Holiday List
3. Employee
4. Lead
5. Email

## 2. How to create an Appointment

This section will go over how to create an appointment

1. Go to Appointment list, click on New
2. Select scheduled time of the appointment
3. Enter customer details
4. In linked documents, if you have already created a lead for the customer you can set it here. Otherwise the system will automatically create a new lead with the customer details from previous step.

![New Appointment](/docs/assets/img/crm/new-appointment.png)
### 2.1 Creating appointments via website

Your customers/leads can create appointment using the webpage `yoursitename.com/book_appointment`. 

![Appointment Webform](/docs/assets/img/crm/appointment-webform.png)
![Appointment Details](/docs/assets/img/crm/appointment-details.png)

It'll match the customer email with leads in the system and if one is found it is linked with the document.
If no lead is found the appointment is marked as "Unverified" and an email is sent to the customer to confirm their email

## 3. Features

### 3.1 Autoassign

Appointments are automatically assigned to employees as per the settings in Appointment Booking Settings. 

### 3.2 Email confirmation

If there is no matching lead in your system, an email will be sent to the email address in the appointment to confirm if the email address is valid. Upon confirmation a new Lead will also be created in the system along with the Appointment.