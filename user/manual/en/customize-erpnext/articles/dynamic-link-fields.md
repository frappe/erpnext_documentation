<!-- add-breadcrumbs -->
# Dynamic Link Fields

Dynamic Link field is a field which can search and hold the value of any DocType. Let's consider an example to learn how Dynamic Link field works.

While creating Opportunity or Quotation, we have to explicitly define if it is for a Lead or a Customer. Based on our selection (Lead/Customer), another link field shows up where we can select the actual Lead or Customer.

If you set the former field as Dynamic Link, where we select actual Lead or Customer, then the later field will be automatically linked to master selected in the first field, i.e. Leads or Customers. Hence we need not insert separate link fields for Customer and Lead.

Below are the steps to insert Custom Dynamic Field. For instance, we will insert Dynamic Link Field in Journal Entry.

#### Step 1: Insert Link Field for Doctype

First, we will create a link field that will be linked to the Doctype.

<img alt="Custom Link Field" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-dynamic-link-1.gif">

By **Doctype** mentioned in the Option field, we mean parent Doctype. So, just like Quotation is one Doctype, which has multiple Quotation under it. Same way, Doctype is also a Doctype which has Sales Order, Purchase Order and other doctypes created as Doctype records.

**Doctype<br>**
---- Sales Order<br>
---- Purchase Invoice<br>
---- Quotation<br>
---- Sales Invoice<br>
---- Employee<br>
---- Work Order<br>
.. and so on.

So linking this field with parent Doctype will list all the Doctype records.

<img alt="journal Voucher Link Field" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-dynamic-link.png">

#### Step 2: Insert Dynamic Link Field

This custom field's type will be "Dynamic Link". In the Option field, the name of the Doctype link field will be mentioned.

<img alt="Custom Dynamic Field" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-dynamic-link-2.gif">

This field will allow selecting document id, based on the value selected in the Doctype link field. For example, if we select Sales Order in the prior field, the Dynamic Link field will list all the Sales Orders ids.

<img alt="Custom Dynamic Field" class="screenshot" src="{{docs_base_url}}/assets/img/customize/customize-dynamic-link-3.gif">

**Customizing options in the Doctype Link field**

By default, the Doctype link field will provide all the forms/doctypes for selection. If you wish this field to show certain specific doctypes in the search result, you will need to write Custom Script for it.
</div>

{next}

<!-- markdown -->
