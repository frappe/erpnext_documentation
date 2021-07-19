<!-- add-breadcrumbs -->
# Buying Settings

Buying Settings is where you can define properties which will be applied in the Buying module's transactions.
You can find Buying Settings at:
> Home > Buying > Settings > Buying Settings

![Buying Settings]({{docs_base_url}}/v12/assets/img/buying/buying-settings.png)

Let us look at the various options that can be configured:

## 1. Supplier
### 1.1 Supplier Naming By

When a Supplier is saved, system generates a unique identity or name for that Supplier which can be used to refer the Supplier in various Buying transactions.

If not configured otherwise, ERPNext uses the Supplier's Name as the unique name. If you want to identify Suppliers using names like SUPP-00001, SUPP-00002, or such other patterned series, select the value of Supplier Naming By as "Naming Series".

You can define or select the Naming Series pattern from: **Settings > Data > Naming Series**

Read [Naming Series](/docs/user/manual/en/setting-up/settings/naming-series) to know more about defining a Naming Series.

### 1.2 Default Supplier Group

Configure what should be the default value of Supplier Group when creating a new Supplier. For example, if most of your suppliers supply you hardware, you can set the default as 'Hardware'.

## 2. Purchasing
### 2.1 Default Buying Price List

Configure what should be the default Price List when creating a new Buying transaction, the default is set as 'Standard Buying'. Item prices will be fetched from this Price List. You can modify the 'Price List' by using the arrow at the right-end of the field to change the currency and country.

### 2.2 Purchase Order Required

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice or a Purchase Receipt directly without creating a Purchase Order first. If retail transactions are involved where the order happens offline, then Purchase Orders can be skipped. If you're accepting sample Items, you can directly create a Purchase Receipt to receive the Items to your Warehouse.

This configuration can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Order" checkbox in supplier master

<img alt="Purchase Order Required" class="screenshot" src="{{docs_base_url}}/v12/assets/img/buying/po-required.png">

### 2.3 Purchase Receipt Required

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice without creating a Purchase Receipt first. In case the Item being transacted is a service, it'll not require a receipt, you can directly create an Invoice.

This configuration can be overridden for a particular supplier by enabling the "Allow Purchase Invoice Creation Without Purchase Receipt" checkbox in the supplier master

<img alt="Purchase Receipt Required" class="screenshot" src="{{docs_base_url}}/v12/assets/img/buying/pr-required.png">

### 2.4 Maintain Same Rate Throughout Purchase Cycle

If this is enabled, ERPNext will validate whether an Item's price is changing in a Purchase Invoice or Purchase Receipt created from a Purchase Order, i.e. it will help you maintain the same rate throughout the purchase cycle.

You can configure the action that system should take if the same rate is not maintained in the "Action If Same Rate is Not Maintained" field:

- **Stop**: ERPNext will stop you from changing the price by throwing a validation error.
- **Warn**: The system will let you save the transaction but warn you with a message if the rate is changed.

## 3. Allow Item to be added multiple times in a transaction

When this checkbox is unchecked, an item cannot be added multiple times in the same Purchase Order. However, you can still explicitly change the quantity. This is a validation checkbox for preventing accidental purchase of the same item. This can be checked for specific use cases where there are multiple sources for the same material, for example in manufacturing.

### 4. Related Topics
1. [Supplier Group](/docs/user/manual/en/buying/supplier-group)

{next}
