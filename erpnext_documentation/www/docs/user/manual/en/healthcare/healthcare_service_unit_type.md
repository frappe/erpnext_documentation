<!-- add-breadcrumbs -->

# Healthcare Service Unit Type

You can define the standard properties of [Healthcare Service Unit](/docs/user/manual/en/healthcare/healthcare_service_unit) using the Healthcare Service Unit Type. By configuring various types of service units in your facility with respective rates and other properties, you can easily create multiple Healthcare Service Units by merely selecting the type. Healthcare Service Unit Type is a generic type. For example, "Operation Theatre" can be a Healthcare Service Unit Type and Neurology-OT, Procedure-Room-1, etc. could be Healthcare Service Units.

## 1. How to Create a Healthcare Service Unit Type

To create a Healthcare Service Unit Type, go to:

> Home > Healthcare > Masters > Healthcare Service Unit Type

- **Service Unit Type**: Enter a unique name for the Service Unit Type.

Now there are two options:

- **Allow Appointments**: Check this if the unit type is for Out Patient facility.
- **Inpatient Occupancy**: Check this if the unit type is for Inpatient facility.

But "Consulting Rooms" can only allow Appointments and

The following option shows up if you check "Allow Appointments":

- **Allow Overlap**: Check this if the unit type can be used by more than one patient or for more than one appointment at once.

For example, Physical Activity Centres will allow Appointments with overlap:

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_service_unit_type_1.png">

However, Consultation rooms will only allow Appointments without overlap:

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_service_unit_type_2.png">

The following option shows up if you check "Inpatient Occupancy":

- **Is Billable**: Check this if the unit type for IPD is billable like Hospital Beds.

For example, Operation Theatres will have Inpatient Occupancy which will be billed. If you check "Inpatient Occupancy" and "Is Billable" the system asks for Item Details to create an item for the Service Unit Type which will be used for billing:

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_service_unit_type.png">

The item is automatically created and linked to the document on save.

If the Healthcare Service Unit Type is not being used, you can disable it. Disabling will not allow selecting the item created for it while billing.

If you want to change the Item Code of the item created for the billable Healthcare Service Unit Type, click on "Change Item Code" button.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/healthcare_service_unit_type_3.png">

## 2. Related Topics
1. [Healthcare Service Unit](/docs/user/manual/en/healthcare/healthcare_service_unit)

{next}
