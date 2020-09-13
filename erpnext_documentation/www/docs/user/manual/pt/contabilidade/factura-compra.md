<!-- add-breadcrumbs -->
# Factura de Compra

**Uma Factura de Compra é uma cobrança que voçê recebe dos seus Fornecedores no qual voçê precisa fazer o pagamento.**

Factura de Compra é exactamente o oposto da sua Factura de Venda. Aqui voçê carrega despesas do seu Fornecedor. Fazendo um Factura de Compra é igual ao fazer uma Ordem de Venda. 

Para aceder a lista de Factura de Compra, vá para:
> Home > Contabilidade > Contas a Pagar > Factura de Compra

![PI Flow](/docs/assets/img/accounts/pi-flow.png)

## 1. Pre-requisitos
Antes de criar uma Factura de Compra, é aconselhavel criar os seguintes primeiro:

* [Item](/docs/user/manual/pt/inventario/item)
* [Fornecedor](/docs/user/manual/pt/compras/fornecedor)
* [Ordem de Compra](/docs/user/manual/pt/compras/ordem-de-compra)
* [Recibo/Recepção de Compra](/docs/user/manual/pt/inventario/recibo-de-compra) (opcional)


## 2. Como criar um Factura de Compra:
Uma Factura de Compra é normalmente criada apartir de uma Ordem de Compra ou de um Recibo de Compra (Recepção de Compra). Os detalhes dos Itens do Fornecedor seram inseridos na Factura de Compra. Contudo, voçê pode sempre criar uma Factura de Compra directamente.

Para inserir automaticamente os itens na Factura de Copmra, faça um click em **Obter Itens de**. Os itens serao inseridos apartir da Ordem de Compra ou Recibo de Compra.

Para criar manual, siga estes passos:

1. Vá para a lista de Factura de Compra, Click em Novo.
1. Selecione o Fornecedor.
1. A data de postagem e hora serao inserido automaticamente, voçê pode editar depois de selecionar a caixa em baito Postagem Hora.
1. Defina a Data do Prazo de Pagamento.
1. Adicione os Itens e quantidades na tabela de Itens.
1. O preço e Valor seram inseridos.
1. Salvar e Submter.

 <img class="screenshot" alt="Purchase Invoice" src="{{docs_base_url}}/assets/img/accounts/purchase-invoice.png">

### 2.1 Opções Adicionais ao criar uma Factura de Compra

* **Está Pago**: Voçê pode selecionar 'Está Paga' caso o valor já tenha sido pago via um [Adiantamento de Registo de Pagamento](/docs/user/manual/pt/contabilidade/adiantamento-pagamento). Deve ser selecionado caso haja um pagamento completo ou parcial.
* **É uma Devolução (Nota de Debito)**: Selecione caso o cliente tenha devolvido os Itens. Para saber mais, visite a pagina [Nota de Debito](/docs/user/manual/pt/contabilidade/nota-debito).
* **Aplicar Valor de Imposto de Retenção**: Caso o Fornecedor selecionado tem uma Categoria de Retenção de Imposto definido, esta caixa será activa. Para mais informações, visite a pagina [Categoria de Retenção de Imposto](/docs/user/manual/pt/accounts/categoria-retenção-imposto).

### 2.2 Statuses

* **Rascunho**: Um rascunho é salvo mas ainda não foi submetido para o sistema.
* **Devolução**: Os Itens foram devolvidos para o Fornecedor.
* **Nota de Debito Criada**: Os Itens foram devolvidos e uma [Nota de Debito](/docs/user/manual/pt/contabilidade/nota-debito) foi criada contra a factura.
* **Submetida**: A Factura de Compra foi submtida para o sistema e o razção geral foi actualizado.
* **Pago**: O total da factura foi entregue ao Fornecedor e um [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento) foi submetido.
* **Não Pago**: A Factura de Compra ainda não foi paga.
* **Expirado**: A data limite de pagamento expirou.
* **Cancelado**: A factura foi cancelada por algum motivo.


## 3. Funcionalidades

### 3.1 Dimensão Contabil
Dimensão Contabil permite que marque ransações baseadas num Territorio especifico, Branch, Cliente, etc. Isto ajuda a ver os extractos de contabilidade separados com base no criterio que selecionou. Para mais, visite a pagina [Dimensão Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil).

