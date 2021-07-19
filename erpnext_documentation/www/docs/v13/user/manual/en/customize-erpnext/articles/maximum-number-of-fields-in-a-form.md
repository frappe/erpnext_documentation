<!-- add-breadcrumbs -->
# Maximum Number of Fields in a Form

Sometimes while creating custom fields, you might have faced an error message that looks like this:

> Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs.

### What does it mean?

In simple terms, it means that you have reached the limit of the maximum number of fields for the specific form/doctype. So, what is the maximum limit of fields?

In MySQL, there is a hard limit of 4096 columns per table, but the effective maximum may be less for a given table. The exact limit depends on several interacting factors.

Every table (regardless of storage engine) has a maximum row size of 65,535 bytes. Storage engines may place additional constraints on this limit, reducing the effective maximum row size.

The maximum row size constrains the number (and possibly size) of columns because the total length of all columns cannot exceed this size (65,535 bytes). For example, `utf8mb3` characters require up to 3 bytes per character, so for a `VARCHAR(140)` column, the server must allocate `140 × 3 = 420` bytes per value. Consequently, a table cannot contain more than `65,535 / 420 = 156` such columns.

In Frappe framework, `VARCHAR(140)` type columns are created based on "Data", "Link", "Select", "Dynamic Link", "Password" and "Read Only" field types. Hence, you can create approximately 156 such columns in the system.

### Solution:

To add more fields to the system, you can do some changes.

1. Convert some of the fields to "Text", "Small Text", "Text Editor" or "Code" type field. In MySQL, BLOB and TEXT columns count from one to four plus eight bytes each toward the row-size limit because their contents are stored separately from the rest of the row. So, converting to those field types will free up some spaces and will allow addition of some more fields.
2. Set smaller value in the "Length" property while creating fields, the default value is 140. The System sets the length of `VARCHAR` based on this property and allocates size for those columns. Hence, smaller Length leads to add more fields.

{next}
