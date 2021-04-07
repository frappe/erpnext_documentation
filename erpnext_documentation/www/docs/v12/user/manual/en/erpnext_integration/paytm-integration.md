<!-- add-breadcrumbs -->
# Paytm Integration

**Paytm integration allows processing transactions with the payment gateway provider Paytm.**

Paytm Integration facilitates processing of payments between Paytm payment portal and ERPNext. Your customers can choose to pay from any credit/debit card, UPI, Netbanking, Paytm Wallet.

To set up Paytm, go to:
> Integrations > Payments > Paytm Settings

## 1.How to get your Paytm API credentials?
1. In order to activate your API credentials, you need to log in to your Paytm account.
2. Then, open the Developer Settings option in the sidebar.
3. Choose API Keys option, it should display a two types of API details (Test/Production).
4. Details mentioned in the Production API details are the credentials that you are supposed to use in Paytm Settings.

<img class="screenshot" alt="Razorpay Settings" src="{{docs_base_url}}/v12/assets/img/setup/integrations/paytm_credentials.png">


## 2.Setting up Paytm

To enable Paytm payment service, you need to configure all the mandatory parameters which you received from the Paytm. If you want to use staging environment of the integration, you can select the staging option and use the test API developer credentials provided by Paytm.
<img class="screenshot" alt="Razorpay Settings" src="{{docs_base_url}}/v12/assets/img/setup/integrations/paytm_settings.png">

On enabling the Paytm integration in ERPNext, the system will create a Payment Gateway record and an Account Head in Chart of Account with the Account type as Bank as seen in the following screenshot.

<img class="screenshot" alt="Stripe COA" src="{{docs_base_url}}/v12/assets/img/setup/integrations/paytm_coa.png">

Also, it will create a Payment Gateway Account entry. Payment Gateway Account is the configuration hub from where you can set Account Heads and the default Payment Request email template for requesting payments from customers.

<img class="screenshot" alt="Payment Gateway Account" src="{{docs_base_url}}/v12/assets/img/setup/integrations/payment_gateway_account_paytm.png">

After configuring Payment Gateway Account, you will be able to accept online payments via Paytm.

## 3.Supporting transaction currencies

Paytm will only work for the Company which has INR (Indian Rupee) as Company Currency.
