<!-- add-breadcrumbs -->

# Patient History Settings

> Introduced in Version 13

Using Patient History Settings, you can configure the doctypes and fields you want in the Patient Medical Record and Patient History.

To update the Patient History Settings, go to:

> Home > Healthcare > Settings > Patient History Settings

## 1. Standard Document Types

The following Standard Document Types are pre-configured in Patient History Settings.

- [Patient Encounter](/docs/v13/user/manual/en/healthcare/patient_encounter)
- [Clinical Procedure](/docs/v13/user/manual/en/healthcare/clinical_procedure)
- [Lab Test](/docs/v13/user/manual/en/healthcare/lab_test)
- [Therapy Session](/docs/v13/user/manual/en/healthcare/therapy_session)
- [Vital Signs](/docs/v13/user/manual/en/healthcare/vital_signs)
- [Inpatient Medication Order](/docs/v13/user/manual/en/healthcare/inpatient_medication_order)

You can add or edit all fields you want to record in the Patient Medical Record and Patient History. Click on the **Add/Edit Fields** button against the doctype you want to edit the config for. A dialog will be shown with all the currently configured fields checked. You can then select what all fields (including custom) should be a part of the Patient Medical Record and click on Save. Then save the settings.

Depending upon your selection, a Patient Medical Record with the configured fields and values will be created on document submission and deleted on document cancellation. If you update the document, the corresponding medical record will also be updated.

## 2. Custom Document Types

Similar to the Standard Document Type configuration, you can configure the Custom Document Types in this table.

- Select the Custom DocType
- Enter the fieldname for the date field of the DocType. This will be used while filtering medical records in Patient History according to dates. For example, the date fieldname for Patient Encounter is encounter_date.
- Then, click on **Add / Edit Fields** button to configure the fields.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/patient-history-settings.gif">

## 3. Related Topics

1. [Patient History](/docs/v13/user/manual/en/healthcare/patient_history)

{next}
