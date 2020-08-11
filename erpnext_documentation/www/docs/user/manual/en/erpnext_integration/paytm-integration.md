<!-- add-breadcrumbs -->
# Paytm Integration

**Paytm is a payment gateway provider which allows processing transactions.**

Paytm Integration facilitates processing of payments between Paytm payment portal and ERPNext. Your customers can choose to pay from any credit/debit card, UPI, Netbanking, Paytm Wallet.

To setup Paytm:
> Explore > Integrations > Paytm Settings

## 1.How to get your Paytm API credentials?
1. In order to activate your API credentials, you need to login to your Paytm account.
2. Open the Developer Settings option in the sidebar.
3. Choose API Keys option, it should display a two types of API details(Test/Production).
4. Details mentioned in the Production API details are the credentials that your are supposed to use in Paytm Settings.

<img class="screenshot" alt="Razorpay Settings" src="{{docs_base_url}}/assets/img/setup/integrations/paytm_credentials.png">


## 2.Setting up Paytm

To enable Paytm payment service, you need to configure all the mandatory parameters which you received from the Paytm. If you want to use staging environment of the integration, you can select staging option and use the test API developer credentials provided by Paytm.
<img class="screenshot" alt="Razorpay Settings" src="{{docs_base_url}}/assets/img/setup/integrations/paytm_settings.png">

On enabling service, the system will create Payment Gateway record and Account head in chart of account with account type as Bank.

<img class="screenshot" alt="Stripe COA" src="{{docs_base_url}}/assets/img/setup/integrations/paytm_coa.png">

Also it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.

<img class="screenshot" alt="Payment Gateway Account" src="{{docs_base_url}}/assets/img/setup/integrations/payment_gateway_account_paytm.png">

After configuring Payment Gateway Account your system is able to accept online payments.

## 3.Supporting transaction currencies

Paytm will only work for the company having `INR (Indian Rupee)` as a Currency.