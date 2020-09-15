<!-- add-breadcrumbs -->
# Ponto de Vendas

**Um Ponto de Vendas refer a hora e lugar aonde a transação a retalho é feita.**

Para operações a retalho, a entrega de bens, accrual de vendas e pagamentos todos acontecem num unico evento, que é normalmente chamado de 'Ponto de Vendas' (POS).

No ERPNext Factura de Vendas podem ser criadas apartir do POS. São dois passos para configurar o POS:

Para aceder o POS, vá para:
> Home > Retalho > Operações de Retalho > POS

## 1. Pre-requisitos
Antes de criar ou usar o Ponto de Vendas, é aconselhavel criar os seguintes:

1. [Perfil POS](/docs/user/manual/pt/contabilidade/perfil-pos)

## 2. Como criar uma Factura POS
Uma vez configurado o perfil POS, voçê pode começar a cobrar no POS.

1. Vá para o POS e selecione o Cliente.
1. Adicione Itens apartir da lista mostrada a direita fazendo um clique neles.
1. Tenha a certeza que o Item tem um Preço de Venda configurado na Lista de Preços.
1. Modifique as quantidades de acordo a necessidade.
1. Para modificar o Preço e Desconto, voçê deve activar no Perfil do POS.
1. Um Armazem por defeito precisa ser configurado para fazer as transações. Se um Armazem foi configurado quer no Item e no Perfil do POS, o do Perfil POS será o preferido.
1. Note que voçê precisa ter Itens nos seus Armazens antes de poder vender. Se os Itens não estão disponiveis, um ponto a vermelho será mostrado proximo ao Item quando selecionado.
  ![Ecrão POS](/docs/assets/img/accounts/pos-screen.png)
1. Quando todos os Itens foram adicionados, clique em Pagar. Será perguntado para submeter a Factura de Venda.
1. Selecione o Modo de Pagamento, Submeter
1. Voçê pode depois imprimir a factura POS.
  ![Ciclo POS](/docs/assets/img/accounts/pos-cycle.gif)
  
Depois da Factura de Vendas ser submetida, voçê pode imprimir ou enviar por email directamente para o cliente.


### 2.2 Adicionando um Item
No balcão de cobrança, o revendedor precisa selecionar Itens no qual o Cliente comprou. No interface do POS voçê pode selecionar um Item de duas formas. Primeiro, fazendo um clique na imagem do Item e a outra, pelo leitor de Codigo de Barras / Nº de Serie.

* **Selecionar Item**: Para selecionar o produto faça um clique na imagem do Item para adicionar ao cartão de compras. O cartão é a area que prepara o cliente para sair aonde permite editar informações do produto, ajustar impostos e adicionar descontos.

* **Codigo de Barras / Nº de Serie**: Um Codigo de Barras / Nº de Serie é a representação de uma maquina de leitura optica relacionada ao objecto no qual é anexado. Digite o Codigo de Barras / Nº de Serie na caixa como mostra a imagem em baixo e pause por um segunte, o item será automaticamente adicionado ao Cartão de Compras.

<img class="screenshot" alt="POS Item" src="{{docs_base_url}}/assets/img/accounts/pos-item.png">

> Dica: Para mudar a quantidade de um Item, digite a quantidade desejada na caixa de quantidade.
São muita das vezes usados se o mesmo Item é comprado em massa.

Se a lista do seu produto é muito longa use o campo de Procura, digite o nome do produto na caixa de Procura.

### 2.3  Apagando um Item do Cartão de Compras
1. Selecione a linha no cartão e clique no botão Apagar que está na caixa numerica

    <img class="screenshot" alt="POS Item" src="{{docs_base_url}}/assets/img/accounts/pos_deleted_item.gif">


2. Defina a Qtd como zero para remover o Item da factura POS. Tem duas formas de apagar um Item.
  * Se a Qtd for 1, clique no sinal menos para tornar zero.
  * Manualmente digite na quantidade 0 (zero).


### 2.4 Trocos

O POS calcula o valor pago extra pelo cliente, no qual o usuário pode devolver pela conta em dinheiro. O Usuário tem que definir a conta para os trocos no Perfil POS.

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/change-amount.png">

