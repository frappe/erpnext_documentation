<!-- add-breadcrumbs -->
# Custom Script for Fetching Values From Master

To pull a value of a link on selection, use the `add_fetch` method.

    
    
    add_fetch(link_fieldname, source_fieldname, target_fieldname)
    

### Example

Let' say you have created a Custom Field **VAT ID** (`vat_id`) in **Customer** and **Sales Invoice** and want to make sure that this value gets updated every time you select a Customer in a Sales Invoice.

To configure this, in the Sales Invoice Custom Script, you can add this line:

    
    
    cur_frm.add_fetch('customer','vat_id','vat_id')
    


{next}
