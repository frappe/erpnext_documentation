<!-- add-breadcrumbs -->
# Transações Bancárias

Este formulario mostra as transações bancárias no ERPNext. 

## 1. Pre-requisitos
Antes de usar o Registo Transações Bancárias, é aconselhavel criar os seguintes:

1. [Banco](/docs/user/manual/pt/contabilidade/banco)
1. [Conta Bancária](/docs/user/manual/pt/contabilidade/conta-bancária)

## 2. Como usar Transações Bancárias
Um Registo de Transações Bancárias não é para ser criado manualmente. É criado automanticamente usando:

1. [Reconciliação Bancária](/docs/user/manual/pt/contabilidade/reconciliação-banco)
    Ou
1. [Integração Plaid](/docs/user/manual/pt/intregação-erpnext/plaid_integration) para sincroniza com os Bancos

### 2.1 Campos Adicionais nas Transações Bancárias

* Data
* Status:
    * Pendente
    * Resolvido
    * Não Reconciliado
    * Reconciliado
* **Conta Bancária**: A Conta Bancária do qual as transações são feitas.

## 3. Funcionalidades/Campos

> Estes campos são actualizados via Reconciliação Bancária e não podem ser modificados apartir daqui.

### 3.1 Moeda e debito/credito

* **Debito**: O valor debitado.
* **Credito**: O valor creditado.
* **Moeda**: A Moeda no qual a transação foi feita.
* **Descrição:** Uma descrição para o extracto.

### 3.2 Referencia

**Numero de Referencia**: Um cheque ou outro numero de referencia.

### 3.3 Registo de Pagamentos

* **Documento de Pagamento**: O documento pelo qual as transações foram feitas quer seja Factura de Vendas, Reembolso de Despesas, Facturas de Compra, Registo de Pagamento ou Lançamento Contabilistico.
* **Registo de Pagamento**: Uma transação especifica. 
* **Valor Alocado**: O valor alocado para esta transação em particular.

**Valor Total Alocado**: O valor total alocado.
**Valor Não Alocado**: O valor total não alocado.
