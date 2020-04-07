<!-- add-breadcrumbs -->

# Fee Validity

Many healthcare facilities do not charge for follow up consultations within a time period after the first visit. You can configure the number of free follow ups allowed as well as the time period for free consultations in Healthcare Settings. This will create a Fee Validity document.

## 1. How to Enable Free Follow Up:

To enable free follow-ups go to:

> Home > Healthcare > Settings > Healthcare Settings

- Check "Enable Free Follow Ups".
- Enter the "Number of Patient Encounters in Valid Days".
- Enter "Valid number of days"

For example, as shown below, a patient can have 3 free follow-ups within 30 days:

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/fee_validity_settings.png">

After this is configured, as soon as you create an Appointment for a new patient, a Fee Validity document will be created.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/fee_validity.png">

This Fee Validity document will be updated with every appointment:

- **Status**: Status is set as _Pending_ till the number of free appointments are completed and the appointment dates are within the "Valid Till" deadline. Once all free appointments have been created the status is updated to _Completed_
- **Max number of visits**: The maximum number of free visits allowed.
- **Visited**: The number of free visits completed.
- **Start Date**: The first free appointment's date.
- **Valid Till**: The last date of Fee Validity. This is calculated as _Start Date + Valid Number of Days_ (from Healthcare Settings).
- **Reference Appointments**: Links to all the appointments covered under the Fee Validity document.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/fee_validity_completed.png">

## 2. Related Topics

1. [Patient Appointment](/docs/user/manual/en/Healthcare/patient_appointment)
1. [Patient](/docs/user/manual/en/Healthcare/patient)
1. [Healthcare Settings](/docs/user/manual/en/Healthcare/healthcare_settings)

{next}
