<!-- add-breadcrumbs -->
# Lançamento Contabilistico

**Um Lançamento Contabilistico é uma entrada feita no Razão Geral que indica as contas afectadas.**

Um Lançamento Contabilistico é uma transação de multi razões aonde as contas debito e credito são selecionadas.

Todos os tipo de registos contabilisticos alem das transações de Vendas e Compras são feitas usando o **Lançamento Contabilistico**. Um **Lançamento Contabilistico** é uma transação normal em contabilidade que afecta varias Contas e a soma dos debitos é igual a soma dos Creditos. Um Lançamento Contabilistico tem impacto no razão principal.

Lançamento Contabilistico podem ser usadas para incluir despeas, saldos de abertura, pagamento de bancos, etc. Por exemplo, booking running expenses, despesas directas como gasolina/transporte, sundry expenses, registo de ajustamento e valores de ajuste de factura.

> Nota: Apartir da versão-13 nós introduzimos o razão imudavel no qual muda a forma de cancelar Lançamento Contabilistico no ERPNext. [Aprenda mais aqui](/docs/user/manual/pt/contabilidade/artigos/immutable-ledger-in-erpnext).

Para aceder a lista de Lançamento Contabilistico, vá para:
> Home > Contabilidade > Razão Geral > Lançamento Contabilistico

