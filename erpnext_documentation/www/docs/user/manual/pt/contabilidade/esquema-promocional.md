# Esquema Promocional

> Introduzido na versão 12

**O Esquema Promocional é um desconto temporario em um ou mais produtos.**

Esquemas Promocionais ajudam o negocio a tornar-se um sucesso com os preços baixos por uma periodo de tempo para atrair mais Clientes. Eles podem ser configuração no ERPNext. O Esquema Promocional está ligado as regras de preço, against each slab system that will generate the pricing rule.

Ao criar o Esquema Promocional, o sistema cria uma [Regra de Preço](/docs/user/manual/pt/contabilidade/regras-preço). Um Esquema Promocional pode ter varias Regras de Preço associadas. No ERPNext, o Esquema é uma forma facil de gerir preço em varios Itens/Grupos baseado em varias condições e Partes.

Para aceder a lista de Esquema Promocional, deve ir:
> Home > Vendas > Itens e Preços > Esquema Promocional

## 1. Pre-requisitos
Antes de criar e usar o Esquema Promocional, é aconselhaver criar os seguintes primeiro:

1. [Item](/docs/user/manual/pt/inventario/item)
1. [Grupo de Item](/docs/user/manual/pt/inventario/grupo-item)
1. [Clientes](/docs/user/manual/pt/CRM/cliente)
1. [Fornecedores](/docs/user/manual/pt/comprar/fornecedor)

## 2. Como criar um Esquema Promocional

1. Vá para a lista de Esquema Promocional e click em Novo.
1. Digite o titulo da regra.
1. Selecione o que vai aplicar como Codigo do Item, Grupo de Item, Marca ou Transação. Selecionando a Transação irá aplicar o esquema no valor total da transação.
1. Baseado no 'Aplicar em', o sistema irá dar-lhe a provisão para selecionar o Codigo de Item / Grupo de Item / Marcar na tabela.
1. Selecione se o esquema é para Vendas, Compras ou ambos e defina a informação da parte.
1. No tab da tabela de Desconto de Preço, defina o desconto de preço, desconto de produto.
1. Usuários pode aplicar o desconto on Codigo de Item / Grupo de Item / Marca selecionando o valor para Aplicar Regra no outro campo.

 <img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes.png">
1. Salvar.

> Nota: Ao salvar o Esquema Promocional, uma nova Regra de Preço é criada.

### 2.1 Campos Adicionais ao criar o Esquema Promocional

#### Condições Mistas
Caso voçê selecione dois ou mais Itens e defina a Quantidade Minima e Maxima. O Esquema Promocional irá ser aplicado somente se o total da soma de Itens for igual as quantidades definidas. Por exemplo, voçê criou um Esquema Promocional no Item 1 e no Item 2 e defina a Quantidade Maxima e Minima como 30, o Esquema Promocional somente irá aplicar caso o total de quantidades for 30.

#### É Acumulativo
Activando esta opção permite que o Esquema Promocional seja aplicado de forma acumulada. Voçê poide definir o 'Valor Min' e o 'Valor Max' para este.

Considere o seguinte senário aonde o Valor Min é 1,500 e Valor Max é 2,000. Agora, caso uma transação for criada por 1,400 então o Esquema Promocional não será aplicado. Contudo, ao criar a segunda factura no valor de 600, o Esquema Promocional irá ser aplicado. Isto acontece desde que o valor total (acumulado) das facturas foi somado até 2,000. De notar que o desconto irá aplicado somente a ultima transação que ultrapasse / chegue até o limite do valor acumulado.

Este pode ser util para dar descontos aos Clientes que compram um Item varias vezes e voçê quer dar uma recompensa em descontos/preços especiais.

## 3. Funcionalidades

### 3.1 Aplicar o Esquema em Outro Item
Esta funcionaliadde verifica a condição do primeiro Item mas aplica esquema/desconto/precos em outros Item.

