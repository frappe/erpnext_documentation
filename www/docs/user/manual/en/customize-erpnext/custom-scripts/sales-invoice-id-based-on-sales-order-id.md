<!-- add-breadcrumbs -->
# Sales Invoice ID Based On Sales Order ID

The script given below allows you to apply naming series to a Sales Invoice, same as that of the corresponding Sales Order.
Sales Invoice uses a prefix M- but the number duplicates itself from the Sales Order Name.

Example: If Sales Order ID is SO-12345, then corresponding Sales Invoice ID will be set as M-12345.

```js
frappe.ui.form.on("Sales Invoice", "refresh", function(frm){
	var sales_order = frm.doc.items[0].sales_order.replace("M", "M-");
	if (!frm.is_new() && sales_order && frm.doc.name!==sales_order){
		frappe.call({
		method: 'frappe.model.rename_doc.rename_doc',
		args: {
			doctype: frm.doctype,
			old: frm.docname,
			"new": sales_order,
			"merge": false
		},
	});
	}
});
```
{next}