### 2.5 Write off Amount
Se voçê estiver a writing off algum valor. Por exemplo quando voçê recebe um valor a mais como o resultado de não ter o valor necessário para o troco, clique em ‘Write off Outstanding Amount’ e defina a conta.

Valores em falta pode ser write off no POS, o usuário tem que digitar o valor em baixo do campo Write Off no ecrão de pagamento.

Por exemplo, valor a pagar é 2,310, mas o Cliente pagou 2,300, então valor written off será de 10.
<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/write-off.png">

O Sistema aloca o valor do Write Off na conta do Razão Geral que foi selecionada no Perfil do POS.

### 2.6 Alterar o Perfil POS

Altere o Perfil POS via:
> Menu > Alterar Perfil POS

Seleciona a Empresa e escolha o Perfil POS apartir da lista. Voçê pode definir o novo Perfil POS selecionado como o seu por defeito para a Empresa.

<img class="screenshot" alt="Change POS Profile" src="{{docs_base_url}}/assets/img/accounts/Change-POS-Profile.png">

## 3. Funcionalidades

### 3.1 Adicionando um Cliente
No POS, o usuário pode selecionar um Cliente existente durante um Ordem ou criar um novo cliente. Esta funcionalidade funciona em modo Offline tambem. O Usuário pode tambem adicionar os detatlhes do cliente como numero de telefone, endereço, etc no formulario. O Cliente que foi criado no POS será sincronizado quando a ligação de Internet restabelecer.

<img class="screenshot" alt="POS Customer" src="{{docs_base_url}}/assets/img/accounts/pos-customer.gif">

### 3.2 Offline POS

No ERPNext, voçê pode criar Facturas POS, mesmo quando não tem Internet. Factura POS criadas no modo offline serão salvas localmente no seu navegador (cached). Se a ligação de Internet estiver desligada ao criar uma Factura POS, voçê poderá continuar as vendas. Uma vez a ligação restabelecida as facturas serão sincronizadas para o seu ERPNext.

Para saber mais sobre como Facturas POS podem ser criadas offline, [verifique aqui.](https://frappe.io/blog/blog/erpnext-features/offline-pos-in-erpnext-7)

### 3.3 Offline Records
Todos os registos do POS são guardados no nevegado, sicronizados e submetidos depois de um minuto de intervalo se o sistema estiver ligado a Internet. O usuário pode ver os registos offline fazendo um clique em Menu > Ver Registos Offline.

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/offline-records.png">

### 3.4 Lançamento Contabilistico (Registo GL) para o Ponto de Vendas:

Debitos:

  * Cliente (total geral)
  * Banco/Dinheiro (pagamento)

Creditos:

  * Recebimento (total geral, menos impostos para cada Item)
  * Impostos (responsabilidades para serem pagas ao governo)
  * Cliente (pagamento)
  * Write Off (opcional)
  * Conta para Trocos (opcional)

Para ver os registos depois de submeter a [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas), clique em **Livro Contabilistico**.

### 3.5 Email

Os Usuário podem enviar email apartir do POS, depois de submeter um pedido, basta fazer o clique em Menu > Email:
<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/pos-email.png">
Depois de sincronizar um pedido POS, email é enviado para o Cliente com a impressão da factura em anexo.

### 3.6 Fechamento do Caixa / POS Closing Voucher

No fim do dia, o caixa pode fechar o seu POS selecionando Fechamento do caixa.
Clique no Menu e selecione 'Fechamento do Caixa'. Selecione o periodo, seu Perfil POS e seu usuario para ir buscar todas as vendas feitas.

Para troca de turno ou fecho de caixa, use [Fechamento do caixa](/docs/user/manual/pt/contabilidade/fecho-caixa-pos).

<img class="screenshot" alt="POS Payment" src="{{docs_base_url}}/assets/img/accounts/pos-closing-voucher.png">

Digite o valor recebido para cada modo de pagamento. Se voçê notar diferença entre o valor do sistema e o valor fisico do dinheiro recolhido, crie um registo de Diferença.

### 4. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Ordem de Compra](/docs/user/manual/pt/compras/ordem-compra)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Solicitação de Pagamento](/docs/user/manual/pt/contabilidade/solicitação-pagamento)
