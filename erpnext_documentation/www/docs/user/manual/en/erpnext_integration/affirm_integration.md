<!-- add-breadcrumbs -->
#Affirm Integration

Whether your customers are planning to take a trip, upgrade some appliances, or just do something kind for someone they care about, they’re all looking for a way to buy the things they love. But the reality is, sometimes these purchases don’t fit comfortably into their monthly budget. This is where we come in: We provide the option for your customers to buy now and pay over time, giving them financial flexibility and the confidence to say yes to that next big purchase.

To setup Affirm,

`Explore > Integrations > Affirm Settings`

<img class="screenshot" alt="Affirm Settings" src="{{docs_base_url}}/assets/img/setup/integrations/affirm_integration.gif">

#### Setup  Affirm

To enable Affirm payment service, you need to configure parameters like API Key, API Secret

<img class="screenshot" alt="Razorpay Settings" src="{{docs_base_url}}/assets/img/setup/integrations/affirm_settings.png">

On enabling service, the system will create Payment Gateway record and Account head in the Chart of Account with account type as Bank.

<img class="screenshot" alt="Razorpay COA" src="{{docs_base_url}}/assets/img/setup/integrations/affirm_coa.png">

Also, it will create Payment Gateway Account entry. Payment Gateway Account is configuration hub from this you can set account head from existing COA, default Payment Request email body template.

<img class="screenshot" alt="Payment Gateway Account" src="{{docs_base_url}}/assets/img/setup/integrations/affirm_payment_gateway.png">

After enabling service and configuring Payment Gateway Account your system is able to select EMI.

####Supporting transaction currencies

Affirm will only work for the company having `USD` as a Currency.