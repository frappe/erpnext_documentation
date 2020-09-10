<!-- add-breadcrumbs -->
# Centro de Custo

**Um Centro de Custo é uma parte de uma organização aonde os custos ou recebimentos são charged.**

No ERPNext voçê pode usar o Centro de Custos com Centro de Lucros.

O seu Plano de Contas esta desenhado para providenciar relatorios para o governo e as autoridades fiscais.

Muitos do negocios tem varias actividades como diferentes linhas de produto, segmentos de mercado, areas de negocio, etc que partilham as mesmas dores de cabeça. Eles devem idealmente ter a sua propria estrutura de relatorios sendo lucrativo ou não. Para este proposito, existe uma estrutura alternativa chamada de Plano de Centros de Custo.

Um Centro de Custo age como uma [Dimensão Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil) que ajudar a gerir os custos baseados num area em particular.

Os Centros de Custo pode ser definidos pelos seguintes niveis:

* Empresa
* Item
* Ordem/Factura

Os Centros de Custo podem estar ligados as seguintes transações:

1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compras](/docs/user/manual/pt/contabilidade/factura-compras)
1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lançamento-contabilistico)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Guia de Remessa](/docs/user/manual/pt/stock/guia-remessa)

E outras transações na qual podem ser usadas para orçamentos. Voçê pode tambem usar os Centros de Custo para [Orçamentos](/docs/user/manual/pt/contabilidade/orçamento).

## 1. Arvore do Centro de Custo

Voçê pode criar uma arvore de Centro de Custo para representar o seu negocio da melhor forma. Cada Recebimento / Registo de Despesa é tambem marcada contra o Centro de Custo. Caso 'Permitir Centro de Custo no Registo das Contas de Balanco', estiver selecionado em baixo das Configurações de Contabibilidade, o sistema irá permitir que um Usuario marque no Registo de Contas de Balanço contra o Centro de Custo.

Por exemplo, Caso voçê tenha dois tipos de vendas:

 * Vendas Rapidas / Walk-in Sales
 * Vendas Online

Voçẽ pode não ter despesas de envio para os seus clientes de vendas rapidas, e não ter renda de compra para os seu clientes online. Caso queira ver os lucros para cada um destes separados, voçẽ deve criar os dois como Centros de Custo e marcar todas a vendas como Centros de Custo "Rapidas/Walk-in" ou "Online". Marque todas as suas compras da mesma forma.

A quando estiver a fazer a sua analise, voçê irá entender melhor qual dos seus segmentos de negocio está melhor. Vendo que ERPNext tem uma opção para adicionar varias Empresas, voçê pode criar Centros de Custo para cada uma delas e gerir separada..

Para acessar o Plano de Centros de Custo, vá para:
> Home > Contabilidade > Orçamentos e Centros de Custo > Plano de Centros de Custo

## 2. Como configurar o Plano de Centros de Custo
1. Vá para o Plano de Centros de Custo.
1. Adicione nodulos de acordo as regiões.
1. Adicione outros nodulos de acordo as necessidades.

Selecionando uma Empresa diferente irá mostrar o Centro de Custo para este Empresa.

<img class="screenshot" alt="Cost Center" src="{{docs_base_url}}/assets/img/accounts/chart-of-cost-center.png"> 

### 3. Topicos Relacionados
1. [Orçamentos](/docs/user/manual/pt/contabilidade/orcamento)
1. [Facturas de Venda](/docs/user/manual/pt/contabilidade/facturas-venda)
1. [Facturas de Compra](/docs/user/manual/pt/contabilidade/facturas-compra)