> Nota: Project e Centro de Custo são tratados como dimensões por defeito.

### 3.2 Pondo em Pausa a Factura

As vezes pode precisar de por eu pausa um factura para evitar ser submetida.

**Pausa a Factura**: Active esta caixa para por a Factura de Compra em Pausa. Este pode ser feito somente antes de submeter. Uma vez 'Pausar Factura' estiver activa e a Factura de Compra já foi submetida, o status irá mudar para 'Temporariamente em Pausa'.

![FC Pausa](/docs/assets/img/accounts/pi-hold.png)

Uma vez a factura de compra for submetida e voçê quer mudar a 'Data de Activação' então pode fazer o click no botão 'Pausar Factura', que está no topo a direita.

Se voçê quer manter factura de compras submetida então pode user a opção 'Bloquear Factura' e se voçê quer desbloquear então use a opção 'Desbloquar Factura'.

![FC Bloquear](/docs/assets/img/accounts/pi_block.png)

Isto no nivel de Pausar Factura, Fornecedores podem ser postos em pausa. [Aprenda mais aqui](/docs/user/manual/pt/compras/fornecedor#23-limite-credito).

### 3.3 Detalhes Factura de Fornecedor

* **Nº da Factura do Fornecedor**: O Fornecedor pode indentificar esta ordem com um numero dele mesmo. Isto é para referencia.
* **Data da Factura do Fornecedor**: A data em que o Fornecedor fez/confirmou a sua ordem.

### 3.4 Endereço e Contacto

* **Endereço do Fornecedor:** Este é o Endereço de Cobrança do Fornecedor.
* **Pessoa de Contacto**: Caso o Fornecedor seja uma Empresa, a pessoa de contacto será procurada neste campo caso definido no formulario [Fornecedor](/docs/user/manual/pt/compras/fornecedor).
* **Endereço de Envio:** Endereço aonde os itens serao enviados.

Para India, os seguintes detalhes podem ser guardados para GST:

* Supplier GSTIN
* Place of Supply
* Company GSTIN

### 3.5 Moeda e Lista de Preço
Voçê pode definir a moeda na qual a Factura de Compra será enviada. Isto é procurado apartir da Ordem de Compra. Caso voçê definiu uma Lista de Preços, então os preços do item serao procurados neste lista. Selecionando 'Ignorar Lista de Preço' irá ignorar as [Regras de Preço](/docs/user/manual/pt/contabilidade/regras-preço) definidos em Contabilidade > Regras de Preço.

![FC Lista de Preços](/docs/assets/img/accounts/pi-price-list.png)

Para saber mais sobre Lista de Preços, [Clica Aqui](/docs/user/manual/pt/inventario/lista-preços).

Para saber mais como gerir transações em varias moedas, [Clica Aqui](/docs/user/manual/pt/contabilidade/artigos/gerir-transações-multiplas-moedas).

### 3.6 Subcontratando ou 'Fornecedor de Materia Prima'

Definindo a opção 'Fornecedor de Materia Prima' é util para subcontractar aonde voçê a materia prima para fabricar um Item. Para saber mais, visita [Pagina de Subcontratação](/docs/user/manual/pt/fabrico/subcontratação).

### 3.7 Tabela de Itens

* **Leitura de Codigo de Barras**: Voçê pode adicionar Itens na tabela de Itens fazendo a leitura dos codigos de barra caso voçê tenha um leitor. Para saber como rastrear [aqui](/docs/user/manual/pt/inventario/artigos/track-items-using-barcode)

* O Codigo do Item, nome, descrição, Imagem e Fabricante serao procurados apartir do [Tabela Item](/docs/user/manual/pt/inventario/item).

* **Fabricante**: Caso o Item é fabricado por um fabricantes especifico, pode ser adicionado aqui. Isto será inserido caso definido na table Item.

* **Quantidade e Preço**: Quando voçê selecionar o Codigo do Item, seu nome, descrição e UdM serao procurados. O 'Factor de Conversão de UDM' é definido por defeito como 1, voçê pode alterar dependendo na UDM recebida do seu vendedor, mais na proxima secção.

 'Lista de Preços' será procurado se a taxa Normal de Compra for definida. 'Ultima Taxa de Compra' mostra o preço do item da sua ultima ordem de compra. Preço é procurado caso tenha sido definido na table de Item. Voçê pode anext um Modelo de Imposto de Item para aplicar o imposto especifico ao item.

* **Peso do Item** será procurado caso tenha sido definido na tabela Item caso contrario manualmente.

* **Desconto na Lista de Preços**: Voçê pode definir um desconto em Itens singulares por percentagem ou no total geral do Item. Leia [Aplicar Desconto](/docs/user/manual/pt/selling/artigo/applying-discount) para mais detalhes.

* **Peso do Item**: Os detalhes do Peso do Item por unidade e UDM são procurados se definidos na tabela Item, caso contrário digite.

* **Detalhes de Contabilidade**: Uma conta de Depesas pode ser alterada aqui.

* **Deferred Expense**: Caso a despesa deste Item será cobrada nos futuros meses em partes, então assinale 'Despesas Activas Futuras'. Para saber mais, visite [Deferred Expense page](/docs/user/manual/pt/contabilidade/deferred-expense).

* **Permitir Taxa de Avaliação Zero**: Assinalando em 'Permitir Taxa de Avaliação Zero' irá permitir submeter o Recibo de Compra mesmo que a Taxa de Avaliação do Item seja 0. Isto pode ser um item de amostra ou de acordo mutuo com o Fornecedor.

* **LDM**: Caso exita uma [Lista de Materiais](/docs/user/manual/pt/fabrico/lista-de-materiais) criado para o Item, será procurado. É util para referencia quando [subcontrato](/docs/user/manual/pt/fabrico/subcontratação).

* **Modelo de Imposto de Item**: Voçê pode definir um Modelo de Imposto de Item para aplicar um Valor de Imposto especifico para este Item em particular. Para saber mais, visite [esta pagina](/docs/user/manual/pt/contabilidade/modelo-imposto-item).

* **Quebra de Pagina** irá criar uma quebra de pagina antes de Item ser impresso.

#### Actualizar Stock

> Nota: Apartir da vesão-13 nós introduzimos o razão imutavel que muda as regras de cancelamento de registo de stocks e registo de transações do passado no ERPNext. [Aprenda mais aqui](/docs/user/manual/pt/contabilidade/artigos/immutable-ledger-in-erpnext).

O caixa de **Actualizar Stock** deve ser selecionada se voçê quer que o ERPNext actualize automaticamente o seu inventario. Consequentemente, não haverá a necessidade de um Guia de Remessa.

### 3.8 Impostos e Taxas
Os Impostos e Taxas serão procurados apartir da [Ordem de Compra](/docs/user/manual/pt/compras/ordem-compra) ou [Recibo de Compra](/docs/user/manual/pt/inventario/recibo-compra).

![Imposto FC](/docs/assets/img/accounts/pi-tax.png)

Viste a pagina [Modelo de Impostos e Taxas de Compra](/docs/user/manual/pt/compras/modelo-impostos-taxas-compra) para saber mais sobre impostos.

O total de impostos e taxas será mostrado na tabela em baixo.

Para adicionar impostos automaticos via Categoria de Impostos, visite [esta pagina](/docs/user/manual/pt/contabilidade/categoria-imposto).

Tenha a certeza de marcar todos seus impostos na tabela de Impostos e Taxas correcto para uma avaluação precisa.

#### Regra de Envio
Uma Regra de Envio define o custo de envio de um Item. O custo será automentado com a distancia de envio. Para saber mais, visite a pagina [Regra de Envio](/docs/user/manual/pt/vendas/regra-envio).

### 3.9 Desconto Adicional

Qualquer Desconto Adicional para a Factura inteira pode ser definido nesta secção. Este desconto pode ser baseado no Total Geral ex., impostos/taxas or Total Liquido, pre-imposto/taxa. O desconto adicional pode ser aplicado como pecentagem ou valor.

![Desconto FC](/docs/assets/img/accounts/pi-discount.png)

Visite a pagina [Aplicando Desconto](/docs/user/manual/pt/vendas/artigos/aplicando-desconto) para mais detalhes.

### 3.10 Adiantamento de Pagamento
Para Itens de grande valor, o vendedor pode pedir um adiantamento de pagamento antes de processar a ordem. O botão **Obter Adiantamentos Recebidos** abre um janel aonde voçê pode procurar as ordens com adiantamento de pagamento feitos. Para saber mais, visite a pagina [Registo de Adiantamento de Pagamento](/docs/user/manual/pt/contabilidade/adiantamento-pagamento).

### 3.11 Termos de Pagamento
O pagamento de uma factura pode ser feito em parte dependendo do seu entendimento como o Fornecedor. Este é posto caso definido na Ordem de Vendas.

![Termos de Pagamento de FC](/docs/assets/img/accounts/pi-pay-terms.png)


Para saber mais, visite a pagina [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento) page.

### 3.12 Write Off
Write off acontece quando o Cliente paga um montante inferior que o valor da factura. Pode ser uma diferença pequena como 0.50. Sobre varias odens, este pode somar um numero muito alto. Para accuracy de contabilidade, esta diferença é um 'written off'. Para saber mais, visite a pagina [Termos de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento#35-dedução-ou-perca).

### 3.13 Termos e Condições
Em transações de Venda/Compras pode conter alguns Termos e Condições baseados nos bens ou serviços que o Fornecedor providencie a um Cliente. Voçê pode aplicar os Termos e Condições para transações que iram aparecer ao imprimir o documento. Para saber mais sobre Termos e Condições, [clique Aqui](/docs/user/manual/pt/configuração/imprimir/termos-e-condições)

### 3.14 Configurações de Impressão

#### Cabeçalho de Carta
Voçê pode imprimir a sua Factura de Compra com o seu Cabeçãlho de Carta. Para saber mais [aqui](/docs/user/manual/pt/configuração/imprimir/cabeçalho-carta).

'Agrupar os mesmos Itens' irá agrupar os itens iguais adicionados multiplas vezes na tabela de Itens. Isto pode ser visto ao imprimir.

#### Imprimir Cabeçalho
O cabeçalho da Factura de Compra pode ser alterado ao imprimir. Voçê pode fazer isto selecionando **Imprimir Cabeçalho**. Para criar um novo Imprimir Cabeçalho va para: Home > Configurações > Impressão > Imprimir Cabeçalho. Saiba mais [aqui](/docs/user/manual/pt/configuração/imprimir/imprimir-cabeçalhos).

Existem caixas adicionais para imprimir Factura de Compra sem o valor, isto pode ser util quando o Item é de grande valor. Voçê pode tambem agrupar os itens iguais numa unica linha ao imprimir.

### 3.15 GST Details (for India)
The following details can be set for GST:

* GST Category
* Invoice Copy
* Reverse Charge
* E-commerce GSTIN
* Eligibility For ITC
* Availed ITC Integrated Tax
* Availed ITC Central Tax
* Availed ITC State/UT Tax
* Availed ITC Cess

### 3.16 Mais Informação

* **É Registo de Abertura**: Caso seja um registo de abertura que irá afectar a sua contabilidade selecione 'Sim'. ex. Se estiver a migrar de um outro ERP para o ERPNext no meio do ano, voçê podeusar o Registo de Abertura para actualizar as contas de balanço no ERPNext.
* **Observações**: Qualquer observação adicional em Facturas de Venda podem ser adicionadas aqui.

### 3.17 Depois de Submeter

Ao submeter uma Factura de Venda, os seguintes documentos pode ser criados contra:

1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Solicitação de Pagamento](/docs/user/manual/pt/contabilidade/solicitação-pagmento)
1. [Landed Cost Voucher](/docs/user/manual/pt/inventario/landed-cost-voucher)
1. [Activos](/docs/user/manual/pt/activos/activo)

![Submeter FC](/docs/assets/img/accounts/pi-submit.png)

## 4. Mais
### 4.1 Impacto na Contabilidade
Simular as Facturas de Venda, num Factura de Compra voçê tem que digitar uma conta de Despesa ou uma Conta de Activo para 
cada linha na tua Tabela de Item. Isto ajuda a indicar se o Item é um Activo
ou uma Despesa. Voçê pode tambem mudar o Centro de Custo. Este pode tambem ser defifnido na
Tabela de Item. O Centro de Custo pode ser definido a nivel da Empresa.

A Factura de Compra irá afectar as suas contas de seguinte forma:

* Registos de Contabilidade (GL Entry) para um entrada dupla de “compras”:
* Debitos:
 * Despesa ou Activo (valor liquido, excluído impostos)
 * Impostos (/astivos se o Tipo-IVA ou despensa contra)
* Creditos:
 * Fornecedores

![Razão FC](/docs/assets/img/accounts/pi-ledger.png)

### 4.2 Contabilidade Quando **Está Pago** esta activo
Se **Está Pago** esta activo, o ERPNext irá tambem fazer os seguintes
lançamentos contabilisticos:

Debitos:

 * Fornecedor

Creditos:

 * Conta Banco/Dinheiro

Para ver os registo na sua Factura de Compra depois de "Submeter", clique em 
“Ver Razão”.

### 4.3 É comprar um "Despesa" ou "Activo"?

Se o item for consumido de imediato ao comprar, ou se for um serviço, então
a compra torna-se "Despesa". Por exemplo, um conta de telefone ou viagem
é uma "Despesa" - pois já foi consumido.

Para os Itens de Inventario, que tem um valor, estas compras não ainda "Despesas",
porque ainda tem um valor enquanto estiverem no seu stock. Eles são
“Activos". Se eles são materia prima (usados num processo), eles tornam-se
"Despesas" no momento que são consumidos. Se tiverem que ser vendidos
para  um Cliente, eles tornam-se "Despesas" quando voçê envia para o Cliente.

### 4.4 Deduzindo Impostos a Fonte

Em muitos países, a lei pode exigir que voçê deduza os impostos, enquanto pagar os
seu fornecedores. Estes impostos podem ser com base numa taxa fixa. Sobre estes tipode de esquema, tipicamento se um Fornecedor ultrapassar um certo limite de pagamento, e
se o tipo de produto é taxavel, voçê pode ter que deduzir algum imposto (que voçê paga de
volta ao seu governo, em nome dos seus Fornecedores).

Para fazer isto, voçê irá ter de fazer uma criar uma Nova Conta de Imposto em “Responsabilidade de Impostos” ou
similar e creditar esta conta pela percentagem que voçê deve deduzir
em cada transação.

### 4.5 Pausar Pagamentos para um Factura de Compra
Exitem duas formas de por uma Factura de Compra em pausa:

- Data de Pausa
- Pausa Explicita

#### Pausa Explicita
Pausa Explicita pausa as facturas de compra indefinidamente.
Para fazer isto, na secção "Pausar Factura" no formulario factura de compra, simplesmente assinale a caixa "Pausar Factura". No campo de texto "Razão para Pausar", digite um comentário explicando o motivo de por a factura em pausa.

Se voçê precisa de pausar uma factura submetida, clique no botão "Criar"
e clique "Bloquar Factura". Tambem, adicione um comentário para explicar porque motivo a factura esta em pausa na caixa de dialogo que aparece e clique "Salvar".

#### Data de Pausa
Data de pausa mantem a factura de compra em pausa até a data especificada. Para fazer, na secção de "Pausar Factura" no formumario de Factura de Compra, selecione a caixa "Pausar Factura". Depois, digite a data de release na caixa de dialogo que aparece e clique "Salvar". A data de release é a data em que o documento pausado expira.

Depois de salvar a factura, voçê pode alterar a data de release simplesmente fazendo um clique no botão "Pausar Factura" e depois "Alterar Data Release". Esta acção irá fazer com que uma caixa de dialogo apareça.

<img class="screenshot" alt="Purchase Invoice on hold" src="{{docs_base_url}}/assets/img/accounts/purchase-invoice-hold.png">

Selecione a nova data de release e clique em "Salvar". Voçê deve tambme digiar um comentário no campo "Razão para Pausar".

Tome nota do seguinte:

- Todas as compras que foram postas em pausa não serão incluídas na tabela de Registo de Pagamento.
- A data de release não pode ser de dias anteriores.
- Voçê pode somente bloquear ou desbloquear um factura de compra não paga.
- Voçê somente pode alterar a data de release se a factura estiver não paga.

### 5. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Impostos de Itens Inteligentes](/docs/user/manual/pt/contabilidade/modelo-imposto-item)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Solicitação de Pagamento](/docs/user/manual/pt/contabilidade/solicitação-pagamento)
1. [Solicitação de Proforma](/docs/user/manual/pt/compras/solicitação-proforma)
1. [Ordem de Compra](/docs/user/manual/pt/compras/ordem-compra)
1. [Recibo de Compra](/docs/user/manual/pt/inventario/recibo-compra)
