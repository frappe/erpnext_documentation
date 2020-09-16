<!-- add-breadcrumbs -->
# Solicitação de Pagamento

**Uma Solicitação de Pagamento é usada para pedir o pagamento a um Cliente de uma Ordem de Venda ou Factura.**

A Solicitação de Pagamento é enviada por email e contem uma ligação ao Gateway de Pagamento se for configurado. Voçê pode criar uma Solicitação de Pagamento via Ordem de Vendas ou Factura de Vendas. Uma Solicitação de Pagamento pode tambem ser configurado contra uma Ordem de Compra ou Factura de Compra para registos Internos. Depois, os pagamentos podem ser processados em massa usando a [Ordem de Pagamento](/docs/user/manual/pt/contabilidade/ordem-pagamento).

Para aceder os Termos de Pagamento vá para:
> Home > Contabilidade > Contas a Receber > Termos de Pagamento

## 1. Pre-requisitos
Antes de criar e usar Solicitação de Pagamento, é aconselhavel criar os seguintes primeiro:

1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Facturas de Compra](/docs/user/manual/pt/contabilidade/facturas-compra)
1. [Ordem de Vendas](/docs/user/manual/pt/vendas/ordem-vendas)
1. [Ordem de Compra](/docs/user/manual/pt/compras/ordem-de-compra)

## 2. Como criar uma Solicitação de Pagamento
Uma Solicitação de Pagamento não pode ser criada manualmente, é criada apartir de uma Ordem de Venda/Compra ou Factura.

### 2.1 Criando uma Solicitação de Pagamento via Ordem de Vendas
Numa Ordem de Venda, clique em Criar e depois clique em Pagamento para fazer um adiantamento de pagamento. Para saber mais sobre adiantamento de pagamento, visite a pagina [Registo de Adiantamento de Pagamento](/docs/user/manual/pt/contabilidade/adiantamento-pagamento).

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-from-so.png">

### 2.2 Criando uma Solicitação de Pagamento via Factura de Vendas
Numa Factura de Vendas, clique em Criar e depois clique em Pagamento para fazer contra a factura. 
<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-from-si.png">

Selecione a Conta do Gateway de Pagamento na Solicitação de Pagamento para as contas. Conta cabeça no gateway de pagmaento será considerada para criar
um Lançamento Contabilistico.

> Nota: Moeda da Factura/Ordem e moeda 'Conta de Gateway Pagamento' devem ser iguais.

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-details-1.png">

### 2.3 Notifique o Cliente
Voçê pode notificar o cliente sobre a Solicitação de Pagamento usando [Formato de Impressão](/docs/user/manual/pt/configuração/imprimir/formato-impressão). Se o contacto de email do cliente foi definido, será inserido automaticamente. Se não foi voçê pode definir o email na Solicitação de Pagamento. 

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-details-2.png">

### 2.4 Request Mail
Here is an example request email. O URL é gerado automaticamente se voçê definiu o respectivo pagamento de integração. Para saber mais sobre integrações, [visite esta pagina](/docs/user/manual/pt/integração-erpnext).

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/assets/img/accounts/pr-email.png">

### 2.5 Solicitação de Pagamento sem usar qualquer Gateway

No caso de voçê não quiser usar qualquer integração ou gateway de pagamento e quise somente enviar a notificação, simplesmente defina a Conta Bancária. Voçê irá ter de escrever a mensagem de acordo e com os seus dados bancários. A parte pode depois transferir os valores para a conta bancária mecionada.

## 3. Topicos Relacionados
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)