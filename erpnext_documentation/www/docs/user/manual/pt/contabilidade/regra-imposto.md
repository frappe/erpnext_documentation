<!-- add-breadcrumbs -->
# Regra de Impostos

**Uma Regra de Impostos automaticamente aplica impostos as transações baseadas em regras pre-feitas.**

Voçê pode definir que [Modelos de Imposto](/docs/user/manual/pt/configuração/configurar-impostos.html) deve ser aplicada nas transações de Vendas / Compras usando a Regra de Imposto. Este pode ser decidido por varios factores como Cliente, Grupo de Cliente, Fornecedor, Grupo de Fornecedor, Item, Grupo de Item ou combinação destes.

Para aceder a lista de Regra de Impostos, vá para:
> Home > Contabilidade > Impostos > Regra de Impostos

## 1. Pre-requisitos
Antes de criar e usar a Regra de Impostos, é aconselhavel criar os seguintes:

1. [Modelo de Impostos e Taxas de Vendas](/docs/user/manual/pt/vendas/modelo-impostos-taxas-vendas)
    
    Ou

1. [Modelo de Impostos e Taxas de Compra](/docs/user/manual/pt/compras/modelo-impostos-taxas-compra)

## 2. Como cria Regra de Impostos
1. Vá para a lista de Regra de Impostos e clique em Novo.
1. Em baixo do Tipo de Imposto selecione a o imposto a ser aplicado as Vendas ou Compras. 
1. Selecione o Modelo de Imposto a ser aplicado.
1. Salvar.
 <img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule.png">

Voçê pode listar os Itens online usando o modulo de Pagina Web. Selecionando 'Usar para Carrinho de Compras' irá usar esta Regra de Imposto para as transações de Carrinho de Compras tambem. Para saber mais, visite a pagina [Carrinho de Compras](/docs/user/manual/pt/website/carrinho-compras).

> Nota: É aconselhavel não usar o Modelo de Vendas/Compras selecionado aqui [Modelo de Imposto de Item](/docs/user/manual/pt/contabilidade/modelo-imposto-item), pode causar interferencia. Se voçê quiser usar algumas taxas de imposto para Regra de Impostos e Modelo de Imposto de Item, utilize um nome diferente para o Modelo de Imposto para Vendas/Compras.

## 3. Funcionalidades
### 3.1 Auto aplicar Regra de impostos baseados em Cliente/Fornecedor
Selecione o Cliente/Fornecedor se o imposto é para ser aplicado para uma parte especifica. Deixe como Todos os Grupos de Clientes/Todos os Grupos de Fornecedores se a Regra de Imposto é aplicavel para todos Clientes/Fornecedores.

Ao selecionar o Cliente/Fornecedor os Endereços de Cobrança e Envio serão inseridos e salvos na ficha de Cliente/Fornecedor.

### 3.2 Auto Aplicar Regra de Imposto baseado em Item / Grupo de Item

Ao definir um Item ou Grupo de Item na Regra de Impostos, esta Regra de Impostos será automaticamente aplicadas a todas novas transações que tenham o Item/Grupo de Item selecionado.

### 3.3 Configurando a Categoria de Imposto
Definindo a Categoria de Imposto permite aplicar varias Regras de Imposto a uma transação baseada em varios factores. Para saber mais, visite a pagina [Categoria de Imposto](/docs/user/manual/pt/contabilidade/categoria-imposto).

### 3.4 Validade
Defina a Data de Inicio e Fim se o imposto é para ser aplicado somente durante um periodo especifico. Deixando ambos em branco irá resultar na Regra de Impostos não ter um limite de tempo.

### 3.5 Prioridade
Definindo um numero de prioridada aqui irá decidir em que ordem a Regra de Impostos será aplicada em caso de varias Regras de Imposto terem o mesmo criterio. '1' é a prioridade maior, '2' tem menos prioridade e assim sucessivamente.

## 4. Como funciona Regra de Impostos?
Funciona com um filtro para aplicar automaticamente modelos de Imposto:

1. Defina o Cliente ou uma região especifica
1. O modelo de Imposto selecionado será aplicado de acordo as condições definidas na Regra de Impostos
1. Será aplicado a uma nova transação de Vendas/Compras baseada no tipo selecionado na Regra de Imposto

Por exemplo, selecionando 'Nitin' como o Cliente e 'Todos Grupos de Itens' irá causar a Regra de Impostos a ser aplicada em todas as transações de vendas aonde o Cliente Nitin aparece. De igual forma, selecionando um 'Cristal de Plastico A' e 'Todos os Grupos de Clientes' irá causar a Regra de Impostos a ser aplicada em todos os Clientes mas somente quando o Item é 'Cristal de Plastico A'. 

Entretando criando uma nova transação no sistema irá selecionar e aplicar o modelo de Imposto com base na regra de imposto definida.

Vamos considerar o cenario para entender melhor a Regra de Impostos. Digamos que definimos duas Regras de Imposto como em baixo.

<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule-1.png">

<img class="screenshot" alt="Tax Rule" src="{{docs_base_url}}/assets/img/accounts/tax-rule-2.png">

Aqui no Estado GST tem Cobrança de País como India e VAT 14% tem Cobrança como Alemanha.

Agora suponhamos que nós tentemos criar a Ordem de Venda para o Cliente cujo País de Cobrança é India, o sistema irá selecionar o Estado GST.
Caso o País de Cobrança do Cliente fosse Alemnha, o sistema iria selecionar VAT 14%.

### 5. Topicos Relacionados
1. [Regras de Preço](/docs/user/manual/pt/contabilidade/regras-preço)
1. [Modelo de Imposto de Item](/docs/user/manual/pt/contabilidade/modelo-imposto-item)
1. [Categoria de Imposto](/docs/user/manual/pt/contabilidade/categoria-imposto)
1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Fornecedor](/docs/user/manual/pt/compras/fornecedor)