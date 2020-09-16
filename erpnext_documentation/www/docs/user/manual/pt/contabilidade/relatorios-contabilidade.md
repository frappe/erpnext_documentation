<!-- add-breadcrumbs -->
# Relatorios Contabilisticos

Alguns dos maiores Relatorios Contabilisticos são:

## 1. Empresa e Contas
### Razão Geral
Vá para: **Contabilidade > Razão Geral > Razão Geral**.

O Razão Geral é um relatorio detalhado para todas as transações feitas em cada conta e para toda transação tem uma conta de Credito e Debito listada.

O relatorio é basedo na tabela GL Entry e pode ser filtrado por muitos filtros pre-definidos como Contas, Centros de Custo, Partes, Projectos e Periodo, etc. Isto ajuda voçê a ter uma actualização completa de todos registos feitos num periodo contra qualquer conta. O resultado pode ser agrupado por Contas, Voucher/Transação e Parte com abertura e fecho de balanços para cada grupo. No caso de contabilidade multi moedas, existe uma opção para verificar os valores em qualquer moeda para alem da moeda base da empresa.

<img alt="General Ledger" class="screenshot"
    src="{{docs_base_url}}/assets/img/accounts/reports/general-ledger.png">

## 2. Extractos Bancários
### 2.1 Contas de Recebimentos e Contas de Pagamentos (AR / AP)
Vá para: **Contabilidade > Contas a Receber > Contas a Receber**.

Estes relatorios ajudam a rastrear os valores pendentes de Clientes e Fornecedores. Tambem informa uma analise de tempo ex. distribuindo valores penndentes baseados em periodos no qual os valores estão pendentes.

<img alt="Accounts Receivable" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/accounts-receivable.png">

#### 2.1.1 Conta de Recebimentos baseados em Termos de Pagamento
Voçê pode tambem ver as Contas de Recebimentos baseados em [Termos de Pagamento](/docs/user/manual/pt/contabilidade/termos-pagamento).

O relatorio de Contas de Recebimento são baseados em termos de pagamento podem ser vistos fazendo o clique na caixa 'Baseado nos Termos de Pagamento' mostrados na seguinte imagem.

<img alt="Accounts Receivable" class="screenshot"
    src="{{docs_base_url}}/assets/img/accounts/reports/accounts-receivable-1.png">

Valores Pendentes contra cada termo de pagamento pode ser visto. **Valor Facturado** mostra cada valor de termo de pagamento e **Valor Pago** mostra valores pagos contra cada termo de pagamento. Pagamento contra cada termo é alocado de forma FIFO.

<img alt="Accounts Receivable" class="screenshot"
    src="{{docs_base_url}}/assets/img/accounts/reports/accounts-receivable-2.png">

### 2.2 Balancete
Vá para: **Contabilidade > Declarações Contabilisticas > Balancete**.

