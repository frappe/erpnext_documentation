<!-- add-breadcrumbs -->
# Request for Quotation

**A Request for Quotation is a document that an organization sends to one or more suppliers asking a quotation for items.**

![Buying Flow](/docs/assets/img/buying/buying_flow_rfq.png)

To access Request for Quotation, go to:
> Home > Buying > Purchasing > Request for Quotation

## 1. Prerequisites
Before creating and using a Request for Quotation, it is advised that you create the following first:

* [Supplier](/docs/user/manual/en/buying/supplier)
* [Item](/docs/user/manual/en/stock/item)

## 2. How to create a Request For Quotation
1. Go to the Request For Quotation list, click on New.
2. Enter the date.
3. Choose the supplier to whom Request for Quotation is to be sent.
4. In the next table, enter items, quantity and the target warehouse where you'll be sending the items.
1. Warehouse can be left blank if 'Maintain Stock' is unticked for the item.
5. Save and submit.

A Request for Quotation (RFQ) can also be created from a submitted Material Request. Once an RFQ is created, you can print and send them the PDF which will have all the details you entered relevant to the RFQ and receive reply by mail. You can also get their reply (Supplier Quotation) from ERPNext itself, see section _3.1 Supplier Quotation by User_. However, for a large number of items, your supplier may be more comfortable with an Excel sheet etc.,

## 3. Features

### 3.1 Get items from
The items in the items table can be fetched from other documents. The options are: Material Request, Opportunity, and Possible Supplier.

* **Material Request**: Items will be fetched from a submitted Material Request that you select. A Material Request can be searched with some matching words and a date range can also be selected to filter the Material Requests.

* **Opportunity**: Items will be fetched from a saved Opportunity. A date range can be selected here also.

* **Possible Supplier**: Select a possible supplier. Then if you have any submitted Material Requests against this supplier, items can be fetched from that.

### 3.2 The Get Suppliers button
Instead of entering the suppliers manually in the table, you can also fetch them using this button. When you click on the Get Suppliers button, you will see a field 'Get Suppliers By'. There are two options to fetch suppliers: by tags or by groups. 

* **By tag**: Go to 'Tag Category' via searching from the search bar. You must have created tags here first and assigned them the the DocType Supplier in the Buying module. Then you can select by Tag and enter a get. On clicking Add 'All Suppliers', suppliers with matching tags will be fetched.

* **By Group**: Select 'Supplier Group' and choose the supplier group from which suppliers need to be added. For example, if you select Hardware, all your hardware suppliers will be added so that you can get a quote from all of them.

In the Supplier table, on expanding a row with the inverted triangle, you'll see an option 'Download PDF' which will open a PDF of the RFQ.

### 3.3 Message for Supplier
Enter any additional messages for the Supplier in this field. This field can be auto filled using an 'Email Template'. The field to select an Email Template is just above Message for Supplier.

### 3.4 Terms and Conditions
In Sales/Purchase transactions there might be certain Terms and Conditions based on which the Supplier provides goods or services to the Customer. You can apply the Terms and Conditions to transactions and they will appear when printing the document. To know about Terms and Conditions, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions)

### 3.5 Print Settings
#### Letterhead
You can print your request for quotation/purchase order on your company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).

'Group same items' will group the same items added multiple times in the items table. This can be seen when you print it.

#### Print Headings
Titles of your documents can be changed. Know more [here](/docs/user/manual/en/setting-up/print/print-headings).

### 3.6 More

**Link to material requests button**: This button links the Request for Quotation to any Material Requests. The items should be the same in the Request for Quotation and the Material Request.

![Link to Material Request]({{docs_base_url}}/assets/img/buying/link-to-material-request.png)

Now, when the Request for Quotation is saved, you can see in the Dashboard that it is linked to the Material Request.
If there are multiple Material Requests with the same items, then the link will be created with the newest Material Request.

## 4. Creating a Supplier Quotation after RFQ
After creation of Request for Quotation, there are two ways to generate Supplier Quotation from Request for Quotation.

### 4.1 Supplier Quotation by User

1. Open Request for Quotation and click on **Supplier Quotation > Create**.

    ![Supplier Quotation from RFQ]({{docs_base_url}}/assets/img/buying/make-supplier-quotation-from-rfq.png)

2. Select the Supplier, click on the supplier again. In this page, click on the + next to 'Supplier Quotation'. A new Supplier Quotation page will be opened, user has to enter the quantity, rate and submit it.

    ![Supplier Quotation from Supplier]({{docs_base_url}}/assets/img/buying/supplier-quotation-from-sup.png)
    
### 4.2 Supplier Quotation from Supplier

1. If a [Contact](/docs/user/manual/en/CRM/contact) is created for the Supplier and an email address is associated with the Contact, the Contact details and the email address will be fetched on selecting the Supplier. Create a Contact and email address if not present already.

2. Click on 'Send Supplier Emails' button.

    **If the Supplier's account is not present**: The system will create Supplier's account and send details to the Supplier. The Supplier will need to click on the link(Password Update) present in the email. After the password update,Supplier can access his portal with the Request for Quotation form. The Supplier will be created as a Website User.

    ![Supplier email if account not present]({{docs_base_url}}/assets/img/buying/supplier-password-update-link.png)

    
    **If Supplier's account is present**: System will send Request for Quotation link to Supplier, Supplier has to login using his credentials to view the Request for Quotation form on portal. 

    ![Supplier email if account present]({{docs_base_url}}/assets/img/buying/send-rfq-link.png)

3. Either way, when the Supplier logs in, the following screen will be shown to them. From here they can send you a quotation:

    ![Supplier Quotation Screen]({{docs_base_url}}/assets/img/buying/rfq-supplier-quotation.png)

    The supplier has to enter amount and notes (payment terms) on the form and click on submit. In the Quotations section, previous quotations will be visible.

4. On submission, system will create Supplier Quotation (draft mode) against the supplier. The user has to review the Supplier Quotation and submit it. When all items from the Request for Quotation have been quoted by a Supplier, the quote status is updated to 'Received' in the Supplier table of 'Request for Quotation'.

    ![RFQ status after supplier quote]({{docs_base_url}}/assets/img/buying/rfq-supplier-quoted.png)

## 5. No quote from Supplier

If a Supplier indicates that they will not provide a quotation for the items, this can be indicated in the RFQ document by checking the 'No Quote' box after the Request for Quotation has been submitted. The No Quote box can be seen on expanding a Supplier row by clicking on the inverted triangle at the right-hand side.

![No Quote from Supplier]({{docs_base_url}}/assets/img/buying/no-quote-supplier.png)

To know about creating a Supplier Quotation, [click here](/docs/user/manual/en/buying/supplier-quotation).

## 6. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/q85GFvWfZGI?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>


### 7. Related Topics
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Supplier Quotation](/docs/user/manual/en/buying/supplier-quotation)
1. [Quotation](/docs/user/manual/en/selling/quotation)
1. [Material Request](/docs/user/manual/en/stock/material-request)

{next}