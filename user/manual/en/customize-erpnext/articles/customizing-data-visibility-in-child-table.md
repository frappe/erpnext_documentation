<!-- add-breadcrumbs -->
# Customizing Data Visibility in Child Tables

In ERPNext, there is a feature called the editable grid. This allows the user to add values in the child table without opening a dialog box/form for each row.

This is how the Quotation Item table renders value when the Editable Grid is enabled. It will have a maximum of four columns in the table.

<img alt="Child Table" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-child-table-5.png">

As per the default setting, only four columns are listed in the child table. Following is how you can add more columns in the Editable Grid itself.

For the field to be added as a column in the table, enter a value in the Column field. Also, ensure that the "Is List View" property is checked for that field.

<img alt="Child Table" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-child-table-2.png">

Based on the value in the Column field, columns will be added to the child table. Ensure that the total value added in the Column field doesn't exceed 10. Based on the Column value, the width for that column will be set.

<img alt="Child Table" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-child-table-3.png">

**Switch to Un-editable Grid**

To have more values shown in the preview of the Quotation Item table, you can disable Editable Grid for the Quotation Item Doctype. Steps below.

<img alt="Child Table" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-child-table.gif">

Once Editable Grid is disabled for the Quotation Item, the values will be rendered in a preview of the Quotation Item table in the following way:

<img alt="Child Table" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-child-table-4.png">

To have a specific field's value shown in the preview, ensure that for that field, in the Customize Form tool, "In List View" property is checked.

<img alt="Child Table" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-child-table-1.png">

{next}
