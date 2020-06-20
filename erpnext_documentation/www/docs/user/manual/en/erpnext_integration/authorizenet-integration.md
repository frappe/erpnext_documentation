<!-- add-breadcrumbs -->
#Authorizenet Integration

A payment gateway is an e-commerce application service provider that authorizes credit card payments for e-businesses, online retailers, bricks and clicks, or traditional brick and mortar.

A payment gateway facilitates the transfer of information between a payment portal (such as a website, mobile phone or interactive voice response service) and the Front End Processor or acquiring bank.

To setup Authorizenet, 

`Explore > Integrations > Authorizenet Settings`

#### Setup Authorizenet

To enable Authorizenet payment service, you need to configure parameters like API Login ID and API Transaction Key.

<img class="screenshot" alt="AuthorizeNet Settings" src="{{docs_base_url}}/assets/img/setup/integrations/authorizenet_settings.png">

On enabling the service, the system will create Payment Gateway record and Account head in chart of accounts having account type as Bank.

<img class="screenshot" alt="AuthorizeNet Chart Of Accounts" src="{{docs_base_url}}/assets/img/setup/integrations/authorizenet_coa.png">

Also, it will create the Payment Gateway Account entry. Payment Gateway Account is a configuration hub from this you can set account head from existing Chart of Accounts(COA), default Payment Request email body template.

<img class="screenshot" alt="Payment Gateway Account" src="{{docs_base_url}}/assets/img/setup/integrations/payment_gateway_account_authorizenet.png">

After enabling service and configuring Payment Gateway Account your system is able to accept online payments.

#### Supporting transaction currencies

- Authorizenet Support currencies like USD and CAD.

#### Authorizenet Sandbox credentials
- Login to AuthorizeNet developer account, <a href="https://sandbox.authorize.net/">AuthorizeNet Developer Account</a>


<img class="screenshot" alt="AuthorizeNet Account" src="{{docs_base_url}}/assets/img/setup/integrations/authorizenet_account.png">

<img class="screenshot" alt="AuthorizeNet Credentials" src="{{docs_base_url}}/assets/img/setup/integrations/authorizenet_credentials.png">