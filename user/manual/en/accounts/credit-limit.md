<!-- add-breadcrumbs -->
# Credit Limit

**Credit Limit is the maximum amount of credit you are willing to offer to a customer.**


A credit limit is the maximum amount of credit that a financial institution or
other lender will extend to a debtor for a particular line of credit. From a
customer's perspective, it is the maximum amount of goods or services he can get without paying upfront.

You can set the Credit Limit in customer, customer group, and in the company.
When a sales order or a sales invoice is submitted, the credit limit will be checked.

The order of precedence is as follows:

* Credit Limit set in Customer
* Credit Limit set in Customer Group
* Credit Limit set in Company


## 1. How to Set Credit Limit
1. Go to: **Selling > Sales > Customer > Customer**.
1. Under Credit Limit and Payment Terms section, set the Credit Limit.
1. If you leave the Credit Limit as the default, i.e., 0, it has no effect.
1. Save.

<img class="screenshot" alt="Credit Limit" src="{{docs_base_url}}/assets/img/accounts/customer-credit-limit.png">

## 2. Features
### 2.1 Credit Controller
You can allow users with a specific role to override the credit limit validation and submit a sales order or sales invoice even when a customer's credit limit is fully utilised.

To set the credit controller role:

1. Go to: **Accounting > Settings > Accounts Settings**
1. Set the role in Credit Controller field.

<img class="screenshot" alt="Credit Limit" src="{{docs_base_url}}/assets/img/accounts/credit_controller_role.png">

### 2.2 Bypass Credit Limit Check for Sales Order

For specific customers, you can set the credit limit to be checked against the cumulative amount of the outstanding sales invoices and not the sales orders. You can do so by ticking 'Bypass credit limit check at Sales Order' checkbox in 'Credit Limit and Payment Terms' section of the customer.

<img class="screenshot" alt="Customer Credit Limit" src="{{docs_base_url}}/assets/img/crm/customer-credit-limit.png">


### 2.3 Credit Limit for Customer Groups
To set credit limit at Customer Group Level:

1. Go to **Selling > Customers > Customer Group**.
1. Open the Customer Group and set the Credit Limit.

### 2.4 Credit Limit for Company
To set credit limit at Company level:

1. Go to **Accounting > Masters and Accounts > Company**.
1. Open the Company and set the Credit Limit.

### 3. Related Topics
1. [Payment Entry](/docs/user/manual/en/accounts/payment-entry)
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Customer](/docs/user/manual/en/CRM/customer)
