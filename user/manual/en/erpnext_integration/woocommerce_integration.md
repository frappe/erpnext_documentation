<!-- add-breadcrumbs -->
# WooCommerce Integration

Using WooCommerce Integration, the system creates Sales Orders in ERPNext for the orders created on WooCommerce using the WooCommerce webhook.

While creating the sales order, if Customer or Item is missing in ERPNext, the system will create new Customer/Item by using the respective details from WooCommerce order data. It also creates Address linked to the Customer using the shipping details from the order data.

## 1. How to setup?

### 1.1 Generate API Key and API Secret

1. From your woocommerce site's sidebar, click on Settings.
2. Click on the "Advanced" tab then click on the REST API link.

    ![Woocommerce API](/docs/assets/img/erpnext_integrations/wc-add-key.png)

3. Click on "Add key" button. Provide the necessary details and click on "Generate API key" button.

    ![Woocommerce API Key](/docs/assets/img/erpnext_integrations/wc-generate-keys.png)

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

![Woocommerce Settings](/docs/assets/img/erpnext_integrations/woocommerce-settings.png)

### 1.3 Woocommerce Webhook Settings

1. Now from your woocommerce site's sidebar, go to Settings.
2. Click on the "Advanced" tab then click on the Webhooks link and then click on "Add webhook" button.
3. Give the webhook a name of your choice.
4. Click on Status dropdown and select "Active".
5. Select Topic as "Order created".
6. Copy the "Endpoint" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Delivery URL" field.
7. Copy "Secret" from "Woocommerce Settings" doctype in your ERPNext site and paste it in "Secret" field.
8. Keep API VERSION as it is and click on Save Webhook. Now it is successfully set up.

![Woocommerce Webhook](/docs/assets/img/erpnext_integrations/wc-webhook.png)

A GIF below to show the entire process:

![Woocommerce Set Up](/docs/assets/img/erpnext_integrations/woocommerce-setup.gif)

**Note:** In the above screenshot and gif, in place of delivery url on woocommerce website, you need to paste the url you will obtain after saving the "Woocommerce Settings" in the "Endpoint" field in your ERPNext instance. Here other URL was pasted as localhost was being used.

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

![Woocommerce Set Up](/docs/assets/img/erpnext_integrations/woocommerce-order.gif)

## 2. Features

### 2.1 Defaults

In the Woocommerce Settings DocType:

- **Warehouse**: This warehouse will be used to create Sales Orders. The fallback warehouse is "Stores".
- **Delivery After (Days)**: This is the default offset (days) for the Delivery Date in Sales Orders. The fallback offset is 7 days from the order placement date.
- **Sales Order Series**: You can set a separate series for Sales Orders created via woocommerce. The fallback series is "SO-WOO-".
- **UOM**: This is the default UOM used for Items and Sales Orders. The fallback UOM is "Nos".

![Woocommerce Defaults](/docs/assets/img/erpnext_integrations/wc-defaults.png)

## 3. Related Topics
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
2. [Item](/docs/user/manual/en/stock/item)
3. [Customer](/docs/user/manual/en/CRM/customer)
4. [Address](/docs/user/manual/en/CRM/address)