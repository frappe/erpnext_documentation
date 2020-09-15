<!-- add-breadcrumbs -->
# Registo de Pagamento

**Um Registo de Pagamento é um registo indicando que o pagamento de uma factura foi feito.**

Registo de Pagamento pode ser contra as seguintes transaçãoes.

* Factura de Vendas
* Factura de Compras
* Ordens de Venda (Adiantamento de Pagamento)
* Ordem de Compra (Adiantamento de Pagamento)
* Reembolso de Despesas
* Transferencia Interna

No ERPNext, tem duas opções no qual o Usuario pode capturar o pagamento:

* Registo de Pagamento (Default)
* Lançamento Contabilistico

Aqui estão os diagramas para entender o fluxo:

Em Vendas:
![Pagamento de Vendas]({{docs_base_url}}/assets/img/accounts/pe-sales.png)

Em Compras:
![Pagamento de Compras]({{docs_base_url}}/assets/img/accounts/pe-purchase.png)


Para aceder a lista de Registo de Pagamento, vá para:
> Home > Contabilidade > Contas de Recebimentos/Pagamentos > Registo de Pagamento

## 1. Pre-requisitos
Um  Registo de Pagamento pode tambem criado directamento e depois ligado a uma Ordem/Factura. Antes de criar e usar o Registo de Pagamento, é aconselhado criar as seguintes:

1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Fornecedor](/docs/user/manual/pt/compras/fornecedor)
1. [Conta Bancária](/docs/user/manual/pt/contabilidade/conta-bancária)

Se voçê estiver a seguir o Ciclo das Vendas/Compras, voçê precisa fazer o seguinte:

1. [Ordem de Vendas](/docs/user/manual/pt/vendas/ordem-vendas) (Adiantamento de Pagamento)
1. [Ordem de Compras](/docs/user/manual/pt/compras/ordem-de-compras) (Adiantamento de Pagamento)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compras](/docs/user/manual/pt/contabilidade/factura-compra)


Para Configurar:

1. [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas)
1. [Empresa](/docs/user/manual/pt/configuração/configuração-empresa) (para as contas padrão)

## 2. Como criar um Registo de Pagamento
Ao submeter o documento no qual o Registo de Pagmento pode ser feito, voçê irá encontrar a opção de Pagamento debaixo do botão **Criar**.

![Registo de Pagamento apartir da OV]({{docs_base_url}}/assets/img/accounts/payment-entry-so.png)

1. Altere a data de postagem.
1. O Tipo de Pagamento será definido com base na transação que fez, 'Recebimento', 'Pagamento' e 'Transferencia Interna'.
1. No Tipo de Parte, Parte, o Nome da Parte será inserido automanticamente.
1. A Conta Paga a Favor e Pago De será inserido como definido no [Formulario Empresa](/docs/user/manual/pt/configuração/configuração-empresa).
1. O Valor Pago será inserido apartir da Factura.
1. Salvar e Submeter.
 ![Registo de Pagamento apartir da OV]({{docs_base_url}}/assets/img/accounts/payment-entry-so.gif)

### 2.1 Criando um Pagamento Manual
Um Registo de Pagamento criado manual não terá uma ordem/factura ligada ao mesmo. Pagamentos feitos desta forma serão guardados na conta do Cliente/Fornecedor e pode ser reconciliados depois usnado a [Ferramenta de Reconciliação de Pagamento](/docs/user/manual/pt/contabilidade/reconciliação-pagamento).

1. Vá para a lista de Registo de Pagamento e clique em Novo.
1. Selecione o Tipo de Parte e o respectivo Cliente/Fornecedor.
1. Selecione a Conta Bancária/Dinheiro Pago a Favor e Pago De. Digite o Numero do Cheque e a data se foi transferencia Bancária.
1. Digite o Valor Pago.
1. Salvar e Submeter.


## 3. Funcionalidades

### 3.1 Definindo o Modo de Pagamento

**Modo de Pagamento**: Criando este ajuda a classificar os Registos de Pagamento baseados no modo de pagamento usado. Modos de Pagamento podem ser Banco, Dinheiro, Cartões, etc.

> **Dica**: No [Modo de Pagamento](/docs/user/manual/pt/contabilidade/modo-de-pagamento), a Conta padrão pode ser definida. Esta conta de Pagamento padrão será inserida nos Registos de Pagamento.

