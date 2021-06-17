<!-- add-breadcrumbs -->
# Dunning

**A document to be sent as a persistent demand for debt payment.**

Dunning is a document to store and send as a persistent demand for debt payment against an unpaid Sales Invoice.

To access the Dunning list, go to:
> Home > Accounting > Dunning

## 1. Prerequisites
Before creating a Dunning, there must be a Sales Invoice since it is created against it.

* [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)

## 2. How to create a Dunning
A Dunning is created against a Sales Invoice.

For manual creation, follow these steps:

1. Go to the Dunning list and click on New.
1. Select an overdue Sales Invoice.
1. Set Dunning Type in the dunning type link field.
1. Set printing setting for the print template of the Dunning letter.
1. The posting date and time will be set to current, you can edit after you tick the checkbox below Posting Time to make a backdated entry.
1. Save and Submit.

 ![Dunning example](/docs/v12/assets/img/accounts/dunning.gif)

### 2.1 What is a Dunning Type
Dunning Type stores default values for overdue days, dunning fee, interest rate and text blocks to be included. For example, a Dunning Type "First Notice" will not have any fees, but Dunning Type "Second Notice" will have a dunning fee and interest charged on the outstanding amount.

 ![Dunning Type](/docs/v12/assets/img/accounts/dunning-type.png)

### 2.2 Statuses

These are the statuses that are auto-assigned to Dunning.

* **Draft**: A draft is saved but yet to be submitted.
* **Unresolved**: The Dunning is unresolved when it is submitted but no payments have been received.
* **Resolved**: The Dunning is resolved when the outstanding payment has been received.
* **Cancelled**: A cancelled status is a cancelled Dunning document.

## 3. Payment

A Payment Entry can be created from a Dunning. It will be pulled together with the Sales Invoice details it is against.
 
![Dunning Payment](/docs/v12/assets/img/accounts/dunning-payment.png)

## 4. Related Topics
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Sales Invoice](/docs/user/manual/en/accounts/purchase-invoice)
