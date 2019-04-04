<!-- add-breadcrumbs -->
# Material Request

A Material Request is a simple document identifying a requirement of a set of
Items (products or services) for a particular reason.

A Material Request can be of type:

* Purchase - If the request material is to be purchased.
* Material Transfer - If the requested material is to be shifted from one warehouse to another.
* Material Issue - If the requested material is to be Issued.
* Manufacture - If the requested material is to be Produced.
* Customer Provided - If the requested material is to be provided by Customer.

<img class="screenshot" alt="Material Request" src="{{docs_base_url}}/assets/img/buying/material-request-flowchart.png">

### 1. How to create a Material Request
1. Go to **Stock > Stock Transactions > Material Request > New**.
1. Enter the required by date.
1. Select from one of the types as listed above.
1. Select the Item and set the quantity.
1. Select the Warehouse for which items is required.
1. You can change the Required by Date for items in this table.
1. Save and Submit.

<img class="screenshot" alt="Material Request" src="{{docs_base_url}}/assets/img/buying/material-request.png">

A Material Request can be generated:

  * Automatically from a Sales Order.
  * Automatically when the Projected Quantity of an Item in stores reaches a particular level.
  * Automatically from your Bill of Materials if you use Production Plan to plan your manufacturing activities.
  * If your Items are inventory items, you must also mention the Warehouse where you expect these Items to be delivered. This helps to keep track of the [Projected Quantity](/docs/user/manual/en/stock/projected-quantity) for this Item.


The User can also raise a [Request For Quotation](/docs/user/manual/en/buying/request-for-quotation) against a Material Request. To create a Request For Quotation the user can click on 'Make'.

> Info: Material Request is not mandatory. It is ideal if you have centralized
buying so that you can collect this information from various departments.

<div>
  <div class="embed-container">
    <iframe src="https://www.youtube.com/embed/55Gk2j7Q8Zw?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
  </div>
</div>

#### 2. Related Topics
1. [Item](/docs/user/manual/en/stock/item)
1. [Auto Creation Of Material Request](/docs/user/manual/en/stock/articles/auto-creation-of-material-request)
