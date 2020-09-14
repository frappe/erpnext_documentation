<!-- add-breadcrumbs -->
# Modelo de Imposto do Item

**Modelo de Imposto do Item é util para taxação inteligente de Itens.**

Se alguns dos seu itens tem atribuidos taxa de impostos diferentes da taxa de impostos normal na tabela de Impostos e Taxas, então voçê pode criar um Modelo de Imposto de Item e atribuir a um [Item](/docs/user/manual/pt/inventario/item) ou [Grupo de Item](/docs/user/manual/pt/inventario/grupo-item). A taxa atribuida no Modelo de Imposto de Item será a principal em vez da taxa normal atribuida na tabela de Impostos e Taxas.

Por exemplo, se a taxa GST é de 18% e foi adicionada na tabela de Impostos e Taxas na Ordem de Vendas, então será aplicado para todos os itens da Ordem de Vendas. Contudo, se voçê precisa de ter uma taxa de imposto diferente para alguns itens, os passos são os seguintes

Para aceder a lista de Modelo de Imposto do Item, vá para
> Home > Contabilidade > Impostos > Modelo de Imposto do Item

Vamos assumir que estamos a criar um Ordem de Vendas. Nós temos o [Modelo de Impostos e Taxas de Vendas](/docs/user/manual/pt/vendas/modelo-impostos-taxas-vendas) com GST 9%. Fora todos os itens de Venda, num Item em particular, somente 5% GST será aplicado, enquanto que outro item está exempto do Imposto (não taxavel). Voçê precisa selecionar o Numero da Conta para o Imposto e definir a taxa a aplicar.

## 1. Pre-requisitos
Antes de cirar e usar o Modelo de Imposto de Item, é aconselhado criar os seguintes primeiro:

1. [Item](/docs/user/manual/pt/inventario/item)
1. Ativar 'Adicionar Automenticamente Imposto e Taxas apartir do Modelo de Imposto de Item' nas [Configurações de Contabilidade](/docs/user/manual/pt/contabilidade/configurações-contabilidade)

## 2. Como criar um Modelo de Imposto de Item
1. Vá para a lista de Modelo de Imposto de Item e clique em Novo.
1. Digite o titulo do Modelo de Imposto de Item.
1. Selecione uma conta e defina a taxa. Adicione mais linhas se necessário.
1. Salvar.

Agora o Modelo de Imposto de Item está pronto para ser atribuido a um Item. Para fazer isto, vá par ao Item, Secção de Imposto do Item e selecione o Modelo de Imposto de Item:

![Imposto do Item no Item](/docs/assets/img/accounts/item-tax-in-item.png)

> Nota: É aconselhavel não usar o Modelo de Vendas/Compras selecionado aqui nas [Regras de Imposto](/docs/user/manual/pt/contabilidade/regras-imposto), pode causar interferencia. Se voçê quiser usar as mesmas taxas para as Regras de Imposto e o Modelo de Imposto de Item, utilize um nome diferente para o Modelo de Imposto de Vendas/Compras.

### 2.1 Mencione se é Aplicavel a Imposto na tabela de Item

Os Modelos de Impostos são pre-criados com valores. Para itens que um valor de imposto diferente dos outros, voçê pode trocar na tabela do Item. Vá para a tabela de Imposto no Item, adicione uma linha, selecione um tipo de imposto e altere taxa. Agora, esta nova taxa irá passar por cima do modelo ao criar uma Ordem/Factura. Por exemplo, no screenshot me baixo voçê pode ver que o valor do imposto definido como 5 e será a taxa utilizada nas transações.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/item-wise-tax.png">

Para um Item que está exempto de impostos, mencione 0% como valor do imposto na tabela do Item.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/exempted-item.png">

> Nota: Para o Modelo de Imposto do Item funcionar, voçê precisa ter a certeza que o tipo de imposto (contas) definido no Modelo de Imposto de Item (que alterou o valor do imposto) esteja presente no Modelo de Impostos e Taxas de Vendas.

> Se voçê quiser incluir varios itens com taxas diferentes, voçê precisa registar eles com contas de imposto diferentes. Por exemplo, VAT 14%, VAT 5% etc.

### 2.2 Calculos de Imposto em Transações

Por exemplo, no screenshot seguinte, o Item tem um Modelo de Imposto de Item atribuido com 5% em duas contas de Imposto.

<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation.png">

O valor procurado apartir do Modelo de Imposto do Item e calculado:
<img class="screenshot" alt="Opening Account" src="{{docs_base_url}}/assets/img/accounts/tax-calculation1.png">

### 2.3 Modelo de Imposto de Item para cada Item
Voçê pode manualmente selecionar um Modelo de Imposto de Item para cada Item na transação:

![Imposto de Item individual](/docs/assets/img/accounts/item-tax-each.png)


### 2.4 Imposto de Item inteligente em Grupo de Itens
Voçê pode atribuir o Modelo de Imposto de Item a um Grupo de Itens modificando a tabela de Imposto do Item na secção do Imposto do Item dentro do documento do Grupo do Item.
<img class="screenshot" alt="Item Tax in Item Group" src="{{docs_base_url}}/assets/img/accounts/item-group-tax.png">

Modelo de Imposto do Item aplicado num Grupo de Item será aplicado em todos os Itens deste mesmo grupo a não ser que um Item individual no Grupo de Itens tenha o seu proprio Modelo de Imposto de Item atribuido.


### 2.5 Validade dos Imposto de Item

<img class="screenshot" alt="Item Tax in Item Group" src="{{docs_base_url}}/assets/img/accounts/item-tax-in-item.png">

Voçê pode atribuir validade aos Modelos de Impostos como mostra a imagem em baixo.

* Baseado na data de postagem da transação, um modelo de imposto valido será automaticamente procurado.
* Se houver mais que um modelo de impostos validos o primeiro modelo de imposto valido apartir da tabela de Imposto de Item será procurado.
* No caso de não haver um modelo de impostos validos então o primeiro modelo de imposto sem a data de 'Valido Apartir' na tabela de Imposto do Item será procurado.

> Nota: Enquanto estiver a adicionar Itens na Factura de Compras a prioridade será para 'Data de Factura de Fornecedor' em vez de 'Data de Postagem' para procurar o Modelo de Imposto de Item valido.

### 2.6 Alguns pontos para anotar

- Se voçẽ definir a Categoria de Imposto em branco, o Modelo de Imposto de Item será aplicado para os Itens na transação.

- Voçẽ pode aplicar Modelos de Imposto de Itens diferentes para Categoria de Impostos diferentes.

- Para um Modelo de Imposto de Item passar por cima das taxas, deve ter uma linha na tabela de Impostos e Taxas com a mesma Conta de Imposto e com a taxe de imposto normal.

- Se voçê quiser aplicar impostos somente aos Itens com um Modelo de Imposto de Item então voçê pode definir a taxa de imposto normal para 0.

### 3. Topicos Relacionados
1. [Regra de Impostos](/docs/user/manual/pt/contabilidade/regra-imposto)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compras](/docs/user/manual/pt/contabilidade/factura-compra)
