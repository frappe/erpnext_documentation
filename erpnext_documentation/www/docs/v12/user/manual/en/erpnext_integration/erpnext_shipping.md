<!-- add-breadcrumbs -->
# ERPNext Shipping

**The ERPNext Shipping app helps you compare shipping rates being offered by multiple service providers, generate labels, and track your shipments' status.**

Integration with the following service providers is available:

1. [Packlink](https://www.packlink.com/en-GB/)
1. [LetMeShip](https://www.letmeship.com/en/)
1. [SendCloud](https://www.sendcloud.com/home-new/)

## 1. Setting Up

For the app to work smoothly, you will have to generate an API key from **at least one** of the platforms listed above. Here is a guide to set them up:

### 1.1 Packlink API

1. Register on [Packlink PRO](https://auth.packlink.com/en-GB/pro/register?platform=PRO&platform_country=UN).
1. Follow [these steps](https://support-pro.packlink.com/hc/en-gb/articles/213431749-How-to-generate-an-API-key-on-PRO) to generate an **API Key**.
1. Search for **Packlink** in the awesomebar.
1. Add the **API Key** to the Packlink DocType, check the 'Enabled' field.
1. Save.

<img class="screenshot" alt="Packlink API" src="{{docs_base_url}}/assets/img/erpnext_integrations/packlink_api.png">

### 1.1 Sendcloud API

1. Register on [Sendcloud](https://panel.sendcloud.sc/accounts/signup/).
1. Follow [these steps](https://support.sendcloud.com/hc/en-us/articles/360024967612-Service-points-for-API-Integrations#step-1-) to generate a **Public Key** and a **Secret Key**.
1. Search for **SendCloud** in the awesomebar.
1. Add the **Public Key** in the 'API Key' field and the **Secret Key** in the 'API Secret' field of the SendCloud DocType.
1. Check the **Enabled** field.
1. Save.

<img class="screenshot" alt="Sendcloud API" src="{{docs_base_url}}/assets/img/erpnext_integrations/sendcloud_api.png">

### 1.1 LetMeShip API

1. Register on [LetMeShip](https://www.letmeship.com/en/).
1. Follow [these steps](https://www.letmeship.com/en/connect-the-shipping-interface/) to generate an **API ID** and **API Password**.
1. Search for **LetMeShip** in the awesomebar.
1. Add the **API ID** and **API Password** to the LetMeShip DocType. Check the **Enabled** field.
1. Save.

<img class="screenshot" alt="LetMeShip API" src="{{docs_base_url}}/assets/img/erpnext_integrations/letmeship_api.png">

## 2. Features

### 2.1 Comparison of Shipping Rates

Once a [Shipment](/docs/user/manual/en/stock/shipment) is submitted, if the app is installed, the button **Fetch Shipping Rates** will appear. On clicking, you will get a list of services along with their service providers and rates.

<img class="screenshot" alt="Fetch Rates" src="{{docs_base_url}}/assets/img/erpnext_integrations/fetch_rates.png">

You can also add frequently used services to your **Preferred Services** using **Parcel Service Type**:

1. Assuming the highlighted service is our frequently used service, let us add it to our **Preferred Services**

 <img class="screenshot" alt="Highlight Service" src="{{docs_base_url}}/assets/img/erpnext_integrations/service_highlight.png">

1. Go to **Parcel Service Type** > **New**. Create a new **Parcel Service**. In our case, it is 'TNT'.
1. Add a **Parcel Service Type**. In our case, it will be 'Economy'.
1. Add 'Economy' to the **Parcel Service Type Alias** table as well.
1. Add a description (optional).
1. Enable the **Show in Preferred Services List** field. Save.

Now when you click on the **Fetch Shipping Rates** button, you will always see the previously highlighted service under **Preferred Services**.

<img class="screenshot" alt="Preferred Service" src="{{docs_base_url}}/assets/img/erpnext_integrations/preferred_service.png">

### 2.2 Creation of Shipment

After comparing rates, you can proceed with any one of the services by clicking **Select** against the appropriate service row. On clicking, a Shipment is automatically created on your service provider's platform.

You will notice that the **Shipment Information** section is updated automatically, based on the Shipment created.

<img class="screenshot" alt="Shipment Creation" src="{{docs_base_url}}/assets/img/erpnext_integrations/create_shipment.gif">

You can also search for your transaction on your service provider's platform using the **Shipment ID** field.

<img class="screenshot" alt="Packlink Shipment" src="{{docs_base_url}}/assets/img/erpnext_integrations/packlink_shipment.png">

### 2.3 Printing Labels

To avail the **Print Shipping Label** button, the **Shipment ID** must be generated in the current record.

<img class="screenshot" alt="Print Label Button" src="{{docs_base_url}}/assets/img/erpnext_integrations/print_label_button.png">

You can then click on it and generate your shipping label.

<img class="screenshot" alt="Dummy Shipping Label" src="{{docs_base_url}}/assets/img/erpnext_integrations/dummy_shipping_label.png">


You can also track your shipment's status by clicking on **View** > **Track Status**.

> **Note** : The currently integrated platforms may not serve your region. Please visit the links attached against them to know more.