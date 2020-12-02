<!-- add-breadcrumbs -->
# E Invoicing under GST

Under GST, all small and large businesses are supposed to generate IRNs for all sales invoices that falls under one of the following categories:
- Business to Business
- Supply to SEZ
- Exports
- Deemed Exports

To help automate the E Invoicing process, we have setup API integration in ERPNext so you can now generate IRNs and signed E Invoices for your Sales Invoices.

## Prerequisites

- GST Accounts must be set in the GST Settings DocType.

## Setting up

Go to E Invoice Settings and click on **Enable** checkbox. This will allow you to enter credentials which are used for connecting with GSP.

1. **Client ID and Client Secret**: These will be generated per customer by the GSP which ERPNext have been integrated with. Contact ERPNext support for getting your credentials.
1. **GSTIN**: Set it to your company GSTIN.
1. **Username**: Username by which you have registered on e-invoice portal.
1. **Password**: Password for the logging into e-invoice portal.

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