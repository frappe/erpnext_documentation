# Selling Settings

Selling Settings is where you can define properties and validations which will be applied to the masters and transactions involved in the sales cycle.

Let's see each option available under Selling Settings in ERPNext.

<img class="screenshot" alt="Selling Settings" src="{{docs_base_url}}/assets/img/selling/selling-settings.png">

## 1. Naming Series
###1.1 Customer Naming By

When a customer is saved, a unique ID is generated for that Customer.

By default, Customer ID is generated based on Customer Name. If you wish to save Customer using a naming series, in the field Customer Naming Series, set value as "Naming Series". Example of Customer ID's saved in Naming Series - "CUST00001, CUST00002, CUST00003..." and so on.

You can set Naming Series for Customers from:

**Setup > Data > Naming Series**

### 1.2 Campaign Naming By

Just like for Customer, you can also configure naming methodology for the Campaign master. By default, a campaign will be saved with Campaign Name.

## 2. Defaults
### 2.1 Default Customer Group and Territory

Select a default [Customer Group](/docs/user/manual/en/CRM/setup/customer-group) which will be auto-updated when creating a new Customer.

Quotations can be created for the Customers as well as for the Leads. When converting a Quotation into a Sales Order, which is created for a Lead, the system attempts to convert that Lead into a Customer. While creating Customer in the backend, values for Customer Group and Territory is picked from Selling Settings. If no default values are found for Customer Group or Territory, then you will receive a validation message asking for Customer Group or Territory. You can also manually convert a Lead into a Customer.

### 2.2 Default Price List

Price List set in this field will be auto-updated in the Price List field of sales transactions like Quotation, Sales Order, Delivery Note, and Sales Invoice.

### 2.3 Close Opportunity After Days

If there are many Opportunities having a status other than Open, then they will be auto-closed after the no. of days mentioned in this field.

### 2.4 Default Quotation Validity Days

Quotations to the customer are valid only for certain days. In the Quotation, you can update Valid Till Date manually. By default, the Valid Till date is auto-set as 30 days from the Quotation's Posting Date. You can change the no. of days in this field as per your business case.

## 3. Requirement checks
### 3.1 Sales Order Required

If you wish to make Sales Order creation mandatory before the creation of a Sales Invoice, then you should set the 'Sales Order Required' field as 'Yes'. By default, this will be 'No'.

### 3.2 Delivery Note Required

To make Delivery Note creation as mandatory before Sales Invoice creation, you should set this field as 'Yes'. By default, this will be 'No'.

### 3.3 Sales Update Frequency
The frequency at which project progress and company transaction details will be updated. By default it is for Each Transaction, you can also set it to Daily or Monthly if you have a lot of transactions every day.

## 4. Other checks
### 4.1 Maintain Same Rate Throughout Sales Cycle

The system by default validates that item price will be the same throughout the sales cycle (Sales Order -> Delivery Note -> Sales Invoice). If you item price will be changing within the cycle and you need to bypass validation of the same rate maintained in the cycle, let this checkbox be unchecked.

### 4.2 Allow User to Edit Price List Rate in Transaction

The item table in sale transactions has a field called Price List Rate. This field is non-editable by default in all the sales transactions. This is to ensure that price of an item is fetched from Item Price record and the user is not able to edit it.

If you need the Item Price fetched from Price List of an item to be editable, you should uncheck this field.

### 4.3 Allow Item to be added multiple times in a transaction
This is a validation check which prevents an item from being added multiple times in the same transaction when unchecked. In some cases this might be an explicit need, if so check this box.

### 4.4 Allow multiple Sales Orders against a Customer's Purchase Order
When creating a Sales Order, you can update the Purchase Order ID and Date received from the Customer. You can create only one Sales Order against the Customer's PO No. and Date. However, if you wish to allow the creation of multiple Sales Orders against the same PO No. of the Customer, tick the checkbox "Allow multiple Sales Orders against a Customer's Purchase Order".

### 4.5 Validate Selling Price for Item against Purchase Rate or Valuation Rate
When making sales, it's important to know that you're not making losses. Enabling this validation will validate item's Selling Price with its valuation/buying price. If item's selling price is found to be less than it's buying price, then you will get a prompt when this checkbox is ticked.

### 4.6 Hide Customer's Tax ID from Sales Transactions
As per the statutory requirement, most of the Customers have unique Tax ID assigned to them. They also need to have this tax ID fetched in the selling transactions. However, if you don't wish to use this functionality, you can disable by checking this property.
