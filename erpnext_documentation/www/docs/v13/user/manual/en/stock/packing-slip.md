<!-- add-breadcrumbs -->
# Packing Slip

**A packing slip is a document that lists the items in a shipment.**

It is usually attached to the goods delivered.

From a single Delivery Note, multiple Packing Slips can be created. It is useful when the shipment is packed in different boxes. Each box can have a weight and number of Items it contains. For example, if you're shipping 20 chairs in 4 boxes, each box can contain 5 chairs with different Packing Slips for each box.

To access the Packing Slip list, go to:
> Home > Stock > Tools > Packing Slip
<p></p>
> Note: In order to create Packing Slips from a Delivery Note, the Delivery Note needs to be in the Draft stage.

## 1. Prerequisites
Before creating and using a Packing Slip, it is advised that you create the following first:

* [Delivery Note](/docs/user/manual/en/stock/delivery-note)


## 2. How to create a new Packing Slip
Usually, you should create a Packing Slip from a Delivery Note when it is in the Draft stage, however, if you want to create a Packing Slip manually, follow these steps.

1. Go to the Packing Slip list, click on New.
1. Select the Delivery Note.
1. Enter the From Package No of this Packing Slip.
1. Click on the Get Items button to fetch the Items and Quantities into the Items table.
1. Save.

Most of these details will be fetched if you create the Packing Slip from the Delivery Note.

<img class="screenshot" alt="Packing Slip" src="{{docs_base_url}}/assets/img/stock/packing-slip.png">


### 1.1 Additional options when creating a Packing Slip
**To Package No**: If there are multiple packages of the same type to be shipped at once then set the From and To Package numbers. For example, package numbers 1 to 5 in one Packing Slip, then package numbers 6 to 10 in the next Packing Slip and so on. This will be shown if you print then Packing Slip. Note that this will only work if you Shipment has that many quantities of the Items.

## 2. Features

### 2.1 Items table

* If this is a Batched Item, you'll have to select the Batch Number.
* The Quantity, UoM, Net Weight, and Weight UoM will be fetched from the Delivery Note.
* Page Break will create a page break just before this item when printing.

### 2.2 Package weight details

These details will be shown when printing the Packing Slip.

**Net Weight**: This is calculated as the sum of weights of all Items in the table.
**Gross Weight**: This is the final total weight including the weight of the packing materials used.
**Gross Weight UOM**: A UoM can be set here for the final weight of the product.

### 2.3 Letterhead
You can print your Packing Slip on your company's letterhead. Know more [here](/docs/user/manual/en/setting-up/print/letter-head).


### 2. Related Topics
1. [Quality Inspection](/docs/user/manual/en/stock/quality-inspection)
1. [Delivery Note](/docs/user/manual/en/stock/delivery-note)