Por exemplo, defina o Item1 e Item2 na tabela 'Aplicar Regra' e defina 'Aplicar Regra no Outro' no Item3. Agora, caso a transação tenha Item1, Item2 e Item3, a Regra de Preço irá ser aplicada ao Item3 vendo que os primeiros dois Itens estavam presentes na transação.

### 3.2 Informação da Parte

Defina se o Esquema Promocional é para Venda ou Compra de Item.

Baseado na sua selecão voçê pode definir a aplicabilidade para um das tabelas Mastre.

* [Cliente](/docs/user/manual/pt/CRM/cliente)
* [Grupo de Cliente](/docs/user/manual/pt/CRM/grupo-cliente)
* [Territorio](/docs/user/manual/pt/selling/territorio)
* [Parceiro de Vendas](/docs/user/manual/pt/vendas/parceiro-vendas)
* [Campanha](/docs/user/manual/pt/CRM/campanha)
* [Fornecedor](/docs/user/manual/pt/compras/fornecedor)
* Grupo de Fornecedor

### 3.3 Validade
Voçê pode tambem definir a data limite de validade do Esquema Promocional. É util para uma promoção de Vendas. Ao deixar as datas em branco o Esquema Promocional não terá uma data de termino.

**Moeda**: Definindo a Moeda aqui irá fazer com o Esquema Promocional a ser aplicado somente quando a Moeda de transação for igual.

### 3.4 Laje de Desconto de Preço

**Descrição da Regra**: Digita a descrição para manter saber que Esquema Promocional se trata.

#### Quantidade e Valor
Especifique a Quantidade minima, quantidade maxima, valor minima ou valor maximo de Item quando se pode aplicar o Esquema Promocional.

Note que se a quantidade ou valor for menor ou exceder os limites definidos aqui, o Esquema Promocional não será aplicado em todos. Contudo, será aplicado caso voçê tenha activado a opção Condições Mixas ou Acumulativo.

### Definindo os Descontos/Taxas
* **Taxa**: Esta sera a nova taxa para um Item. Por exemplo, se voçê vender um Item por 100 e quer vender por 112 para uma parte especifica, então pode selecionar Taxa e definir a Taxa como 112.
* **Percentagem de Desconto**: Uma percentagem de desconto especifico pode ser definido. Por exemplo, um desconto de 10% num Item que valha 500 resultaria no preço de 450.
* **Desconto de Valor**: Um desconto de valor fixo pode ser aplicado. Por exemplo, se voçê vender um Item por 100 e quer vender com um desconto de 7, então esta condição pode ser definida usando a opção Desconto de Valor.

#### Filtros para definir Desconto

* **Armazem**: Definindo um Armazem aqui irá fazer com que o Esquema Promocional seja aplicado somente a um Item se for deste Armazem especificado aqui.

* **Prioridade**: Considere o Grupo de Item, voçê quer definir regras especificas num dos Itens do grupo. Este pode ser feito criando uma novo Esquema Promocional e definindo uma prioridade maior. 

* **Sugestão de Threshold**: Este é o threshold baseado no qual o sistema irá notificar para ajustar a quantidade do Item para o desconto. Por exemplo, se a Quantidade Min for 10 e o limite for 9, o sistema irá notificar para adicionar mais 1 Item para o ddesconto ser aplicado. Isto tambem aplica-se ao valor definido..

* **Validar Regra Aplicada**: Caso o preço digitado não seja valido para o Item, o sistem não irá aceitar aplicar uma taxa/desconto diferente.

### 3.5 Laje de Desconto de Produto
Um Desconto de Produto é aplicado quando um ou mais Itens são de Borla na compra de outros Itens. Muitos dos campos na tabela são os mesmos que a secção anterior.

As opções adicionais são:
* **Mesmo Item**: Caso voçês queira dar o Item de Borla (desconto de produto) na compra de um Item, active esta caixa. Caso voçê queira dar outro Item, desactive e selecione o Item para dar de Borla.

