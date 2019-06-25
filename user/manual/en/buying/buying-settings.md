<!-- add-breadcrumbs -->
# Buying Settings

Buying Settings is where you can define properties which will be applied in the Buying module's transactions. 
You can find Buying Settings at:
> Home > Buying > Settings > Buying Settings

![Buying Settings]({{docs_base_url}}/assets/img/buying/buying-settings.png)

Let us look at the various options that can be configured:

## 1. Supplier
### 1.1 Supplier Naming By

When a Supplier is saved, system generates a unique identity or name for that Supplier which can be used to refer the Supplier in various Buying transactions.

If not configured otherwise, ERPNext uses the Supplier's Name as the unique name. If you want to identify Suppliers using names like SUPP-00001, SUPP-00002, or such other patterned series, select the value of Supplier Naming By as "Naming Series".

You can define or select the Naming Series pattern from: **Settings > Data > Naming Series**

[Click here](/docs/user/manual/en/setting-up/settings/naming-series) to know more about defining a Naming Series.

### 1.2 Default Supplier Group

Configure what should be the default value of Supplier Group when creating a new Supplier. For example, if most of your suppliers supply you hardware, you can set the default as 'Hardware'.

## 2. Purchasing
### 2.1 Default Buying Price List

Configure what should be the default Price List when creating a new Buying transaction, the default is set as 'Standard Buying'. Item prices will be fetched from this Price List. You can modify the 'Price List' by using the arrow at the right-end of the field to change the currency and country.

### 2.2 Purchase Order Required

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice or a Purchase Receipt directly without creating a Purchase Order first.

### 2.3 Purchase Receipt Required

If this option is configured "Yes", ERPNext will prevent you from creating a Purchase Invoice without creating a Purchase Receipt first.

### 2.4 Maintain Same Rate Throughout Purchase Cycle

If this is checked, ERPNext will stop you from changing an Item's price in a Purchase Invoice or Purchase Receipt created by a Purchase Order, i.e. it will maintain the same price throughout the purchase cycle. If there is a requirement where the Item's price can change, you should uncheck this option.

## 3. Allow Item to be added multiple times in a transaction

When this checkbox is unchecked, an item cannot be added multiple times in the same Purchase Order. However, you can still explicitly change the quantity. This is a validation checkbox for preventing accidental purchase of the same item. This can be checked for specific use cases where there are multiple sources for the same material, for example in manufacturing.

### 4. Related Topics
1. [Supplier Group](/docs/user/manual/en/buying/setup/supplier-group)

{next}