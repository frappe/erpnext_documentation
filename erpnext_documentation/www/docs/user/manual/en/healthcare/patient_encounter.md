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

You can also create and record encounter details for a patient from Patient Appointment, the Patient Encounter or the Patient master documents by using the "Create > Patient Encounter" button.
If you are creating a Patient Encounter manually, you can search for a Patient by name, email, phone number etc.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/patient_encounter_1.png">

## 2. Features

### 2.1 Medical Coding

You can also attach one or more Medical Codes to designate the Diagnosis in the Medical Coding Section. You will have to select the Medical Code Standard with which you wish to encode the diagnosis and then select the Code by searching the Code itself or the Code Description.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_4.png">

### 2.2 Medication

You can prescribe medicines in the Medication section by selecting the drug codes (Stock Item) and appropriate dosages. If you are not managing Stock, and Items are not configured, you can simply enter the Medicine name and strength in the Strength field which will be printed. You can optionally add a comment in the Medication table entry and select a Dosage Form (Tablet, Syrup).

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_medication.png">

If you maintain stock, Inventory for medicines can be managed using the Stocks Module:

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare-inventory.png">

### 2.3 Lab Tests (Investigations)

In the Investigations section, you can prescribe Lab Tests for the Patient. If you have Lab Test Templates configured, you can select from the list and add comments optionally.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_investigation.png">

Lab Tests can be configured to be created automatically on Sales Invoice submission by checking _Create Lab Test(s) on Sales Invoice Submission_ in [Healthcare Settings](/docs/user/manual/en/healthcare/healthcare_settings).

### 2.4 Clinical Procedures

You can also prescribe a Clinical Procedure to be performed for the Patient in the Procedures section. Select the Clinical Procedure Template and optionally assign a date for conducting the Procedure.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/encounter_procedures.png">

### 2.5 Billing and Prescriptions

The Pharmacy (Sales / Accounts) User can fetch medication and investigation (Lab Test) orders from Patient Encounter using the _Get items from > Prescription_ in Sales Invoice.

Clinical Procedure orders can be fetched using the "Get Prescribed Clinical Procedures" button while booking  Appointment for the procedure. These will then be available for billing via the _Get items from > Healthcare Services_.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/prescription.png">

## 3. Actions

After you have completed filling up all the necessary sections, you can Submit the document. The Action buttons will be visible only after submission.

  * Vital Signs: _Create > Vital Signs_ button will take you to the new Vital Signs screen to record the vitals of the Patient.

  * Medical Record: _Create > Medical Record_ button will take you to the new Medical Record screen to record details. You can also attach some report to the record.

  * Clinical Procedure: Using _Create > Clinical Procedure_ button you can create a Clinical Procedure.

  * Patient History: _View > Patient History_

  * Schedule Admission: You can Schedule Admission using this button. This will create an Inpatient Record.

> Note: User should have appropriate privileges (User Role) to view the buttons

## 4. Related Topics

1. [Patient Appointment](/docs/user/manual/en/Healthcare/patient_appointment)
1. [Clinical Procedure Template](/docs/user/manual/en/Healthcare/clinical_procedure_template)
1. [Lab Test Template](/docs/user/manual/en/Healthcare/lab_test_template)

{next}