<!-- add-breadcrumbs -->
# Document Title

**You can customize the title of documents based on properties so that you have meaningful information for the list views.**

For example, the default title on a Quotation is the customer name, but if you are dealing with only a few customers and sending lots of quotations to each customer, you may want to customize.

<img class="screenshot" alt = "Customize Title"
    src="{{docs_base_url}}/assets/img/customize/customize-document-title.png">

## Setting Title Fields

From ERPNext Version 6.0 onwards, all transactions have a 'Title' property. If there is not a title property, you can add a **Custom Field** as title and set the **Title Field** via **Customize Form**.

You can set the default value of that property by using Python style string formatting in **Default** or **Options**

1. To edit a default title, go to Customize Form
2. Select the Form for which you would like to change the Title Field.
3. Edit the **Title Field** in the form.

## Defining Titles

You can define the title by setting document properties in braces `{}`. For example, if your document has fields `customer_name`, you can specify that as the Title of the Form.

<img class="screenshot" alt = "Customize Title"
    src="{{docs_base_url}}/assets/img/customize/customize erpnext-defining-titles.gif">

Alternatively, you can also define a particular field as the 'Title Field' in Customize Form.

<img class="screenshot" alt = "Customize Title"
    src="{{docs_base_url}}/assets/img/customize/customize-document-title-6.png">

## Fixed or Editable Titles

If your title is generated as a default title, it can be edited by the user by clicking on the heading of the document.

<img class="screenshot" alt = "Editable Title"
    src="{{docs_base_url}}/assets/img/customize/customize-document title.gif">

If you want a fixed title, you can set the rule in the **Options** property. In this way, the title will be automatically updated every time the document is updated.

{next}
