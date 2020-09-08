<!-- add-breadcrumbs -->
# Dimensão Contábil

> Introduzido na Versão 12

Dimensão Contábil significa marcar todas as transações com a dimensão exacta como um Ramo, Unidade de Negócio, etc. Permite que voçê mantenha cada segmento separado, consequentemente limitando a manutenção geral nas contas do GL e o seu Plano de Contas mantem-se limpo.

Centro de Custo e Projectos são tratados como dimensões por defeito no ERPNext. Ao configurar Dimensão Contábil, este campo será adicionado nos relatorios de transação aonde será aplicado. 

No ERPNext voçê pode criar contas dimensionais configuraveis e usar em transações e relatórios.

Para acessar a lista de Dimensão Contábil, deve ir:
> Home > Contabilidade > Mestres Contábeis > Dimensão Contábil

## 1. Como criar uma conta Dimensão Contábil no ERPNext.

1. Ir para lista de Dimensão Contábil e fazer um click no botão Novo.
1. Selecionar o Documento de Referencia no qual voÇẽ quer usar como dimensão personalizada. Por exemplo, caso selecione Departamento como Documento de Referencia, a dimensão será baseada no Departamento.
1. Digite o nome da dimensão (Este nome irá aparecer na transação para o qual dimensões são criadas).
1. Dentro da tabela por defeito de Dimensões voçễ pode mencionar a dimensão por defeito da empresa como mostra no screenshot em baixo. Esta dimensão será automaticamente fetched na transação contra essa empresa especifica.
1. Marque "Obrigatório" caso voçê queira que a dimensão para ser obrigatória nas transações.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/accounting-dimension.png">


## 2. Funcionalidades

Ao passo que cria dimensões, campos personalizados vão ser criados usando trabalhos em segundo plano para aquela dimensão especificada. Voçê pode ver elas na secção de Dimensão Contábil dentro das transações que tenham um impacto nas entradas de Contabilidade (GL Entry).

### 2.1 Usando dimensões nas transações

Para marcar uma transação com uma dimensão voçê pode selecionar a dimensão na secção de Dimensão Contábil como mostra a imagem em baixo.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-section.png">

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-transaction.png">

### 2.2 Filtrando Relatórios com base nas dimensões

Voçê pode filtrar varios relatórios financeiros como Lucro e Percas, Folha de Balanço, General Ledger baseado nestas dimensões.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/report-dimensions.png">

### 2.3 Fazendo a dimensão contábil obrigatório para contas de "Lucros e Percas" e "Folhas de Balanço"
Lucros e Percas é o grupo de Contas de Recebimentos e Despesas que representam as suas transações de contabilidade dentro de um periodo.

As contas da Folha de Balanço são Aplicações de fundos (Activos) e Fonte de Fundos (Responsabilidades) que significam a net-worth da sua empresa num certo tempo.

Ao selecionar as caixas 'Obrigatório para contas Lucros e Percas' ou 'Obrigatório para Folhas de Balanço' voçê pode configurar as dimensões para serem obrigatorias para 'Lucros e Percas' e 'Folhas de Balanço'.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-mandatory.png">

### 2.4 Desactivando as contas de dimensão quando não são necessárias

Voçê pode desactivar as dimensões caso voçê não precise mais. As transações antigas com dimensão contábil ficaram intactas.

<img alt="Create custom dimension" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/dimension-disable.png">


### Topicos Relacionados
1. [Centro de Custo](/docs/user/manual/pt/contabilidade/centro-custo
1. [Orçamento](/docs/user/manual/pt/contabilidade/orcamento)
1. [Relatorios de Contabibilidade](/docs/user/manual/pt/contabilidade/relatorios-contabilidade)