### 3.2 Pagamento Apartir/Para

![Partes de Pagamento]({{docs_base_url}}/assets/img/accounts/payment-party.png)

* **Tipo de Parte**: Quer seja Cliente, Fornecedor, Funcionário, Acionista, Estudante ou Membro de uma NGO.
* **Parte**: A parte especifica no qual o Registo de Pagamento é feito.
* **Nome da Parte**: O nome da parte, é inserido automaticamente.
* **Conta Bancária da Empresa**: Sua Empresa [Conta Bancária](/docs/user/manual/pt/contabilidade/conta-bancária).
* **Conta Bancária da Parte**: A Parte [Conta Bancária](/docs/user/manual/pt/contabilidade/conta-bancária).
* **Contacto**: Se a Parte for uma organização, a Pessoa de Contacto será guardada aqui.

### 3.3 Contas

![Registo de Pagamentos]({{docs_base_url}}/assets/img/accounts/payment-accounts.png)

* **Balanço da Parte**: O valor geral recebido ou pago de um Cliente ou Fornecedor das Factura definidas no Registo de Pagamento corrente. Valores Pagos serão positivos e se foi feito adiantamento de pagamento, serão negativos.
* **Conta Paga Apartir de**: A [Conta](/docs/user/manual/pt/contabilidade/plano-de-contas) no qual o valor será deduzido quando o Pagamento for submetido.
* **Conta Paga Para**: A [Conta PdC](/docs/user/manual/pt/contabilidade/plano-de-contas) no qual o valor será adiconado quando o Pagamento for submetido.

* **Conta da Moeda**: As Moedas destas contas serão inseridas como definidas na [Conta](/docs/user/manual/pt/contabilidade/plano-de-contas) e não podem ser modificadas aqui. Para saber mais sobre transações em multiplas moedas, [visite esta pagina](/docs/user/manual/pt/contabilidade/artigos/gerir-transações-multiplas-moedas).
* **Conta de Balanço**: O valor do balanço total de todas as facturas das contas selecionadas.

**Valor Pago**: O **valor total** pago para o Registo de Pagamento corrente é mostrado neste campo.

> **Nota**: Quando fizer Registo de Pagamntos, a conta de Banco padrão será inserida nas seguintes ordens se foi definida:

> * Formulario Empresa
> * Conta padrão do Modo de Pagamento
> * Conta Bancária Cliente/Fornecedor
> * Selecionar manualmente no Registo de Pagamento

### 3.4 Referencia

#### Procurando Facturas Não Pagas

Este pode ser usado para fazer pagamentos a varias Facturas de Venda usando o Registo de Pagamento. Quando ao criar um Novo Registo de Pagamento, ao fazer o clique no botão **Obter Facturas Pendentes** todas as Factura Pendentes e Ordens abertas serão inseridas. Voçê precisa digitar o 'Valor Pago' para ver este botão. Apartir daqui o limite de datas e as facturas para serem procuradas e selecionadas.

![Factura Pendente]({{docs_base_url}}/assets/img/accounts/outstanding-pe.png)

Se a Parte não fez pagamento completo, digite o valor pago no campo 'Alocado'.

Se ao criar o Registo de Pagamento para um Cliente, o valor de pagamento será alocado contra a Factura de Venda. Da mesma forma, ao criar um Registo de Pagamento para o Fornecedor, Valor Pago será alocado contra a Factura de Compra

#### Tabela de Referencia de Pagamentos

* **Tipo**: Quer o pagamento seja feito contra a Ordem de Vendas, Factura de Vendas ou Lançamento Contabilistico.
* **Nome**: O ID particular da transação é inserido/selecionado aqui.
* **Valor Total**: O Valor total de uma Factura/Lançamento Contabilistico na linha.
* **Em Falta**: O valor a receber/pagar para esta factura.
* **Alocado**: Se o Valor Pago for menos que o valor da factura somente o valor pago será alocado para as facturas inseridas no Registo de Pagamento. O pagamento pode ser feito em partes, por exemplo, se houver trê facturas no valor de 20, 20, 20, o Valor Pago é de 60 então esta Valor Pago será distribuido equitativamente. [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento) podem tambem ser incluidos.

 ![Factura Pendente]({{docs_base_url}}/assets/img/accounts/outstanding-pe.png)

