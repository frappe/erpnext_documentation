<!-- add-breadcrumbs -->
# Introduction

ERPNext comes batteries included for all requirements of a manufacturing business like maintaining Warehouses, Workstation / Machine, Operations, Finished Goods, Raw Materials, Bill of Materials tracking, Work Order planning and execution, procurement, and a lot more.

<img class="screenshot" alt="BOM" src="{{docs_base_url}}/v13/assets/img/manufacturing/onboarding.png">

## 1. Master Data

The Manufacturing module in ERPNext helps you to maintain Warehouses(location), Workstations, Operations, Finished Goods, and Raw Materials. For manufacturing Operations and their respective Workstations are important, which can be configured based on the Finished Goods in the Bill of Materials. Warehouses are useful to store the Raw Materials and the Finished Goods. In ERPNext, users can create separate Warehouse to keep Raw Materials, and Finished Goods.

More details are as below:

1. [Warehouse](/docs/v13/user/manual/en/stock/warehouse)
1. [Workstation / Machine](/docs/v13/user/manual/en/manufacturing/workstation)
1. [Operation](/docs/v13/user/manual/en/manufacturing/operation)
1. [Raw Material / Finished Good](/docs/v13/user/manual/en/stock/item)
1. [Routing](/docs/v13/user/manual/en/manufacturing/routing)


## 2. Transaction Data

The Manufacturing module in ERPNext helps you to maintain a multilevel Bill of Materials (BOMs) for your Items. It helps in product costing, production planning, creating work orders for your manufacturing shop floors, creating job cards, and planning inventory by getting your material requirements via BOMs (also called [Material Requirements Planning or MRP](http://erpnext.com/blog/general/what-is-mrp-and-do-yo…)).

More details are as below:

1. [Bill Of Materials](/docs/v13/user/manual/en/manufacturing/bill-of-materials)
1. [Work Order](/docs/v13/user/manual/en/manufacturing/work-order)
1. [Job Card](/docs/v13/user/manual/en/manufacturing/job-card)
1. [Production Plan](/docs/v13/user/manual/en/manufacturing/production-plan)

## 3. Types of Production Planning

Broadly, there are three types of Production Planning Systems:

 * __Make to Stock:__ In these systems, production is planned based on a forecast and the Items are then sold to distributors or customers. All fast-moving consumer goods that are sold in retail shops like soaps, packaged water, etc. and electronics like phones are made to stock.
 * __Make to Order:__ In these systems, items are manufactured only after the customer places an order of a certain number according to the customer's requirement. For example, a wedding cake.
 * __Engineer to Order:__ In this case, each sale is a separate project and has to be designed and engineered to the requirements of the customer. Common examples of this are any custom business-like furniture, machine tools, specialty devices, metal fabrication, etc.

Most small and medium-sized manufacturing businesses are based on a make to order or engineer to order system and so is ERPNext.

For engineer to order systems, the Manufacturing module should be used along with the [Project module](/docs/v13/user/manual/en/projects).

## 4. Manufacturing impact on Inventory

Work order status is dependent upon the stock transactions made against it. In ERPNext, you can transfer the raw materials required to make finished goods from Store to Work In Progress Warehouse. From Work-In-Progress warehouse the raw materials can be consumed using the Stock Entry. You get the option to either bulk consume the raw materials and add the finished good or consumed the materials first and then add the finished good.

## 5. ERPNext Manufacturing Demo

Check out the following video to know about features in the manufacturing module.

<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/xE74wdQU5cc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

<!-- <img class="screenshot" alt="Task" src="{{docs_base_url}}/v13/assets/img/manufacturing/manufacturing.png"> -->

{next}
