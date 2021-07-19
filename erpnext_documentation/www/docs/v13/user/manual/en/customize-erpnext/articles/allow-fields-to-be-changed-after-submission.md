<!-- add-breadcrumbs -->
# Allow Fields to be Changed After Submission

Once a document is submitted, fields are frozen, and no editing is allowed.  However, there are certain standard fields like Letter Head, Print Heading which can still be edited. If **Allow on Submit** property is checked, the field will be editable even after the document is submitted.

Here is an example. In 'Sales Invoice' DocType, 'Letter Head' field can be edited even after submitting the sales invoice.

![Allow on Submit](/docs/v13/assets/img/customize/allow-on-submit-on-standard-field.gif)

> Note: You cannot enable 'Allow on Submit' for standard fields. Certain standard field come with this propertly enabled by default. However, you can enable this for custom fields that you create.

To set this property for a custom field,

1. Go to Customize Form.
2. Select the Form in which you want to set this property.
1. Select the custom field.
3. Tick 'Allow on Submit' checkbox.
4. Update.

![Allow on Submit on Custom Field](/docs/v13/assets/img/customize/allow-on-submit-on-custom-field.gif)

After updating Customize Form, you should reload your ERPNext account. Then check form, and field to confirm whether or not it is editable in submitted form as well.

{next}

<!-- markdown -->