#### O que é um Valor Não Alocado?
Quando um Registo de Pagamento é feito no ERPNext e o Valor Pago é maior que o total da factura, é guardado na conta do Cliente/Fornecedor. Este valor está correntemente 'Não Alocado'. Valor não alocado pode ser usado contra futuras facturas.

Por exemplo, voçê cria uma Factura de Vendas no total de 1,000 e o Cliente paga 1,500. Quando fizer outra factura em nome do mesmo Cliente outra vez por 1,000, o valor pago de 500 previamente pode será ser usado.

### 3.5 Dedução ou Perca

Quano um Registo de Pagamento é criado contra um factura, pode haver alguma diferente no Valor Pago actual e o valor pendente da factura. Esta diferença pode ser devido a erros de arredondamento ou mudanças de taxa de cambio. Voçẽ pode definir uma Conta aqui aonde esta diferença será alocada.

![Factura Pendente]({{docs_base_url}}/assets/img/accounts/pe-get-outstanding.gif)

As percas/deduções pode ser written off:
![Deduções de Pagamento]({{docs_base_url}}/assets/img/accounts/payment-deductions.png)

Vejamos um exemplo aqui aonde o valor pago é de 25 mas o valor alocado é de 30 vendo que 30 é o valor a ser recebido pela factura. O 'Valor da Diferença' será de 5 neste caso. Este valor da diferença pode acontecer devido a descontos ou Taxas d Cambio. O Valor da Diferença precisa ser 0 para poder submeter o Registo de Pagmento. Este pode ser ajustado usando o botão **Criar Registo de Diferença**. O valor será ajustado na Conta Write Off.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-5.gif">

### 3.6 Write Off

Write off pode acontecer quando o valor pago +e enos que o valor alocado. ex. o valor em falta é considerado perdido nas taxas mistas ou esse valor não será pago. É considerado uma perca.

![Pagamento Write Off]({{docs_base_url}}/assets/img/accounts/payment-write-off-1.png)

Nesta tabela, a dedução ou perca nos pagamentos pode ser ajustados como explicado no exemplo anterior da secção.

![Pagamento Write Off]({{docs_base_url}}/assets/img/accounts/payment-write-off.png)

### 3.5 Depois de Submeter
Salvar e Submeter um Registo de Pagamento. Ao submeter, valores pendentes serão actualizados nas Facturas.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-8.png">

Se o registo de pagamento foi criado contra a Ordem de Venda ou Ordem de Compra, a campo 'Adiantamento Pago' será actualizado. Ao criar a Factura contra estras transações, Registo de Pagmento será auto-actualizado para que voçê aloque o valor da factura contra o adiantamento de pagamento feito.

Para os pagamentos de recebimentos, as contas ficam desta forma.

 * Debito: Conta de Banco ou Dinheiro
 * Credito: Cliente (Devedor)

Para pagamentos de saida:

 * Debito: Fornecedor (Credor)
 * Credito: Conta Banco ou Dinheiro

## 4. Outros Casos

### 4.1 Registo de Pagamento Multi Moedas

Se voçê quer manter as contas dos recebimentos/pagamentos em moeda estrangeira, então as contas em moeda estrangeira (diferenta a moeda da Empresa) e ligue a uma conta de Parte. Por exemplo:

![Moeda Estrangeira no Cliente]({{docs_base_url}}/assets/img/accounts/cust-foreign-acc.png)

O ERPNext permite que voçẽ mantenha contas e facturas em [multiplas moedas](/docs/user/manual/pt/contabilidade/contabilidade-multi-moedas). Se a factura é feita na moeda da parte, a Taxa de Cambio entre a moeda base da Empresa e da parte são incluidas na factura.

> Nota: Uma conta separada Devedor/Credor precisa ser criada e selecionada na Factura de Vendas/Ordem para qua a taxa de cambios funcione correctamente. Por exemplo, se o Cliente é dos US, crie uma conta de recebimento chamada 'Devedor US'.

Ao criar o Registo de Pagamento contra esta factura, a taxa de cambio será inserida, mas voçê pode definir a Taxa de Cambio no momento do pagamento para igualar os seis registos.

Clique no botão **Definir Cambio de Ganho/Perca** para automaticamente incluir uma linha para write off o valor diferente.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-6.png">

