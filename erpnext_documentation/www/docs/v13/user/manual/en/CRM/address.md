<!-- add-breadcrumbs -->
# Address

You can record the addresses associated with a Lead, Customer, Supplier, Shareholder, Sales Partner or a Warehouse.

You can also add an Address as a standalone record without linking it to any of the entities listed above.

To access the Address list, go to:
> Home > CRM > Address

## 1. How to create an Address

1. Go to the Address list and click on New.
1. Select Address Type.
1. Enter details in Address Line 1, Address Line 2, City/Town, County, State, Country.
1. Enter Email Address, Phone and Fax.
1. Enter Link DocType and Link Name to link this address to customer, supplier etc.
4. Save.
    ![Contact](/docs/v13/assets/img/crm/address.png)

You can also add an Address from the Customer or Supplier record by clicking on “New Address" button as shown below.

![Add Address From Customer](/docs/v13/assets/img/crm/add-address-from-customer.png)

To Import multiple addresses from a spreadsheet, use the [Data Import Tool](/docs/v13/user/manual/en/setting-up/data/data-import).

---
## 2. Features

### 2.1 Link an Address to Multiple Entities

An address may be linked to multiple customers or multiple suppliers.

An address can also be linked to customers and suppliers at the same time.

![Link One Address to Multiple Entities](/docs/v13/assets/img/crm/link-address-to-multiple-entities.png)

### 2.2 Address Title

If the address is not linked to any entity you need to manually add a title.

If the address is linked to an entity like a customer or supplier, the title is generated automatically in 'Entity Name-Address Type' format.

![Address Title](/docs/v13/assets/img/crm/address-title.png)

### 2.3 Preferred Billing Address and Shipping Address

If you check 'Preferred Shipping Address', the address would be automatically added in the Shipping Address in Sales Order, Sales Invoice and Delivery Note transactions.

Similarly, if you check 'Preferred Billing Address', the address would be automatically added in the Billing Address in Sales Order, Sales Invoice and Delivery Note transactions.

### 2.4 GST Localization for India
If the customer or supplier has registered under GST, you can enter GSTIN and GST State in Address. Make sure GSTIN entered is in valid format.
![GST Details in Address](/docs/v13/assets/img/crm/gst-details-in-address.png)

In sales transactions along with address, GSTIN is also fetched.

![GST Details in Sales Order](/docs/v13/assets/img/crm/gst-details-in-sales-order.png)

You can also add addresses of your own company's facilities. Check 'Is Your Company Address', select Company in Link DocType, and Company Name in Link Name for such addresses and you can select them in GST Sales Invoice to print your own address.

![Company Address](/docs/v13/assets/img/crm/company-address.png)

>GSTIN is to be added in Address and not in Customer/Supplier, as one Customer/Supplier may have multiple GSTIN (one for each state where he conducts his business).


### 3. Related Topics
1. [Customer](/docs/v13/user/manual/en/CRM/customer)
1. [Supplier](/docs/v13/user/manual/en/buying)
1. [Sales Partner](/docs/v13/user/manual/en/selling)

{next}
