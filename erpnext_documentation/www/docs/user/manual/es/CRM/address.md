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
1. Ingrese Link DocType y Link Name para vincular esta dirección al **cliente**, **proveedor**, **etc**.
4. Guardar

    <img class="screenshot" alt="Contacto" src="{{docs_base_url}}/assets/img/crm/address.png">

También puede agregar una dirección del registro de cliente o proveedor haciendo clic en el botón "Nueva dirección" como se muestra a continuación.

<img class="screenshot" alt="Contacto" src="{{docs_base_url}}/assets/img/crm/address-from-supp.png">

Para importar varias direcciones desde una hoja de cálculo, use la [Herramienta de importación de datos](/docs/user/manual/en/setting-up/data/data-import).

---
## 2. Características

### 2.1 Vincular una dirección a varias entidades

Una dirección puede estar vinculada a varios clientes o proveedores.

Una dirección también se puede vincular a clientes y proveedores al mismo tiempo.

<img class="screenshot" alt="Contacto" src="{{docs_base_url}}/assets/img/crm/link_address_to_multipl_entities.png">

### 2.2 Título Dirección

Si la dirección no está vinculada a ninguna entidad, debe agregar un título manualmente.

Si la dirección está vinculada a una entidad como un cliente o proveedor, el título se genera automáticamente en formato 'Nombre de entidad-Tipo de dirección'.

<img class="screenshot" alt="Contacto" src="{{docs_base_url}}/assets/img/crm/address_title_generation.png">

### 2.3 Dirección de facturación y dirección de envío preferidas

Si marca 'Dirección de envío preferida', la dirección se agregará automáticamente en la Dirección de envío en las transacciones de Orden de venta, Factura de venta y Nota de entrega.

De manera similar, si marca 'Dirección de facturación preferida', la dirección se agregará automáticamente en la Dirección de facturación en las transacciones de Orden de venta, Factura de venta y Nota de entrega.

### 2.4 Localización de GST para India
Si el cliente / proveedor se ha registrado para GST, ingrese Party GSTIN y GST State. Asegúrese de que GSTIN ingresado esté en formato válido.

En las transacciones de ventas junto con la dirección, también se obtiene GSTIN.

<img class="screenshot" alt="Contacto" src="{{docs_base_url}}/assets/img/crm/gstin_in_so.png">

También puede agregar direcciones de las instalaciones de su propia empresa. Marque "Es la dirección de su empresa", seleccione Empresa en Link DocType y Nombre de la empresa en Link Name para dichas direcciones y puede seleccionarlas en GST Sales Invoice para imprimir su propia dirección.

<img class="screenshot" alt="Contacto" src="{{docs_base_url}}/assets/img/crm/own_company_address.png">


>GSTIN debe agregarse en Dirección y no en Cliente / Proveedor, ya que un Cliente / Proveedor puede tener múltiples GSTIN (uno para cada estado donde realiza su negocio).


### 3. Related Topics
1. [Customer](/docs/user/manual/en/CRM/customer)
1. [Supplier](/docs/user/manual/en/buying)
1. [Sales Partner](/docs/user/manual/en/selling)

{next}
