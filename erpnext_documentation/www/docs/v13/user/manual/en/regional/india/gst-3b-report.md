<!-- add-breadcrumbs -->

###  GSTR3B Report in ERPNext

To generate GSTR3B Report in ERPNext navigate to <br>
> **Accounting > Goods and Services Tax (GST India) > GSTR 3B Report** <br>

or simply search for GSTR 3B Report in awesomebar.

Click New to generate a new report or select an existing report to update it or download JSON.

Enter the following details to generate the report:
1. Company Name
2. Company Address linked to the GSTIN for which the report is to be generated
3. Year
4. Month

![GSTR 3B Report](/docs/v13/assets/img/regional/india/gstr-3b-input.png)

Click Save to generate the report. An existing report can also be updated/regenerated on clicking
save.

After saving you can see the JSON output in the text field below which can also be downloaded by
using the Download JSON button in the top right corner as shown in the image below.

![GSTR 3B With JSON](/docs/v13/assets/img/regional/india/gstr-3b-report.png)

If you want to print the report it can also be printed and viewed in GSTR3B Form by clicking on View Form as shown below

![Download Option in GSTR 3B](/docs/v13/assets/img/regional/india/gstr-3b-download.png)

Note: To make sure the report is calculated accurately and correctly please make sure of the following things.

1. Since GST is a destination based tax, please make sure all Indian Customers and Suppliers have gst state (even the Unregistered ones).

2. Nil rated, exempted or non-gst items have Is nill rated or Is Non GST checkbox is checked in the item master.

![GST Exempted](/docs/v13/assets/img/regional/india/gst-item.png)

3. Proper account heads are entered in GST Settings.

4. Proper Eligibility For ITC field is selected. For eg: All Other ITC or Ineligible

{next}