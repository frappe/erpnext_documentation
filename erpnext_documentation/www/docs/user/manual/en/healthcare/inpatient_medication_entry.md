<!-- add-breadcrumbs -->
# Inpatient Medication Entry

**An Inpatient Medication Entry (IPME) is created to process Inpatient Medication Orders in bulk based on some filters and to optionally update stock on dispensing the drugs.**

To access the Inpatient Medication Entry list, go to:

> Home > Healthcare > Inpatient > Inpatient Medication Entry

## 1. Prerequisites

Before creating an Inpatient Medication Entry, you need to create the following records first:

* [Patient](/docs/user/manual/en/healthcare/patient)
* [Inpatient Record](/docs/user/manual/en/healthcare/inpatient_record)
* [Inpatient Medication Order](/docs/user/manual/en/healthcare/inpatient_medication_order)

## 2. How to Create an Inpatient Medication Entry

1. Go to the Inpatient Medication Entry list and click on New.
2. Select the Company.
3. Set the Posting Date.
4. There are various filters available to fetch the pending Inpatient Medication Orders:

    - **Item Code (Drug)**
    - **Assigned To**: You can select the user who is assigned for the Inpatient Medication Order completion.
    - **Patient**
    - **Healthcare Practitioner** who has prescribed the drugs.
    - **Healthcare Service Unit** where you want to dispense the drugs. You can use these filters whenever you are dispensing drugs in a particular HSU like an Isolation Ward, etc.
    - **Date and Time filters**

    <img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/assets/img/healthcare/ime-filters.png">

5. After setting the filters, click on the **Get Pending Medication Orders** button to fetch the pending orders which fall under the selected filters.
6. Optionally, check/uncheck _Update Stock_. If checked, specify the Warehouse from where drugs should be consumed.

    <img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/assets/img/healthcare/ime-stock.png">

### 2.2 On Submission of Inpatient Medication Entry

The corresponding Inpatient Medication Order Entries are marked as completed.

<img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/assets/img/healthcare/imoe-completed.png">

If _Update Stock_ is checked, then stock validations are made and orders are processed to make Stock Entry with references updated against each entry.
You can check the references for Inpatient Medication Entry in the Stock Entry, and in Stock Entry Detail table for the Patient and corresponding Entry.

<img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/assets/img/healthcare/ime-stock-entry.png">

<img class="screenshot" alt="IPMO-PE" src="{{docs_base_url}}/assets/img/healthcare/ime-stock-entry-detail.png">

## 2.3 On Cancellation of Inpatient Medication Entry

The corresponding Stock Entry is cancelled and the linked Inpatient Medication Order Entry is marked as incomplete again.

## 3. Related Topics

1. [Inpatient Medication Order](/docs/user/manual/en/healthcare/inpatient_medication_order)

{next}
