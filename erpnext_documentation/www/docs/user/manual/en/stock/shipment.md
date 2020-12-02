---
title: Shipment
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: A Shipment is a document that keeps track of real-world Shipments created against a Delivery Note or independently. This is particularly useful for shippers who want to track all their Shipment information such as AWB Number, Shipment Status, Carrier, etc. within ERPNext.
 keywords: Shipment, Shipping, frappe, Delivery, erpnext new features, erp, open source erp, free erp, stock
---

# Shipment

**A Shipment is a document that keeps track of real-world Shipments created against a Delivery Note or independently.**

Shipments are particularly useful for shippers who want to track all their Shipment information such as AWB Number, Shipment Status, Carrier, etc. within ERPNext.

To access the Shipment list, go to:
> Home > Stock > Stock Transactions > Shipment

## 1. Prerequisites
Before creating and using a Shipment, it is advised that you create the following first:

* Company and Customer [Address](/docs/user/manual/en/CRM/address) with Postal Code, Email Address and Phone Number set.
* Customer [Contact](/docs/user/manual/en/CRM/contact).

## 2. How to create a Shipment
A Shipment can be created manually or from a Delivery Note:

### 2.1. Manual Shipment
To create a Shipment manually, follow these steps:

1. Go to the Shipment list, click on New.
 <img class="screenshot" alt="Unsaved Shipment" src="{{docs_base_url}}/assets/img/stock/unsaved-shipment.png">
1. Select an option in the **Pickup from** field. On selecting one of the three options, you will be prompted to select a Company/Supplier/Customer based on your selection.
1. If you select 'Company' in the **Pickup from** field, along with the Address you must also select a **Pickup Contact Person** who will be a user from your organization, in ERPNext. Make sure the Last Name, Email Address and Phone Number are set for this user.
1. You can similarly fill the **Delivery To** section.
1. Add Shipment Parcel Information in the **Shipment Parcel** table.
1. Fill in the Value of Goods.
1. Select a Pickup Date.
1. Add a Description of Contents in this Shipment.
1. You can optionally fill the Shipment Information section if you are tracking Shipments manually.
1. Save and Submit.
 <img class="screenshot" alt="Submitted Shipment" src="{{docs_base_url}}/assets/img/stock/shipment-submitted.png">

### 2.1. Shipment from Delivery Note
To create a Shipment from a Delivery Note, click on **Create > Shipment**.
 <img class="screenshot" alt="Submitted Shipment" src="{{docs_base_url}}/assets/img/stock/shipment-from-delivery-note.png">

## 3. Features

### 3.1. Shipment Parcel

You can specify the length, width, height and weight of a parcel in the Shipment. If there are multiple parcels of the same dimensions, the **count** field can be set accordingly.

To automatically fetch frequently used parcel dimensions, a Parcel Template can be created and set in the **Parcel Template** field. After setting the template, click on **Add template**.
 <img class="screenshot" alt="Submitted Shipment" src="{{docs_base_url}}/assets/img/stock/shipment-parcel.png">

### 3.2. Shipment Information Section
The Shipment Information section is an **optional** section where a user can manually track Shipment information. Here are some of the fields:

1. **Service Provider**: A Service Provider can be a third party service that provides shipping services from various carriers.
1. **Shipment ID**: The unique Shipment ID on your Shipping platform.
1. **Shipment Amount**: Total cost incurred on Shipment
1. **Carrier**: The Carrier that handles your Shipment and delivers it.
1. **Carrier Service**: The type/category of service provided by the carrier. For e.g. some carriers have categories such as Economy, Express, etc.
1. **AWB Number**: For International Shipments. Air Waybill (AWB) gets a unique number, to make it easy to identify and track your Shipment.

### 4. Related Topics
1. [Delivery Note](/docs/user/manual/en/stock/delivery-note)
1. [Packing Slip](/docs/user/manual/en/stock/packing-slip)