Vendo que a Taxa de Cambio fluctua constantemente, isto pode levar a diferença no valor de pagamento contra o total da factura. Esta diferença do total pode ser alocada no valor da Taxa de Cambio Ganho/Perdido.

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-7.png">

Pagamento pode tambem ser feitos independentemente das facturas criando um no Registo de Pagamento.

Para saber mais sobre gerindo transações em multiplas moedas [visite esta pagina](/docs/user/manual/pt/contabilidade/artigos/gerir-transações-multiplas-moedas).

### 4.2 Transferencia Interna

Transferencia Interna é usad em casos aonde o dinheiro é transerido entre contas da mesma Empresa. Por exemplo, se o cliente dos US usando PayPal, transferir dinheiro para uma conta bancária pode ser considerado como Transferencia Interna.

As seguintes transferencias internas pode ser geridas apartir do Registo de Pagamento.

1. Banco - Dinheiro
4. Banco - Dinheiro
3. Dinheiro - Dinheiro
2. Dinheiro - Banco

<img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-9.png">

### 4.3 Gerindo Diferentes Cenarios de Pagamento

Para uma factura não paga, valor pendente = total geral. Ao criar o Registo de Pagamento, o valor pendente será reduzido.

Em muito dos casos, para alem das vendas a retalho, cobranças e pagamento são actividades diferentes. Exitem varias combinação no qual estes pagamento são feito. Estes casos aplicam-se quer para Vendas e Compras.

 * Eles podem ser adiantados (100% de adiantamento).
 * Post shipment. Ou na entrega ou dentro de alguns dias da entrega.
 * Metade em adiantamento e metade durante ou depois da entrega.
 * Pagamento podem ser feitos em conjunto para um conjunto de facturas.
 * Adiantamentos pode ser feitos em conjunto para um conjunto de facturas (e podem ser repartidos entre as facturas).

O ERPNext permite que voçê faça a gestão de todos este cenarios. Todas os registos contabilisticos (GL Entry) podem ser feitos contra uma Factura de Vendas, Factura de Compra ou Registo de Pagamento ou Adiantamento de Pagamento (em casos especiais, uma factura pode ser feita via Factura de Vendas tambem).

O total pendente contra um factura é a soma de todos os registos de pagmaento que foram feitos "contra" (ou estão ligados a) esta factura. Desta forma voçẽ pode combinar ou dividir os pagamentos em Registo de Pagamentos para gerir os cenarios.

### 4.4 Diferença entre Registo de Pagamento e Lançamento Contabilistico

1. Usando o Lançamento Contabilistico requer um entendimento em que Conta será Debitada ou Creditada. No Registo de Pagamento, é gerido por trás, daí ser simples para o Usuário.
1. Registo de Pagamento é mais eficiente em gerir pagamentos em moeda estrangeira.
1. Cheques podem ser imprimidos apartir do Registo de pagamento usnado o Formato de Impressão de Cheques.
1. Lançamento Contabilistico pode ser usado para:
 - Actualizar saldo de abertura em Contas.
 - Registo de Depreciação de Activos Fixos.
 - Para ajustar a Nota de Credito contra a Factura de Venda e Notas de Debito contra Factura de Compra, em casos que não tenha algum pagamento.

### 4.5 Pagamentos Usando Lançamento Contabilisto

Para fazer pagamentos usando o Lançamento Contabilistico siga os passos:

1. Activar Pagamento via Lançamento Contabilistico. Vá para **Contabilidade > Mestre Contabil > Configurações de Contabilidade**, assinale a caixa 'Fazer Pagamentos via Lançamento Contabilistico'.

2. Faça o pagamento. Ao submeter o documento contra o qual o Lançamento Contabilistico pode ser feito, voçê irá encontrar o Pagamento em baixo do botão **Criar**.

 <img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/payment-entry-1.png">

3. Lançamento Contabilistico. Salvar e submeter o Lançamento contabilistico para registar o pagamento contra a factura
 <img class="screenshot" alt="Making Payment" src="{{docs_base_url}}/assets/img/accounts/journal-entry.png">


## 5. Topicos Relacionados
1. [Solicitação de Pagamento](/docs/user/manual/pt/contabilidade/solicitação-pagamento)
1. [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
