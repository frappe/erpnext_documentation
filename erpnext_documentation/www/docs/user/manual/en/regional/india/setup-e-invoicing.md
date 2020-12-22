<!-- add-breadcrumbs -->
# E Invoicing under GST

Under GST, all small and large businesses are supposed to register all sales invoices onto GST portal that falls under one of the following categories:
- Business to Business
- Supply to SEZ
- Exports
- Deemed Exports

To help automate the E Invoicing process, we have integrated ERPNext with a GSP so you can easily generate IRNs and signed E Invoices from your ERPNext Sales Invoices.

## Prerequisites

- You must have a registered account on E Invoice [portal](https://einvoice1.gst.gov.in/)
- GST Accounts must be set in the **GST Settings** DocType.

## Setting up


### Getting Credentials

1. Login into E Invoice [portal](https://einvoice1.gst.gov.in/) with your username & password.
1. Click on **API registration** on the sidebar.
1. Click on **User Credentials** from the expanded list.
1. Click on **Create API User**.
1. Click on **Through GSP** and select **Adequare Info Private Limited**.
1. Create a username and password which will be used to authenticate with GSP.

### Setting Up ERPNext

Go to **E Invoice Settings** and click on **Enable** checkbox.

1. **GSTIN**: GSTIN by which your company is registered on e-invoice portal.
1. **Username**: Username created in previous step.
1. **Password**: Password created in previous step.

### Generating IRN

Create a sales invoice and keep it under Draft state. Click on **E Invoicing** button group and then on **Generate IRN**. If Sales Invoice doesn't have any validation errors, IRN will be generated and updated in the Sales Invoice. You can now submit the invoice and print E Invoice with QRCode image by selecting **GST E Invoice** Print Format while printing.

<img class="screenshot" src="/docs/assets/img/regional/india/einv_gen_irn_button.png">

<img class="screenshot" src="/docs/assets/img/regional/india/einv_generated_irn.png">

<img class="screenshot" src="/docs/assets/img/regional/india/einv_print_format.png">

### Cancel IRN

Once you generate IRN for an invoice and submit it, you will have **Cancel IRN** button in the E Invoicing button group. Clicking on it will open up a popup which will ask for reason of cancellation and remark. Once you cancel the IRN, invoice will look something like this.

<img class="screenshot" src="/docs/assets/img/regional/india/einv_cancel_irn_button.png">

<img class="screenshot" src="/docs/assets/img/regional/india/einv_cancelled_irn.png">

### Generating E Way Bill

E Way Bill can be generated along with IRN if Transporter Info is provided. You can find Transporter Info section in the bottom part of the invoice. You must select transporter, mode of transport and distance to generate E Way Bill. You can also generate E Way Bill after generating IRN and submitting the invoice. 

<img class="screenshot" src="/docs/assets/img/regional/india/einv_gen_ewaybill_button.png">

<img class="screenshot" src="/docs/assets/img/regional/india/einv_gen_ewaybill_dialog.png">

### Cancelling E Way Bill

The process is similar to cancelling of IRN. Click on Cancel E Way Bill and then enter reason and remarks for cancellation.

<img class="screenshot" src="/docs/assets/img/regional/india/einv_cancel_ewaybill_button.png">

<img class="screenshot" src="/docs/assets/img/regional/india/einv_cancelled_ewaybill.png">