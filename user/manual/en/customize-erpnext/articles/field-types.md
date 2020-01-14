<!-- add-breadcrumbs -->
# Field Types

The following are the types of fields you can define while creating new ones, or while amending standard ones.

#### Link

Link field is connected to another master from where it fetches data. For example, in the Quotation master, the Customer is a Link field. To know more, [click here](/docs/user/manual/en/customize-erpnext/articles/creating-custom-link-field).

#### Dynamic Link

Dynamic Link field is one which can search and hold value of any document/doctype. [Click here](/docs/user/manual/en/customize-erpnext/articles/dynamic-link-fields) to learn how Dynamic Link Field functions.

#### Check

This will enable you to have a checkbox here.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-checkbox.png">

#### Select

Select will be a drop-down field. You can add multiple results in the Option field, separated by row.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-select-field.png">

#### Table

A table will be a kind of Link field which renders another DocType within the current form. For example, the Item Table in the Sales Order is a Table field, which is linked to Sales Order Item DocType.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-table-field-type.png">

#### Attach

Attach field allows you to browse a field from the File Manager and attach the same herein.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-attach-field.png">

#### Attach Image

Attach Image is a field wherein you will be allowed to attach Images of the format jpeg, png, etc. This becomes the Image representing that particular DocType. For e.g., you would want the image of an Item in its DocType, you can choose your field to be an Attach Image Field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-attach-image.png">

#### Text Editor

Text Editor is a text field. It has text-formatting options. In ERPNext, this field is generally used for defining Terms and Conditions.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-text-editor.png">

#### Date

This field will enable you to enter the Date in this field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-date-field.png">

#### Date and Time

This field will give you a date and time picker. The current date and time (as provided by your computer) are set by default.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-date-and-time.png">

#### Barcode

In this field, you can specify the field as Barcode which will allow you to enter a Barcode number. Oce you do that, the Barcode would automatically get generated against the number. 

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-barcode.png">

#### Button

This kind of field will be an action button, like Save, Submit, etc.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-button-field.png">

#### Code

If the Field Type is selected as code, you will be able to enter a Code to the field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-markdown-editor.png">

#### Color

You will have the option of specifying the color for this Form.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-field-type-color.png">

#### Column Break

Since ERPNext has multiple column layouts, using Column Breaks, you can divide a set of fields into a maximum of two columns. 

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-column break.png">

#### Currency

Currency field holds numeric value, like Item Price, Amount, etc. Currency field can have value up to six decimal places. Also, you can have a currency symbol being shown for the currency field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-field-type-currency.png">

#### Data

The data field will be a simple text field. It allows you to enter a value of up to 140 characters.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-data-field.png">

#### Float

Float field carries numeric value, up to nine decimal places. Precision for the float field is set via [Set Precision](/docs/user/manual/en/customize-erpnext/articles/set-precision)

> Setup > Settings > System Settings

The setting will be applicable on all the float field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-float.png">

#### Geolocation

Use Geolocation field to store GeoJSON <a href="https://tools.ietf.org/html/rfc7946#section-3.3">feature_collection</a>. Stores polygons, lines, and points. Internally it uses the following custom properties for identifying a circle.

For more understanding, [click here](/docs/user/manual/en/customize-erpnext/articles/geolocation-field)

#### HTML

You can select the field to be an HTML field when you want the data to be entered in HTML format.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-html.png">

#### Image

Image field will render an image file selected in another attach field.

For the Image field, under Option (in Doctype), a field name should be provided where the image file is attached. By referring to the value in that field, the image will be a reference in the Image field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/cutomize-image-field.png">

#### Int (Integer)

The integer field holds numeric value, without decimal place.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/cuxtomize-int-field.png">

#### Small Text

Small Text field carries text content and has more character limit than the Data field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-small-text.png">

#### Long Text

You can define your field to a Long Text Field when you would want to enter data with an unlimited character limit.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-long-text.png">

#### Text

This field type would allow you to add text in the field. The character limit in Small text, Long text and Text fields shall be determined based on the Relational Database Management System.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-text.png">

#### Markdown Editor

This field will allow you to add the text in Markup language.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-markdown-editor.png">

#### Password

The password field will have decoded value in it.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-password.png">

#### Percent

You can define the field as a Percentage field which in the background will be calculated as a percentage.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-percent.png">

#### Rating

You can define the field as a Rate field which in the background will be calculated as Rating.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-rating.png">

#### Read Only

Read Only field will carry data fetched from another form which will be non-editable. You should set Read Only as field type if its source for value is predetermined.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-read-only.png">

#### Section Break

Section Break is used to divide the form into multiple sections.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-section-break.png">

#### Signature

You can define the field to be a Signature field wherein you can add the Digital Signature in this field. To know more, [click here](/docs/user/manual/en/customize-erpnext/articles/signature-field)

#### Table MultiSelect

This is a combination of 'Link' type and 'Table' type fields. Instead of a child table with 'Add Row' button, in one field multiple values can be selected.  

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-table-multiselect.png">

#### Time

This is a Time field where you can define the Time in the field.

<img alt="Field Types" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-field-type-time.png">

{next}

