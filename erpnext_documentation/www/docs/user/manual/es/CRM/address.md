<!-- add-breadcrumbs -->
# Dirección

Puede registrar las direcciones asociadas con un cliente potencial, un cliente, un proveedor, un accionista, un socio de ventas o un almacén.

También puede agregar una dirección como un registro independiente sin vincularla a ninguna de las entidades enumeradas anteriormente.

Para acceder a la lista de direcciones, ir a:
> Inicio > CRM > Address (o en la barra de búsqueda: Dirección lista)

## 1. Como crear una dirección

1. Ir a la lista de direcciones y dar click en nuevo
1. Seleccionar tipo de dirección.
1. Ingresar los detalles en **Dirección línea 1**,**Dirección línea 2**, **Ciudad / Provincia**, **País**, **Estado**, **País**.
1. Ingresar **Dirección de correo**, **Teléfono** y **Fax**
1. Ingrese Link DocType y Link Name para vincular esta dirección al cliente, proveedor, etc.
4. Guardar
    <img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/address.png">

You can also add an Address from the Customer or Supplier record by clicking on “New Address" button as shown below.

<img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/address-from-supp.png">

To Import multiple addresses from a spreadsheet, use the [Data Import Tool](/docs/user/manual/en/setting-up/data/data-import).

---
## 2. Features

### 2.1 Link an Address to Multiple Entities

An address may be linked to multiple customers or multiple suppliers.

An address can also be linked to customers and suppliers at the same time.

<img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/link_address_to_multipl_entities.png">

### 2.2 Address Title

If the address is not linked to any entity you need to manually add a title.

If the address is linked to an entity like a customer or supplier, the title is generated automatically in 'Entity Name-Address Type' format.

<img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/address_title_generation.png">

### 2.3 Preferred Billing Address and Shipping Address

If you check 'Preferred Shipping Address', the address would be automatically added in the Shipping Address in Sales Order, Sales Invoice and Delivery Note transactions.

Similarly, if you check 'Preferred Billing Address', the address would be automatically added in the Billing Address in Sales Order, Sales Invoice and Delivery Note transactions.

### 2.4 GST Localization for India
If the customer/supplier has registered for GST, enter Party GSTIN and GST State.Make sure GSTIN entered is in valid format.

In sales transactions along with address, GSTIN is also fetched.

<img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/gstin_in_so.png">

You can also add addresses of your own company's facilities. Check 'Is Your Company Address', select Company in Link DocType, and Company Name in Link Name for such addresses and you can select them in GST Sales Invoice to print your own address.

<img class="screenshot" alt="Contact" src="{{docs_base_url}}/assets/img/crm/own_company_address.png">


>GSTIN is to be added in Address and not in Customer/Supplier, as one Customer/Supplier may have multiple GSTIN (one for each state where he conducts his business).


### 3. Related Topics
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Supplier](/docs/user/manual/en/buying)
1. [Sales Partner](/docs/user/manual/en/selling)

{next}
