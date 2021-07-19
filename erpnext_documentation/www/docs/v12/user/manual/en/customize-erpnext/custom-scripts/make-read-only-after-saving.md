<!-- add-breadcrumbs -->
# Make Read Only After Saving

Use the method `cur_frm.set_df_property` to update the field's display.

In this script we also use the `__islocal` property of the DocType to check if the
document has been saved at least once or is never saved. If `__islocal` is `1`,
then the document has never been saved.

```js
frappe.ui.form.on("MyDocType", "refresh", function(frm) {
	// use the is_new method of frm, to check if the doc is saved or not
	frm.set_df_property("myfield", "read_only", frm.is_new() ? 0 : 1);
}
```

{next}
