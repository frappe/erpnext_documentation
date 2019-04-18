<!-- add-breadcrumbs -->
# Loyalty Program

A customer loyalty program is a structured and long-term marketing effort which provides incentives to repeat customers who demonstrate loyal buying behavior. Successful programs are designed to motivate customers in a business's target market to return often, make frequent purchases, and shun competitors.

### 1. How to create a loyalty program
1. Go to: **Accounts > Retail Operations > Loyalty Program > New**.
1. Enter a name for the Loyalty Program.
1. Select whether single tiered or multi tiered (gold, silver, etc,.).
1. Set a start and end date for the program.
1. Select the Customer Group and Territory for which this program is applicable, the default is all.
1. For opting in all customers by default, tick on 'Auto Opt In (For all customers)'.
1. In the table, enter:
  1. **Tier name**: To be assigned to a Customer based on his eligibility.
  1. **Collection Factor**: How much of an amount needs to be spent to gain 1 loyalty point.
  1. **Minimum Amount**: Spent to qualify into that tier.
1. Set the Conversion Factor, eg: 1 point = 1 USD.
1. Set an expense account from where you'll offer the benefits.
1. Set a Cost Center to track Profit/Loss from the Loyalty Program.
1. Save. 

<img class="screenshot" alt="Loyalty Program" src="{{docs_base_url}}/assets/img/accounts/loyalty-program.png">

### 2. Loyalty Point Entry
Go to: **Accounts > Retail Operations > Loyalty Point Entry**.
This acts as a log to give an overview about which Customer earned how many points across which Invoice. It holds the data Invoice and Customer.

<img class="screenshot" alt="Loyalty Program 3" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-3.png">

### 3. Customer
**Loyalty Program** section in Customer master.

<img class="screenshot" alt="Loyalty Program 1" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-1.png">

**Loyalty Point** earned can be viewed in Customer's dashboard.

<img class="screenshot" alt="Loyalty Program 2" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-2.png">

### 4. How it works ?

#### 4.1 Earning Points
* Firstly, a **Loyalty Program** needs to be created (as shown in the first screenshot).
* Assign this **Loyalty Program** to a **Customer**.
* Go to **Sales Invoice > New** and create an invoice for the **Customer** to whom you have assigned **Loyalty Program**.
* For this example, an invoice is created with a grand total of 10,000 INR and according to the **Loyalty Program** for a minimum spent of 1,0000 INR, the Silver Tier collection factor will be eligible and for each 1,000 INR spent, the **Customer** will receive 1 point (hence the total point earned on this transaction is 10).
* Upon submission of the invoice, **Loyalty Point Entry** will be created for this invoice (as shown above under Loyalty Program Entry section).
* In the **Loyalty Program** upon minimum spent of 19,000, Gold Tier would be eligible. So, if we were to duplicate our current invoice and submit it, the **Customer** will be automatically upgraded to Gold tier as his total expenditure under this current **Loyalty Program** has exceeded the minimum spent value for Gold tier collection factor (as his last invoice was 10,000 INR and duplicated from that gives another invoice of 10,000 INR, hence his total expenditure becomes 20,000 INR).

> Note: The minimum spent in Loyalty Program does not mean a minimum value for a single invoice. Rather it means the sum of amount of invoices for that customer under a particular Loyalty Program scheme.

#### 4.2 Redeeming Points
* Continuing from the above example where we have created 1 invoice and earned 10 points over it, we create another invoice by duplicating the first, and under the collapsible section for **Loyalty Program**, we check the checkbox for 'Redeem Loyalty Points'.
* The fields for 'Loyalty Point', 'Redemption Account' and 'Redemption Cost Center' will become visible under this section. The account and cost center will be fetched from the **Loyalty Program** assigned to the **Customer**.
* Since we have earned 10 points, we can use as many of them as we want. If we try to use more than what we have an error will be thrown.
* For this example, we'll use all 10 points to be redeemed. Doing so will enable another field which will display the amount calculated using (loyalty point * conversion factor). So basically, '10' INR will be lessened from our outstanding amount.
* When submitted, 2 **Loyalty Point Entry** will be created. One for redeemed, which will be a negative value and one for the current invoice (as the amount is still eligible under a tier).

> Note: For an invoice on which points have been earned, if a return invoice is created, it will delete the original Loyalty Point Entry and create a new one after subtracting the original amount with the returned amount. Also, when cancelling an invoice, its subsequent Loyalty Point Entry will also be deleted.

#### 5. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Customer Group](/docs/user/manual/en/CRM/customer-group)

