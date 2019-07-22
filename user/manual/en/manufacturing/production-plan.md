# Production Plan

Production Plan helps the user to plan production against multiple Sales Orders or the Material Requests. Also, it helps in Material Procurement planning for the raw-material item, based on the quantity of finished product to be manufactured.

To use the Production Plan, go to:

> Home > Manufacturing > Production > Production Plan

<img class="screenshot" alt="Production Plan" src="{{docs_base_url}}/assets/img/manufacturing/production_plan.png">

## Planning for Production

### Production Against Sales Orders

* Select option as Sales Order from the 'Get Items From' drop-down list. The system will show the filters, using that we can pull the Sales Orders for the production.

<img class="screenshot" alt="Sales Order Filters" src="{{docs_base_url}}/assets/img/manufacturing/sales_order_filter.png">

* Click on Get Sales Orders to fetch sales orders based on above filters.

<img class="screenshot" alt="Sales Orders" src="{{docs_base_url}}/assets/img/manufacturing/sales_orders.png">

* Click on 'Get Items for Work Order' to fetch the items from the above Sales Orders.

<img class="screenshot" alt="Sales Order Item" src="{{docs_base_url}}/assets/img/manufacturing/sales_order_items.png">

* Include Exploded Items: This includes subassembly items of Raw Materials in the production.

### Production Against Material Requests

* Select option as Material Request from the Get Items From drop-down list. The system will show the filters, using that we can pull the Material Requests for the production.

<img class="screenshot" alt="Material Request Filters" src="{{docs_base_url}}/assets/img/manufacturing/material_request_filter.png">

* Click on 'Get Material Request' to fetch material requests based on above filters.

<img class="screenshot" alt="Material Requests" src="{{docs_base_url}}/assets/img/manufacturing/material_requests.png">

* Click on Get Items for Work Order to fetch the items from the above material requests.

<img class="screenshot" alt="Material Request Item" src="{{docs_base_url}}/assets/img/manufacturing/material_request_items.png">

## Planning for Material Requests

* Click on the 'Get Raw Materials for Production' button to fetch raw materials required in the production.

<img class="screenshot" alt="Material Request Plan" src="{{docs_base_url}}/assets/img/manufacturing/material_request_plan.png">

Use the following checkboxes to perform certain actions:
  * <b>Include Non Stock Items</b>: To  include non-stock items in the material request planning.
  * <b>Include Subcontracted Items</b>: To add subcontracted item's raw materials if include exploded items is disabled
  * <b>Ignore Existing Projected Quantity</b>: If enabled then the system will create the Material Request even if the user has already ordered or requested the respective items.
  * <b>For Warehouse</b>: User can set the Warehouse for which they want to create the material request.
  * <b>Download Materials Required</b>:- When this checkbox is ticked, the User will get the Excel sheet with the raw materials that are needed to complete this production plan. User can select the Warehouse to check the available quantity in the respective Warehouse. If the User has kept the 'For Warehouse' field as blank then the system will give the Excel sheet with raw materials and Warehouse-wise available quantity of the respective raw materials. Excel sheet will look similar to:

 <img class="screenshot" alt="Material Request Plan" src="{{docs_base_url}}/assets/img/manufacturing/material_request_excel.png"> 

## Provision To Make Work Order and Material Request

Once the Production Plan is submitted, the user gets an option to make Work Orders for the production items and Material Requests for the raw materials.

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/make_po_mr.png">

### What if user wants to make work order for the sub-assembely items?

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/nokia_phone_bom.png">

In the above example, the User creates the Nokia Headphone first and then creates the Nokia Charger and then creates final finished goods. Here, the User wants to make the work order for the Nokia Headphone and Nokia Charger, to do this, the user has to enable the field "Make Work Order for Sub Assembly Items" in the Production Plan against the item Nokia Lumia.

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/production_plan_for_subassembely.png">

* On clicking make Work Order, the system will generate the Work Order for the sub-assembly items and the finished good items:

<img class="screenshot" alt="Make PO or MR" src="{{docs_base_url}}/assets/img/manufacturing/wo_against_the_production_plan.png">
