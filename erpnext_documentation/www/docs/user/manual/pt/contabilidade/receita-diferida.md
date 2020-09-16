# Receita Diferida

**Receita Diferida refere a adiantamento de pagamento uma Empresa recebe por um produto ou serviço que estão para ser entregues ou feitos no futuro.** 

É tambem conhecido como Receitas não Ganhas.

A empresa que recebe o pre-pagamento regista o valor como uma Receita Diferida nas folhas de balanço como uma responsabilidade. A Receita Diferida é uma responsabilidade porque reflete uma receita que não foi ganha e representa produtos ou serviços devidos a um Cliente. Como o produto ou serviço é entregue com o tempo, é reconhecido como receita no extracto de Recebimentos.

## 1. Como usar uma Receita Diferida

Internet e provedores de difusão de serviços oferecem planos de subscrição anual ou trimestral. Eles recebem um adiantamento de pagamento completo de um Cliente para meses, mas alocar o recebimento mensal e alocar nos livros de contabilidade. Este é Receita Diferida para o Fornecedor e para o Cliente [Receita Diferida](/docs/user/manual/pt/contabilidade/receita-diferida). De seguida está como devem ser configuradas as contas Receita Diferida no ERPNext para automatizar o processo.

### 1.1 Item

Na ficha do Item criado para um plano de Subscrição, em baixo da seção Receita Diferida, verifique o campo **Activa Receita Diferida**. Voçê pode tambem selecionar uma conta Receita Diferida para este iitem em particular e o numero de meses.

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-item.png">

### 1.2 Factura de Vendas

Ao criar a Factura de Vendas para o Item Receita Diferida, em vez de postar na conta de Recebimentos, a conta Receita Diferida é creditada pelo valor da venda. Se voçê fez a definição da conta e perido no Item, então a conta e a Data de Inicio e Fim do serviço serão inseridos automaticamente.

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-invoice.gif">

### 1.3 Lançamento Contabilistico

Baseado na Data de Inicio eFim definidos na tabela do Item da Factura De Vendas, o Lançamento Constabilistico é criado automaticamente no fim de cada mês. Debita o valor da conta Receita Diferida e credita na conta Recebimentos selecionada para o Item na Factura de Vendas.

De seguida um exemplo do Recebimento da Receita Diferida do Item alocado usando varios Lançamentos Contabilisticos.

<img class="screenshot" alt="Item - Deferred Revenue" src="{{docs_base_url}}/assets/img/accounts/deferred-jv.png">

## 2.  Video

<div class="embed-container">
  <iframe src="https://www.youtube.com/embed/j6mx-EHU4aY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
  </iframe>
</div>

### 3. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas)
