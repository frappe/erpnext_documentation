---
title: Centro de Custo Distribuido
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Um Centro de Custo Distribuido é um Centro de Custo em que varios Centros de Custo são marcadados com a percentagem apropriada.
 keywords: frappe, erpnext, relatorios contabilidade, Centro de Custo, Entrada GL.
---

<!-- add-breadcrumbs -->
# Centro de Custo Distribuido

**Um Centro de Custo Distribuido é um Centro de Custo em que varios Centros de Custo são marcadados com a percentagem apropriada.**

Caso o negocio tenha um Centro de Custo Mestre com outros Centros de Custo dependentes. Em todas transações dos Centros de Custo, é dificil manter o orçamento, lucro e percas para cada Centro de Custo dependente manualmente com a percentagem alocada no Centro de Custo Mestre. Esta funcionalidade ajudar a automatizar o processo de registo manual.

Por exemplo, se no seu negocio, caso o Centro de Custo 'B' e 'C' depende do Centro de Custo 'A' por 20% e 80%. Então, voçê pode mencionar 'A' como um Centro de Custo Distribuido. Ajuda a rever os lucros, despesas e orçamento do 'A' no 'B' e 'C' com as percentagens alocadas.

No ERPNext voçê pode criar Centros de Custo Distribuidos e usar em transações e relatorios.

## 1. Como criar um Centro de Custo Distribuido
1. Vá para a lista de Centro de Custo, click em Novo.
1. Digite o nome do Centro de Custo.
1. Selecione o Centro de Custo parent.
1. Activar a caixa, **Activar Centro de Custo Distribuido**: Ao activar, a tabela Centro de Custo Distribuido irá aparecer. Então depois selecione o Centro de Custo e aloque a percentagem correspondente.
1. Quando terminar click em Salvar.

  <img class="screenshot" alt="Distributed Cost Center" src="{{docs_base_url}}/assets/img/accounts/distributed_cost_center.png">

Os seguintes relatorios serão automaticamente actualizados quando o filtro Centro de Custo é adicionado:

  * [Relatorios de Contabilidade](/docs/user/manual/pt/contabilidade/relatorios-contabilidade)
    * Extractos Financeiros
    * Variante de Orçamento
    * Razão Geral
  * [Analise de Lucros](/docs/user/manual/pt/contabilidade/artigos/rastreando-lucros-usando-centros-custo)

### 2. Topicos Relacionados
1. [Centro de Custo](/docs/user/manual/pt/contabilidade/centro-custo)
