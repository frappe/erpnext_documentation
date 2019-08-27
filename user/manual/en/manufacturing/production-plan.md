<!-- add breadcrumbs -->
# Production Plan

**A Production Plan helps in production and material planning for the Items planned for manufacturing. These production items can be committed via Sales Order (to Customers) or Material Requests (internally).**

Production Plan helps the user to plan production against multiple Sales Orders or the Material Requests. Also, it helps in Material Procurement planning for the raw material item, based on the quantity of finished products to be manufactured.

To access the Production Plan list, go to:

> Home > Manufacturing > Production > Production Plan

## 1. Prerequisites 
Before creating and using a Production Plan, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)
* [Material Request](/docs/user/manual/en/stock/material-request)
* [Sales Order](/docs/user/manual/en/selling/sales-order)
* [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials)
* [Routing](/docs/user/manual/en/manufacturing/routing)

## 2. How to Create a Production Plan
As mentioned earlier, a Production Plan can be used for planning the manufacture of Items against Sales Orders or Material Requests.

The common steps are:

1. Go to the Production Plan list, click on New.
1. Select whether to get items from a [Sales Order](/docs/user/manual/en/selling/sales-order) or a [Material Request](/docs/user/manual/en/stock/material-request).

A Production Plan can also be created manually where you can select the Items to manufacture.

### 2.1 Production Against Sales Orders

1. Select option as Sales Order from the 'Get Items From' drop-down list. The system will show the filters, using that you can pull the Sales Orders for the production. You don't need to use all these filters if you have only a few Sales Orders in a particular time frame.

  ![Production Plan fetch items]({{docs_base_url}}/assets/img/manufacturing/pp_fetch_from.png)

1. Click on Get Sales Orders to fetch sales orders based on the above filters.

  ![Sales Order Filters]({{docs_base_url}}/assets/img/manufacturing/sales_order_filter.png)

1. Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders. Items only for which a BOM is present will be fetched.
  ![Get items for Production Plan]({{docs_base_url}}/assets/img/manufacturing/get_items_wo.png)

1. On expanding a row in the Items to Manufacture table, you'll see an option to 'Include Exploded Items'. Ticking this includes raw materials of the sub-assembly items in the production process.

### 2.2 Production Against Material Requests

1. Select option as Material Request from the Get Items From drop-down list. The system will show the filters, using that we can pull the Material Requests for the production.

  <img class="screenshot" alt="Material Request Filters" src="{{docs_base_url}}/assets/img/manufacturing/material_request_filter.png">

1. Click on 'Get Material Request' to fetch material requests based on the above filters.

  <img class="screenshot" alt="Material Requests" src="{{docs_base_url}}/assets/img/manufacturing/material_requests.png">

1. Click on Get Items for Work Order to fetch the items from the above material requests.

  <img class="screenshot" alt="Material Request Item" src="{{docs_base_url}}/assets/img/manufacturing/material_request_items.png">

### 2.3 Planning for Material Requests

Clicking on the 'Get Raw Materials for Production' button will fetch the required raw material Items in the Material Request Plan table. For example, to manufacture 200 plastic canes, you need 100 raw plastic Nos but have only 20 in your Warehouse, then clicking this button will add a row with 80 in the Required Quantity column.

<img class="screenshot" alt="Material Request Plan" src="{{docs_base_url}}/assets/img/manufacturing/material_request_plan.png">

Use the following checkboxes to perform certain actions:

  * <b>Include Non Stock Items</b>: To include non-stock items in the material request planning. i.e. Items for which 'Maintain Stock' checkbox is unticked. Refer the [Item page](/docs/user/manual/en/stock/item#12-options-when-creating-an-item) for more details.
  * <b>Include Subcontracted Items</b>: To add subcontracted Item's raw materials if include exploded items is disabled.
  * <b>Ignore Existing Projected Quantity</b>: If enabled then the system will create the Material Request even if the user has already ordered or requested the respective items. For example if you need 100 quantity of raw material A and even if you already have 150, enabling this checkbox will add a request for 100 quantity of that raw material.
  * <b>For Warehouse</b>: User can set the Warehouse for which they want to create the material request. When creating Stock Entries during the production process, the system will look for raw material stock in this Warehouse.
  * <b>Download Materials Required</b>:- When this checkbox is ticked, the User will get the Excel sheet with the raw materials that are needed to complete this Production Plan. User can select the Warehouse to check the available quantity in the respective Warehouse. If the User has kept the 'For Warehouse' field as blank then the system will give the Excel sheet with raw materials and Warehouse-wise available quantity of the respective raw materials. Excel sheet will look similar to:

 <img class="screenshot" alt="Material Request Plan" src="{{docs_base_url}}/assets/img/manufacturing/material_request_excel.png"> 

### 2.4 After Submitting

Once the Production Plan is submitted, the User gets an option to make Work Orders for the production items and Material Requests for the raw materials.

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/make_po_mr.png">

### 2.5 Making work order for the sub-assembly items

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/nokia_phone_bom.png">

In the above screenshot, the User creates the Nokia Headphone first and then creates the Nokia Charger and then creates final finished goods.

Here, the User wants to make the work order for the Nokia Headphone and Nokia Charger, to do this, the user has to enable the field "Make Work Order for Sub Assembly Items" in the Production Plan against the item Nokia Lumia.

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/production_plan_for_subassembely.png">

On clicking make Work Order, the system will generate the Work Order for the sub-assembly items and the finished good items:

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/wo_against_the_production_plan.png">

## 3. Related Topics
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)
1. [Job Card](/docs/user/manual/en/manufacturing/job-card)
