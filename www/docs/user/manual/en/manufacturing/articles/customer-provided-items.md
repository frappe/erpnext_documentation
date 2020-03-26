<!-- add-breadcrumbs -->
# Customer Provided Items

In Contract Manufacturing, in some cases, the Customer provides specific items as one or few of the BOM components. These items cannot be received using a 'Buying Cycle' since that will mean making Customer as a Supplier at the same time. It will also go through each doctype in the cycle.

In this feature, Customer Provided Item is received through 'Stock Entry' with type 'Material Receipt' from a 'Material Request' with type 'Customer provided'. This feature is used when someone subcontracts the manufacturing process to you and supplies the raw materials.

<img alt="Customer Provided Material Request" class="screenshot" src="/docs/assets/img/articles/material-request-customer-provided.png">

Here are the steps on how to setup a 'Customer Provided' item.

1.  Got to [Item Doctype](/docs/user/manual/en/stock) and add a new 'Customer Provided' item.

    > Home > Stock > Items and Pricing > Item

2.  In the 'Purchase, Replenishment Details' section, check 'Is Customer
    Provided' and set a default Customer. Note that 'Is Purchase Item' needs to be unticked to use this feature.

    <img alt="Item Purchase Details" class="screenshot" src="{{docs_base_url}}/assets/img/articles/item-customer-provided.png">

How to receive a 'Customer Provided' Item?

1.  If a 'Production Plan' is used, 'Material Request' for this item can be auto created. That is, the item to be manufactured is fetched first via Sales Order or Material Request, Items are fetched for the Work Order using the 'Get Items for Work Order' button, then click on the 'Get Raw Materials for Production' button.

    <img alt="Material Request in Production Plan" class="screenshot" src="{{docs_base_url}}/assets/img/articles/material-request-production-plan.png">

2. Once a component in a BOM is set as 'Customer Provided' and 'Material Request' is created from a 'Production Plan', it will create both 'Material Request' with type 'Purchase' and 'Customer Provided'. From there, a 'Stock Entry' with purpose 'Material Receipt' can be created.

   <img alt="Stock Entry from Material Request" class="screenshot" src="{{docs_base_url}}/assets/img/articles/create-mr-from-production-plan.png">

3. A 'Material Request' can have multiple 'Stock Entry' - Material Receipt. It
   will reflect it in the status.

4. Customer will be able to track their 'Material Requests' in a Web Portal
   'Material Requests'. The portal is filtered to show only the 'Material Request' of the customer.

   <!-- <img alt="Partial Delivery from Stock Entry" class="screenshot" src="{{docs_base_url}}/assets/img/articles/partial-delivery-mr.png"> -->

