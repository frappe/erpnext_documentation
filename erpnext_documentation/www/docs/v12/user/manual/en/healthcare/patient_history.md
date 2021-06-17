<!-- add-breadcrumbs -->
# Patient Medical History

Maintenance of accurate and complete medical records of patients is one of the rudiments for healthcare practitioners and providers. Over and above, the ease at which the information is accessible by a practitioner is critical in rendering effective, high quality care.

ERPNext Healthcare helps you to draw up the medical history of a Patient anytime by quickly searching and selecting the Patient.

To view the Patient History, you can go to:

> Home > Healthcare > Records and History > Patient History

The history of patient interactions is maintained in the Patient Medical Record document type. These records are automatically created on submission of Patient Encounter, Vital Signs, Clinical Procedure, Lab Test, Therapy Session, and Inpatient Medication Order.

From version 13 onwards, you can configure what all document types and fields should be a part of the Patient Medical Record and Patient History using [Patient History Settings](/docs/user/manual/en/healthcare/patient_history_settings).

**View > Patient History** button is available in all the forms which Healthcare Practitioners use so that they can easily switch to the "Patient  History" page to view the patient history.

## 1. Sections

- **Patient Information**: As soon as you select the Patient, all the information from the Patient record is fetched and displayed on the page's sidebar.
- **Patient Vitals**: Based on the Vital Signs captured for the patient over, this section renders charts for visualizing how the Blood Pressure, Respiratory/Pulse Rate, Temperature, and BMI are varying with time. You can click on individual buttons render the required chart.
- **Documents for Patient Interactions**: A timeline of documents fetched from the Patient Medical Records is shown in this section. You can see the doctype name, link to the document, and the date on which the record was created. On load, a summary of each document is shown. You can use the arrow below each document to get a detailed view.
- **Filters**: From version 13 onwards, you can also filter what all doctypes you want to see the interactions of using a multi-select list filter. Using the date range filter you can get the history feed between any two dates.

<img class="screenshot" alt="Patient History" src="{{docs_base_url}}/v12/assets/img/healthcare/patient-history-1.gif">

## 2. Adding Medical Records Manually

Medical Record automatically keeps track of all Complaints, Diagnosis, and other information captured as part of a Patient Encounter, Vital Signs, Lab Investigations, ordered Clinical Procedures, Admissions, etc.

In the Patient document, **Create > Medical Record** will allow you to record notes manually. You can also attach files when doing this, and the Medical Record will display links to the attached file alongside the notes. It's also possible to add Medical Records from the Patient Encounter.

<img class="screenshot" alt="Patient Medical Record" src="{{docs_base_url}}/v12/assets/img/healthcare/medical_record_2.png">

## 3. Related Topics

1. [Patient History Settings](/docs/user/manual/en/healthcare/patient_history_settings)

{next}