## 1. Como criar um Lançamento Contabilistico
1. Vá para a lista de Lançamento Contabilistico, clique em Novo.
1. O Tipo de Lançamento será 'Lançamento Contabilistico'. Isto é um tipo de registo geral. Visite [secção 3](/docs/user/manual/pt/contabilidade/lançamento-contabilistico#3-tipo-lançamento-contabilistico) para saber mais sobre os tipos.
1. Voçê pode alterar a Data de Postagem.
1. Aumente a tabela, selecione uma Conta para debitar o valor.
1. Os detalhes acima podem ser adicionados apartir do [Modelo de Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/modelo-lancamento-contabilistico) tambem  com o campo 'Apartir do Modelo'.
1. Selecione o Tipo de Parte e a Parte se for uma entrada de devedor.
1. Adicione a linha aonde para o valor de credito.
1. De notar que  no fim o total de debito e credito devem ser iguais.
1. Salvar e Submeter.

  <img class="screenshot" alt="Journal Entry" src="{{docs_base_url}}/assets/img/accounts/journal-entry.png">

**Livro Financeiro**: Voçẽ pode digitar este registo para um [Livro Financeiro](/docs/user/manual/pt/contabilidade/livro-financeiro) especifico. Ao deixa este campo em branco, o Lançamento Contabilistico irá mostrar todos os Livros Financeiros.

### 1.1 Lançamento Rapido
Quando ao criar um Lançamento Contabilistico, um botão **Lançamento Rapido** pode ser visto no topo a direito. Isto faz com que criar um Lançamento Contabilistico seja facil. Digite o valor, selecione a conta, adicionar um comentario. Este irá salvar a tabela 'Lançamento Contabilistico' com os detalhes selecionados.

![Lançamento Rapido](/docs/assets/img/accounts/quick-entry.png)

## 2. Funcionalidades
### 2.1 Lançamento Contabilistico

* **Dimensão Contabil**: Um Projecto ou Centro de Custo pode ser ligado aqui para rastrear os custos separados. Para saber mais, [visite esta página](/docs/user/manual/pt/contabilidade/dimensao-contabil).
  ![Dim Contabil](/docs/assets/img/accounts/je-acc-dim.png)

* **Nº da Conta Bancária**: Se voçê adicionou uma [Conta Bancária](/docs/user/manual/pt/contabilidade/conta-bancária), o numero associado a conta bancária será procurada..
* **Tipo de Referencia**: Se Lançamento Contabilistico estiver associados a outras transações, pode ser referenciada aqui. Selecione o Tipo de Referencia e o documento especifico. Por exemplo, se voçẽ estiver a criar um Registo de Jornal contra uma Factura de Venda especifica. Ligue este Registo de Jornal a factura. O valor "em falta" da factura será afectado.

  ![Referencia](/docs/assets/img/accounts/je_table_reference.png)

De seguida são os documentos que podem ser selecionados no Lançamento Contabilistico em Tipo de Referencia:

  * [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
  * [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
  * Lançamento Contabilistico
  * [Ordem de Vendas](/docs/user/manual/pt/vendas/ordem-vendas)
  * [Ordem de Compra](/docs/user/manual/pt/compras/ordem-compra)
  * [Reembolso de Despesas](/docs/user/manual/pt/recursos-humanos/reembolso-despesas)
  * [Activos](/docs/user/manual/pt/activos/activo)
  * [Emprestimos](/docs/user/manual/pt/gestão-emprestimos/emprestimo)
  * [Entrada de Folha de Pagamento](/docs/user/manual/pt/recursos-humanos/folha-de-pagamento)
  * [Adiantamento a Funcionário](/docs/user/manual/pt/recursos-humanos/adiantamento-funcionário)
  * [Reavaliação da Taxa de Cambio](/docs/user/manual/pt/contabilidade/reavaliação-taxa-cambio)
  * [Desconto de Facturas](/docs/user/manual/pt/contabilidade/desconto-de-facturas)

* **É um Adiantamento**: Se for um adiantamento de pagamento feito pelo Cliente, defina esta opção como 'Sim'. Este é util quando voçê ligou o 'Tipo de Referencia' no formulario para este Lançamento Contabilistico. Selecionando 'Sim' irá ligar este lançamento Contabilistico a transação selecionada no campo 'Nome da Referencia'. Para saber mais, visite a pagina [Registo de Adiantamento de Pagamento](/docs/user/manual/pt/contabilidade/adiantamento-pagamento).

* **Observação do Usuário**: Qualquer observação adiconal sobre o registo pode ser acrescentado aqui neste campo.

### 2.2 Lançamento Contabilistico Inverso
Em qualquer Lançamento Contabilistico submetido, existe um botão dedicado para o Lançamento Contabilistico Inverso. Ao fazer o clique no botão 'Lançamento Contabilistico Inverso', o sistema criar um Lançamento Contabilistico invertendo o valor de debito e credito das respectivas contas.

<img alt="Reverse Journal Entry" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reverse-journal-entry.png">

### 2.3 Lançamento de Diferença
A 'Diferença' é a diferença que fica depois de submeter todos os valores do debito e credito.

Como em contabilidade os registos duplos, o total do debito deve ser igual ao tota do credito.

Este deve ser zero ao submeter o Lançamento Contabilistico. Se este numero não for zero, voçê pode fazer o clique em 'Efectuar Registo de Diferença' e o sistema irá automaticamente adicionar uma nova linha com o valor necessário para dar o total zero. Selecione a conta para debito/credito e prossiga.

  ![Efectua Registo de Diferença](/docs/assets/img/accounts/make-difference.png)

### 2.4 Referencia Referencing

Um Numero de Referencia pode ser digitado manual e Data de Referencia pode ser definida. Ao digitar o Numero de Referencia aqui, a 'Observação' será visivel, por exemplo:

> Nota: fornecedor

> Referencia #2321 datada 30-09-2019 ₹ 1,000.00 a favor da Factura de Venda ACC-SINV-2019-00064

Na secção da Referencia, os seguintes campos podem ser digitados manualmente se a cobrança foi registada offline e não no sistema ERPNext. Isto é somente para futura referencia.

* Nº da Cobrança
* Data da Cobrança
* Data de Vencimento

### 2.5 Registo de Multi Moedas

Se as contas selecionadas são em moedas diferentes, selecione a caixa 'Multiplas Moedas'. Se esta caixa não estiver activa, voçê não poderá selecionar qualquer moeda estrangeira no Lançamento Contabilistico. Isto irá mostra a moeda diferente e irá buscar a 'Taxa de Cambio'. Para saber mais, viste a pagina [Contabilidade Multi Moedas](/docs/user/manual/pt/contabilidade/contabilidade-multi-moedas).

![Multi Moeda](/docs/assets/img/accounts/je-multi-currency.png)

### 2.6 Modelo de Lançamento Contabilistico

Campo **Apartir do Modelo**: Selecionando uma opção aqui irá carregar os detalhes apartir de um Modelo de Lançamento Contabilistico.

Irá procurar e adiconar os seguinte detalhes no registo:

- Tipo de Entrada
- Empresa
- Series
- Contas no Lançamento Contabilisto
- É de Abertura

Para saber mais vá para pagina [Modelo de Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/modelo-lancamento-contabilistico).

### 2.7 Configurações de Impressão

![Configurações de Impressão de Lançamento](/docs/assets/img/accounts/je_print_settings.png)

**Pagar a / Receber de**: O nome digitado aqui irá aparecer na Factura de Vendas. Isto é util para imprimir cheques. Vá para a Visão de Impressão no Lançamento Contabilistico e selecione 'Formato de Impressão de Cheque'.

#### Cabeçalho de Carta
Voçê pode imprimir o seu Lançamento Contabilistico no Cabeçalho de Carta da empresa. Saiba mais [aqui](/docs/user/manual/pt/configuração/imprimir/cabeçalho-carta).

#### Imprimir Cabeçalho
Lançamento Contabilisticos podem ter um titulo diferente por questões de impressão.
Voçê pode fazer isto selecionando **Imprimir Cabeçalho**. Para criar um novo Imprimir Cabeçalho vá para:

Home > Configurações > Impressão > Imprimir Cabeçalho

Saiba mais [aqui](/docs/user/manual/pt/configuração/imprimir/imprimir-cabeçalhos).

### 2.7 Mais Informação

* **Modo de Pagamento**: Aonde o pagamento foi feito usando Transferencia Bancária, Visa, Cartão de Debito, Cheque ou Dinheiro. Novos Modelos de Pagamento podem ser criados. Se uma Conta Bancária foi definida no Modo de Pagamento, será procurada aqui quando Modo de Pagamento for selecionado.
* **É de Abertura**: Se o Lançamento Contabilistico for do tipo 'Registo De Abertura' este campo será definido como 'Sim'. Para saber mais visita a pagina [Saldo de Abertura](/docs/user/manual/pt/contabilidade/saldo-abertura).
* **Apartir do Modelo**: Quando um modelo é selecionado, a tabela 'Lançamento Contabilistico' ficará vazia antes de carregar as contas apartir dos modelos. Voçê pode adiconar mais registos de lançamento depois.

## 3. Tipo de Lançamento Contabilistico
Vamos dar uma olhada aos  lançamentos contabilisticos comuns que podem ser feitos via Lançamento Contabilistico no ERPNext.

### 3.1 Lançamento Contabilistico

Este é um tipo geral que pode ser usado para varios motivos. Vamos ver alguns exemplos.

#### Despesas (non accruing)

Muitas vezes pode não ser necessário to accrue uma despesa, mas pode ser
alocada directamente contra a Conta de despesa no pagamento. Por exemplo, uma avanço de viagem
ou conta de telefone. Voçê pode debitar directamento Despesas de Telefone
(em vez de usar o seu tefone da empresa) e creditar o seu Banco ao pagar.

  * Debito: Conta de Despesa (tipo despesa de Telefone).
  * Credito: Conta Banco ou Dinheiro.

#### Creditando Salários

Para creditar salário dos funcionários, Tipo de 'Lançamento Contabilistico' é usado. Neste caso,

  * Debito: Os componentes de Salário.
  * Credito: A Conta do banco.

### 3.2 Lançamento Contabilistico Inter Empresa
Se um transação ocrre entre uma empresa maẽ e filha, ou empresas filhas, ou duas empresa pertencendo ao mesmo grupo, esta opção pode ser usado para fazer Lançamento Contabilistico Inter Empresa.

Para saber mais visite a pagina [Lançamento Contabilistico Inter Empresa](/docs/user/manual/pt/contabilidade/lançamento-contabilistico-inter-empresa).

### 3.3 Registo Bancário
Use este tipo quando estiver a fazer ou receber um pagamento usando uma [Conta Bancária](/docs/user/manual/pt/contabilidade/conta-bancária). Por exemplo, pagando impostos para entretenimento etc usando a Conta Bancária da Empresa.

### 3.4 Registo de Caixa
Este é o mesmo que 'Registo Bancário' mas o pagamento é feito via a Conta a Dinheiro.

### 3.5 Registo de Cartão de Credito
Isto é o tipo de registo para facilmente identificar todos os registos de cartão de credito.

### 3.6 Nota de Debito

Este é um documento enviado pelo clinte (sua Empresa) para um fornecedor (seu Fornecedor) quando retornar bens/itens.

Voçê poide tambem criar uma Nota de Debito directamente apartir da Factura de Compra.

"Nota de Debito" é feita para um Fornecedor contra uma Factura de Compra ou aceite
como uma nota de credito apartir do Fornecedor quando a empresa devolve os bens. Quando uma 
Nota de Debito é feita, a Empresa pode receber o pagamento do Fornecedor ou
ajustar o valor numa outra factura.

  * Debito: Conta Fornecedor.
  * Credito: Conta de Devolução de Compra.

Para saber mais, [visite esta página](/docs/user/manual/pt/contabilidade/nota-debito).

### 3.7 Nota de Credito
Este é um documento enviado pelo fornecedor a um cliente quando devolve bens/itens.

"Nota de Credito" é feita para um Cliente contra um Factura de Vendas quando a
empresa precisa ajudar o pagamento pelo bens retornados. Quando a Nota de Credito
é feita, o vendedor por fazer o pagamento para o clinte ou ajustar
o valor numa outra factura.

  * Debito: Conta de Vendas de Devolução.
  * Credito: Conta de Cliente.

Para saber mais, [visite a página](/docs/user/manual/pt/contabilidade/nota-credito).

> Uma nota de debito/credito normalmente é criada pelos valores do bens devolvidos ou menos.

### 3.8 Contrapartida

Uma Contrapartida é alocada quando a transação é alocado dentro do mesmo Tipo de Empresa:

* Dinheiro para Dinheiro
* Banco para Banco
* Dinheiro para Banco
* Banco para Dinheiro

Isto é usado para registar remoção ou deposito de dinehro de uma Conta Bancária. Quando é usado este registo, o dinheiro não sai da empresa a não ser que seja usado para pagar algo.

### 3.9 Registo de Imposto Especial

Quando a Empresa compra bens apartir de um Fornecedor, a empresa paga direitos de Registo de Imposto Especial
sobre estes bens ao Fornecedor. E quando a empresa vende estes bens ao Cliente,
recebe direitos de Registo de Imposto Especial. A Empresa irá deduzir impostos de Registo de Imposto Especial e depositar o balanço
na conta do Governo.

  * Quando a Empresa compra bens com direitos de Registo de Imposto Especial:
    * Debito: Conta de Compra, Conta de Registo de Imposto Especial.
  	* Credito: Conta de Fornecedor.

  * Quando a Empresa venda os bens com direitos de Registo de Imposto Especial:
    * Debito: Conta do Cliente.
    * Credito: Conta de Vendas, Conta de Registo de Imposto Especial.

> Nota: Aplicavel na India, pode não ser aplicado no seu País.
Por favor verifique os regulamentos do seu País.


### 3.10 Write Offs or Bad Debts

Se voçê estiver a writing off uma Factura como a bad debt, voçê pode criar um Comprovante de Diario Journal
Voucher similiar a um Pagamento, excepto que em vez de debitar o seu Banco, voçê pode
debito um Conta de Despesa chamada Bad Debts.

  * Debito: Bad Debts Written Off
  * Credito: Cliente

> Nota: Pode haver regulações no seu País ante de voçê puder write off bad
debts.

### 3.11 Saldo de Abertura

Esta entrada é util quando migrar de um sistema para o ERPNext em qualquer periodo do ano. Suas contas em falta, equidades, etc,  podem ser guardadas no ERPNext usando este tipo de registo. Este tipo de registo irá procurar as contas de Balanço.

### 3.12 Depreciação

Depreciação é quando voce write off algum valor dos seus activos como uma despesa.
Por exemplo se voçê tiver um computador que irá usar por 5 anos, voçê pode 
distribuir as despesas durante o periodo e passar um Lançamento Contabilistico no fim de cada ano reduzindo
o seu valor por uma certa percentagem.

  * Debito: Depreciação (Despesa).
  * Credito: Activo (A Conta no qual voçê alocou o activo para ser depreciado).

Para saber mais, visite a página [Depreciação de Activo](/docs/user/manual/pt/activos/depreciação-activos).

> Nota: Pode haver regulamentos no seu País que definem o valor que
voçê pode depreciar uma lista de Activos.

### 3.13 Reavaliação da Taxa de Cambio
Se o seu Plano de Contas tem contas com multiplas moedas, o Lançamento Contabilistico do tipo 'Reavaliação da Taxa de Cambio' pode ajudar a lidar com esta situação. Este registo é para ser criado apartir de um formulario de Reavaliação da Taxa de Cambio. Para saber mais [Visita a página Reavaliação da Taxa de Cambio](/docs/user/manual/pt/contabilidade/reavaliação-taxa-cambio).

### 4. Topicos Relacionados
1. [Lançamento Contabilistico Inter Empresa](/docs/user/manual/pt/contabilidade/lançamento-contabilistico-inter-empresa)
1. [Nota de Credito](/docs/user/manual/pt/contabilidade/nota-credito)
1. [Nota de Debito](/docs/user/manual/pt/contabilidade/nota-debito)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Botão de Registo de Diferença](/docs/user/manual/pt/contabilidade/artigos/botão-registo-diferença)
1. [Livro Financeiro](/docs/user/manual/pt/contabilidade/livro-financeiro)
