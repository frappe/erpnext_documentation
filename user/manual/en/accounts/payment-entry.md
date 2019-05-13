<!-- add-breadcrumbs -->
# Payment Entry

Payment Entry can be made against following transactions.

* Sales Invoice.
* Purchase Invoice.
* Sales Order (Advance Payment).
* Purchase Order (Advance Payment).
* Expense Claim.

#### 1. How to make a Payment Entry
On submitting a document against which Payment Entry can be made, you will find Make Payment button.

1. Go to: **Accounts > Billing > Payment Entry > New**.
1. You can change the posting date.
1. Select the Payment Type.
1. Select the Party Type.
1. Select the Party, name will be fetched automatically.
1. Set the Account Paid To and Account Paid From.
1. Enter the amount paid.
1. Save and Submit.

You will have to fill in a lot of missing details if you create Payment Entry directly. Following are the detailed steps for payment entry via an invoice where some of the details are already fetched.

#### 1.1 Mode of Payment
In the Payment Entry, select Mode of Payment (eg: Bank, Cash, Wire Transfer). In the Mode of Payment master, default Account can be set. This default payment Account will fetch into Payment Entry.

<img class="screenshot" alt="Making Paymentt" src="{{docs_base_url}}/assets/img/accounts/payment-entry-2.gif">

#### 1.2 Payment Amount

Enter actual payment amount received from the Customer or paid to the Supplier or Employee.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-3.png">

#### 1.3 Allocate Amount

If creating Payment Entry for the Customer, Payment Amount will be allocated against Sales Invoice.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-4.gif">

On the same lines, when creating Payment Entry for a Supplier, Payment Amount will be allocated against Purchase Invoice.

You Entry can be created directly from **Account > Payment Entry > New**. In the new entry, on selection of the Party (Customer/Supplier), all the outstanding Invoices and open Orders will be fetched for party. The Payment Amount will be auto-allocated, preferably against invoice.

#### 1.4 Deductions
When making payment entry, there could be some difference in the actual payment amount and the invoice outstanding. This difference could be due to rounding error, or change in the currency exchange rate. You can set an Account here where this difference amount will be booked.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-5.gif">

#### 1.5 Submit
Save and Submit Payment Entry. On submission, outstanding will be updated in the Invoices. 

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-8.png">

If payment entry was created against Sales Order or Purchase Order, field Advance Paid will be updated in them. when creating Payment invoice against those transactions, Payment Entry will auto-update in that Invoice, so that you can allocate invoice amount against advance payment entry.

For incoming payment, accounts posting will be done as following.

  * Debit: Bank or Cash Account
  * Credit: Customer (Debtor)

For outgoing payment:

  * Debit: Supplier (Creditor)
  * Credit: Bank or Cash Account

### 2. Other cases
#### 2.1 Multi Currency Payment Entry

ERPNext allows you maintain accounts and invoicing in the [multiple currency](/docs/user/manual/en/accounts/multi-currency-accounting). If invoice is made in the party currency, Currency Exchange Rate between companies base currency and party currency is also entered in the invoice. When creating Payment Entry against that invoice, you will again have to mention the Currency Exchange Rate at the time of payment.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-6.png">

Since Currency Exchange Rate is fluctuating all the time, it can lead to difference in the payment amount against invoice total. This difference amount can be booked in the Currency Exchange Gain/Loss Amount.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-7.png">

Payments can also be made independent of invoices by creating a new Payment Entry.

#### 2.2 Internal Intransfer

Following internal transfers can be managed from the Payment Entry.

1. Bank - Cash
2. Cash - Bank
3. Cash - Cash
4. Bank - Bank

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-9.png">

#### 2.3 Managing Outstanding Payments

In most cases, apart from retail sales, billing and payments are separate activities. There are several combinations in which these payments are done. These cases apply to both sales and purchases.

  * They can be upfront (100% in advance).
  * Post shipment. Either on delivery or within a few days of delivery.
  * Part in advance and part on or post delivery.
  * Payments can be made together for a bunch of invoices.
  * Advances can be given together for a bunch of invoices (and can be split across invoices).

ERPNext allows you to manage all these scenarios. All accounting entries (GL Entry) can be made against a Sales Invoice, Purchase Invoice or Payment Entry of advance payment (in special cases, an invoice can be made via a Sales Invoice too).

The total outstanding amount against an invoice is the sum of all the accounting entries that are made “against” (or are linked to) that invoice. This way you can combine or split payments in Payment Entry to manage the
scenarios.

#### 2.4 Difference between Payment Entry and Journal Entry

 1. Journal Entry requires understanding of which Account will get Debited or Credited. In the Payment Entry, it is managed in the backend, hence simpler for the User.
 2. Payment Entry is more efficient in managing payment in the foreign currency.
 3. Journal Entry can still be used for:
	- Updating opening balance in an Accounts.
	- Fixed Asset Depreciation entry.
	- For adjusting Credit Note against Sales Invoice and Debit Note against Purchase Invoice, in case there is no payment happening at all.
 4. Payment Entries are used if a cheque is printed.

#### 3. Related Topics
1. [Payments](/docs/user/manual/en/accounts/payments)
1. [Payment Request](/docs/user/manual/en/accounts/payment-request)
1. [Payment Terms](/docs/user/manual/en/accounts/payment-terms)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
