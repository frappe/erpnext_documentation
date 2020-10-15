<!-- add-breadcrumbs -->
# M-Pesa Integration

**M-Pesa integration allows processing transactions with the payment gateway provider M-Pesa.**

M-Pesa Integration facilitates processing of payments between M-Pesa application and ERPNext. M-Pesa Integration only works with the POS to facilitate the payments for the same. This feature doesn't work with the shopping cart.

To set up M-Pesa, go to:
> Integrations > Payments > M-Pesa Settings

## 1.How to get your M-Pesa credentials?
1. In order to activate your API credentials, you need to log in to your M-Pesa account.
2. Then, open the Go live section of the application and follow the steps to get the approval for the app.
3. All the test cases are satisfied and expected results match the final results. You need to submit the document and follow the steps to get the final credentials for your application.
4. Details mentioned in the Production URL and Credentials section are the credentials that you are supposed to use in M-Pesa Settings.

<img class="screenshot" alt="Mpesa Credentials" src="{{docs_base_url}}/assets/img/setup/integrations/mpesa_credentials.png">


## 2.Setting up M-Pesa

To enable M-Pesa Express, you need to configure all the mandatory parameters which you received from the M-Pesa. If you want to use staging environment of the integration, you can select the staging option and use the staging credentials provided by M-Pesa by creating a separate application for the same.
<img class="screenshot" alt="Mpesa Settings" src="{{docs_base_url}}/assets/img/setup/integrations/mpesa_settings.png">

On enabling the M-Pesa integration in ERPNext, the system will create a Payment Gateway record and an Account Head in Chart of Account with the Account type as Bank as seen in the following screenshot.

<img class="screenshot" alt="Mpesa COA" src="{{docs_base_url}}/assets/img/setup/integrations/mpesa_coa.png">

It will also create a mode of payment with same name and account as the payment gateway, along with certain custom fields in pos settings to handle pos payments.
<img class="screenshot" alt="Mpesa COA" src="{{docs_base_url}}/assets/img/setup/integrations/mpesa_pos_settings.png">

Also, it will create a Payment Gateway Account entry. Payment Gateway Account is the configuration hub from where you can set Account Heads and the default Payment Request email template for requesting payments from customers.

<img class="screenshot" alt="Payment Gateway Account" src="{{docs_base_url}}/assets/img/setup/integrations/payment_gateway_account_mpesa.png">

After configuring Payment Gateway Account, you will be able to accept online payments via M-Pesa.

## 3.Supporting transaction currencies

M-Pesa will only work for the Company which has KSH (Kenyan Shilling) as Company Currency.
