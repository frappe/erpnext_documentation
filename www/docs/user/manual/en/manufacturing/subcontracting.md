<!-- add-breadcrumbs -->
# Subcontracting

**In subcontracting, you employ an external party to carry out tasks for your organization, especially manufacturing.**

Subcontracting is a type of job contract that seeks to outsource certain types
of work to other companies. It allows work on more than one phase of the
project to be done at once, often leading to quicker completion.

Subcontracting is practiced by various industries. For example, manufacturers
who make a number of products from complex components subcontract certain
components and package them at their facilities.  

If your business involves outsourcing certain processes to a third party Supplier where you supply the raw materials and the third party does the labor/production, you can track this by using the subcontracting feature of ERPNext.  

## 1. How to Set up Subcontracting

1. Create separate Items for the unprocessed and the processed product. For example, if you supply unpainted X to your Supplier and the Supplier returns you X, you can create two Items: “X-unpainted” and “X”.
2. Create a Warehouse for your Supplier so that you can keep track of Items supplied. (you may supply a month's worth of Items in one go).
3. For the processed Item, in the Item master, enable “Is Sub Contracted Item”.

  <img class="screenshot" alt="Sub-Contracting" src="{{docs_base_url}}/assets/img/manufacturing/subcontract.png">
  
### 1.1 Creating a BOM
Make a [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials) for the processed Item, with the unprocessed Items as sub-items. Let's consider a simple example, where you manufacture a pen. The processed
pen will be named under Bill of Materials(BOM), whereas, the nib, plastic, ink, etc. will be categorized as sub-items.

This BOM will be without Operations if all of the production work is done by the third party.

<img class="screenshot" alt="Sub-Contracting" src="{{docs_base_url}}/assets/img/manufacturing/subcontract2.png">

### 1.2 Creating a Purchase Order
Make a Purchase Order for the processed Item, the one for which you've created a BOM. When you “Save”, in the “Raw Materials Supplied”, all your un-processed Items will be updated based on your Bill of Materials. You can also select the Warehouse in which the raw materials would be reserved for subcontracting under Reserve Warehouse. 

1. The costs involved with the subcontracting process should be recorded in the Rate field of the Items table in the Purchase Order shown as follows:

  <img class="screenshot" alt="Sub-Contracting" src="{{docs_base_url}}/assets/img/manufacturing/subcontract3.png">

1. In the previous image, we are providing the subcontractor with 2 boxes of each of the 3 materials to manufacture 240 pens. The cost involved with one pen is 27 and the total cost for all pens is hence 6,480

1. You need to set 'Supply Raw Materials' as Yes since this Purchase Order is for subcontracting.

1. From a Purchase Order, select the raw materials to transfer to subcontractor:
  ![Sub-Contracting](/docs/assets/img/manufacturing/po_material_transfer_subcontract.gif)

1. Once the [Purchase Order](/docs/user/manual/en/buying/purchase-order#35-raw-materials-supplied) is submitted, you can view the reserved quantity of the item from the item dashboard as well.

  <img class="screenshot" alt="Sub-Contracting" src="{{docs_base_url}}/assets/img/manufacturing/subcontract3-reserved-material.png">

### 1.3 Creating Stock Entry to Transfer Raw Materials
Now that the raw materials are reserved, make a Stock Entry to deliver the raw material Items to your Supplier.

In the Purchase Order, click on Transfer > Material to Supplier. Set the Source and Target Warehouses. The Stock Entry will be of type 'Send to Subcontractor' where you transfer from one Warehouse to another. Tick 'From BOM' and select the BOM, enter the quantity, and click on the Get Items button.

<img class="screenshot" alt="Sub-Contracting" src="{{docs_base_url}}/assets/img/manufacturing/subcontract4.png">

### 1.4 Creating a Purchase Receipt to receive the finished items
Receive the Items from your Supplier using a [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt). You need to enter the Supplier Warehouse from where the raw materials will be taken and finished goods will be received in the Accepted Warehouse. Consider this like a backflush for subcontracting.

Click on Create > Purchase Receipt from the Purchase Order. Set the Accepted and Supplier Warehouses. Make sure to check the “Consumed Quantity” in the “Raw Materials” table so that the correct stock is maintained at the Supplier’s end. You need to select the Supplier's Warehouse where you'll receive the finished goods.

<img class="screenshot" alt="Sub-Contracting" src="{{docs_base_url}}/assets/img/manufacturing/subcontract5.png">

## 2. Notes
* Make sure that the “Rate” of processed Item is the processing rate
(excluding the raw material rate).

* ERPNext will automatically add the raw material rate for your
valuation purpose when you receive the finished Item in your stock.

* ERPNext will automatically default the 'Reserve Warehouse' in the Purchase Order
from the BOM. If not found in the BOM, it would default it from the default
Warehouse set in the Item. You can set the default Reserve Warehouse for all the Items in the Purchase Order from the 'Reserve Warehouse' field in the Raw Materials Supplied section.

## 3. Video

<iframe width="660" height="371" src="https://www.youtube.com/embed/ThiMCC2DtKo" frameborder="0" allowfullscreen></iframe>

## 4. Related Topics
1. [Purchase Order](/docs/user/manual/en/buying/purchase-order)
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)

{next}
