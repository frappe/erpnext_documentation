<!-- add-breadcrumbs -->
# Quality Inspection

In ERPNext, you can mark your incoming or outgoing products for Quality
Inspection.

To enable this feature go to:
> Home > Stock > Tools > Quality Inspection 

## 1. Prerequisites
Before creating and using a Quality Inspection, it is advised that you create the following first:

* [Item](/docs/user/manual/en/stock/item)
* Enable Quality Inspection Criteria in the Item master:
    ![Enable Quality Inspection](/docs/assets/img/stock/enable-quality-inspection.png)

## 2. How to create a new Quality Inspection 

1. From a Purchase Receipt/Delivery note in the Draft stage, go the Item table's Quality Inspection field and click on Create a New Quality Inspection.
1. Select the inspection type whether Incoming (Purchase), Outgoing (Sales), or In Process (Manufacturing).
1. Select the Reference document type whether Purchase Receipt, Purchase Invoice, Delivery Note, Sales Invoice, or, Stock Entry.
1. Select the Item and set the sample size which will be inspected. Note that only Items for which Inspection Criteria is enabled in the Item master will be fetched.
1. The Quality Inspection Template set in the Item master will be fetched.
1. You can change who it's inspected by and also add who it's verified by.
1. Any additional Remarks about the Inspection can be added.
1. Save and Submit.

<img class="screenshot" alt="Quality Inspection" src="{{docs_base_url}}/assets/img/stock/quality-inspection.png">

## 3. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/WmtcF3Y40Fs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 4. Related Topics
1. [Purchase Receipt](/docs/user/manual/en/stock/purchase-receipt)
1. [Delivery Note](/docs/user/manual/en/stock/delivery-note)
1. [Stock Entry](/docs/user/manual/en/stock/stock-entry)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)