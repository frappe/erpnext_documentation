<!-- add-breadcrumbs -->
# Rastreando Lucros de Projecto usando Centro de Custo

Para rastrear despesas e lucros por projecto, voçẽ pode usar os Centro de Custo. Voçê deve criar a uma Centro de Custo separado para cada Projecto. Isto irá ajudar-lhe.

- Alocação de Orçamento de despesas para Projectos.
- Restreando Lucros de Projectos.

Vamos verificar os passos em Projectos e Centros de Custo de como devem estar ligados, e usar as transações de vendas e compras.

### 1. Ligando Projectos e Centros de Custo

#### 1.1 Crie um Projecto

Para criar um novo Projecto, vá para:

`Projectos > Projecto > Novo`

<img alt="Project Default Cost Center" class="screenshot" src="{{docs_base_url}}/assets/img/articles/project-cost-center-4.png">

#### 1.2 Criar um Centro de Custo

Vendo que orçamento e Centro de Custo para cada Projecto irá ser gerido separado, voçê deve criar um Centro de Custo separado para cada Projecto.

Para criar um Novo Centro de Custo, vá para:

`Contabilidade > Configuração > Centro de Custo`

[Clique aqui para aprender como usar os Centros de Custo.](/docs/user/manual/pt/contabilidade/centro-custo)

#### 1.3 Actualizar os Centros de Custo em Projectos

Actualizar Centros de Custo em Projectos.

<img alt="Project Default Cost Center" class="screenshot" src="{{docs_base_url}}/assets/img/articles/project-cost-center-1.png">

Nas transações de vendas e compras, se o Projecto for selecionado, então o Centro de Custo irá ser inserido apartir da ficha do Projecto.

Vamos verificar como esta configuração vai afectar os registos de venda e compra.

### 2. Projecto e Centros de Custo nas Transações de Vendas e Compras

#### 2.1 Projectos em Transações de Vendas

Em transações de vendas (no qual a Ordem de Venda, Guia de Remessa e Factura de Vendas), Projectos serão selecionados na secão Mais Info. Ao selecionar um Projecto, o respectivo Centro de Custo irá ser actualizado para todos os Itens naquela transação. Centros de Custo serão actualizados em todas as transações que tenham o campo Centro de CUsto.

<img alt="Project Default Cost Center" class="screenshot" src="{{docs_base_url}}/assets/img/articles/project-cost-center-2.png">

#### 2.2 Projectos em Transações de Compras

Em transações de compras, Projectos são definidos para cada linha do item. Isto porque voçê pode criar um registo consolidade de compras para varios projectos. Ao selecionar o Projecto, o seu centro de custo padrão será inserido.

Como no sistem de avaliação perpetual inventory, despesas para os itens comprados serão alocados em materia prima quando consumidos. Ao consumir bens, se voçê criar registo de Pedido de Material (stock), então o Custo da Despesa (digamos Custo de Bens Vendidos) e Centro de Custo de Projectos deve ser actualizado no registo.

<img alt="Project Default Cost Center" class="screenshot" src="{{docs_base_url}}/assets/img/articles/project-cost-center-3.png">

### 3. Relatorio de Contabilidade para um Projecto

#### 3.1 Lucros Projectwise

Vendo que Centro de Custo de Projectos é actualizado quer nos registos de Vendas e Compras, voçê pode verificar os Lucros dos Projectos baseados em Centros de Custo.

**Analise Mensal do Projecto**

<img alt="Project Default Cost Center" class="screenshot" src="{{docs_base_url}}/assets/img/articles/project-cost-center-5.png">

**Lucros Gerais - Overall Profitability**

<img alt="Project Default Cost Center" class="screenshot" src="{{docs_base_url}}/assets/img/articles/project-cost-center-6.png">

#### 3.2 Orçamento Projectwise

Voçê pode definir orçamentos a favor de Centros de Custo associados a um Projecto. Em qualquer momento, voçê pode ver o Relatorio de Variação de Orçamento para analizar as despesas vs orçamentos contra um Centro de Custo.

Para verificar o relatorio de Variação de Orçamento, vá para:

`Contabilidade > Orçamento e Centro de Custo > Relatorio de Variaçãio de Orçamento`

[Clique aqui para aprender mais sobre o orçamento apartir do Centro de Custo](/docs/user/manual/pt/contabilidade/orcamento.html).

<!-- markdown -->

{next}
