<!-- add-breadcrumbs -->
# Inpatient Medication Order

**An Inpatient Medication Order (IPMO) is created to make the nursing process easier. When patients are admitted to the hospital, there are medications that need to be provided to them according to the prescribed schedule. An Inpatient Medication Order is created to prescribe the medications to the admitted patient with the service unit information, the drug, dosage, dosage form, and the date and time when the drug has to be consumed.**

To access the Inpatient Medication Order list, go to:

> Home > Healthcare > Inpatient > Inpatient Medication Order

## 1. Prerequisites

Before creating an Inpatient Medication Order, you need to create the following records first:

* [Patient](/docs/v13/user/manual/en/healthcare/patient)
* [Inpatient Record](/docs/v13/user/manual/en/healthcare/inpatient_record)

## 2. How to Create an Inpatient Medication Order

You can create an Inpatient Medication Order in two ways.

### 2.1 Manual creation

1. Go to Inpatient Medication Order list view and click on New.
2. Select the Patient. The patient list is filtered to only have inpatients as options here.
3. Optionally select the Healthcare Practitioner.
4. Set the Start Date for the order. The schedule for the prescribed drugs will be created starting from this date.
5. In the Medication Orders table, there is an **Add Medication Orders** button. Click on the button. A dialog box will be shown to fill up the prescription details.
6. Select the drug (item), dosage, period, and dosage form. Then click on **Add**.
7. Detailed schedule entries for the order beginning from the Start Date are added to the table. Close the dialog.
8. Save and Submit. The End Date will be set automatically based on the prescription duration.
9. You can see the Total Orders and Completed Orders in the Other Details section.

<img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/v13/assets/img/healthcare/ipmo-manual.gif">

### 2.2 IPMO from Patient Encounter

1. After creating a Patient Encounter for an inpatient, with drugs prescribed in the Drug Prescription table, you can see an option for creating Inpatient Medication Order under **Create > Inpatient Medication Order**.
2. You can use this button to create the IPMO. IPMO with an expanded view of the schedule will be created. Save and Submit.

<img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/v13/assets/img/healthcare/ipmo-pe.gif">

### 2.3 Statuses

The statuses for IPMO are governed by the total completed order entries. The order entries are marked as completed when an [Inpatient Medication Entry](/docs/v13/user/manual/en/healthcare/inpatient_medication_entry) is created against that order entry.

* **Draft**: A draft is saved but yet to be submitted to the system.
* **Pending**: No order entry in the Medication Orders table has been completed.
* **In Progress**: Some order entries in the Medication Orders table have been completed.
* **Completed**: All order entries in the Medication Orders table have been completed.
* **Cancelled**: The Inpatient Medication Order has been cancelled.

<img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/v13/assets/img/healthcare/ipmo-status.png">

## 3. Related Topics

1. [Inpatient Medication Entry](/docs/v13/user/manual/en/healthcare/inpatient_medication_entry)
1. [Patient Encounter](/docs/v13/user/manual/en/healthcare/patient_encounter)

{next}
