<!-- add-breadcrumbs -->
# Orçamento

**Orçamento é um plano financeiro que ajuda a controlar as despesas da Empresa.**

No ERPNext, voçê pode gerir os Orçamentos contra um Centro de Custo ou Projecto. Isto é util em controlar as suas despesas. Na versão 12, voçê pode tambem criar [Dimensões Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil) separados para marcar transações com campos diferentes.

Por exemplo, se voçê faz vendas online, voçê pode definir o Orçamento para cada anuncio e configurar o ERPNext para parar ou avisar quando passar o valor disponivel definido no Orçamento.

Orçamentos são tambem bons para motivos de planeamento. Quando voçê estiver a fazer planos para o proximo Ano Financeiro, voçê iria marcar lucros baseados no qual iria definir as suas despesas. Configurando um orçamento irá dar a certeza de que as suas despesas não saiam do controle a qualquer momento.

Para aceder a lista de Orçamento, vá para:
> Home > Contabilidade > Centros de Custo e Orçamento > Orçamento

## 1. Como Criar um novo Orçamento
1. Vá para a lista de Orçamento e clique em Novo.
1. Selecione o que vai orçamentar, Centro de Custo, Projecto ou uma [Dimensão Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil).
1. Na tabela de contas, selecione a conta de recebimentos/despesas pelo qual o orçamento será definido. Vamos definir um orçamento para as despesas de telefone para o ano.
 <img class="screenshot" alt="Budget" src="{{docs_base_url}}/assets/img/accounts/budget-account.png">
1. Digite o valor do Orçamento para essa conta.
1. Salvar e Submeter.


## 2. Funcionalidades
### 2.1 Distribuição Mensal

Voçê pode definir o registo de Distribuição Mensal para distribuir o orçamento entre meses. Se voçê não definir a distribuição mensal, o ERPNext irá calcular o orçamento anual ou em proporções iguais para cada mês.

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/monthly-budget-distribution.png">

### 2.2 Acções de Controle (Alertas)

Acções de Controle podem ser activadas quando:

* Uma [Solicitação de Material](/docs/user/manual/pt/inventario/solicitação-material) está a ser submetida
* Uma [Ordem de Compra](/docs/user/manual/pt/compras/ordem-de-compra) está a ser submetida
* Quando uma despesa actual está a ser criada (por um lançamento contabilistico ou factura de compra).

Voçê pode definir a acção de controle no Orçamento baseado na Solicitação de Material, Ordens de Compra ou em despesas actuais. Poderá tambem definir a acção de controle para orçamentos anuais ou mensais.

![Acções de Controle](/docs/assets/img/accounts/control-actions.png)

Exitem trẽs tipos de acção de controle.

* **Parar**: Este não irá permitir os usuários em submeter a transação.
* **Aviso**: Este irá mostra uma mensagem de aviso mas deixa o usuário submeter a transação.
* **Ignorar**: Este não irá nem prevenir o usuário de submeter as transações nem mostrar a mensagem de erro.

Voçê pode definir acções separadas para orçamentos mensais e anuais. Se voçê exceder o orçamento, um aviso será mostrado:

<img class="screenshot" alt="Monthly Distribution" src="{{docs_base_url}}/assets/img/accounts/budget-warning.png">

Note que aviso similar é acionado para qualquer tipo de transação definida no orçamento para uma Conta em particular.

## 3. Relatorio de Variação de Orçamento

A qualquer momento, voçê poderá verificar o Relatorio de Variação de Orçamento para analizar a despesa actual ocorrida vs o orçamento alocadocontra o centro de custo ou projecto.

Para verificar o Relatorio de Variação de Orçamento, vá para:

> Home > Contabilidade > Centro de Custo e Orçamento > Relatorio de Variação de Orçamento

<img class="screenshot" alt="Budget Variance Report" src="{{docs_base_url}}/assets/img/accounts/budget-variance-report.png">

## 4. Video
Aqui está um video de demonstração:
<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/wWHkB0jlXNk?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
 </iframe>
</div>

## 5. Topicos Relacionados
1. [Centro de Custo](/docs/user/manual/pt/contabilidade/centro-custo)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
