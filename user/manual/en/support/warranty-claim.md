<!-- add-breadcrumbs -->
# Warranty Claim

**A Warranty Claim is when a Customer claims free repairs within the Warranty Period of the item/service you're providing.**

If you are selling Items under warranty or if you have sold and extended service contract like the Annual Maintenance Contract (AMC), your Customer may contact you about an issue or a break-down of the product and provide you the Serial No of this Item.

To access the Warranty Claim list, go to:

> Home > Support > Warranty > Warranty Claim

## 1. Prerequisites
Before creating and using Warranty Claim, it is advised that you create the following first:

* [Customer](docs/user/manual/en/CRM/customer)
* [Serial Number](docs/user/manual/en/stock/serial-no)
* [Item](docs/user/manual/en/stock/item)

## 2. How to Create Warranty Claim

1. Go to the Warranty Claim list, click on New.
1. Select a Customer, 
1. Select the Serial Number of the Item on which Warranty Claim is to be recorded. The system will then automatically fetch the Serial No’s details and indicate whether this is under warranty or AMC.
1. Enter a description of the Issue. User can upload and image and create a table.
1. Save.
    ![Warranty Claim]({{docs_base_url}}/assets/img/support/warranty-claim.png)

### 2.1 Additional Options when Creating a Warranty Claim

* **Status**: While creating a Warranty Claim, the status will be set as "Open". User can change the status to:
    * Work In Progress: Fix/repairs are being done on the Item
    * Closed: The repairs have been done and the Warranty Claim is now closed.
    * Cancelled: The Warranty Claim was invalid and the claim was closed.
* **Issue Date**: While creating the Warranty Claim, the current date will be captured. This field is editable.


## 3 Features

### 3.1 Item and Warranty Details:

Once a Serial Number is selected, the following details about the Item will be fetched:

* Item Code
* Item Name
* Item Description

The details about Warranty/AMC will be fetched according to the Serial Number.

* **Warranty / AMC Status:** The possible options are "Under Warranty", "Out of Warranty", "Under AMC", or "Out of AMC". The status can be changed to Out of Warranty/AMC if the Item has been tampered with or Warranty is void depending on your terms of service.
* Warranty Expiry Date
* AMC Expiry date

    ![Warranty Serial](/docs/assets/img/support/warranty-serial.png)

### 3.2 Resolution
* **Resolution Date:** When the warranty or AMC is Closed, current date and time will be fetched in resolution Date field automatically. This field is also editable.
* **Resolved By:** Set the Email ID of the User who has resolved the Warranty Claim. The email ID is linked with [User](/docs/user/manual/en/setting-up/users-and-permissions/adding-users) created in the system.
* **Resolved Details:** This is a text field. User can enter details about the Warranty or AMC claim. A User can also upload the image, enter or create a table.

    ![Warranty Resolution](/docs/assets/img/support/warranty-resolution.png)

### 3.3 Customer Details

The following details of the [Customer](/docs/user/manual/en/CRM/customer) will be fetched:

* Customer Name
* Contact Person
* Territory
* Customer Group
* Customer Addresss

**Service Address:** User can enter the Service Address if it is different from Customer Address.

![Warranty Customer](/docs/assets/img/support/warranty-customer.png)

### 3.4 More Information

* **Company:** The Warranty or AMC is created from the company will be selected automatically.
* **Raised By:** User can enter the Name of the person who has raised the Warranty or AMC in case the Customer is an organization.
* **From Company:** User can enter the name of the company from which the warranty or AMC has been created.

If a Customer visit is required to address the issue, you can create a new
Maintenance Visit record from this.

## 4. Related Topics
1. [Issue](/docs/user/manual/en/support/issue)
1. [Maintenance Visit](/docs/user/manual/en/support/maintenance-visit)

{next}
