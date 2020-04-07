<!-- add-breadcrumbs -->

# Clinical Procedures Template

ERPNext Healthcare allows you to configure templates with various properties of Clinical Procedures to ease out the Procedure creation process. You can create templates so that you don't have to enter the consumables, rates and linked items every time you create a [Clinical Procedure](/docs/user/manual/en/healthcare/clinical_procedure) for a Patient.

## 1. How to Create a Clinical Procedure Template

You can create new Clinical Procedure Templates by going to:

> Home > Healthcare > Consultation Setup > Clinical Procedure Template

1. Enter a unique name for the Template.
2. The Clinical Procedure Template automatically creates an Item linked to it for billing purposes. For this reason, enter an Item Code, Item Group and Description for the item.
3. Optionally select the Medical Department for which the Clinical Procedures will be conducted.
4. Check "Is Billable" if you want to bill the procedure like a Knee Surgery. If you check this, set a rate for the Procedure. You may not want to bill procedures like Wound Cleaning.
5. Save.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/clinical_procedure_template.png">

## 2. Features

### 2.1 Automatic Item Creation for Templates

Templates allow you to manage the billable Item, rate etc. for a particular procedure. The system automatically creates an Item linked to the template when it is saved.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/clinical_procedure_item.png">

You can change the Item Code linked to the Procedure if needed using the Change Item Code button.

### 2.2 Manage Procedure Consumables

The Consumables section lets you set the consumable Stock Items with default quantities etc. which will be needed during the Procedure, so that these items will be preloaded in the Clinical Procedures created based on the template. This allows the performing practitioner to easily input the consumed quantities or add additional items which have been consumed during the actual procedure.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/procedure_consumables.png">

### 2.3 Invoice Consumables Separately

If the "Invoice Consumables Separately" option is checked, the charges for the consumable Items will be added to the Sales Invoice separately in addition to the "Billing Rate" of the procedure.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/invoice_separately.png">

### 2.4 Configure Sample Collection

Note that you can also enable "Sample Collection" for a Clinical Procedure if applicable.

<img class="screenshot" alt="ERPNext Healthcare" src="{{docs_base_url}}/assets/img/healthcare/sample_collection.png">

## 3. Related Topics

1. [Clinical Procedure](/docs/user/manual/en/Healthcare/clinical_procedure)
1. [Sample Collection](/docs/user/manual/en/Healthcare/sample_collection)

{next}