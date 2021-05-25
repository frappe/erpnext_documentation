<!-- add-breadcrumbs -->

# Therapy Type

> Introduced in Version 13

As therapists, you might be prescribing a number of different therapies for a patient right from Intensive Upper Limb Training to Functional Mobility and so on. Every therapy might have a set of exercises. ERPNext helps you templatize the therapies using the "Therapy Type" DocType. With this, you can create and link therapies to Healthcare Service Units, add standard rates and Item details for billing, and also add exercises according to Body Parts.

To create an Exercise Type, go to:

> Home > Healthcare > Rehabilitation and Physiotherapy > Therapy Type

## 1. How to Create a Therapy Type

1. Go to Therapy Type list, click on New.
2. Enter a unique Therapy Name.
3. Enter the Item details such as Item Code, Item Name, Item Group and optionally some description.
4. Check "Is Billable" if this Therapy Type will be billed and enter the rate for one therapy session.
5. You can optionally add the default duration for one therapy session which will be used while booking an appointment for it.
6. You can also add the Healthcare Service Unit and the Medical Department for the Therapy Type.
7. Save.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/therapy-type.png">

## 2. Features

### 2.1 Add Exercises According to Body Parts

Many times, you might need to prescribe exercises that are specific to the affected body parts for Patients. You can easily add these Body Parts in the _Therapy For_ field and click on *Add Exercises* to add the Exercise Types for those body parts. For that, you will have to link Exercise Type to Body Parts in the Exercise Type document.

For example:

- Exercise "Wall Pushups" is for Hand, Muscles and Joints.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/exercise-1.png">

- Exercise "Sit to Stand" is for Legs and Core.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/exercise-2.png">

- Exercise "Thera-band Upper Body" is for Muscles, Joints, Back, Legs.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/exercise-3.png">

Then while creating the Therapy Type template, you can select the body parts in the "Therapy For" field and exercises for those Body Parts will be added to the Exercise table.

<img class="screenshot" src="{{docs_base_url}}/v13/assets/img/healthcare/add-exercises.gif">

### 2.2 Disable Therapy Types

You can also disable some Therapy Types if you are not conducting sessions for them. For example, your Physiotherapy Unit is under renovation and some Healthcare Service Units like the Aquatic Therapy pool are not available, then you can set the document as disabled and it will be filtered out while booking appointments or prescribing therapies in Patient Encounter, etc.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/therapy-disabled.png">

### 2.3 Change Item Code

You can also change the Item Code which will be used for billing from the Therapy Type screen itself. Click on **Change Item Code** button, enter the new Item Code and click "Change Item Code" in the dialog. The Item will be renamed.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/therapy-change-item-code.png">

### 2.4 Prescribe Therapies in Patient Encounter

You can prescribe therapies in Patient Encounter and a Therapy Plan will be created automatically on submit.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/therapy-encounter.jpg">

### 2.5 Book Appointment for Therapy Type

For booking Patient Appointment for any Therapy Type, select the therapy in _Therapy_ field. You can also use the **Get Prescribed Therapies** button to fetch all therapies prescribed for that Patient in the previous Patient Encounter.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/v13/assets/img/healthcare/therapy-appointment.png">

## 3. Related Topics
1. [Exercise Type](/docs/v13/user/manual/en/healthcare/exercise_type)
1. [Therapy Plan](/docs/v13/user/manual/en/healthcare/therapy_plan)
1. [Therapy Session](/docs/v13/user/manual/en/healthcare/therapy_session)
1. [Patient Appointment](/docs/v13/user/manual/en/healthcare/patient_appointment)
1. [Patient Encounter](/docs/v13/user/manual/en/healthcare/patient_encounter)

{next}
