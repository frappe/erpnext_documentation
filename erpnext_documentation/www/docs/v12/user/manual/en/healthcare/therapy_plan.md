<!-- add-breadcrumbs -->

# Therapy Plan

> Introduced in Version 13

A Therapy Plan lists all the therapies required for the Patient along with the number of sessions which will be conducted for each therapy. It also keeps a track of the progress as per the number of sessions completed.

To create a Therapy Plan, go to:

> Home > Healthcare > Rehabilitation and Physiotherapy > Therapy Plan

## 1. How to Create a Therapy Type

## 1.1 Therapy Plan for billing Therapy Sessions individually

1. Go to Therapy Plan list, click on New.
2. Select the Naming Series.
3. Select the Patient.
4. Select the Start Date for the Plan.
5. In order to add therapies to the plan, click on **Add Row** button in the child table. Select the Therapy Type and set the number of sessions required to complete it.
6. Save.

<img class="screenshot" alt=Therapy Plan" src="{{docs_base_url}}/assets/img/healthcare/therapy-plan.png">

## 1.2 Therapy Plan from Therapy Plan Template

Therapy Plan Templates are used by some healthcare facilities for prescribing therapy plans as packages. In such cases, the number of sessions to be conducted, and the total cost is fixed. The Therapy Plan created using the Therapy Plan Template will not be billed for individual sessions but for the package as a whole.

1. Select the Naming Series.
2. Select the Patient.
3. Set the Start Date for the Therapy Plan.
4. Select the [Therapy Plan Template](/docs/user/manual/en/healthcare/therapy_plan_template) from which you want to create the Plan.
5. The Therapy Types, and No. of Sessions will be fetched automatically.
6. Save.

<img class="screenshot" alt="Therapy Plan from Therapy Template" src="{{docs_base_url}}/assets/img/healthcare/therapy-plan-from-template.gif">

While fetching Healthcare Services for invoicing, the Therapy Plan is only available for billing if the plan is created using a Therapy Plan Template. If the Therapy Plan is not created from a Therapy Plan Template, individual Therapy Sessions are fetched during billing.

<img class="screenshot" alt="Therapy Plan Template Invoice" src="{{docs_base_url}}/assets/img/healthcare/therapy-plan-template-invoice.gif">

## 2. Features

### 2.1 Automatic creation of Therapy Plan from Patient Encounter

You can prescribe therapies in Patient Encounter and a Therapy Plan will be created automatically on submission of Patient Encounter.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/therapy-encounter.jpg">

### 2.2 Create and Track Therapy Sessions

You can create Therapy Session from the Therapy Plan. It will give you options based on the Therapy Types prescribed in the current plan.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/create-therapy-session.png">

Once the Therapy Session is submitted, the count for _Sessions Completed_ for that Therapy is automatically updated in the Therapy Plan.

### 2.3 Create Sales Invoice from Therapy Plan

If the Therapy Plan is created from Therapy Plan Template and is not invoiced yet, it will give you an option to create a Sales Invoice from the Therapy Plan.

<img class="screenshot" alt="Sales Invoice from Therapy Plan" src="{{docs_base_url}}/assets/img/healthcare/sales-invoice-from-therapy-plan.png">

## 3. Related Topics
1. [Therapy Type](/docs/user/manual/en/healthcare/therapy_type)
1. [Therapy Session](/docs/user/manual/en/healthcare/therapy_session)
1. [Patient Encounter](/docs/user/manual/en/healthcare/patient_encounter)

{next}
