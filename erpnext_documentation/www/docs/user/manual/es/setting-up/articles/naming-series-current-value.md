<!-- add-breadcrumbs -->
# Configuración del valor actual para nombrar series

La función Naming Series le permite definir el prefijo para nombrar documentos. Por ejemplo, si una orden de venta tiene el prefijo "SO", entonces la serie se generará como SO-00001, SO-00002 ... y así sucesivamente. [Haga clic aquí](/docs/user/manual/en/setting-up/settings/naming-series.html) para saber cómo puede personalizar Number Series para una transacción / master en ERPNext.

### 1. Configuración del valor actual

La función Naming Series también ofrece una herramienta en la que puede establecer el valor actual para un prefijo específico. Por lo general, esto es necesario si ha comenzado a utilizar ERPNext recientemente y tiene transacciones antiguas en el sistema anterior, y desea que la serie de numeración comience desde donde terminó en el sistema anterior. Consideremos un escenario para aprender esto mejor.

Por ejemplo, tiene 322 órdenes de venta creadas en su sistema anterior con SO00322 como Id. De orden de venta más alta. En ERPNext, necesita la primera orden de venta para recoger # 323 cuando se guarda. Para habilitar esto, debe establecer el valor actual para la serie SO en los siguientes pasos.

#### Ir a la herramienta Naming Series

`Configuración > Sistema > Naming Series`

#### Update Series Section

<img alt="Update Series Section" class="screenshot" src="{{docs_base_url}}/assets/img/articles/current-no-1.png">

#### Select Prefix

Considering our scenario, prefix for Sales Order will be "SO".

<img alt="Series Prefix" class="screenshot" src="{{docs_base_url}}/assets/img/articles/current-no-2.png">

#### Current Value

If you have currently 12 Sales Orders created in your account, then current value updated will be 12. You can edit Current Value to 322, and then click on Update Series Number.

<img alt="Series Current Value" class="screenshot" src="{{docs_base_url}}/assets/img/articles/current-no-3.png">

With this setting, you will have numbering for the New Sales Orders starting with #323.

### 2. Error Due Series Number

If you receive a Duplicate Name error while saving a transaction, for example, while saving Item Price, you receive an error saying:

`Duplicate name Item Price RFD/00016`

This error message indicates that when you are saving Item Price, system is trying to allocate "RFD/00016" to that Item Price record. But it is finding that Item Price with this ID is already existing in your system.

This error could arise because Current Value for Series/Prefix of Item Price is disturbed and not in sync with actual Current Value. While actual Current Value for Item Price could be 20 (or any number more than 16), someone has set Current Value for this series as 15. 

To confirm actual Current Value for particular Series, you should check report for document in question (Item Price in this case), and check for the Item Price ID with highest value. 

Let's assume we find that actual Current Value for Item price is 22, then you go Naming Series, and set Current Value for the Prefix/Series of Item Price to 22, and Update Series Number.

These instructions is applicable for all the documents in ERPNext for which user can customize Series and its Current Value.

Let's consider another scenario to learn this better. On assigning a document to another user, error message says:

`Duplicate name ToDo TDI00014286`

This indicate the Current Value for Series/Prefix of ToDo (TDI) has been disturbed. You should follow these steps to correct value for Current Value for TDI prefix.

1. Check ToDo report for the highest ToDo id value.
1. Setup >> Settings >> Naming Series
1. Check section B of Update Series
1. Select Prefix for ToDo "TDI"
1. Ensure that highest number for ToDo is updated as Current Value in Naming Series. If not, correct Current Value, and click on "Update Series Numbering".

<!-- markdown -->
