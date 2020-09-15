<!-- add-breadcrumbs -->
# Regras de Preço

**Uma Regras de Preço define as regras de desconto/preço que são aplicados baseados certas condições.**

Uma Regras de Preço tem muitas opções na qual voçê pode control o preço de um Item. Filtros como quantidade, data, grupos e outras condições podem ser definidas.

Uma Regras de Preço é de alguma forma similar a [Regra de Impostos](/docs/user/manual/pt/contabilidade/regras-imposto).

A seguir são alguns casos que podem ser endereçados usando as Regras de Preço:

- Como politica de promoção de ve venda, se o Cliente comprar mais de 10 unidade de um item, ele tem 20% de desconto.
- Para o Cliente "XYZ", o preço de venda para um Item especifico poderia ser atualizado como ###.
- Itens categorizados em baixo de Grupos de Item especificos tem mesmo preço de venda ou compra.
- Clientes que pertencem a um Grupo de Clientes especifico devem ter ### preço de venda, ou % Desconto em Itens.
- Fornecedores categorizados em baixo de Grupos de Fornecedores devem ter ### o preço de compra aplicado.

Para ter Desconto e Lista de Preços para um Imte auto-aplicado, crie Regras de Preço para ele.

Para aceder a lista de Regras de Preço, vá para:
> Home > Contabilidade > Regras de Preço

## 1. Pre-requisitos
Antes de criar e usar as Regras de Preço, é aconselhavel criar estes:

1. [Item](/docs/user/manual/pt/stock/item)
1. [Grupo de Itens](/docs/user/manual/pt/stock/grupo-item)
1. [Cliente](/docs/user/manual/pt/CRM/customer)
1. [Fornecedor](/docs/user/manual/pt/compras/fornecedor)

## 2. Como criar uma Regra de Preços
1. Vá para a lista de Regras de Preço e clique em Novo.
1. Defina o titulo para a regra.
1. Selecione o que Aplicar em Codigo de Item, Grupo de Item, Marca ou Transação.
1. Selecione se voçê quer aplicar desconto de Preço ou desconto de Produto. Se voçê quiser oferecer produtos então selecione o desconto de produto.
 <img alt="Applicable On" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-on.png">
