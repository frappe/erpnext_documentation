<!-- add-breadcrumbs -->
# Field Types

The following are the types of fields you can define while creating new ones, or while amending standard ones.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](/docs/v13/user/manual/en/customize-erpnext/articles/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](/docs/v13/user/manual/en/customize-erpnext/articles/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here.

![Check Field TYpe](/docs/v13/assets/img/customize/field-type-check.png)

#### Select

Select will be a drop-down field. You can add multiple results in the Option field, separated by row.

![Select Field Type](/docs/v13/assets/img/customize/field-type-select.png)

#### Table

A table will be a kind of Link field which renders another DocType within the current form. For example, the Item Table in the Sales Order is a Table field, which is linked to Sales Order Item DocType.

![Table Field Type](/docs/v13/assets/img/customize/field-type-table.png)

#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

![Attach Field Type](/docs/v13/assets/img/customize/field-type-attach.png)

#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

![Field Type Image](/docs/v13/assets/img/customize/field-type-image.png)

#### Text Editor

Text Editor is a text field. It has text-formatting options. In ERPNext, this field is generally used for defining Terms and Conditions.

![Field Type Text Editor](/docs/v13/assets/img/customize/field-type-text-editor.png)

#### Date

This field will enable you to enter the Date in this field.

![Field Type Date](/docs/v13/assets/img/customize/field-type-date.png)

#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

![Field Type Date and Time](/docs/v13/assets/img/customize/field-type-date-and-time.png)

#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Oce you do that, the Barcode would automatically get generated against the number.

![Field Type Barcode](/docs/v13/assets/img/customize/field-type-barcode.png)

#### Button

This kind of field will be an action button, like Save, Submit, etc.

![Field Type Button](/docs/v13/assets/img/customize/field-type-button.png)

#### Code

If the Field Type is selected as code, you will be able to enter a Code to the field.

![Field Type Code](/docs/v13/assets/img/customize/field-type-code.png)

#### Color

You will have the option of specifying the color for this Form.

![Field Type Colour](/docs/v13/assets/img/customize/field-type-colour.png)

#### Column Break

Since ERPNext has multiple column layouts, using Column Breaks, you can divide a set of fields into a maximum of two columns.

![Field Type Column Break](/docs/v13/assets/img/customize/field-type-column-break.png)

#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

![Field Type Currency](/docs/v13/assets/img/customize/field-type-currency.png)

#### Data

The data field will be a simple text field. It allows you to enter a value of up to 140 characters, making this the most generic field type. To enable validations for Email, Name, or Phone Number inputs, set options to "Email", "Name", "Phone" in Settings > DocType.

![Field Type Data](/docs/v13/assets/img/customize/field-type-data.png)

#### Float

Float field carries numeric value, up to nine decimal places. Precision for the float field is set via [Set Precision](/docs/v13/user/manual/en/customize-erpnext/articles/set-precision)

> Setup > Settings > System Settings

The setting will be applicable on all the float field.

![Field Type Float](/docs/v13/assets/img/customize/field-type-float.png)

#### Geolocation

Use Geolocation field to store GeoJSON <a href="https://tools.ietf.org/html/rfc7946#section-3.3">feature_collection</a>. Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

Read [Geolocation field](/docs/v13/user/manual/en/customize-erpnext/articles/geolocation-field) for more understanding.

![Field Type Geolocation](/docs/v13/assets/img/customize/field-type-geolocation.png)

#### HTML

You can select the field to be an HTML field when you want the data to be entered in HTML format.

![Field Type HTML](/docs/v13/assets/img/customize/field-type-html.png)

#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

![Field Type Image](/docs/v13/assets/img/customize/field-type-image2.png)

#### Int (Integer)

The integer field holds numeric value, without decimal place.

![Field Type Integer](/docs/v13/assets/img/customize/field-type-integer.png)

#### Small Text

Small Text field carries text content and has more character limit than the Data field.

![Field Type Small Text](/docs/v13/assets/img/customize/field-type-small-text.png)

#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

![Field Type Long Text](/docs/v13/assets/img/customize/field-type-long-text.png)

#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

![Field Type Text](/docs/v13/assets/img/customize/field-type-text.png)

#### Markdown Editor

This field will allow you to add the text in Markup language.

![Field Type Markdown Editor](/docs/v13/assets/img/customize/field-type-markdown-editor.png)

#### Password

The password field will have decoded value in it.

![Field Type Password](/docs/v13/assets/img/customize/field-type-password.png)

#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

![Field Type Percent](/docs/v13/assets/img/customize/field-type-percent.png)

#### Rating

You can define the field as a Rate field which in the background will be calculated as Rating.

![Field Type Rating](/docs/v13/assets/img/customize/field-type-rating.png)

#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

![Field Type Read Only](/docs/v13/assets/img/customize/field-type-read-only.png)

#### Section Break

Section Break is used to divide the form into multiple sections.

![Field Type Section Break](/docs/v13/assets/img/customize/field-type-section-break.png)

#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field. Read documentation for [Signature Field](/docs/v13/user/manual/en/customize-erpnext/articles/signature-field) to know more.

#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.

![Field Type Table MultiSelect](/docs/v13/assets/img/customize/field-type-table-multiselect.png)

#### Time

This is a Time field where you can define the Time in the field.

![Field Type Time](/docs/v13/assets/img/customize/field-type-time.png)

#### Duration

You can use the Duration field if you want to define a timespan.

![Field Type Duration](/docs/v13/assets/img/customize/field-type-duration.png)

If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

![Field Type Duration Options](/docs/v13/assets/img/customize/field-type-duration-options.png)

This is how the duration field looks after the above changes.

![Field Type Duration](/docs/v13/assets/img/customize/field-type-duration2.png)

{next}

