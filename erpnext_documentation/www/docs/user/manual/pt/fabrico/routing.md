<!-- add-breadcrumbs -->
# Routing

**Routing is a template of BOM Operations.**

A Routing stores all Operations along with the description, hourly rate, operation time, batch size, etc. Creating a Routing for your BOM Operations is useful when similar Operations are used for manufacturing different items.

To access the Routing list, go to:
> Home > Manufacturing > Bill of Materials > Routing

## 1. Prerequisites
* [Operation](/docs/user/manual/en/manufacturing/operation)
* [Workstation](/docs/user/manual/en/manufacturing/workstation)

## 2. How to Create a Routing
1. Go to the Routing list, click on New.
1. Enter a name for the Routing.
1. Enter the Operations in the BOM Operation table:
    1. Select the Operation.
    1. The default Workstation will be fetched.
    1. Enter the Hourly Rate for running this Operation.
    1. Enter the Operation Time in minutes.
    1. Enter the Batch Size, i.e. the number of units processed in this Operation.
    1. The Operating Cost will be calculated based on the Hourly Rate and the Operation Time.
1. Save.

    ![Routing](/docs/assets/img/manufacturing/routing.png)

Once created, a Routing can be selected in a BOM to fetch the Operations stored in the Routing.
![Routing BOM](/docs/assets/img/manufacturing/routing-bom.png)

## 2. Related Topics
1. [Work Order](/docs/user/manual/en/manufacturing/work-order)
1. [Bill Of Materials](/docs/user/manual/en/manufacturing/bill-of-materials)

{next}