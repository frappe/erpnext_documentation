<!-- add-breadcrumbs -->
# E-Invoicing under GST

> Introduced in version 13

E-Invoicing has been introduced to standardize the invoicing process. All ERPs and software have to accommodate the invoice format defined by GSTN. It also provides a level of automation in filling GSTR reports.

Under the new e-invoicing system, businesses with turnover higher than ₹50Cr are supposed to get all business to business (B2B) invoices electronically authenticated with GSTN by generating a unique Invoice Reference Number (IRN).

To help automate the E-Invoicing process, we have integrated ERPNext with a GST Suvidha Provider (GSP) so you can easily authenticate ERPNext Sales Invoices with GSTN.

## 1. Prerequisites

- You must have a registered account on E-Invoice [portal](https://einvoice1.gst.gov.in/)
- GST Accounts must be set in the "GST Settings" DocType.

> Note: Using this integration for automatic process involves additional charges. Contact ERPNext Sales Team for more information.

## 2. Setting up E-Invoicing

### 2.1 Getting Credentials

1. Login into E-Invoice [portal](https://einvoice1.gst.gov.in/) with your username and password. Register with a username and password if you haven't created an account already.
1. Click on "API registration" on the sidebar.
1. Click on "User Credentials" from the expanded list.
1. Click on "Create API User".
1. Click on "Through GSP" and select "Adequare Info Private Limited".
1. Create a username and password which will be used to authenticate with GSP.

### 2.2 Setting Up ERPNext

Go to "E-Invoice Settings" and click on the "Enable" checkbox.

1. **GSTIN**: GSTIN by which your company is registered on the e-invoice portal.
1. **Username**: Username created in the previous step for authenticating with GSP.
1. **Password**: Password created in the previous step for authenticating with GSP.

### 2.3 Generating IRN

Create a Sales Invoice and keep it in the Draft state. Click on the **E-Invoicing** button group and then on **Generate IRN**. If the Sales Invoice doesn't have any validation errors, IRN will be generated and updated in the Sales Invoice. You can now submit the invoice and print the E-Invoice with QRCode image by selecting "GST E-Invoice" Print Format while printing.

![Generate IRN in Invoice](/docs/v13/assets/img/regional/india/generate-irn-in-invoice.png)

Once IRN is generation process is successful, QRCode and IRN will be stored in the Sales Invoice. Once these are generated, Sales Invoice fields cannot be edited.

![IRN in Invoice](/docs/v13/assets/img/regional/india/irn-in-invoice.png)

You can print the E-Invoice using the default GST E-Invoice Print Format. Or you can manually edit your own print format to include e-invoice fields.

![E Invoice Print Format](/docs/v13/assets/img/regional/india/einv-print-format.png)

### 2.4 Cancel IRN

If you have generated IRN for an invoice with faulty data then, you can cancel it with the **Cancel IRN** button under the E-Invoicing button group. Clicking on it will open up a popup which will ask for the reason for cancellation and remark.

![E Invoice Cancel IRN Button](/docs/v13/assets/img/regional/india/einv-cancel-irn-button.png)

Once you cancel the IRN, the invoice will look something like this.

![E Invoice WIth IRN Cancelled](/docs/v13/assets/img/regional/india/einv-cancelled-irn.png)

## 3. E-Way bill

### 3.1 Generating E-Way Bill

E-Invoicing reduces the additional step involved in generating E-Way Bills. Now you can provide **Transporter Info** along with IRN generation to generate E-Way Bill for the invoice. You can find the Transporter Info section in the bottom part of the invoice. You must select **Transporter**, **Mode of Transport**, and **Distance** to generate E Way Bill. You can also generate E Way Bill after generating IRN and submitting the invoice.

![E Invoice Generate Eway Bill](/docs/v13/assets/img/regional/india/einv-generate-ewaybill-button.png)

You will see a popup with relevant info before submitting:
![E Way Bill Dialog](/docs/v13/assets/img/regional/india/einv-gen-ewaybill-dialog.png)

### 3.2 Cancelling-E Way Bill

The process is similar to the cancellation of IRN. Click on Cancel E-Way Bill and then enter reason and remarks for cancellation.

![Cancel E-way Bill](/docs/v13/assets/img/regional/india/einv-cancel-ewaybill-button.png)

<img class="screenshot" src="/docs/v13/assets/img/regional/india/einv_cancelled_ewaybill.png">
![](/docs/v13/assets/img/regional/india/)

{next}