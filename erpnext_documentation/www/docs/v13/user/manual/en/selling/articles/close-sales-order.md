<!-- add-breadcrumbs -->
#Close Sales Order

In the submitted Sales Orders, you will find **Stop** option. Stopping Sales Order will restrict user from creating Delivery Note and Sales Invoice against it.

![Close Option in Sales Order](/docs/v13/assets/img/selling/close-option-in-sales-order.png)

####Scenario

An order is received for ten Wind Turbines. Sales Order is also created for ten units. Due to scarcity of stock, only seven units are delivered to the customer. Pending three units are to be delivered soon. Customer informs that they don't need to deliver pending item, as they have purchased it from other vendor.

In this case, create Delivery Note and Sales Invoice will be created only for the seven units. And the Sales Order should be set as stopped.

![Closed Sales Order](/docs/v13/assets/img/selling/closed-sales-order.png)

Once Sales Order is set as stopped, you will not have pending quantities (three in this case) reflecting in Pending to Deliver and Pending to Invoice reports. To make further transactions against Stopped Sales Order, you should first Unstop it.

You will find same funtionality in the Purchase Order as well.

{next}

<!-- markdown -->