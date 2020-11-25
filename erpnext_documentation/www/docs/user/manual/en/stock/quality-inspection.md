<!-- add-breadcrumbs -->
# Quality Inspection

In ERPNext, you can mark your incoming or outgoing products for Quality
Inspection.

To access this feature go to:
> Home > Stock > Tools > Quality Inspection

## 1. Prerequisites
Before creating and using a Quality Inspection, it is advised that you do the following first:

* **Create an [Item](/docs/user/manual/en/stock/item)**.
* **Enable Quality Inspection Criteria in the Item master**. On enabling either checkboxes, **submission** of a stock delivery/receipt document will be allowed only after a Quality Inspection is done against it:
    ![Enable Quality Inspection](/docs/assets/img/stock/quality-inspection-pre-requisite.png)
* (Optional) **Create a Quality Inspection Template**. You can add inspection parameters and acceptance criteria in the template, which can be easily fetched into any Quality Inspection. After saving the template, you can set this template in the Item Master (as shown above).
    ![Quality Inspection Template](/docs/assets/img/stock/quality-inspection-template.png)

## 2. How to create a new Quality Inspection

1. From a **Draft** Purchase Receipt/Delivery Note, go to the Item table's Quality Inspection field and click on Create a New Quality Inspection. You can also create a Quality Inspection for Job Card in order to monitor the quality of in-process items. In this case, you can create a Quality Inspection for the Production Item in Job Card.
1. Select the inspection type whether Incoming (Purchase), Outgoing (Sales), or In Process (Manufacturing).
1. Select the Reference Document Type whether Purchase Receipt, Purchase Invoice, Delivery Note, Sales Invoice, Stock Entry, or Job Card.
1. Select the Item and set the sample size which will be inspected. Note that only Items having Inspection Criteria enabled in the Item master, will be fetched.
1. The Quality Inspection Template set in the Item master will be fetched.
1. You can change who it's inspected by and also add who it's verified by.
1. Any additional Remarks about the Inspection can be added.
1. Save. Set the Status. Submit.

<img class="screenshot" alt="Quality Inspection" src="{{docs_base_url}}/assets/img/stock/quality-inspection.png">

## 3. Features
### 3.1 Formula Based Quality Checks
The acceptance of a parameter/check, in a Quality Inspection, can depend on a certain formula in many cases. The Readings table has a field called **Acceptance Criteria Formula** where you can specify a formula that determines whether a certain check is Accepted or Rejected.

<img class="screenshot" alt="Acceptance Criteria Formula" src="{{docs_base_url}}/assets/img/stock/acceptance-criteria-formula.png">

This formula depends on the many Reading fields in the Readings table. It can be set manually or via a template.

After setting it, update the readings and Save. The Status field in the Readings table rows is set automatically based on the formula for acceptance.

<img class="screenshot" alt="Acceptance Criteria Formula" src="{{docs_base_url}}/assets/img/stock/qi-formula-based.gif">

The status for the entire Quality Inspection can then be decided by the user.

## 4. Video
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
1. [Job Card](/docs/user/manual/en/accounts/job-card)
