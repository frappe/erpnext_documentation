<!-- add-breadcrumbs -->
# Contact

Contacts do not need to be linked to another document, they can be stand alone. You can even create a contact with only a first name, not linked to any other document or party (Customer/Supplier).

The Contact_ID is automatically created:

1. If only a First Name is entered that First Name defines the ID , thus First name (only).
2. If a First Name and a Party is linked the ID becomes “FirstName-Party”.
 
Contacts can, but do not have to be linked, to:  User, Customer, Supplier, and Sales Partner. Since Customers and Addresses are not directly linked to a User, all links go via Contacts.

A Contact can be linked to the (web) user. If that user is also a Customer, it is linked to the Customer by the Customer ID

Contacts and Addresses in ERPNext are stored separately so that you can
attach multiple Contacts or Addresses to Customers and Suppliers.

### 1. How to create a Contact

1. Go to **> CRM > Sales Pipeline > Contact > New**.
2. Choose a status if applicable.
3. Enter additional details as needed.
4. Save.
    <img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/contact.png">

You can also add a Contact or Address directly from the Customer record, click on “New Contact” or “New Address”.

<img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/contact-from-cust.png">

> Tip: When you select a Customer in any transaction, one Contact and Address
gets pre-selected. This is the “Default Contact or Address”.

To Import multiple Contacts and Addresses from a spreadsheet, use the [Data Import Tool](/docs/user/manual/en/setting-up/data/data-import).

---
### 2. Features
#### 2.1 Address Titles

The Address Title (Name of person or organization that this address belongs to) is a free format unlinked field. The ID is automatically created from the Address Title and Address Type. (AddressTitle-AddressType).

#### 2.2 Address Linking

Addresses can be entered individually (unlinked)  or linked to customers, leads, suppliers or Sales Partners. 

Linking is done in the reference section where the links can be established.

(Contributed by Robert Becht)

#### 3. Related Topics
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Sales Partner](/docs/user/manual/en/selling)
1. [Supplier](/docs/user/manual/en/buying)