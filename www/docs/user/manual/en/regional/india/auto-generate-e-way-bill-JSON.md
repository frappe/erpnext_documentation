<!-- add-breadcrumbs -->
# Auto-generating e-Way Bill JSON from Sales Invoice

Under GST, transporters should carry an e-Way Bill when moving goods from one place to another when certain conditions are satisfied.

To help speed up creation of e-Way Bills, you can now auto-generate a JSON file from your ERPNext site which can be used to quickly generate an e-Way Bill on the <a href="https://ewaybillgst.gov.in">GST e-Way Bill System</a>.


## Prerequisites

- GST Accounts must be set in the GST Settings DocType.

- Fields required to generate a valid e-Way Bill must be entered in Sales Invoice. To identify the required fields and for more information, you can refer to the <a href="https://docs.ewaybillgst.gov.in/html/formatdownloadnew.html">JSON schema</a>.

## Instructions

### On your ERPNext site:

1. After entering the required data, submit the Sales Invoice(s).

1. You should now see a button labelled **e-Way Bill JSON** under the **Make** menu at the top-right corner.

	<img class="screenshot" src="/docs/assets/img/regional/india/ewb_invoice_button.png">

1. If you want to generate a JSON file for multiple invoices, you can select the relevant invoices from Sales Invoice List and find the **Generate e-Way Bill JSON** button under the **Actions** menu in the top-right corner.

	<img class="screenshot" src="/docs/assets/img/regional/india/ewb_list_button.png">

1. Upon clicking this button, your data will be validated in accordance with the <a href="https://docs.ewaybillgst.gov.in/html/formatdownloadnew.html">JSON schema</a> and the auto-generated JSON file will be downloaded onto your device.

### On the GST e-Way Bill System:

1. Log in to the <a href="https://ewaybillgst.gov.in">GST e-Way Bill System</a> using your credentials.

1. Under the **e-Waybill** section in the left sidebar, click on **Generate Bulk**.

1. Choose and upload the auto-generated file. You can safely ignore any warning regarding Document No. raised by the e-Way Bill System.

	<img class="screenshot" src="/docs/assets/img/regional/india/ewb_warning.png">

1. The e-Way Bill System should now display a description of the e-Way Bill(s) you are trying to generate. If it looks okay and no errors are encountered, you can proceed to generate the e-Way Bill(s) by clicking the **Generate** button.

1. You will now be able to view the e-Way Bill No. generated against your Sales Invoice(s). Please make a note of this as it will be useful later.

1. To print the e-Way Bill(s), go back to the e-Way Bill System Dashboard by clicking the <i class='fa fa-home'></i> icon and select **Print EWB** under the **e-Waybill** section.


You can now enter the e-Way Bill No. in your Sales Invoice for future reference.

<img class="screenshot" src="/docs/assets/img/regional/india/ewb_invoice_field.png">
