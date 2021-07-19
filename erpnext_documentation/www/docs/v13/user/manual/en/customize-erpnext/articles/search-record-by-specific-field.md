<!-- add-breadcrumbs -->
# Search Record by Specific Field

While creating any DocType, you may want to link a particular field to another DocType. For example, in Sales Order DocType, 'Customer' field allows you to select an existing customer. Such fields are called [Link Fields](/docs/v13/user/manual/en/customize-erpnext/articles/field-types#link).

Using Link Fields you can create a


Let's assume that you want to see that Item in a Sales Order along with its Item Group. The steps to do this are given below:

#### Step 1: Go to Customize Form

> Home > Customization > Form Customization > Customize Form

#### Step 2: Select the Document for which you want multiple fields to be visible in the Search Field

Here, we will select the Document Item.

#### Step 3:  Search Field

Update Warehouse field name in the Search By field.

<img alt="Search By in Customize Form" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/customize-search-record-1.png">

<img alt="Search By in Customize Form" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/customize-search-record-2.png">

Once these settings have been updated, while creating a Sales Order, when you select the Item, you will also be able to the warehouse there.

<img alt="Search By in Customize Form" class="screenshot" src="{{docs_base_url}}/v13/assets/img/customize/customize-search-record-3.png">

{next}

<!-- markdown -->
