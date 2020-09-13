<!-- add-breadcrumbs -->

# Facturas Inter Empresa

**Um Jornal de Factura de Inter Empresa é feito entre organizações que pertencem ao mesmo grupo.**

Ao criar Facturas de Compra ou Facturas de Venda para um empresa singular, voçê pode criar facturas inter-ligadas para multiplas empresas.

Por exemplo, voçê pode criar uma Factura de Vendas para a empresa 'Empresa ABC' e criar a Factura de Venda contra esta Factura de Compra para outra empresa 'Empresa XYZ' e ligar ambas.

## 1. Como criar Facturas Inter Empresa

### 1.1 Configuração
1. Vá para: **Contabilidade > Contas a Receber > Cliente**.
1. Selecione o Cliente que voçê quer escolher para fazer factura inter-ligada.
1. Active a caixa, **É Cliente Interno** como mostra em baixo:

 <img class="screenshot" alt="Internal Customer" src="{{docs_base_url}}/assets/img/accounts/make-internal-customer.png">

1. Adicione a empresa que o Cliente representa no campo **Representa a Empresa**. Esta é a empresa pelo qual a Factura de Venda será criada.
1. Na tabela **Permitido Fazer Transação Com**, adicione a empresa pelo qual voçê irá criar a Factura de Compra. 
1. Agora, quando voçê criar a Factura de Compra contra a Empresa A (cliente é da empresa B), o vendedor é da empresa A), será ligado a Factura de Venda da empresa A usando este Cliente Interno da empresa B.
1. Agora, voçê precisa fazer o mesmo procedimento para configurar o Fornecedor para facturas inter-ligação.
1. Vá para: **Contabilidade > Contas a Pagar > *Selecione o Fornecedor***
1. Assinale É Fornecedor Interno.
1. No campo **Representa a Empresa** , adicione a empresa pelo qual voçê adicionou na tabela **Permitido Fazer Transação Com** para o Cliente.
1. Na tabela **Permitido Fazer Transação Com** para o Fornecedor, adicione a empresa pelo qual o Cliente representa. Este é a empresa pelo qual voçê vai criar uma Factura de Compra inter-ligada.
1. Aqui está um screenshot da empresa Fornecedora para evitar qualquer confusão:

 <img class="screenshot" alt="Internal Supplier" src="{{docs_base_url}}/assets/img/accounts/make-internal-supplier.png">

### 1.2 Criando a Factura
1. Agora, crie a nova [Factura de Venda](/docs/user/manual/pt/contabilidade/factura-vendas), e preencha os campos.
1. Lembre-se de selecionar o Cliente que é o cliente interno e a empresa pelo qual ele esta a comprar.
1. Salvar e Submeter a Factura.

 <img class="screenshot" alt="Inter company invoice" src="{{docs_base_url}}/assets/img/accounts/make-inter-company-invoice.png">

1. Antes de voçê fazer uma *Factura Inter Empresa* voçê precisa fazer o seguinte:
 1. O preço de venda e compra entre as empresas deve estar sincronizado.
 1. Vá para **Inventario > Lista de Preços**, crie uma nova Lista de Preços para as transações inter empresa.
 1. Assinale ambas opções Vendas e Compras neste Lista de Preço.
 1. Vá para **Comprar > Fornecedor > *fornecedor interno***, na moeda e secção de lista de preço, defina a lista de preço para a nova que foi criada.
 1. Faça o mesmo para o cliente interno, ex. defina a lista de preço para o novo.
 1. Agora, voçê pode fazer uma Factura de Compra ou Venda Inter Empresas.
1. Debaixo do botão **Criar**, voçê irá encontrar uma ligação **Factura Inter Empresa**, ao fazer o clique na ligação, voçê irá ser enviado para uma nova pagina do formulario de Factura de Compra.
1. Aqui, o fornecedor e a empresa serão auto-procurados dependendo na empresa que selecionou na Factura de Vendas.
> ***Lembre-se**: Somente pode have um Fornecedor ou Cliente Interno por empresa.*
1. Submeter a factura, feito! Agora, ambas as facturas estão inter-ligadas. *Tambem, ao cancelar qualquer uma das facturas, a ligação será quebrada tambem.*

> Nota: Uma Factura Inter Empresa somente irá afectar o razão contabilistico e não o razão de stock. Isto porque as empresas pertencem ao mesmo grupo de empresas.

Voçê pode fazer o mesmo processo ao criar Facturas de Compra e depois uma Factura de Venda inter-ligadas apartir da Factura de Compra submetida.

### 2. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
1. [Lançamento Contabilistico Inter Empresa](/docs/user/manual/pt/contabilidade/lançamento-contabilistico-inter-empresa)