Um Balancete é um relatorio que mostra contas de balanço de todas as contas
(“Razão" e "Grupo") para qualquer periodo. Um empresa prepara o balancete periodicamente, normalmente no fim de cada periodo de relatorios. O proposito geral em produzir um balancete é de assegurar que todos os registo na empresa alocados no sistema estejam matematicamente correctos. Os totais das Colunas de Debito e Credito devem sempre iguais a qualquer periodo, para ter a certeza de que os registos estão correctos. No ERPNext, o relatorio mostra as seguintes colunas:

  * Abertura (Dr): Balanço de Abertura de Debito com a Data de Inicio
  * Abertura (Cr): Balanço de Abertura de Credito com a Data de Inicio
  * Debito: Valor Total Debitado contra a conta entre o periodo escolhido
  * Credito: Valor Total Creditado contra a conta entre o periodo escolhido
  * Fecho (Dr): Fecho do Balanço de Debito até a Data Final
  * Fecho (Cr): Fecho do Balanço de Credito até a Data Final

Tem algumas outras opções para incluir ou excluir Registo de Fecho de Periodo, mostrar / esconder contas com valores a zero e para mostrar o Balanço dos Anos Fiscais anteriores não encerrados P&L (Recebimentos & Despesas). Todos os dizeres no relatorios são mostrados na moeda base da Empresa.

<img alt="Trial Balance" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/trial-balance.png">

### 2.3 Folha de Balanço
Vá para: **Contabilidade > Declarações Financeiras > Balanço**.

A Folha de Balanço é um extracto financeiro de uma empresa aonde mostra activos, responsabilidades e equidades no periodo de tempo particular.

A Folha de Balanço no ERPNext mostra-lhe uma forma de analisar mais flexivel o seu estado financeiro. Voçê pode correr o relatorio para cruzar com varios anos para comparar os valores. Voçê pode verificar os valores para um Livro Especifico ou Centro de Custo. Voçê pode tambem escolher qualquer moeda para mostrar os balanços.

<img alt="Balance Sheet" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/balance-sheet.png">

### 2.4 Extracto do Fluxo de Caixa
Vá para: **Contabilidade > Declarações Financeiras > Fluxo de Caixa**.

Um Fluxo de Caixa é um extracto financeiro no qual mostra os recebimentos e pagamentos de dinheiro ou parecidos para uma empresa. É usado para analizar a posição liquida da Empresa.

<img alt="Cash Flow Statement" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/cash-flow.png">

### 2.5 Extracto de Lucro e Percas
Vá para: **Contabilidade > Declarações Financeiras > Calculo de Lucros e Perdas**.

Um extracto de Calculo de Lucros e Perdas é um extracto financeiro no qual resume todas as revenues e despeas num periodo de tempo. O relatorio é tambem conhecido como Extracto P&L.

No ERPNext, voçê pode correr o relatorio para cruzar varios anos / periodos e comparar os valores. Voçê pode tambem verificar os valores de um Livro Financeiro especifico, Projecto ou Centro de Custo. Voçê pode escolher qualquer moeda para mostrar os balanços. Se voçê estiver a correr o relatorio para ver balanços a cada quarto / mensais, voçê precisa escolher se quer mostrar balanços acumulados or somente para cada periodo.

<img alt="Profit and Loss Statement" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/profit-and-loss.png">

### 2.6 Extractos Financeiros Consolidados
Vá para: **Contabilidade > Declarações Financeiras > Declaração Financeira Consolidada**.

O relatorio mostra a Folha de Balanço, Extracto de Lucro e Perdas e Fluxo de Caixa para um grupo de Empresa, by merging extractos financeiros de todas as subsidiarias. Mostra balanços para todas empresas individuais bem como os balanços acumulados para um grupo de Empresas.

<img alt="Consolidated Financial Statement" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/consolidated-financial-statement.png">

## 3. Impostos
### 3.1 Registo de Vendas e Compras
Vá para: **Contabilidade > Impostos > Registo de Vendas *ou* Registo de Compras**.

O relatorio de Vendas e Registo de Compras mostra todas transaçõe de Vendas e Compras para um periodo com o valor facturado e detalhes de impostos. Neste relatorio, cada imposto fica numa coluna separada, para que possa facilmente ver o total dos impostos coletados / pagos por um periodo para cada tipo de imposto, no qual ajuda a pagar os impostos ao governo.

<img alt="Sales Register" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/sales-register.png">

## 4. Orçamento e Centros de Custo
### 4.1 Desvio de Orçamentos
Vá para: **Contabilidade > Orçamento e Centros de Custo > Relatorio de Desvios de Orçamento**.

No ERPNext, voçê pode atribuir uma despesa de orçamento para uma conta de despesas contra qualquer centro de custo. Este relatorio faz a comparação entre o orçamentado e a despesa actual e os desvios (a diferença entre os dois) mensalmente / Trimestral / Anual.

<img alt="Budget Variance" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/budget-variance.png">

## 5. Relatorio de Impostos para India
### 5.1 GSTR-1 (India)
Vá para: **Accounts > Goods and Services Tax (GST India) > GSTR-1**.

The GSTR-1 report helps Indian users to file monthly return of outward supplies. This report shows all the sales transactions of the company in Govt specified format. The output of the report is changed based on the selected type of business (B2B, B2C Large, B2C Small, CDNR and Export).

<img alt="GSTR-1" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/gstr-1.png">

### 5.2 GSTR-2 (India)
Vá para: **Accounts > Goods and Services Tax (GST India) > GSTR-2**.

The GSTR-2 report helps Indian users to file monthly return of inward supplies. The report gives the details of all inward supplies of goods or services received during a month, in Govt specified format.

<img alt="GSTR-2" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/gstr-2.png">

## 6. Analiticos
### 6.1 Registo de Vendas e Compras de Item Inteligente
Vá para: **Contabilidade > Contas a Receber > Registo de Vendas de Item Inteligente *ou* Registo de Compras de Item Inteligente**.

O relatorio Registo de Vendas e Compras de Item Inteligente mostra todas as Vendas e Compras para um periodo com preço do item, quantidade, valor e detalhes de imposto. Neste relatorio, impostos tem um coluna separada, para que possa facilmente ver os impostos para cada Item. Apartir deste relatorio voçê pode ver que itens foram mais vendidos ou comprados.

<img alt="Item Wise Sales Register" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/item-wise-sales-report.png">

Uma analise mais detalhes pode ser feita usando o filtro 'Agrupar Por' que mostra dados de venda para um Cliente, Fornecedor, Territorio especifico, etc. Voçê pode encontrar que Itens são mais populares e em que região ou que Cliente mais compra e que Item.

<img alt="Group By Sales Register" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/group-by-sales-register.png">

### 6.2 Tendências de Factura de Vendas e Compras
Vá para: **Contabilidade > Rentabilidade > Tendências de Factura de Vendas *ou* Tendências de Facturas de Compra**.

Outro relatorio muito util são as Tendências de facturação, apartir des relatorio voçê pode facilmente obeter as tendências dos Itens mensalmente, trimestral ou anual. Voçê pode ter uma udea das quantidades e valores de Vendas e Compras.

<img alt="Sales Invoice Trends" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/sales-invoice-trends.png">

## 7. Para Cobrar
- **Itens Pedidos a serem Cobradas:** Este relatorio mostra os itens que foram pedidos pelos cliente, contra as Facturas de Venda que ainda não foram criadas / parcialmente criadas.
- **Itens Entregues a serem Cobrados:** Os itens no qual foram entregues aos clientes, mas as Facturas de Venda não foram criadas / parcialmente criadas.
- **Itens da Ordem de Compra a Facturar:** O relatior mostra os itens que foram feitas a ordem apartir do fornecedor, mas não foi feita ainda a Factura de Compra.
- **Itens Recebidos a serem Cobrados:** Os itens que foram recebidos apartir dos fornecedores, mas a Factura de Compra ainda não foi criada.

## 8. Outros Relatorios
### 8.1 Balancete para a Parte
Vá para: **Contabilidade > Relatorios > Balancete para a Parte**.
Normalmente voçêo precisar ver o balanço dos seus cliente e fornecdores. Voçẽ facilmente ver todos clientes ou fornecedores e individuais.

<img alt="Sales Invoice Trends" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/reports/party-wise-trail-balance.png">

### 8.2 Saldo Credito de Cliente
O relatorio mostra o limite de credito, pendentes e balanço de credito para cada cliente.
