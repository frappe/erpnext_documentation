<!-- add-breadcrumbs -->
# Request for Quotation

**A Request for Quotation is a document that an organization sends to one or more suppliers asking a quotation for items.**

![Buying Flow](/docs/v13/assets/img/buying/buying_flow_rfq.png)

To access Request for Quotation, go to:
> Home > Buying > Purchasing > Request for Quotation

## 1. Prerequisites
Before creating and using a Request for Quotation, it is advised that you create the following first:

* [Supplier](/docs/v13/user/manual/en/buying/supplier)
* [Item](/docs/v13/user/manual/en/stock/item)

## 2. How to create a Request For Quotation
1. Go to the Request For Quotation list, click on New.
2. Enter the date.
3. Choose the Supplier to whom the Request for Quotation is to be sent.
4. In the next table, enter items, quantity and the target warehouse where you'll be sending the items.
1. Warehouse can be left blank if 'Maintain Stock' is unticked for the item.
5. Save and submit.

![Create RFQ]({{docs_base_url}}/v13/assets/img/buying/rfq-create.png)

A Request for Quotation (RFQ) can also be created from a submitted Material Request. Once an RFQ is created, you can print and send suppliers the PDF which will have all the details you entered relevant to the RFQ. You can also get their reply (Supplier Quotation) in ERPNext itself, see section [4.1 Supplier Quotation by User](#41-supplier-quotation-by-user).
However, for a large number of items, your supplier may be more comfortable with an Excel sheet, etc.

## 3. Features

### 3.1 Get items from
The items in the items table can be fetched from other documents. The options are: Material Request, Opportunity, and Possible Supplier.

* **Material Request**: Items will be fetched from a submitted Material Request that you select. A Material Request can be searched with some matching words and a date range can also be selected to filter the Material Requests.

* **Opportunity**: Items will be fetched from a saved Opportunity. A date range can be selected here also.

* **Possible Supplier**: Select a possible supplier. Then if you have any submitted Material Requests against this supplier, items can be fetched from that.

![RFQ get items]({{docs_base_url}}/v13/assets/img/buying/rfq-get-items.png)

### 3.2 Get Suppliers
Instead of entering the suppliers manually in the table, you can also fetch them using the 'Get Suppliers' button. When you click on **Tools > Get Suppliers**, you will see the field 'Get Suppliers By'. There are two options to fetch suppliers: By Tag or By Group.

* **By tag**: Go to 'Tag Category' via searching from the search bar. You must have created tags here first and assigned them to a Supplier in the Buying module. Then you can select 'By Tag'. On clicking Add 'All Suppliers', suppliers with matching tags will be fetched.

* **By Group**: Select 'Supplier Group' and choose the supplier group from which suppliers need to be added. For example, if you select Hardware, all your hardware suppliers will be added so that you can get a quote from all of them.

![RFQ get suppliers]({{docs_base_url}}/v13/assets/img/buying/rfq-get-suppliers.png)

In the Supplier table, on expanding a row with the inverted triangle, you'll see an option 'Download PDF' which will open a PDF of the RFQ.

### 3.3 Link to Material Requests:
When you click on **Tools > Link to Material Requests**, it links the Request for Quotation to available Material Requests. The items should be the same in the Request for Quotation and the Material Request.

![Link to Material Request]({{docs_base_url}}/v13/assets/img/buying/link-to-material-request.png)

Now, when the Request for Quotation is saved, you can see in the Dashboard that it is linked to the Material Request.
If there are multiple Material Requests with the same items, then the link will be created with the newest Material Request.

### 3.4 Email Preview
In the 'Email Details' section, of a Draft Request for Quotation, there is a provision to build and preview your email to be sent to the Supplier.
![Email Details Section]({{docs_base_url}}/v13/assets/img/buying/email-details-section.png)

Enter any additional messages for the Supplier in the 'Message for Supplier' field. This field can be auto-filled using the 'Email Template' field.

A salutation can be added and the 'Subject' field can be changed as well. Once done, you can click on the 'Preview Email' button and see a preview of the email which will be sent.
![Preview Email]({{docs_base_url}}/v13/assets/img/buying/email-preview.png)

### 3.5 Terms and Conditions

In Sales/Purchase transactions, there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/docs/v13/user/manual/en/setting-up/print/terms-and-conditions)

### 3.6 Print Settings
#### Letterhead
You can print your request for quotation/purchase order on your company's letterhead. Know more [here](/docs/v13/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when you print it.

#### Print Headings
Titles of your documents can be changed. Know more [here](/docs/v13/user/manual/en/setting-up/print/print-headings).

## 4. Creating a Supplier Quotation after RFQ
After creation of Request for Quotation, there are two ways to generate Supplier Quotation from Request for Quotation.

### 4.1 Supplier Quotation by User

1. Open Request for Quotation and click on **Supplier Quotation > Create**.

    ![Supplier Quotation from RFQ]({{docs_base_url}}/v13/assets/img/buying/make-supplier-quotation-from-rfq.png)

2. Select the Supplier, click on the supplier again. In this page, click on the + next to 'Supplier Quotation'. A new Supplier Quotation page will be opened, user has to enter the quantity, rate and submit it.

    ![Supplier Quotation from Supplier]({{docs_base_url}}/v13/assets/img/buying/supplier-quotation-from-sup.png)

### 4.2 Supplier Quotation from Supplier

1. If a [Contact](/docs/v13/user/manual/en/CRM/contact) is created for the Supplier and an email address is associated with the Contact, the Contact details and the email address will be fetched on selecting the Supplier. Create a Contact and email address if not present already.

2. Click on **Tools > Send Emails to Suppliers**.

    **If the Supplier's account is not present**: The system will create the Supplier's account and send details to the Supplier. The Supplier will need to click on the link (Password Update) present in the email. After the password update, the Supplier can access their portal with the 'Request for Quotation' form. The Supplier will be created as a Website User.

    ![Supplier email if account not present]({{docs_base_url}}/v13/assets/img/buying/supplier-email-with-update-password.png)


    **If Supplier's account is present**: The system will send a Request for Quotation link to the Supplier. The Supplier must log in using his credentials to view the Request for Quotation form on the portal.

    ![Supplier email if account present]({{docs_base_url}}/v13/assets/img/buying/supplier-email-normal.png)

3. Either way, when the Supplier logs in, the following screen will be shown to them. From here they can send you a quotation:

    ![Supplier Quotation Screen]({{docs_base_url}}/v13/assets/img/buying/rfq-supplier-quotation.png)

    The Supplier has to enter the amount and notes (payment terms) on the form and click on Submit. In the Quotations section, previous quotations will be visible.

4. On submission, ERPNext will create a Supplier Quotation (draft mode) against the Supplier. The user has to review the Supplier Quotation and submit it. When all the items from the Request for Quotation have been quoted by a Supplier, the quote status is updated to 'Received' in the 'Suppliers' table of the Request for Quotation.

    ![RFQ status after supplier quote]({{docs_base_url}}/v13/assets/img/buying/rfq-supplier-quoted.png)

Read [Supplier Quotation](/docs/v13/user/manual/en/buying/supplier-quotation) to know more.

## 5. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/q85GFvWfZGI?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>


### 6. Related Topics
1. [Purchase Order](/docs/v13/user/manual/en/buying/purchase-order)
1. [Supplier](/docs/v13/user/manual/en/buying/supplier)
1. [Supplier Quotation](/docs/v13/user/manual/en/buying/supplier-quotation)
1. [Quotation](/docs/v13/user/manual/en/selling/quotation)
1. [Material Request](/docs/v13/user/manual/en/stock/material-request)

{next}
