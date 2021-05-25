<!-- add-breadcrumbs -->

# Patient Encounter

ERPNext Healthcare allows you to record every encounter with patients through the Patient Encounter document. You can also create a Patient Encounter based on a previously booked Appointment.

## 1. How to Create a Patient Encounter

To create a Patient Encounter, go to:

> Home > Healthcare > Consultation > Patient Encounter

1. Select a Naming Series for the document.
2. If you select an Appointment, Patient details, Department and Healthcare Practitioner, etc will be fetched automatically.
3. Otherwise, you can separately select a Patient. Patient details will be fetched.
4. Select the Healthcare Practitioner. The Department will be fetched automatically.
5. Set the Encounter Date and Time.
6. Select the Symptoms and Diagnosis in the Encounter Impression section. You can opt to include the captured data in Patient Encounter print by checking "In Print".
7. Save.

You can also create and record encounter details for a patient from Patient Appointment, the Patient Encounter or the Patient master documents by using the **Create > Patient Encounter** button.
If you are creating a Patient Encounter manually, you can search for a Patient by name, email, phone number etc.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/patient_encounter_1.png">

## 2. Features

### 2.1 Medical Coding

You can also attach one or more Medical Codes to designate the Diagnosis in the Medical Coding Section. You will have to select the Medical Code Standard with which you wish to encode the diagnosis and then select the Code by searching the Code itself or the Code Description.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/encounter_4.png">

### 2.2 Medication

You can prescribe medicines in the Medication section by selecting the drug codes (Stock Item) and appropriate dosages. If you are not managing Stock, and Items are not configured, you can simply enter the Medicine name and strength in the Strength field which will be printed. You can optionally add a comment in the Medication table entry and select a Dosage Form (Tablet, Syrup).

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/encounter_medication.png">

If you maintain stock, Inventory for medicines can be managed using the Stocks Module:

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/healthcare-inventory.png">

### 2.3 Lab Tests (Investigations)

In the Investigations section, you can prescribe Lab Tests for the Patient. If you have Lab Test Templates configured, you can select from the list and add comments optionally.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/encounter_investigation.png">

Lab Tests can be configured to be created automatically on Sales Invoice submission by checking _Create Lab Test(s) on Sales Invoice Submission_ in [Healthcare Settings](/docs/v13/user/manual/en/healthcare/healthcare_settings).

### 2.4 Clinical Procedures

You can also prescribe a Clinical Procedure to be performed for the Patient in the Procedures section. Select the Clinical Procedure Template and optionally assign a date for conducting the Procedure.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/encounter_procedures.png">

### 2.5 Therapies

If your Healthcare facility offers Rehabilitation and Physiotherapy services, you can prescribe therapies in the Patient Encounter and a Therapy Plan will be created automatically on submission of Patient Encounter.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/therapy-encounter.jpg">

### 2.6 Billing and Prescriptions

The Pharmacy (Sales / Accounts) User can fetch medication and investigation (Lab Test) orders from Patient Encounter using the **Get items from > Prescription** in Sales Invoice.

Clinical Procedure orders can be fetched using the **Get Prescribed Clinical Procedures** button while booking an Appointment for the procedure. These will then be available for billing via the **Get items from > Healthcare Services**.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/prescription.png">

## 3. Actions

> Note: User should have appropriate privileges (User Role) to view the buttons

After you have completed filling up all the necessary sections, you can Submit the document. The Action buttons will be visible only after submission.

  * Vital Signs: **Create > Vital Signs** button will take you to the new Vital Signs screen to record the vitals of the Patient.

  * Medical Record: **Create > Medical Record** button will take you to the new Medical Record screen to record details. You can also attach some report to the record.

  * Clinical Procedure: Using **Create > Clinical Procedure** button you can create a Clinical Procedure.

  * Patient History: **View > Patient History**.

  * Schedule Admission: You can Schedule Admission using this button. This will create an Inpatient Record.

> This Form has been Changed in Version 13

## 4. Related Topics

1. [Patient Appointment](/docs/v13/user/manual/en/healthcare/patient_appointment)
1. [Clinical Procedure Template](/docs/v13/user/manual/en/healthcare/clinical_procedure_template)

{next}
