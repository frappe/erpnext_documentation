<!-- add-breadcrumbs -->
# Sample Collection

It's critical for a Laboratory to manage collected samples and print labels for those samples, automate sample collection, etc.

## 1. How to create a Sample Collection

To create a Sample Collection go to

> Home > Healthcare> Laboratory > Sample Collection > New Sample Collection

1. Enter the name of the Patient. All the patient details will be auto-fetched.
2. Select the Lab Test Sample in the Sample field. You can configure the Lab Test Sample master as per your requirements. The Sample UOM is automatically fetched from the Lab Test Sample doc.
3. Set the Quantity of the sample collected.
4. Select the user who collected the sample in the "Collected By" field.
5. Set the Date and Time of sample collection in the "Collected On" field.
6. Save and Submit.

  ![Sample Collection](/docs/v12/assets/img/healthcare/sample-collection.png)

## 2. Features

## 2.1 Sample Collection automation

You can also automate the creation of Sample Collection document for each Lab Test by enabling the 'Create Sample Collection document for Lab Test' option in [Healthcare Settings](/docs/user/manual/en/healthcare/healthcare_settings) and configure samples in the Lab Test Template.

![Lab Sample Collection](/docs/v12/assets/img/healthcare/lab-sample-collection.png)

## 2.2 Sample labeling

Printing of sample identification tags is also possible in ERPNext. By default a print format called "Sample ID Print" is made available, but you can always customize this directly using the [Print Format Builder](/docs/user/manual/en/setting-up/print/print-format-builder.html) or even create a custom [Print Format](/docs/user/manual/en/customize-erpnext/print-format.html) if required. The number of labels required has to be set in the "No. of prints" field in the Sample Collection document. Accordingly, those many labels will be generated in the print view.

![Sample Print](/docs/v12/assets/img/healthcare/sample-print.png)

## 3. Related Topics

1. [Lab Test](/docs/user/manual/en/healthcare/lab_test)
1. [Lab Test Template](/docs/user/manual/en/healthcare/lab_test_template)

{next}
