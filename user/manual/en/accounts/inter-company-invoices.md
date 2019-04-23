<!-- add-breadcrumbs -->

# Inter Company Invoices

Along with creating Purchase Invoices or Sales Invoices for a single company, you can create inter-linked invoices for multiple companies.

Such as, you can create a Purchase Invoice for a company say 'Company ABC', and create a Sales Invoice against this Purchase Invoice for a company say 'Company XYZ' and link them together.

### 1. How to create Inter Company Invoices
#### 1.1 Setting up
1. Go to: **Accounts > Masters > Customer**.
1. Select the customer who you would want to choose for the inter-linked invoice.
1. Enable the checkbox, **Is Internal Customer** shown as follows:

    <img class="screenshot" alt="Internal Customer" src="{{docs_base_url}}/assets/img/accounts/make-internal-customer.png">

1. Add the company which the Customer represents in the **Represents Company** field. This the company for which the Sales Invoice will be created.
1. In the **Allowed To Transact With** table, add the company against which you will be creating a Purchase Invoice. 
1. Now, when you create a Purchase Invoice against company A (customer is from company B, seller is company A), it'll be linked to the Sales Invoice for company A created using this Internal Customer from company B.
1. Now, you need to follow a similar procedure for setting up a Supplier for inter-linked invoices.
1. Go to: **Accounts > Masters > *Select the Supplier***
1. Tick on 	Is Internal Supplier.
1. In the **Represents Company** field, add the company which you added in the table **Allowed To Transact With** for the Customer.
1. In the table **Allowed To Transact With** for the Supplier, add the company which the Customer represents. This is the company against which you are going to make an inter-linked Purchase Invoice.
1. Here is a screenshot of the Supplier company to avoid any confusion:

    <img class="screenshot" alt="Internal Supplier" src="{{docs_base_url}}/assets/img/accounts/make-internal-supplier.png">

#### 1.2 Creating the Invoice
1. Now, create a new [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice), fill up the fields.
1. Remember to select the Customer who is an internal customer and company from which he's buying.
1. Save and Submit the Invoice.

    <img class="screenshot" alt="Inter company invoice" src="{{docs_base_url}}/assets/img/accounts/make-inter-company-invoice.png">

1. Before you make an *Inter Company Invoice* you need to do the following:
  1. The selling and buying price between the companies should be in sync.
  1. Go to **Stock > Price List**, create a new Price List for inter company transactions.
  1. Tick both Selling and Buying in this new Price List.
  1. Go to **Buying > Supplier > *internal supplier***, in the currency and price list section, set the price list to new one just created.
  1. Do the same for the internal customer, i.e., set the price list to the new one.
  1. Now, you can make an inter company Purchase or Sales Invoice.
1. Under the **Make** button dropdown, you will find a link **Inter Company Invoice**, on clicking the link, you will be routed to a new Purchase Invoice form page.
1. Here, the supplier and company will be auto-fetched depending on the company you selected in the Sales Invoice.
> ***Remember**: There can only be a single Internal Supplier or Customer per company.*
1. Submit the invoice, done! Now, both the invoices are inter-linked. *Also, on cancelling any of the invoices, the link will break as well.*

You can follow the same process to create a Purchase Invoice and then an inter-linked Sales Invoice from the submitted Purchase Invoice.

#### 2. Related Topics
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/user/manual/en/accounts/purchase-invoice)
1. [Inter Company Journal Entry](/docs/user/manual/en/accounts/inter-company-journal-entry)
