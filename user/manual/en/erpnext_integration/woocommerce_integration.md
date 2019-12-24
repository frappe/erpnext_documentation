<!-- add-breadcrumbs -->
# WooCommerce Integration

Using WooCommerce Integration, the system creates Sales Orders in ERPNext for the orders created on WooCommerce using the WooCommerce webhook.

While creating the sales order, if Customer or Item is missing in ERPNext, the system will create new Customer/Item by using the respective details from WooCommerce order details. It also creates Address linked to the Customer using the shipping details from the order data.

## 1. How to setup?

### 1.1 Generate API Key and API Secret

1. From your woocommerce site's sidebar, click on Settings.
2. Click on the "Advanced" tab then click on the REST API link.
3. Click on "Add key" button. Provide the necessary details and click on "Generate API key" button.

### 1.2 Woocommerce Settings

1. On your ERPNext site, go to: **Home > Integrations > Settings > Woocommerce Settings**.
2. Paste the API key and secret generated in the previous step into the "API consumer key" and "API consumer secret" fields.
3. In the "Woocommerce Server URL" paste the url of your WooCommerce site.
4. Make sure "Enable Sync" is checked.
5. Select the "Tax Account" and "Freight and Forwarding Account" in the Account Details Section.
6. Select the "Creation User" in Defaults section. This user will be used to create Customers, Items and Sales Orders. Ensure that the user has the relevant permissions.
7. Select the "Company" that will be used to create the Sales Orders.
8. Click Save.
9. After saving the Woocommerce Settings, "Secret" and "Endpoint" are generated automatically.

### 1.3 Woocommerce Webhook Settings

1. Now from your woocommerce site's sidebar, go to Settings.
2. Click on the "Advanced" tab then click on the Webhooks link and then click on "Add webhook" button.
3. Give the webhook a name of your choice.
4. Click on Status dropdown and select "Active".
5. Select Topic as "Order created".
6. Copy the "Endpoint" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Delivery URL" field.
7. Copy "Secret" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Secret" field.
8. Keep API VERSION as it is and click on Save Webhook. Now it is successfully set up.

<img class="screenshot" alt="Woocommerce Integration" src="{{docs_base_url}}/assets/img/erpnext_integrations/woocommerce_setting_config.gif">

**Note:** In above gif, inplace of delivery url on woocommerce website, you need to paste the url you will obtain after saving the "Woocommerce Settings" page (i.e. Endpoint from "Woocommerce Settings"). I pasted other url because I was using localhost. Please paste your endpoint in place of Delivery URL.

### 1.4 Woocommerce order creation and syncing:
1. From your Woocommerce website, register yourself as a user on the Account page.
2. Now Click on Addresses option and provide the required details.
3. Click on "Shop" option and now available products can be seen.
4. Add the desired products into the cart and click on "View Cart".
5. From the cart, once you have added the desired products, you can click on "Proceed to Checkout".
6. All billing details and Order details can be seen now. Once you are ok with it, click on "Place Order" button.
7. "Order Received" message can been seen indicating that the order has been placed successfully.
8. Now on your ERPNext instance, check the following Document Types: Customer, Address, Item, Sales Order. They will be fetched and created from the webhook data.
9. In case the orders are not synced, you can check the error in **Home > Settings > Core > Error Log**.

<img class="screenshot" alt="Woocommerce Integration" src="{{docs_base_url}}/assets/img/erpnext_integrations/woocommerce_demo.gif">

## 2. Features

### 2.1 Defaults

In the Woocommerce Settings DocType:

- **Warehouse**: This warehouse will be used to create Sales Orders. The fallback warehouse is "Stores".
- **Delivery After (Days)**: This is the default offset (days) for the Delivery Date in Sales Orders. The fallback offset is 7 days from the order placement date.
- **Sales Order Series**: You can set a separate series for Sales Orders created via woocommerce. The fallback series is "SO-WOO-".
- **UOM**: This is the default UOM used for Items and Sales Orders. The fallback UOM is "Nos".

## 3. Related Topics
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
2. [Item](/docs/user/manual/en/stock/item)
3. [Customer](/docs/user/manual/en/CRM/customer)
4. [Address](/docs/user/manual/en/CRM/address)