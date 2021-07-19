<!-- add-breadcrumbs -->
# Shopify Integration - Ecommerce Integrations app

The Shopify Connector pulls the orders from Shopify and creates Sales Order against them in ERPNext.

While creating the sales order if Customer or Item is missing in ERPNext the system will create new Customer/Item by pulling respective details from Shopify.

### How to Setup Connector?


#### Note to users of old Shopify Connector

If you have not setup Shopify Connector on your ERPNext site you can proceed to next step.

If you are using old Shopify integration that's provided in ERPNext then you will have to disable the connector before proceeding. After installing the app, it will migrate existing data e.g. unique product_id for items to separate doctype. Once you are done configuring new integration, you can confirm the status of migration by going to "Ecommerce Integration Log" doctype.

#### App Installation

- If you are hosting your ERPNext site on Frappe Cloud, you can quickly install the app by going to your site Dashboard. The app is available in [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce-integrations)
- If you want to install it on Private bench on Frappe Cloud refer [Frappe Cloud documentation](https://frappecloud.com/docs/bench/install-custom-app)
- If you are self hosting ERPNext you can install the app using Frappe bench. Refer [bench documentation](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) for installing Frappe Apps.

The repository for app is hosted on GitHub: [http://github.com/frappe/ecommerce_integrations/](http://github.com/frappe/ecommerce_integrations/)

#### Create A Private App in Shopify

1. Click on Apps in menu bar
<img class="screenshot" alt="Menu Section" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/app_menu.png">

2. Click on **Manage private apps** to create private app
<img class="screenshot" alt="Manage Private Apps" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/manage_private_apps.png">

3. Fill up the details and create app. Each app has its own Password and Shared secret
<img class="screenshot" alt="App Details" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/app_details.png">


#### Setting Up Shopify  on ERPNext:-
Once you have created a Private App on Shopify, setup App Credentials and other details in Shopify Setting in ERPNext.

> To access Shopify Setting, go to:
Awesome bar > "Shopify Setting"

Note: Shopify does not support insecure HTTP connection. Your ERPNext site must be able to accept HTTPS requests. Access your ERPNext site using `https://` url before proceeding.

1. Fill-up Password and Shared Secret from Shopify's Private App.
<img class="screenshot" alt="Setup Private App Credentials" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/app_details.png">

2. Setup Customer, Company and Inventory configurations
<img class="screenshot" alt="ERP Configurations" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/main-settings.png">

3. Setup Sync Configurations.
    The system pulls Orders from Shopify and creates Sales Order in ERPNext. You can configure ERPNext system to capture payment and fulfillments against orders.
<img class="screenshot" alt="Sync Configure" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/series-setting.png">

4. Setup Tax Mapper.
    Prepare tax and shipping charges mapper for each tax and shipping charge you apply in Shopify
<img class="screenshot" alt="Taxes and Shipping Charges" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/tax-mapping.png">


After setting up all the configurations, enable the Shopify sync and save the setting. This will register the API's to Shopify and the system will start Order sync between Shopify and ERPNext.


### Syncing Old Orders From Shopify

Once you are done with the Shopify configuration and have enabled Shopify Syncing, you also get a provision to sync your old orders from Shopify into ERPNext. This syncing will happen in background and can take few hours depending on number of orders you have.


1. Enable "Sync Old Shopify Orders"
1. Enter the From and To dates between which the orders need to be synced

<img class="screenshot" alt="Sync Order By Date" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/sync-old-orders.png">


### Inventory Sync

You can update your inventory with Shopify for items that are synced from Shopify. Inventory sync is done every hour with a scheduled job. Inventory levels of items that have changed since last sync are pushed to Shopify. Inventory levels of ERPNext warehouses are mapped 1 to 1 with Shopify locations.

1. To enable inventory sync click on the checkbox, this will show you a table to map ERPNext warehouse with Shopify Location.
2. Select sync frequency. 30 to 60 minutes is recommended frequency.
3. Click on "Fetch Shopify Locations" button to populate Shopify locations in the table.
4. Link each location with ERPNext warehouse.
5. Save the settings.

<img class="screenshot" alt="Inventory Syncing with Shopify" src="{{docs_base_url}}/v13/assets/img/erpnext_integrations/ecommerce_integrations/shopify/inventory-sync.png">

> Note: This connector assumes that ERPNext is main source of information about inventory levels, any changes done to Shopify inventory levels will be overwritten by ERPNext if ERPNext inventory levels change.

> Note: Shopify does not support fractional quantity. If fractional quantity is found in ERPNext, the inventory level on Shopify will be set by rounding it down to nearest whole number.


### Item Sync

You can enable sync of new ERPNext items to Shopify by checking "Upload new ERPNext items to Shopify".

You can also update Shopify item upon updating ERPNext item.

Following fields are uploaded / updated:

| ERPNext Field    | Shopify Field   |
| :-:              | :-:             |
| Item Name        | Title           |
| Item Code        | SKU             |
| Description body | Description     |
| Item Group       | Product Type    |
| Weight per Unit  | Weight          |
| Weight UOM       | Weight UOM      |

By default all items are marked as Draft on Shopify and not published in any store.

Purpose of providing this functionality is to sync items with Shopify. It's not possible to map every fields 1-to-1. Upon creation of item on Shopify using this method, it's linked with ERPNext, this eliminates possibility of duplication. You can modify items on Shopify later to add more details.


> Note: This feature is not supported in data import or for variant / template items.


### Cancellation of Orders
This connector handles various cancellation scenario in following manner:

1. If Order on Shopify is cancelled and it doesn't have invoice or Delivery note linked against it then ERPNext Sales Order is cancelled.
2. If ERPNext Sales Order does have any linked document, then status of order on Shopify is added to the respective document. Cancellation and preparation of appropriate documents has to be done by user based on this information.
