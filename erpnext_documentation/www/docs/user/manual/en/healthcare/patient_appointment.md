<!-- add-breadcrumbs -->
# Patient Appointment

ERPNext Healthcare allows you to book Patient Appointments for any date and alert patients via Email or SMS. You can easily organize appointments for each Practitioner based on their availability schedules.

<!-- <img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment_calendar.png"> -->

To create a Patient Appointment, go to:

> Home > Healthcare > Consultation > Patient Appointment


## 1. Prerequisites

Before creating a Patient Appointment, these need to be created first:

* [Patient](/docs/user/manual/en/Healthcare/patient)
* [Healthcare Practitioner](/docs/user/manual/en/Healthcare/healthcare_practitioner)
* [Practitioner Schedule](/docs/user/manual/en/Healthcare/practitioner_schedule)

You can book appointments for a registered Patient by searching for Patient by Patient ID, Name, Email or Mobile number. It is also possible to register a new Patient from the Appointment screen itself by selecting "Create a new Patient" in the Patient field.

  <img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/patient_appointment_link.png">

## 2. How to Create a Patient Appointment

1. Go to Patient Appointment list, click on New.
2. Select the [Patient](/docs/user/manual/en/Healthcare/Patient) for which you want to set up an Appointment. The Patient Name, Gender and Patient Age will be auto-fetched on selecting the Patient. If the patient is an Inpatient (Admitted) then the Inpatient Record will also be auto-fetched for them.
3. You can optionally select the [Service Unit](/docs/user/manual/en/Healthcare/healthcare_service_unit) where you would want to schedule the appointment. In that case, it will be marked as "Occupied" for the duration of the Appointment.
4. If you need to book Appointment for Clinical Procedure select a [Clinical Procedure Template](/docs/user/manual/en/Healthcare/clinical_procedure_template). If you want to select a Clinical Procedure which has been prescribed for the patient in the previous Patient Encounter click on "Get Prescribed Clinical Procedures" button to select from a list of Clinical Procedures that are prescribed for the selected Patient.
5. You can optionally select the "Appointment Type" and the "Duration (in minutes)". Note that, selecting the "Appointment Type" will automatically set the duration of the appointment as configured in the Appointment Type. This will allow you to override the duration of appointments set by the Practitioner Schedule and the time slots will adjust to the next available time automatically.
6. If you have check "Automate Appointment Invoicing" in [Healthcare Settings](/docs/user/manual/en/Healthcare/healthcare_settings), setting the "Mode of Payment" and "Amount" fields in Patient Appointment is mandatory.
7. Then click on the **Check Availability** button. It will allow you to select the Medical Department, Healthcare Practitioner and Date for which the appointment is to be booked. On selecting the details, all the available time slots for the practitioner will be fetched from the [Practitioner Schedule](/docs/user/manual/en/Healthcare/practitioner_schedule) and displayed with status indicators for the selected date. You can select a time slot and hit **Book**.
8. Once booked, the scheduled time of the Appointment and the Service Unit as per the Practitioner and appropriate Status will be set in the document.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/check_availability.png">

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/appointment.png">

## 3. Features

### 3.1 Patient Appointment Calendar

You can click on "Calendar" view from the Patient Appointment list view. Types of Appointments can be differentiated by setting the "Color" field in [Appointment Type](/docs/user/manual/en/Healthcare/appointment_type)

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare-appointments.png">

### 3.2 Appointment Rescheduling

You can reschedule the Patient Appointment by clicking on the Reschedule button in the document and following the same steps.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/reschedule.png">

### 3.3 Managing Schedules

Patient Appointment booking considers any "Approved" Leave Applications for the Practitioner (Employee linked in the master) and does not allow booking Patient Appointments on such days.

While booking it also checks for Appointment Overlaps and restricts the booking for same slots.

### 3.4 Notes and Referrals

In the "More Info" section of Patient Appointment document, user can add **Notes** and also select a **Referring Practitioner** to help track referrals.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/more_info.png">

### 3.5 Out Patient SMS Alerts

Optionally, you can configure [Healthcare Settings](/docs/user/manual/en/Healthcare/healthcare_settings) in ERPNext to automatically send an SMS alert to the Patients about the booking confirmation via "Out Patient SMS Alerts".

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/outpatient_sms_alert.png">

### 3.6 Automate Appointment Invoicing
ERPNext Healthcare automatically creates a Sales Invoice as soon as you book a Patient Appointment. To enable this, you can check "Automate Appointment Invoicing" in Healthcare Settings.

If enabled, the Patient Appointment will prompt you to select the **Mode of Payment** and enter the **Amount** collected as the Consultation Charge.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/automate_invoicing.png">

> Note: If you have not enabled this, you can always use **Get Items From > Healthcare Services** in Sales Invoice

### 3.7 Status Indications

Status indicates the state of the Patient Appointment. The various Statuses are:

- **Scheduled**: When the Patient Appointment has not yet started but scheduled on a future Date.
- **Open**: When the Patient Appointment has been scheduled for today.
- **Closed**: When a Patient Encounter or Clinical Procedure has been created for the Patient Appointment.
- **Expired**: When the Appointment date has passed and no Patient Encounter or Clinical Procedure has been created against it.
- **Cancelled**: When the Appointment is Cancelled.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/status.png">


## 4. Actions
  * Vital Signs: "Create > Vital Signs" button will take you to the new Vital Signs screen to record the vitals of the Patient.

  * Encounter: From the Appointment screen you can directly create and record the "Patient Encounter" to record the details of the visit.

  * View "Patient Medical History".

> Note: User should have appropriate privileges (User Role) to view the buttons

## 5. Related Topics
1. [Patient](/docs/user/manual/en/Healthcare/patient)
1. [Practitioner Schedule](/docs/user/manual/en/Healthcare/practitioner_schedule)
1. [Healthcare Practitioner](/docs/user/manual/en/Healthcare/healthcare_practitioner)
1. [Healthcare Service Unit](/docs/user/manual/en/Healthcare/healthcare_service_unit)
1. [Patient Encounter](/docs/user/manual/en/Healthcare/patient_encounter)
1. [Clinical Procedure](/docs/user/manual/en/Healthcare/clinical_procedure)
1. [Vital Sign](/docs/user/manual/en/Healthcare/vital_signs)

{next}