1. Para um unico item, selecione Codigo do Item e selecione os Itens.
1. Se voçê quiser aplicar Regras de Preço em todos os itens, selecione 'Grupo de Itens' e selecione **Todos os Grupos de Item** (parente Grupo de Item).
1. Defina o desconto/preço a ser aplicado. Para saber mais, [vá para esta seção](/docs/user/manual/pt/contabilidade/regras-preço#36-esquema-de-desconto-de-preço).
1. Salvar.

### 2.1 Opções Adicionais ao criar as Regras de Preço

#### Armazem
Definindo o Armazem aqui irá causa a Regra de Preço a ser aplicada somente se o item for selecionar apartir do Armazem especificado aqui.

#### Regra Aplicar Em
Baseado no atributo selecionado no campo 'Aplicar Em', voçê pode definir a Regra de Preços baseados nestes:

* [Item](/docs/user/manual/pt/inventario/item)
* [Grupo de Itens](/docs/user/manual/pt/inventario/grupo-item)
* Marca
* Transação (no total geral da transação)

Nesta tabela, voçê pode selcionar o Item/Grupo de Item/Marca especifica. Por exemplo, se voçê selcionar o Aplicar Em 'Grupo de Item' e selecionar na tabela 'Materia Prima', esta Regra de Preço será aplicada somente aos itens que pertencem ao grupo 'Materias Primas'.

**UdM**: A Regra de Preços será aplicada somente se a UdM definida for igual com a transação.

#### Condição

Nesta campo voçê adiciona uma condição em python para verificar o valor do campo no documento de transação, como mostra em baixo na Factura de Vendas:
```
customer=='Customer Name' and status!='Overdue'
```

Por favor note que somente uma unica linha de condição python irá funcionar, usando o nome do campo do nome do documento.

#### Condições Mistas
Se voçê selecionar dois ou mais Itens e definir a Quantida Min e Max. A Regra de Preços será aplicada somente se o total da soma dos Itens for igual a quantidade definida. Por exemplo, voçê criou a Regra de Preços no Item 1 e Item 2 e definiu a Quantidad min e Max como 30, a Regra de Preços será aplicada somente se o total da quantidade for 30

#### É Acumulativo
Activando está opção permite que a Regra de Preço seja aplicada de forma cumulativa. Voçê precisa definir o 'Valor Min' e 'Valor Max' para isto.

Considere o cenario aonde o Valor Min é de 1,500 e o Valor Max é de 2,000. Agora, se uma transação for criado para 1,400 entá a Regra de Preços não será aplicada. Contudo, ao criar a segunda factura com o valor 600, a Regra de Preços será aplicada. Isto acontece vendo que o valor total (cumulativo) das facturas foi de 2,000. Note que o desconto será aplicado somente a ultima transação que seja igual ao limite cumulativo.

Este pode ser util para dar descontos se o Cliente compra um Item multiplas vezes e voçê quer reward him com descontos/preços especiais.

## 3. Funcionalidades

### 3.1 Aplique a Regre Em Outro
Esta funcionalidade verifica a condição no primeiro Item mas aplica regra em outro Item.

![Aplique a regrea em outro](/docs/assets/img/articles/pricing-rule-other.png)

Por exemplo, defina Item1 e Item2 na tabela 'Aplicar Regra Em' e defina 'Aplicar Regra em Outro' no Item3. Agora, se a transação tem Item1, Item2, e Item3, a Regra de Preços será aplicada no Item3 vendo que os primeiros dois Itens estão presentes na transação.

### 3.2 Informação da Parte

Defina se a Regra de Preços é para Item de Vendas ou Compras.

Baseado na sua selecão voçê pode definir a aplicabilidade para um das tabelas.

* [Cliente](/docs/user/manual/pt/CRM/cliente)
* [Grupo de Cliente](/docs/user/manual/pt/CRM/grupo-cliente)
* [Territorio](/docs/user/manual/pt/vendas/territorio)
* [Parceiro de Vendas](/docs/user/manual/pt/vendas/parceiro-vendas)
* [Campanha](/docs/user/manual/pt/CRM/campanha)
* [Fornecedor](/docs/user/manual/pt/compras/fornecedor)
* Grupo de Fornecedor

### 3.3 Quantidade e Valor
Defina a qtd minima, qtd maxima, valor minimo ou valor maximo para um Item quando esta Regra de Preços deve ser aplicada.

Note que se a quantidade ou valor for menor ou passar os limites definidos aqui, a Regra de Preços não será aplicada de todo. Contudo, será aplicada se voçê activou as opções Condições Mistas or Cumulativas.

<img alt="Applicable Qty" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-qty-amt.png">

### 3.4 Validade
Voçê pode tambem definir o intervalo de datas quando a Regra de Preços será valida. Este é util para as promoções de venda. A deixar em branco as datas a Regra de Preços não tera um limite de tempo.

<img alt="Period" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-period.png">

### 3.5 Margem

![Margem de Regra de Preços](/docs/assets/img/articles/pricing-rule-margin1.png)

* **Tipo de Margem**: Ao vender um Item, voçê pode ser por uma certa margem. Se voçê não quiser adicionar preços de venda aos Itens sempre e gostaria de automaticamente definir uma margem, pode ser feito com esta funcionalidade.

* **Percentagem de Margem ou Valor**: A margem pode ser definida baseada em Percentagem ou Valor, ex: 5% de margem ou $50 de preço fixo.

Para mais detalhes sobres como adicionar margens [Clique aqui](/docs/user/manual/pt/vendas/artigos/adding-margin)

### 3.6 Esquema de Desconto de Preço
O papel actual a ser aplicado é definido nesta secção.

![Regra de Preços](/docs/assets/img/articles/pricing-rule-rule.png)

* **Preço**: Aqui é o novo preço para um Item. Po exemplo, se voçê vend um Item por 100 e quer vender por 112 para uma parte especifica, então selecione o Preço e defina como 112.
* **Percentagem de Desconto**: A percentagem de desconto pode ser definido. A percentagem de desconto pode ser definido para uma [Lista de Preços](/docs/user/manual/pt/inventario/lista-preços) especifico. Deixando o 'Para Lista de Preço' em branco irá aplicar a Regra de Preços para todas as Listas de Preço.
* **Valor de Desconto**: Um valor fixo de desconto será aplicado. Por exemplo, se voçê vende um Item por 100 e quer vender com um desconto de 7, então esta condição pode ser definida usando a opção Valor de Desconto.

### 3.7 Configurações Avançadas

![Pricing Rule Advance](/docs/assets/img/articles/pricing-rule-adv.png)

* **Threshold for Suggestion**: Este é o threshold beseado no qual o sistema irá notificar para ajustar a Quantidade do Item para desconto. Por exemplo, se Quantidade Min for 10 e o Threshold 9, o sistema irá notificar para adiconar mais 1 Item para o desconto ser aplicado. Este é aplicado tambem a definição do valor.

* **Prioridade**: Considere um Grupo de Itens, voçê quer definir regras especificas num Item de um grupo. Esta pode ser feito criando uma nova Regra de Preços e selecionando uma prioridade mais alta. Este pode ser aplicado a Grupo de Cliente e Grupo de Fornecedores.

* **Aplicar Regras de Preço Multiplas**: Para entneder este, considere um Item com o Preço 500. Exitem duas Regras de Preço que são P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Activando esta opção irá aplicar o total de 15% ao Preço do Item que será 425.

* **Aplicar Desconto ao Preço**: O desconto será compounded. Considere o mesmo cenario que o de cima. Ao activar esta opção, 10% será aplicado em 500 que irá dar 450, então 5% será aplicado em 450 que irá dar 427.5.

* **Validar Regras de Preço**: Mostra a mensagem de validação se o desconto/preço definidos manualmente por si na transação não é igual a Regra de Preços.

 Este é util quando o maior destribuidor na hierarquia decide o desconto/preço a ser aplicado e voçê está somente a validar se a Regra de Preços é aplicada correctamente.

## 4. Tipos de Descontos de Regras de Preços
### 4.1 Desconto de Preço

1. No Tipo de Marge, voçê pode definir se a margem +e calcular como percentagem ou um valor. Ex: 10% margem na lista de preços do fornecedor na altura das vendas.

1. Preço mencionado na Regra de Preços irá ser dada prioridade sobre Lista de Preços de Item (Preços de Item).

 <img alt="Applicable Rate" class="screenshot" src="/docs/assets/img/articles/pricing-rule-price.png">

1. Percentagem de Desconto pode ser aplicado a uma Lista de Preços especifica (Vendas ou Compras). Para aplicar em ambas, deixe o campo 'Para Lista de Preços' em branco.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount.png">

1. Desconto pode ser tambem definido em termos de valor.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-discount-amt.png">

### 4.2 Desconto de Produto

1. "Compre 2 quantidade e leva 1 de borla do mesmo item." Para configurara este tipo de regras, definina a Preço ou Desconto de Produto como 'Desconto de Produto', selecione a mesma caixa de Item, e defina a quantidade.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-same-product-free.png">

1. "Compre 2 quantidade e leve 1 de borla de outro item." Para configurar este tipo de regras. Defina o Preço ou Desconto do Produto como Desconto de Produto, não selecione a 'Mesmo Item' caixa e defina o 'Item de borla' e a quantidade.

 <img alt="Discount" class="screenshot" src="{{docs_base_url}}/assets/img/articles/pricing-rule-other-product-free.png">

### 5. Topicos Relacionados
1. [Esquemas de Promoção](/docs/user/manual/pt/contabilidade/esquema-promocional)
1. [Regras de Imposto](/docs/user/manual/pt/contabilidade/regras-imposto)
1. [Fornecedor](/docs/user/manual/pt/compras/fornecedor)
1. [Item](/docs/user/manual/pt/inventario/item)
