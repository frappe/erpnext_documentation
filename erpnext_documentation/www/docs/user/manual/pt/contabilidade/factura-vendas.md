<!-- add-breadcrumbs -->
# Factura de Vendas

**Uma Factura de Vendas é uma cobrança que voçê envia para os seu Clientes no qual os Clientes fazem o pagamento.**

Factura de Vendas é uma transação de contabilidade. Ao submeter uma Factura de Vendas, o sistema actualiza os recebimentos e books os valores na conta de Cliente.

Para aceder a lista de Factura de Vendas, vá para:
> Home > Contabilidade > Contas a Receber > Factura de Vendas

![Fluxograma OD](/docs/assets/img/accounts/so-flow.png)

## 1. Pre-requisitos
Antes de criar e usar a Factura de Venda, é aconselhavel criar os seguintes primeiro:

* [Item](/docs/user/manual/pt/inventario/item)
* [Cliente](/docs/user/manual/pt/CRM/cliente)

* Opcional:
 * [Ordens de Venda](/docs/user/manual/pt/vendas/ordem-vendas)
 * [Guia de Remessa](/docs/user/manual/pt/inventario/guia-de-remessa)

## 2. Como criar uma Factura de Venda
Uma Factura de Venda é normalmente criada apartir de uma Ordem de Venda ou Guia de Remessa. Os detalhes dos Itens do Cliente seram inseridos na Factura de Vendas. Contudo, voçê poide tambem criar Factura de Vendas directamente, poir exemplo, uma factura POS.

Para inserir os detalhes automaticamente a Factura de Vendas, clique em **Obter Itens de**. Os detalhes podem ser inseridos apartir de uma Ordem de Venda, Guia de Remessa ou Proforma.

Para criar manual, siga estes passos:

1. Vá para a lista de Factura de Vendas e clique em Novo.
1. Selecione o Cliente.
1. Definir o Prazo de Pagamento.
1. Na tabela de Itens, selcione os Itens e as quantidades.
1. Os preços seram incluidos automaticamente se [Preço de Item](/docs/user/manual/pt/inventario/preço-item) for adicionado, caso contrario adicione na tabela.
1. A data de postagem e hora sera automaticamente inserida, voçê pode depois fazer um clique na caixa em baixo da Hora de Postagem para alterar.
1. Salvar e Submeter.
 ![FV](/docs/assets/img/accounts/sales-invoice-1.png)

### 2.1 Opções Adicionais ao criar um Factura de Vendas