* **Aplicar Regras de Preço Multiplo**: Para entender isto, considere a Taxa do Item de 500. Existem duas Regras de Preço nele, o P1 e P2. P1 aplica 10% de desconto e P2 aplica 5%. Activando esta opção irá aplicar o total de 15% na taxa de Item que da 425.

* **UdM**: O Esquema Promocional será aplicado somente se a UdM (Unidade de Medida) definida for igual ao da transação.

* **Taxa**: Um Item pode ser oferecido sem custo pelo Fornecedor mas poderá haver um Imposto. Digitando a Taxa aqui significa que o Cliente irá ter de pagar o Imposto aplicado.


## 4. Tipos de Esquema Promocionais
### 4.1 Desconto de Preço

Neste tipo de esquema promocional, o usuáro tem um opção para definir o desconto em termos de percentagem ou valor de acord a quantidade min, quantidade max, valor minimo e valor maximo do produto. Usuários podem tambem configurara o esquema aonde eles podem definir uma Taxa flat para os productos baseados na quantidade ou valor do produto.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-price-discount.png">

### 4.2 Desconto do Produto

Neste tipo de esquema promocional, o usuário tem um opção para dar um produto de borla na compra do mesmo produto ou outro com as condições quantidade min, quantidade maxima, valor minimo, valor maximo.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-product-discount.png">

## 5. Como configurar o Esquema Promocional (Exemplos)

Vamos entender como configurar o esquema promocional no ERPNext usando alguns exemplos.

### 5.1 Condições Mistas de Esquemas

Cliente A comprou 10 quantidade de Bolo Britannia por 5 Rs pacote e 5 quantidade de Bolo Britannia por 10 Rs pacote. Agora, o Fornecedor quer dar um desconto de 10% ao Cliente A. O Fornecedor tambem quer dar um desconto de 10% ao Cliente B que comprou 15 quantidade de Bolo Britannia Cake por 5 Rs pacote.

Portanto, o Fornecedor quer aplicar o desconto nos produtos Bolo Britannia 5 Rs, Bolo Britannia 10 Rs somente se o Cliente comprou 15 quantidades de qualquer um dos produtos ou a soma de ambos.

Para configurar isto no ERPNext os passos são os seguintes:

1. Definir Aplicar em como Codigo de Item.
1. Definir o Codigo de Item para o Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela de Regras de Preço do Codigo de Item.
1. Activar o campo "Condições Mistas".
1. Na tabela desconto de preço, definir a qtd min, qtd max como 15.
1. Definir o tipo de desconto como Percentagem de Desconto e o valor 10.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-mixed-conditions.png">

### 5.2 Para aplicar o desconto em outro Item

Cliente A comprou 30 quantidades do Bolo Britannia 5 Rs pacote e 2 quantidades de Bolo Britannia 15 Rs. O Fornecedor quer vender o produto Bolo Britannia 15 Rs ao preço baixo de 12. Aqui o preço original para o produto Bolo Britannia 15 Rs é 15.

O Fornecedor quer aplicar a regra somente se o Cliente comprou o min de 30 quantidades do produto Bolo Britannia 5 Rs ou Bolo Britannia 10 Rs.

Para configura no ERPNext siga as instruções em baixo

1. Definir Aplicar como Codigo de Item.
1. Definir o Codigo do Item para Bolo Britannia 5 Rs, Bolo Britannia 10 Rs na tabela Regra de Preços de Codigo de Item.
1. Aplicar a Regra em Outro como Codigo de Item e definir o Codigo de Item como Bolo Britannia 15 Rs.
1. Na tabela desconto de preço, definir a qtd min de 30.
1. Definir o tipo de desconto como Taxa e digitar 12.

<img alt="Promotional Scheme" class="screenshot" src="{{docs_base_url}}/assets/img/accounts/promotional-schemes-discount-on-other.png">

## 6. Topicos Relacionados
1. [Regra de Preço](/docs/user/manual/pt/contabilidade/regras-preço)
1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Fornecedor](/docs/user/manual/pt/comprar/fornecedor)
1. [Item](/docs/user/manual/pt/inventario/item)
