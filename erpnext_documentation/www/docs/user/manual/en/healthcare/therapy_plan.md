<!-- add-breadcrumbs -->

# Therapy Plan

> Introduced in Version 13

A Therapy Plan lists all the therapies required for the Patient along with the number of sessions which will be conducted for each therapy. It also keeps a track of the progress as per the number of sessions completed.

To create a Therapy Plan, go to:

> Home > Healthcare > Rehabilitation and Physiotherapy > Therapy Plan

## 1. How to Create a Therapy Type

1. Go to Therapy Plan list, click on New.
2. Select the Naming Series.
3. Select the Patient.
4. Select the Start Date for the Plan.
5. In order to add therapies to the plan, click on **Add Row** button in the child table. Select the Therapy Type and set the number of sessions required to complete it.
6. Save.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/therapy-plan.png">

## 2. Features

### 2.1 Automatic creation of Therapy Plan from Patient Encounter

You can prescribe therapies in Patient Encounter and a Therapy Plan will be created automatically on submission of Patient Encounter.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/therapy-encounter.jpg">

### 2.2 Create and Track Therapy Sessions

You can create Therapy Session from the Therapy Plan. It will give you options based on the Therapy Types prescribed in the current plan.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/create-therapy-session.png">

Once the Therapy Session is submitted, the count for _Sessions Completed_ for that Therapy is automatically updated in the Therapy Plan.

## 3. Related Topics
1. [Therapy Type](/docs/user/manual/en/healthcare/therapy_type)
1. [Therapy Session](/docs/user/manual/en/healthcare/therapy_session)
1. [Patient Encounter](/docs/user/manual/en/healthcare/patient_encounter)

{next}