* **Incluir Pagamento (POS)**: Se a factura for venda a retalho / Ponto de Venda. [Saiba mais aqui](/docs/user/manual/pt/contabilidade/factura-vendas#324-facturas-pos).
* **É uma Nota de Credito**: Selecione isto se o cliente devolveu os Itens. Para saber mais detalhes, visite a pagina [Nota de Credito](/docs/user/manual/pt/contabilidade/nota-credito).

<img class="screenshot" alt="Sales Invoice" src="{{docs_base_url}}/assets/img/accounts/sales-invoice.png">

Para India:
**e-Way Bill No**: According to GST rules, transporters need to carry an e-Way Bill. To know how to generate an e-Way Bill, [visit this page](/docs/user/manual/pt/regional/india/auto-generate-e-way-bill-JSON).

### 2.2 Statuses

Estes são os estados auto atribuídos as Facturas de Venda.

* **Rascunho**: Um rascunho é salvo mas não submetido ainda.
* **Submetido**: A factura foi submetida ao sistema e o razão geral foi actualizado.
* **Pago**: Cliente fez o pagamento e o [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento) foi submetido.
* **Não Pago**: Factura é gerada mas o pagamento está pendente dentro do prazo de pagamento.
* **Expirado**: Pagamento está pendente e o prazo de pagamento expirado.
* **Cancelado**: A Factura de Venda foi cancelada por qualquer motivo. Uma vez a factura cancelada, os movimentos em Contabilidade e Stock são desfeitos.
* **Nota de Credito Criada**: O Item foi retornado pelo Cliente e a [Nota de Credito](/docs/user/manual/pt/contabilidade/nota-credito) é criada contra a factura.
* **Devolvido**: É atribuido a Nota de Credito contra a Factura de Venda original. Apesar de poder tambem criar uma Nota de Credito sozinha.
* **Não Paga e Descontada**: Pagamento está pendente e qualquer subscrição foi descontada usando [Desconto de Facturas](/docs/user/manual/pt/contabilidade/desconto-de-facturas).
* **Expirada e Descontada**: Pagamento está pendente e prazo de pagamento expirado e qualquer subscrição foi descontada usando [Desconto de Facturas](/docs/user/manual/pt/contabilidade/desconto-de-facturas).

## 3. Funcionalidades
### 3.1 Datas

* **Data de Postagem**: A data em que a Factura de Venda irá afectar os seus livros de Contabilidade. ex. Razão Geral. 
Irá afectar os balanços neste periodo contabil.

* **Data Limite de Pagamento**: A data que expira o pagamento (caso tenha vendido a credito).
O limite de credito pode ser definido na tabela [Cliente](/docs/user/manual/pt/CRM/cliente#25-limite-de-credito-e-termos-de-pagamento).

### 3.2 Dimensão Contabil
Dimensão Contabil permite que marque as transações baseadas num Territorio especifico, Branch, Cliente, etc. Isto ajuda a ver os extractos de contabilidade separados baseados na dimensão selecionada. Para saber mais, verifique a ajuda da funcionalidade [Dimensão Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil).

> Nota: Projecto e Centros de Custo são tratados como Dimensões por defeito.

### 3.3 Detalhes da OC de Cliente

* **Ordem de Compra de Clientes**: Rastrei o Nº da OC do Cliente recebido, primariamente para prevenir a criação de Ordens de Venda ou Facturas duplicadas para a mesma OC recebida pelo seu Cliente. Voçê pode fazer mais configurações de Validação sobre o Nº de OC do Cliente nas [Configurações de Venda](/docs/user/manual/pt/vendas/configurações-venda#44-permitir-ordens-de-venda-multiplas-contra-ordem-de-compra-de-clientes)
* **Data da Ordem de Compra do Cliente**: A data em que o Cliente fez a Ordem de Compra.

 ![Endereço Cliente](/docs/assets/img/accounts/si-customer.png)

### 3.4 Endereço e Contacto

* **Endereço Cliente:** Este é o Endereço de Cobrança do Cliente.
* **Pessoa de Contacto**: Se o Cliente for uma empresa, a pessoa de contacto será procurada no campo se foi definido no formulario [Cliente](/docs/user/manual/pt/CRM/cliente).
* **Territorio:** Um [Territorio](/docs/user/manual/pt/vendas/territorio) é uma região aonde o Cliente pertence, procurado no formulario do Cliente. O valor default é Todos os Territorios.
* **Endereço de Envio:** Endereço para aonde os Itens seram enviados.

Para India, the following details can be recorded for GST purposes. You can capture these details in the Address and Customer master, which would be fetched in the Sales Invoice.

* Billing Address GSTIN
* Customer GSTIN
* Place of Supply
* Company GSTIN

### 3.5 Moeda
Voçê pode definir a moeda em que a Factura de Venda será feita. Pode ser procurado apartir da ficha de Cliente ou transações anteriores como Ordens de Venda.

* Deseja selecionar a moeda do Cliente somente para a referencia do Cliente, aonde os registo de contabilidade seram feitos na moeda base da Empresa somente. Aprenda mais [aqui](/docs/user/manual/pt/contabilidade/artigos/gerir-transações-multiplas-moedas).
* Mantenha as contas de recebimento separadas na moeda do Cliente. Os Recebimentos para esta factura devem ser postados naquela moeda. [Clique aqui](/docs/user/manual/pt/contabilidade/contabilidade-multi-moedas) para aprender mais sobre Contabilidade Multi Moedas.

### 3.6 Lista de Preços

Se voçê selcionar uma Lista de Preços, então os preços do item seram procurados apartir desta lista. Selecionando 'ignorar Regras de Preço' irá ignorar as [Regras de Preço](/docs/user/manual/pt/contabilidade/regras-preço) definidos em Contabilidade > Regras de Preço.

Para saber mais sobre Lista de Preços, [clique aqui](/docs/user/manual/pt/inventario/lista-preços).


### 3.7 A tabela de Itens

> Nota: Apartir da versão-13 nós introduzimos o razão imudavel que muda as regras de cancelamento de registo de stocks e transações de stock no ERPNext com datas anteriores. [Saiba mais aqui](/docs/user/manual/pt/contabilidade/artigos/razão-imudavel-erpnext).

#### Actualizar Stock
Activando esta caixa irá actualizar o razão do Stock ao submeter a Factura de Vendas. Se voçê criou uma Guia de Remessa, o Razão de Stock será alterado. Se voçê **não criou** uma Guia de Remessa selecione esta caixa.

* **Leitura de Codigo de Barras**: Voçê pode adiconar Itens na tabela fazendo a leitura dos seus codigos de barra se voçê tiver um leitor de codigos de barra. Para saber como rastrear [aqui](/docs/user/manual/pt/inventario/artigos/track-items-using-barcode)

* O Codigo do Item, nome, descrição, Imagem e Facbricante seram procurados apartir do [Ficha de Item](/docs/user/manual/pt/inventario/item).

* **Desconto e Margem**: Voçê pode aplicar um desconto percentual a Itens individuais ou no valor total do Item. Leia [Aplicando Desconto](/docs/user/manual/pt/vendas/artigos/aplicando-desconto) para mais detalhes.

* **Preço**: O Preço é procurado se definido na [Lista de Preços](/docs/user/manual/pt/inventario/lista-preços) e o valor total será calculado.

* **Drop Ship**: Envio de Descarga/Entrega é quando voçê faz a transação de venda, mas o Item é entregue pelo Fornecedor. Para saber mais, visite a pagina [Drop Shipping](/docs/user/manual/pt/vendas/artigos/drop-shipping).

* **Detalhes Contabilisticos**: As  contas de Recebimentos e Despesas podem ser alteradas aqui se quiser. Se este Item for um [Activo](/docs/user/manual/pt/activos/activo), pode ser ligado aqui. É util quando voçê esta a [Vendendo um Ativo](/docs/user/manual/pt/activos/vendendo-um-activo).

* **Deferred Revenue**: Se o Recebimento para este Item será cobrado nos meses futuros em parcelas, então selecione 'Activar Recebimento Futuro'. Para saber mais, visite a [Pagina de Recebimento Futuro](/docs/user/manual/pt/contabilidade/deferred-revenue).

* **Peso do Item**: Os detalhes de Peso do Item por unidade e UDM de Peso são procurados se definidos na tabela Item.

* **Detalhes de Stock**: Os seguintes detalhes serao procurados apartir da tabela Item:
 * **Armazem**: O Armazem aonde o stock será enviado.
 * **Quantidade Disponivel em Armazem**: A quantidade disponivel no Armazem selecionado.

* **Numero de Lote e Numero de Serie**: Se o seu Item é serializado ou tem Lotes, voçê irá ter de digitar o [Numero de Serie](/docs/user/manual/pt/inventario/numero-serie) e [Lote](/docs/user/manual/pt/inventario/lote) na tabela Itens. Voçê está autorizado a digitar varios Numeros de Serie numa unica linha (cada um em linhas separadas) e voçê deve digitar o mesmo Numero de Series como quantidade.

* **Modelo de Imposto de Item**: Voçê pode definir o Modelo de Imposto de Item para a plicar o valor do Imposto para este Item em particular. Para saber mais, visite [esta pagina](/docs/user/manual/pt/contabilidade/modelo-imposto-item).

* Referencias: Se esta Factura de Venda foi criada apartir de uma Orde de Venda/Guia de Remessa, será citada aqui. Tambem, a Quantidade Entregue será mostrada.

* **Quebra de Pagina** irá criar uma quebra de pagina mesmo antes do Item ser impresso.

### 3.8 Registo de Horas

Se voçê quiser cobrar os Funcionários trabalhando em Projectos com base nas horas (baseado em contracto),
eles tem que preencher o Registo de Horas que consiste no preço de cobrança deles. Quando voçê fizer uma nova Factura de Venda,
selecione o Projecto para o qual a cobrança será feita, e o correspondente registo de Registo de Horas
para o Projecto será inserido.

Se o seu Funcionario está a trabalhar numa localização e precisa cobrar, voçê pode criar uma Factura com base no Registo de Horas.

![Registo de Horas FV](/docs/assets/img/accounts/si-timesheet.png)

Para saber mais, [visite esta pagina](/docs/user/manual/pt/projectos/factura-vendas-registo-horas).

### 3.9 Impostos e Taxas
Os Impostos e Taxas serão procurados apartir da [Ordem de Vendas](/docs/user/manual/pt/vendas/ordem-vendas) ou [Guia de Remessa](/docs/user/manual/pt/inventario/guia-remessa).

Visite a pagina [Modelo de Impostos e Taxas de Vendas](/docs/user/manual/pt/vendas/modelo-impostos-taxas-vendas) para saber mais sobre Impostos.

O total de impostos e taxas será mostrado na tabela em baixo.

Para adicionar impostos automaticos via a Categora de Imposto, visite [esta pagina](/docs/user/manual/pt/contabilidade/categoria-imposto).

Tenha a certeza de marcar todos os seus impostos na tabela Impostos e Taxas correctamento para uma Valuação correcta.

![Imposto FV](/docs/assets/img/accounts/si-tax.png)

#### Regra de Envio
Uma Regra de Envio ajuda a definir o custo de evnio de um Item. O custo normalmente ir+a aumentar com a distancia do envio. Para saber mais, visite a painga [Regra de Envio](/docs/user/manual/pt/vendas/regra-envio).

### 3.10 Redenção a Lealdade de Pontos

Se um Cliente estiver no Programa de Lealdade, eles pode escolher se redimir. Para saber mais, visite a pagina [Programa de Lealdade](/docs/user/manual/pt/contabilidade/programa-lealdade).

### 3.11 Descontos Adicionais
Qualquer desconto adicional para a Factura completa pode ser definido nesta secção. Este desconto pode ser baseado no Total Geral ex. imposto/taxas ou Valor Liquido ex. pre imposto/taxas. O desconto adicional pode ser aplicado como uma percentagem ou valor.
Visite a pagina [Aplicando Desconto](/docs/user/manual/pt/vendas/artigos/aplicando-desconto) para mais informações.

![FV e Desconto](/docs/assets/img/accounts/si-add-discount.png)

### 3.12 Adiantamento de Pagamento
Para Itens de grande valor, o vendedor pode pedir uma adiantamento de pagamento antes de processar o pedido. O botão **Obter Adiantamentos Recebidos** abre uma janela aonde voçê pode procurar as ordens aonde o pagamento foi feito. Para saber mais, visite a pagina [Registo de Adiantamento de Pagamento](/docs/user/manual/pt/contabilidade/adiantamento-pagamento).

### 3.13 Termos de Pagamento
O pagamento para uma factura pode ser feito em partes depdendendo do entendimento com o Fornecedor. Este é procurado caso definido na Ordem de Venda. Para saber mais, visite a pagina [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento).

### 3.14 Write Off
Write off acontece quando o Cliente paga um valor inferior ao valor da factura. Isto pode ser uma diferença pequena de 0.50. Juntando muitas ordens, isto pode ser um valor muito grande. Para accuracy contabilistico, esta diferença de valor é 'written off'. Para saber mais, visite a pagina [Termos de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento#25-deduções-ou-percas).

### 3.15 Termos e Condições
Poderá existe um certo termo e condição no Item que estiver a vender, este pode pode ser aplicado aqui. Para saer mais sobre adicionando Termos e Condições, [clique aqui](/docs/user/manual/pt/configuração/imprimir/termos-e-condições).

### 3.16 Informação de Transporte

Se voçê aluga o transporte de Itens para a sua localização, os detalhes de transporte podem ser incluidos aqui. Isto não é o mesmo que [Envio de Descarga](/docs/user/manual/pt/vendas/artigos/drop-shipping).

* **Transportador**: O Fornecedor que irá transporta os Item do seu Cliente. A funcionalidad de transportador deve ser activada na ficha do Fornecedor, para selecionar o [Fornecedor](/docs/user/manual/pt/comprar/fornecedor) aqui.
* **Motorista**: Voçê pode adicionar o Motorista aqui que irá levar o modo de transportar.

Os detalhes são normalmente procurados apartir da Guia de Remessa.

 ![Guia de Transporte](/docs/assets/img/accounts/si-transporter.png)

Os seguintes detalhes podem ser guardados:

* Distancia em km
* Modeo de Transporte quer seja carro, avião, comboio ou navio.

Para India, GST:

* GST Transporter ID
* Transport Receipt No
* Vehicle No
 The GST Vehicle Type can be changed

A Data do Recibo de Transporte e Nome do Motorista será procurada.

### 3.17 Configurações de Impressão

#### Cabeçalho de Carta
Voçê pode imprimir a sua Factura de Venda com o Cabeçalho de Carta da sua Empresa. Saiba mais [aqui](/docs/user/manual/pt/configuração/impressão/cabeçalho-carta).

'Agrupar os mesmos itens' irá agrupar os itens iguais adicionados multiplas vezes na tabela de Itens. Isto pode ser visto ao imprimir.

#### Imprimir Cabeçalhos
Cabeçalhos de Factura de Vendas pode tambem ser alterado ao imprimir o documento. Voçẽ pode fazer isto selecionando o **Imprimir Cabeçalhos**. Para criar um novo Imprimir Cabeçalhos va para: Home > Configurações > Imprimir > Imprimir Cabeçalho. Saiba mais [aqui](/docs/user/manual/pt/configuração/imprimir/imprimir-cabeçalhos).

Tem caixas adicionais para imprimir Factura de Vendas sem o valor, este pode ser util quando o Item é de grande valor. Voçê pode tambem agrupar os Itens iguais numa unica linha ao imprimir.

### 3.18 GST Details (for India)

The following details can be set for GST:

* GST Category
* Invoice Copy
* Reverse Charge
* E-commerce GSTIN
* Print Heading

### 3.19 Mais Informação
Os seguintes detalhes de Vendas são guardados:

* **Campanha**: Se esta factura faz parte de uma Campanha de Vendas continua, pode ser ligada. Para saber mais, visite a pagina [Pagina de Campanha](/docs/user/manual/pt/CRM/campanha).
* **Fonte**: Uma Fonte Lead pode ser marcado aqui para saber a fonte da Venda. Para saber mais, visite a pagina [Fonte Lead](/docs/user/manual/pt/CRM/lead_source).

 ![FV Mais info](/docs/assets/img/accounts/si-more-info.png)

### 3.20 Detalhes Contabilisticos

* **Debitar em**: A conta no qual os recebimentos serão booked para este Cliente.
* **É Registo de Abertura**: Se este for um registo de abertura que afecta as suas contas selecione 'Sim'. ex. Se voçê estiver a migrar de um ERP para o ERPNext no meio do ano, voçê pode querer usar o Registo de Abertura para actualizar as suas contas de balanço no ERPNext.
<!-- deprecated * **C-Form Applicable**: A C Form is used for the reduction of applicable taxes, select yes if applicable to your transaction. Note: C Form is not applicable in India since GST. -->
* **Observações**: Qualquer observação adiconal sobre a Factura de Venda pode ser adicionada aqui.

 ![Detalhes Contabilisticos FV](/docs/assets/img/accounts/si-acc-details.png)

### 3.21 Comissão

Se a venda foi feita por via de um dos seus Parceiros de Venda, voçê pode adicionar os detalhes de comissão aqui. Este é procurado apartir da Ordem de Venda/Guia de Remessa.

### 3.22 Grupo de Vendas

**Revendedores:** O ERPNext permite adicionar varios Revendedores que tenham trabalhado neste negocio. Este tambem é procurado apartir da Ordem de Venda/Guia de Remessa.

### 3.23 Procurando Automaticamente os Numeros de Lote do Item

Se voçẽ vende Item apartir de um [Lote](/docs/user/manual/pt/inventario/lote),
o ERPNext irá automaticamente procurra o numero do lote para si se o "Actualizar Stock"
estiver activo. O numero do lote será procurado pela ordem de Primeiro a Expirar primeiro a Sair
(FEFO). Este é uma variante do Primeiro a Entrar Primeiro a Sair (FIFO) que dá prioridade aos Itens que vão expirar primeiro.

Note que se a o primeiro lote na fila não satisfazer o pedido na factura,
o proximo lote na fila pode ser usado e selecionado. Se não tiver um lote que satisfaça o pedido, o ERPNext irá cancelar a tentativa de inserir automaticamente o numero de lote.

### 3.24 Facturas POS

Considere o cenario aonde a transação a retalh é feita. Por ex. Loja de retalho.
Se voçê selecionar a caixa **É POS**, então todo o seu **Perfirl POS** de usuário será inserido
na Factura de Venda e poderá fazer o pagamento facilmente.

Tambem, se voçê selecionar **Actualizar Stock** o stock será actualizado automaticamente,
sem que voçê precisar criar uma Guia de Remessa.

<img class="screenshot" alt="POS Invoice" src="{{docs_base_url}}/assets/img/accounts/pos-sales-invoice.png">

### 3.25 Depois de Submeter

A submeter uma Factura de Venda, os seguintes documentos são criados:

1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Solicitação de Pagamento](/docs/user/manual/pt/contabilidade/solicitação-pagamento)
1. [Desconto da Factura](/docs/user/manual/pt/contabilidade/desconto-da-factura)
1. [Guia de Remessa](/docs/user/manual/pt/inventario/guia-remessa)

![Submeter FV](/docs/assets/img/accounts/si-submit.png)


## 4. Mais
### Impacto na Contabilidade

Todas as vendas deve ser alocadas contra uma "Conta de Recebimento". isto refere a uma
Conta na secção de "Recebimentos" do seu Plano de Contas. É de boa practica
classificar o recebimento por tipo (de produto, serviço, etc). A Conta de Recebimento deve ser definida para cada linha da tabela de Itens.

> Dica: Para definir as Contas de Recebimentos dos Itens, voçê pode definir no Item ou
Grupo de Item.

A outra conta que é afectada é a Conta de Cliente. Isto é 
automaticamente definido apartir de "Debitar em" na secção de cabeçalho.

Voçê pode tambem mencionar o Centro de Custo no qual a Recebimento foi alocado.
Lembre-se que os seus Centros de Custo dizem-lhe os Lucros de diferentes linhas
de negocio ou produto. Voçê pode definir o Centro de Custo default na 
tabela Item. Veja tambem: [Dimensões Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil).

### Lançamento Contabil (GL Entry) para um entrada dupla de "Vendas":
Ao fazer a alocação da venda (accrual):

* **Debito:** Cliente (total geral)
* **Credito:** Recebimentos (total liquido, menos impostos para cada Item)
* **Credito:** Impostos (responsabilidades a serem pagas ao governo)

 ![Razão FV](/docs/assets/img/accounts/si-ledger.png)

> Para ver as entradas na sua Factura de Vendas depois de "Submeter", clique em "Ver Razão".

## 5. Topicos Relacionados
1. [Centro de Custo](/docs/user/manual/pt/contabilidade/centro-custo)
1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
1. [Recibo de Compra](/docs/user/manual/pt/inventario/recibo-compra)
1. [Imposto de Item Inteligente](/docs/user/manual/pt/contabilidade/modelo-imposto-item)
1. [Ordem de Vendas](/docs/user/manual/pt/vendas/ordem-vendas)
1. [Proforma](/docs/user/manual/pt/vendas/proforma)
1. [Guia de Remessa](/docs/user/manual/pt/inventario/guia-remessa)
