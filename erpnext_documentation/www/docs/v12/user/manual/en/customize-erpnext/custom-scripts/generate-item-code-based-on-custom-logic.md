<!-- add-breadcrumbs -->
# Generate Item Code Based On Custom Logic

Add this Custom Script in the script of **Item**, so that the new Item Code is
generated just before the Item gets saved.



    cur_frm.cscript.custom_validate = function(doc) {
        // clear item_code (name is from item_code)
        doc.item_code = "";

        // first 2 characters based on item_group
        switch(doc.item_group) {
            case "Test A":
                doc.item_code = "TA";
                break;
            case "Test B":
                doc.item_code = "TB";
                break;
            default:
                doc.item_code = "XX";
        }

        // add next 2 characters based on brand
        switch(doc.brand) {
            case "Brand A":
                doc.item_code += "BA";
                break;
            case "Brand B":
                doc.item_code += "BB";
                break;
            default:
                doc.item_code += "BX";
        }
    }


{next}
