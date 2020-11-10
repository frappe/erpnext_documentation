<!-- add-breadcrumbs -->
# Lab Test

**Lab Test allows recording multiple laboratory test details including organism, sensitivity, etc.**

ERPNext Healthcare allows you to manage a clinical laboratory efficiently by allowing you to enter lab tests and print or email test results, manage samples collected, create invoices, etc. You can configure Lab Test Templates for each Test and its result format or create new ones as explained in [Setting Up Laboratory](/docs/user/manual/en/healthcare/setup_laboratory)

Once you have all the necessary Lab Test Templates configured, you can start creating Lab Tests by selecting a Test Template every time you create a Test.

## 1. How to create a Lab Test

To create a Lab Test, go to:

> Home > Healthcare > Laboratory > Lab Test > New Lab Test

1. Set the Naming Series.
2. Select the [Lab Test Template](/docs/user/manual/en/healthcare/lab_test_template). Medical Department will automatically be fetched from the template.
3. Select the Patient. The patient details will be auto-fetched.
4. You can optionally select the Requesting Practitioner and the Lab Technician.
5. Save.
6. After saving all the data configured in the template will be fetched and set in the lab test document.
7. You can change the pre-configured data according to your requirements. Add comments if any, in the Comments section.

    ![Lab Test](/docs/assets/img/healthcare/lab-test.png)

8. As the results get ready, you can enter the details of the results in the Lab Test document. All presets, Normal Values etc. as configured in the Lab Test Template are made available Lab Test for easy data capture.

For example, Grouped Test:
    ![Lab Result](/docs/assets/img/healthcare/lab_test_2.png)

Descriptive Test:
    ![Lab Result](/docs/assets/img/healthcare/lab-result.png)

Components for which _Allow Blank_ is not checked, will throw a validation if left blank on submit.

    ![Lab Result](/docs/assets/img/healthcare/result-mandatory.png)

## 2. Features

### 2.1 Create multiple Lab Tests

It is also possible to use the "Create Multiple" option from the Lab Test list view to create all the lab tests ordered or billed for a patient. You can create multiple lab tests from a previously created Sales Invoice or Patient Encounter.

![Lab Test Multiple](/docs/assets/img/healthcare/lab_test_3.png)

You can select the Patient and then the Encounter or Invoice from which you need to pull the tests without having to open the Encounter/Sales Invoice to look up the orders.

![Lab Test](/docs/assets/img/healthcare/patient-encounter-lab-tests-1.png)

The tests prescribed in the Investigations section of that Patient Encounter would be pulled.

![Lab Test](/docs/assets/img/healthcare/patient-encounter-lab-tests.png)

![Lab Test](/docs/assets/img/healthcare/patient-encounter-lab-tests-2.png)

In the case of Sales Invoice, the items (Lab Test Template items) billed in the invoice will be pulled to create Lab Tests.

### 2.2 Automatic Sample Collection document creation

If the Lab Test Template has sample collection configured, then on creating the Lab Test, sample collection document(s) will be created automatically. To create Sample Collection documents for every Lab Test, enable _Create Sample Collection document for Lab Test_ option in Healthcare Settings and configure samples in the Lab Test Template.

![Lab Sample Collection](/docs/assets/img/healthcare/lab-sample-collection.png)

### 2.3 Automatic Lab Test creation on Sales Invoice submission

ERPNext Healthcare also allows creation of Lab Tests automatically when any lab tests are billed (via Sales Invoice). To configure this enable _Create Lab Test(s) on Sales Invoice Submission_ option in [Healthcare Settings](/docs/user/manual/en/healthcare/healthcare_settings).

### 2.4 Organism Test Results

Organisms are an optional entry for descriptive lab tests. You can select the organism, set the colony population and select the colony UOM.

### 2.5 Sensitivity Results

In the case of Descriptive lab tests, if _Sensitivity_ option is enabled in the template you can enter the sensitivity results of the sample against various antibiotics in the Sensitivity child table. The Sensitivity and Antibiotic masters are pre-configured in ERPNext. You can extend or modify them as per your needs.

![Sensitivity](/docs/assets/img/healthcare/sensitivity.png)

### 2.6 Format Test Result

ERPNext also allows you to format test result for each test/event in your result.

![Format Test Result](/docs/assets/img/healthcare/format-result-value.png)

![Formatted Result](/docs/assets/img/healthcare/formatted-result.png)

### 2.7 Laboratory SMS Alerts

You can configure the messages for sending SMS alerts to patients whenever the lab test results are ready in the [Healthcare Settings](/docs/user/manual/en/healthcare/healthcare_settings). For this, you must setup [SMS Settings](/docs/user/manual/en/setting-up/sms-setting) first.

## 3. Related Topics

1. [Lab Test](/docs/user/manual/en/healthcare/lab_test)
1. [Sample Collection](/docs/user/manual/en/healthcare/sample_collection)

{next}
