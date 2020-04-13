<!-- add-breadcrumbs -->

# Therapy Session

ERPNext helps you track every session conducted with the Patient in the Therapy Session DocType. You may or may not book an appointment for the session. It helps you map the Patient progess by keeping a track of Targeted Counts, Counts Completed and the Assistance Level required for the Patient to complete each Exercise.

To create an Therapy Session, go to:

> Home > Healthcare > Rehabilitation and Physiotherapy > Therapy Session

## 1. How to Create a Therapy Session

### 1.1 Create Therapy Session document

1. Go to Therapy Session list, click on New.
2. Select the naming series.
3. If a Patient Appointment has been booked for the session, select the Patient Appointment. All other details will automatically be fetched.
4. If no Appointment has been booked, select the Patient.
5. Select the Therapy Type and the Therapy Plan for that Patient. As soon as you select the Therapy Type, the Healthcare Service Unit, Rate, Duration Medical Department and all the Exercises from the template are automatically fetched.
6. If the session is being conducted by some therapist, select the therapist in the Healthcare Practitioner field.
7. You can select a Start Date and Time.
8. Save.
9. You can then increase number of Counts Completed and once a particular exercise has been completed select the Level of Assistance required for that exercise. The count indicators are shown on the dashboard of the document, green indicates completion, orange indicates unreached goals.
10. Once you have recorded the entire session with the counts you can submit the document. The Therapy Plan will then be updated with the number of sessions.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/therapy-session.png">

### 1.2 Create Therapy Session from Patient Appointment

After booking an appointment for a Therapy Type, click on _Create > Therapy Session_ to create a session from Patient Appointment.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/therapy-session-from-appointment.png">

Refer [Therapy Plan](/docs/user/manual/en/healthcare/therapy_plan) to understand creation of Therapy Sessions from Therapy Plan.

## 2. Features

### 2.1 Invoicing Therapy Sessions

In order to invoice Therapy Sessions:

1. You can create a new Sales Invoice.
2. Select the Patient.
3. Click on _Get Items From > Healthcare Services_.
4. The dialog will show you all the unbilled sessions of that particular patient. After selecting the items, the rates for sessions will be fetched automatically from the Therapy Type template.
5. You can also manually add items in the child table for billing.
5. Save and Submit.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/therapy-invoicing.png">

## 3. Related Topics
1. [Therapy Type](/docs/user/manual/en/healthcare/therapy_type)
1. [Therapy Plan](/docs/user/manual/en/healthcare/therapy_plan)
1. [Patient Appointment](/docs/user/manual/en/healthcare/patient_appointment)

{next}
