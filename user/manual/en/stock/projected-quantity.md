<!-- add-breadcrumbs -->
# Projected Quantity

**Projected Quantity is the level of stock that is predicted for a particular Item based on the current stock levels and other requirements.**

It is the quantity of gross inventory that includes supply and demand in the past which
is done as part of the planning process.

The projected inventory is used by the planning system to monitor the reorder
point and to determine the reorder quantity. The projected Quantity is used by
the planning engine to monitor the safety stock levels. These levels are
maintained to serve unexpected demands.

Having tight control of the projected inventory is crucial to determine
shortages and to calculate the right order quantity.

<img class="screenshot" alt="Projected Quantity" src="{{docs_base_url}}/assets/img/stock/projected_quantity.png">

The formula to calculate projected quantity is as follows:

*Projected Qty = Actual Qty + Planned Qty + Requested Qty + Ordered Qty - Reserved Qty*

  * **Actual Qty**: Quantity available in the Warehouse. This is the actual physical stock you have.
  * **Planned Qty**: Quantity, for which, Work Order has been raised, but is pending to be manufactured.
  * **Requested Qty**: Quantity requested for purchase, but not ordered. Quotation created but not Sales Order.
  * **Ordered Qty**: Quantity ordered for purchase, but not received. Sales Order submitted but not Delivery Note.
  * **Reserved Qty**: Quantity ordered for sale, but not delivered. Updates when a Sales Order is submitted.
  * **Delivered quantity** It is updated when a Delivery Note is created. If five out of ten items are delivered, this field will be updated as 5.
  * **Work Order quantity**: Similar to Delivered quantity, it gets updated when you create a Work Order for the items in the Sales Order.

#### Related Topics
1. [Warehouse](/docs/user/manual/en/stock/warehouse)
1. [Material Request](/docs/user/manual/en/stock/material-request)