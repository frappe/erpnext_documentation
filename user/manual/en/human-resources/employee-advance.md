<!-- add-breadcrumbs -->
# Employee Advance

**Sometimes employees go outside for company's work and company pays some amount for their expenses in advance. This is when the employee can create an Employee Advance form where details such as the Purpose of Expense and Expense Amount can be recorded.**

Once the Employee Advance is created by the Employee, the Expense Approver can submit the advance record after verification. After Employee Advance gets submitted, the accountant releases the payment and makes the Payment Entry.

To access Employee Advance, go to:

> Human Resources > Expense Claims > Employee Advance 

## 1. Prerequisites

1. [Employee](/docs/user/manual/en/human-resources/employee)
1. [Department](/docs/user/manual/en/human-resources/department)
1. [Chart of Accounts](/docs/user/manual/en/accounts/chart-of-accounts)

## 2. How to create an Employee Advance
1. Go to: Employee Advance > New.
1. Select Employee to whom you need to give the advance.
1. Enter the Purpose and Advance Amount.
1. Select the Advance Account and Mode of Payment.
1. Save.

    <img class="screenshot" alt="Expense Claim" src="{{docs_base_url}}/assets/img/human-resources/employee-advance.png">

> Note: The Employee can only Save the Employee Advance but cannot Submit it. It can be only submitted by the Expense Approver.

## 3. Features

### 3.1 Employee Advance Submission

Employee Advance record can be created by any Employee but they cannot submit the record.

After saving Employee Advance, Employee should [Assign document to Approver](/docs/user/manual/en/using-erpnext/assignment.html). On assignment, approving user will also receive email notification. To automate email notification, you can also setup [Email Alert](/docs/user/manual/en/setting-up/notifications.html).

After verification, the Expense Approver can Submit (Accept) the Employee Advance form or Reject the request.

### 3.2 Make Payment Entry

After submission of Employee Advance record, accounts user will be able to create a [Payment Entry](/docs/user/manual/en/accounts/payment-entry) using the 'Create' button.

The Payment Entry will look like following:

<img class="screenshot" alt="Employee Advance Payment via Payment Entry" src="{{docs_base_url}}/assets/img/human-resources/employee-advance-payment-entry.png">


Alternatively, a [Journal Entry](/docs/user/manual/en/accounts/journal-entry) can also be created against the Employee Advance.


<img class="screenshot" alt="Employee Advance Payment via Journal Entry" src="{{docs_base_url}}/assets/img/human-resources/employee-advance-journal-entry1.png">

> Note: Make sure the Party Type is selected as Employee and the Reference Type is selected as Employee 
Advance.


<img class="screenshot" alt="Employee Advance Payment via Journal Entry" src="{{docs_base_url}}/assets/img/human-resources/employee-advance-journal-entry2.png">



On submission of the Payment Entry/ Journal Entry, the paid amount and status will be updated in Employee Advance record.

### 3.3 Adjust Advances on Expense Claim

Later when the employee claims the expense, an advance record can be fetched in the Expense Claim and linked to the claim record.


## Related Topics

1. [Expense Claim](/docs/user/manual/en/human-resources/expense-claim)



{next}
