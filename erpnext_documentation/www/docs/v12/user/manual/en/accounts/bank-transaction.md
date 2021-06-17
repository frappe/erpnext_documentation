<!-- add-breadcrumbs -->
# Bank Transaction

This form shows bank transactions in ERPNext. 

## 1. Prerequisites
Before using Bank Transaction Entry, it is advised that you create the following first:

1. [Bank](/docs/user/manual/en/accounts/bank)
1. [Bank Account](/docs/user/manual/en/accounts/bank-account)

## 2. How to use Bank Transaction
A Bank Transaction Entry is not intended to be created manually. It is automatically created using:

1. [Bank Reconciliation](/docs/user/manual/en/accounts/bank-reconciliation)
    Or
1. [Plaid Integration](/docs/user/manual/en/erpnext_integration/plaid_integration) to sync with Banks

### 2.1 Additional fields in Bank Transaction

* Date
* Status:
    * Pending
    * Settled
    * Unreconciled
    * Reconciled
* **Bank Account**: The Bank Account from which the transactions were made.

## 3. Features/Fields 

> These fields are updated via Bank Reconciliation and are not intended to be modified from here.

### 3.1 Currency and debit/credit

* **Debit**: The amount debited.
* **Credit**: The amount credited.
* **Currency**: The Currency in which the transaction was done.
* **Description:** A description for the statement.

### 3.2 Reference

**Reference Number**: A cheque or other reference number.

### 3.3 Payment Entries

* **Payment Document**: The document against which the transaction was made whether a Sales Invoice, Expense Claim, Purchase Invoice, Payment Entry, or Journal Entry.
* **Payment Entry**: The specific transaction. 
* **Allocated Amount**: The amount allocated for this particular transaction.

**Allocated Amount**: The total allocated amount.
**Unallocated Amount**: The total unallocated amount.
