# Vehicle Log

**Vehicle Log is used to enter Odometer readings, Fuel Expenses and Service Expense details.**

To access Vehicle Log, go to:

> Human Resources > Fleet Management > Vehicle Log


## 1. Prerequisites

Before creating a Vehicle Log, it is necessary that you create the following documents:

* [Vehicle](/docs/user/manual/en/human-resources/vehicle)


## 2. How to create a Vehicle Log

1. Go to Vehicle Log list, click on New.
1. Select License Plate and Employee.
1. Enter Odometer Reading information such as Date and Odometer (reading).
1. Enter Refueling Details [optional] such as Fuel Qty, Fuel Price, Supplier and Invoice Ref.

    <img class="screenshot" alt="Vehicle Log" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log1.png">


1. Additionally, Vehicle Service Details can also be added as shown (optional).

    <img class="screenshot" alt="Vehicle Log" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log2.png">

1. Save. Once the information is saved, the Model and Make values will be automatically fetched.


	

## 3. Features

Fleet Management in ERPNext allows you to automatically create an [Expense Claim](/docs/user/manual/en/human-resources/expense-claim) against your Vehicle Expenses.

### 3.1 Make Expense Claim against Vehicle Expenses

Click on Make Expense Claim button. This button appears only in case of Submitted Vehicle Logs.

<img class="screenshot" alt="Expense Claim Button" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log-expense-claim-button.png">

When you click on 'Make Expense Claim',

  1. The Date, Employee, Expense total are fetched over to the created Expense Claim.
  2. The sum of Fuel Expenses and Service Expenses is calculated and fetched over to Expense Claim Amount.
  3. Employee can submit the Expense Claim for further processing.

	<img class="screenshot" alt="Vehicle Log" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log-expense-claim.png">

## 4. Related Topics

1. [Expense Claim](/docs/user/manual/en/human-resources/expense-claim)



