<!-- add-breadcrumbs -->
# Loyalty Program

**A Loyalty Program allows Customers to earn points by spending a certain amount and lets them redeem the points in future purchases.**

A Customer Loyalty Program is a structured and long-term marketing effort that provides incentives to repeat Customers. Successful programs are designed to motivate Customers in a business's target market to return often, make frequent purchases, and shun competitors.

To access the Loyalty Program list, go to:
> Home > Retail > Retail Operations > Loyalty Program

## 1. Prerequisites
Before creating and using a Loyalty Program, it is advised to create the following first:

1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)

## 2. How to Create a Loyalty Program
1. Go to the Loyalty Program list and click on New.
1. Enter a Name for the Loyalty Program.
1. Select whether the program is Single Tiered or Multi Tiered (gold, silver, etc).
1. Set a start and end date for the program.
1. Select the Customer Group and Territory for which this program is applicable, the default is all.
1. For opting in all Customers by default, tick on 'Auto Opt In (For all customers)'. Otherwise, the program needs to be assigned from the [Customer master](/docs/user/manual/en/accounts/loyalty-program#22-loyalty-points-in-customer).
1. In the table, enter:
 2. **Tier name**: To be assigned to a Customer based on his eligibility.
 2. **Collection Factor**: How much amount needs to be spent to gain 1 Loyalty Point in ERPNext.
 2. **Minimum Amount**: Minimum amount to be spent to qualify into a tier.
1. Set the Conversion Factor, eg: 10 USD = 1 point.
1. Save. 

 <img class="screenshot" alt="Loyalty Program" src="{{docs_base_url}}/assets/img/accounts/loyalty-program.png">

### 2.1 Redemption section

* **Conversion Factor**: When redeeming loyalty points, this factor decides how much money is 1 Loyalty Point worth. For example, if a Customer has 100 Loyalty Points, and 1 Loyalty Point = 1 USD, then the Customer use Items up to 100 USD with their loyalty points for future purchases.

* **Expense Account**: Set an Expense Account from where you'll offer the benefits. This is useful to track the benefits offered separately. 

* **Expiry Duration (in days)**: The collected loyalty points will expire after the number of days set in this field.

### 2.2 Loyalty Points in Customer

Set a Loyalty Program section in the Customer master to assign a Loyalty Program to a Customer.

<img class="screenshot" alt="Loyalty Program 1" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-1.png">

**Loyalty points** earned can be viewed in the Customer's dashboard.

<img class="screenshot" alt="Loyalty Program 2" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-2.png">

### 2.3 Loyalty Point Entry
Go to: **Accounts > Retail Operations > Loyalty Point Entry**.
This acts as a log to give an overview of which Customer earned how many points against which Sales Invoice. It holds the data Invoice and Customer.

<img class="screenshot" alt="Loyalty Program 3" src="{{docs_base_url}}/assets/img/accounts/loyalty-program-3.png">

## 3. How does a Loyalty Program work?

### 3.1 Earning Points

* Firstly, a **Loyalty Program** needs to be created as explained in the first section.
* Assign this **Loyalty Program** to a **Customer**.
* Create a new Sales Invoice for the **Customer** to whom you have assigned **Loyalty Program**.
* For this example, an invoice is created with a grand total of 3,000 INR and according to the **Loyalty Program** for a minimum spent of 2,000 INR, the Silver Tier collection factor will be eligible and for each 300 INR spent, the **Customer** will receive 1 point (hence the total points earned on this transaction is 15).
* Upon submission of the invoice, a **Loyalty Point Entry** will be created for this invoice (as shown above under Loyalty Program Entry section).
* In our **Loyalty Program** upon minimum spent of 6,000, Gold Tier would be eligible. So, when another invoice is submitted with the same value, the total sales from this Customer becomes 6,000. So now, the **Customer** will be automatically upgraded to the Gold tier.

> Note: The minimum spent in Loyalty Program does not mean a minimum value for a single invoice. Rather it means the sum of amount of invoices for the Customer under a particular Loyalty Program scheme.

### 3.2 Redeeming Points

* Let's continue from the above example where we created 1 invoice and earned 15 points from it. When creating another invoice for the same Customer, go to the Loyalty Points section and enable the checkbox to 'Redeem Loyalty Points'.
 ![Loyalty Program Invoice](/docs/assets/img/accounts/loyalty-program-inv.png)
* The fields for 'Loyalty Point', 'Redemption Account' and 'Redemption Cost Center' will become visible under this section. The account and Cost Center will be fetched from the **Loyalty Program** assigned to the **Customer**.
* Since the Customer has earned 15 points, we can use all of it until expiry. If we try to use more than what we have an error will be thrown.
* For this example, we'll use all 15 points to be redeemed. Doing so will enable another field that will display the amount calculated using (loyalty point * Conversion Factor). So, '150' INR will be deducted from our the amount since our 'Conversion Factor' was '10'.
 ![Loyalty Invoice](/docs/assets/img/accounts/loyalty-program-inv2.png)
* When submitted, 2 **Loyalty Point Entries** will be created. One for redeemed, which will be a negative value and one for the current invoice (as the amount is still eligible under a tier). The Customer was also upgraded to Gold since the minimum amount to be spent for Gold was 6,000.
 ![Loyalty Point](/docs/assets/img/accounts/loyalty-point-2.png)

> Note: For an invoice on which points have been earned, if a return invoice is created, it will delete the original Loyalty Point Entry and create a new one after subtracting the returned amount from the original amount. Also, when canceling an invoice, its subsequent Loyalty Point Entry will be deleted.

### 4. Related Topics
1. [Cost Center](/docs/user/manual/en/accounts/cost-center)
1. [Sales Invoice](/docs/user/manual/en/accounts/sales-invoice)
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Customer Group](/docs/user/manual/en/CRM/customer-group)

