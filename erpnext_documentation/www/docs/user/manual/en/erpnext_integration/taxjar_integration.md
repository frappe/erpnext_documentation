<!-- add-breadcrumbs -->
# TaxJar Integration

TaxJar Integration provides sales tax calculations at checkout. This functionality is provided completely through the TaxJar API, our sales tax API. When a customer visits a cart or checkout page, your platform will make a request to the API with the merchant and customer’s details to calculate the right amount of sales tax. You’ll use that data to collect sales tax for the merchant during the checkout process.

You can also import transactions (orders and refunds) into TaxJar directly from your platform through the TaxJar API. Merchants can see their transactions by logging into the TaxJar app at https://app.taxjar.com. At this time, TaxJar provides reporting for US merchants.

Once a merchant imports their transactions into TaxJar, we can automatically file their sales tax returns. If you implement sales tax reporting in your integration, no additional work is needed to support sales tax filing. Merchants can enroll in AutoFile directly from the TaxJar app at https://app.taxjar.com.

## 1. How to set up TaxJar?

### 1.1 Generate API Key and API Secret

1. From your TAXJAR site's sidebar, click on Settings.
2. Click on the "Advanced" tab then click on the REST API link.

    ![Taxjar API](/docs/assets/img/erpnext_integrations/)

3. Click on the "Add key" button. Provide the necessary details and click on the "Generate API key" button.

    ![Taxjar API Key](/docs/assets/img/erpnext_integrations/)

### 1.2 Taxjar Settings

1. On your ERPNext site, go to: **Home > Integrations > Settings > Taxjar Settings**.
2. Paste the API key and secret generated in the previous step into the "Live API Key" fields.
3. Select the "Tax Account" and "Freight and Forwarding Account" in the Account Details section.
4. Select the "Creation User" in the Defaults section. This user will be used to create Customers, Items, and Sales Orders. Ensure that the user has the relevant permissions.
5. Click Save.

![TaxJar Settings](/docs/assets/img/erpnext_integrations/)

A GIF below to show the entire process:

![Taxjar Set Up](/docs/assets/img/erpnext_integrations/)

> **Note:** In the above screenshot and GIF

## 2. Features

### 2.1 Defaults

In the Taxjar Settings DocType:

- **Enable Tax Calculation**: Check this field to auto calculate sales tax.
- **Create TaxJar Transaction**: Check this field to enable create an auto transaction on the Taxjar Platform.

In Customer, Quotation, Sales Order and Sales Invoice Doctype:

- **exempt_from_sales_tax**: Check this field to exempt this transaction for auto Sales Tax Calculation.


![ Defaults](/docs/assets/img/erpnext_integrations/)

## 3. Related Topics
1. [Sales Order](/docs/user/manual/en/selling/sales-order)
2. [Item](/docs/user/manual/en/stock/item)
3. [Customer](/docs/user/manual/en/CRM/customer)
4. [Address](/docs/user/manual/en/CRM/address)
