<!-- add-breadcrumbs -->
# Rename Buttons in Form View

In a submitted Sales Order, you can see multiple options under the 'Create' option:

<img alt="Custom Script" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-button-all.png">

You can use this custom script to rename the buttons:

```
frappe.ui.form.on('Sales Order', {                          
	on_submit: function(frm){
	//	console.log('reloaded doc on submit')
		location.reload()
	},
	onload_post_render: function(frm){                      
		var bt = ['Delivery', 'Work Order', 'Invoice', 'Material Request', 'Request for Raw Materials', 'Purchase Order', 'Payment Request', 'Payment', 'Project', 'Subscription']
		bt.forEach(function(bt){
			frm.page.remove_inner_button(bt, 'Create')
			});
		frm.page.add_inner_button('Order Raw Materials', () => cur_frm.cscript.make_raw_material_request(), 'Create')
		}
	}
);
```

Using this script, we have removed/hidden the unwanted buttons, and then renamed one:

<img alt="Custom Script" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-button-rename.png">

**Note:** To learn more about the JS APIs, visit the [frappe documentation](https://frappe.io/docs/user/en/api/form).

To check the method which is called, you will need to check JS file for that doctype. In this example, for renaming 'Request For Raw Materials', we are referring to [this line](https://github.com/frappe/erpnext/blob/782f45ae5f272173b5daadb493d40cf7ccf131b4/erpnext/selling/doctype/sales_order/sales_order.js#L167).

{next}
