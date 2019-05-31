<!-- add-breadcrumbs -->
# Supplier Scorecard

**A Supplier Scorecard is an evaluation tool used to assess the performance of suppliers.**

Supplier scorecards can be used to keep track of item quality, delivery, and responsiveness of suppliers across long periods of time. This data is typically used to help in purchasing decisions.
A Supplier Scorecard is manually created for each supplier.

## 1. How to create Supplier Scorecard

1. Go to **Buying > Supplier Scorecard > Supplier Scorecard > New**.
2. Select a supplier to score.
3. Select the evaluating period whether weekly, monthly, or yearly.
4. Setup the scoring function (details in next section).
5. A supplier scorecard is created for each supplier individually. Only one supplier scorecard can be created for each supplier. 
<img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/supplier-scorecard.png">

## 2. Features
### 2.1 Scoring Setup
The supplier scorecard consists of a set evaluation periods, during which the performance of a supplier is evaluated. This period can be weekly, monthly or yearly. The current score is calculated from the score of each evaluation period based on the weighting function. The default formula is linearly weighed over the previous 12 scoring periods. 
<img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/supplier-scorecard-weighing.png">
This formula is customizable.

#### Supplier Standings

The supplier standing is used to quickly sort suppliers based on their performance. These are customizable for each supplier. 

The scorecard standing of a supplier can also be used to restrict suppliers from being included in Request for Quotations or being issued Purchase Orders. The following screen can be seen on expanding a row in the 'Scoring Standings' table, click on the downward facing arrow.
<img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/supplier-scorecard-standing.png">

### 2.2 Criteria Setup
A supplier can be evaluated on several individual evaluation criteria, including (but not limited to) quotation response time, delivered item quality, and delivery timeliness. These criteria are weighed to determine the final period score. 

To create a  new Criteria, go to Buying > Supplier Scorecard > Supplier Scorecard Criteria:
<img class="screenshot" alt="Purchase Order" src="{{docs_base_url}}/assets/img/buying/supplier-scorecard-criteria.png">

Note: Criteria weights for a scorecard should add up to 100. 

### 2.3 Supplier Scorecard Variables
The method for calculating each criteria is determined through the Criteria Formula field, which can use a number of pre-established variables. This can be seen in the preceding screenshot.

The value of each of these variables is calculated over the scoring period for each supplier. Examples of such variables include:

 - The total number of items received from the supplier
 - The total number of accepted items from the supplier
 - The total number of rejected items from the supplier
 - The total number of deliveries from the supplier
 - The total amount (in dollars) received from a supplier

![Supplier Scorecard variable](/docs/assets/img/buying/supplier-scorecard-variables.png)

Variables are pre-set, additional variables can be added through server-side customizations. Tick the Custom checkbox if the variable you're creating is for a custom field.

The criteria formula should be customized to evaluate the suppliers in each criteria in a way that best fits the company requirements.

### 2.4 Evaluation Formulas
The evaluation formula uses the pre-established or custom variables to evaluate an aspect of supplier performance over the scoring period. Formulas can use the following mathematical functions:

* addition: + 
* subtraction: -
* multiplication: *
* division: /
* min: min(x,y)
* max: max(x,y)
* if/else: (x) if (formula) else (y)
* less than: <
* greater than: >
* variables: {variable_name}

It is crucial that the formula be solvable for all variable values. This is most often an issue if the value resolves to 0. For example:
```
{total_accepted_items} / {total_received_items}
```

This example would resolve to 0 / 0 in periods where there are no received items, and therefore should have a check to protect in this case:
```
({total_accepted_items} / {total_received_items}) 
if {total_received_items} > 0
else 1.
```

### 2.5 Evaluating the Supplier
An evaluation is generated for each Supplier Scorecard Period by clicking the "Generate Missing Scorecard Periods" button. The supplier's current score can be seen, as well as a visual graphic showing the performance of the supplier over time. Any actions against the supplier are also noted here, including warnings when creating RFQs and POs or preventing these features for this supplier altogether.

### 3. Related Topics
1. [Supplier](/docs/user/manual/en/buying/supplier)
1. [Supplier Quotation](/docs/user/manual/en/buying/supplier-quotation)

{next}