<!-- add-breadcrumbs -->
# Update Date Field Based On Value In Other Date Field

The script given below would auto-set value for the date field, based on the value in another date field.

Example: Production Due Date must be set as two days before Delivery Date. Let us assume that the Delivery Date for a project has already been defined, and there is a Field 'Production Due Date' as a 'Date' field type present already in the form. Applying the following script shall ensure that the  Production Due Date gets auto updated to two days prior to the delievry date.

    cur_frm.cscript.custom_delivery_date = function(doc, cdt, cd){
    cur_frm.set_value("production_due_date", frappe.datetime.add_days(doc.delivery_date, -2));
     }

{next}