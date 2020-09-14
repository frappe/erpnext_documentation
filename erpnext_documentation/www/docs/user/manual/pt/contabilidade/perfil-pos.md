<!-- add-breadcrumbs -->
# Perfil do Ponto de Venda

**No ERPNext, um perfil do POS permite usar as funcionalidades do Ponto de Venda.**

POS inclui funcionalidades avançadas para usar funcionalidades diferentes, tais como
gestão de inventário, CRM, finanças, armazens, etc., tudo contruido num software
POS. Antes do POS modernos, todas estas funções eram feitas independentes e
necessitavam de digitar as informações manualmente, que poderia
levar a cometer erros de registo.

Se voçê estiver em operações de retalho, voçê quer que o seu Ponto de Vendas seja rapido
e o mais eficiente possivel. Para fazer isto, voçê pode criar um Perfil do POS para o usuário.

Para aceder a lista de Perfil do POS, vá para:
> Home > Retalho > Operações de Retalho > Perfil de Ponto-de-Venda

## 1. Como criar um Perfil de POS
1. Vá para o Perfil de Ponto-de-Venda e clique em Novo.
1. Digite o nome do perfil.
1. Selecione o [Nome das Series](/docs/user/manual/pt/configuração/configurar/nome-das-series).
1. Defina a Conta Write Off e o Centro de Custo Write Off para o qual as transações serão registadas.
1. Definir o modo de pagamento na tabela, o por defeito será Dinheiro caso nada seja definido aqui. Somente os modos de pagamento definidos aqui irão aparecer ao usar o POS. Depois de adicionar os modos de pagamento, definir um deles como o modo por defeito activando a caixa.
 <img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/pos-setting/default_mop.png">
1. Definir o valor por defeito para os metodos de pagamento (recomendado: 0).
1. Salvar.
 <img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/pos-setting/pos_profile.png">

### 1.1 Opções Adicionais ao criar o Perfil de POS

* **Cliente**: Usuário podem vender certos produtos para Clientes particulares apartir do POS ao adicionar Grupo de Itens, Grupo de Cliente no Perfil do POS.
* **Armazem**: As quantidades de Stock no Armazem selecionado serão afectados pelas transações do POS com o Perfil de POS.
* **Campanha**: Um [Campanha](/docs/user/manual/pt/CRM/campanha) de vendas pode estar ligada aqui para rastrear o total de vendas.
* **Endereço da Empresa**: Se o contador de POS este definido num Branch da Empresa, o endereço pode ser selecionado aqui.

* **Actualizar Stock**: Se activo, a quantidade de stock será afectada quando transações forem feitas com o Perfil do POS. Isto é, Registo do Razão de Stocks será feito quando voçê "Submeter" esta Factura de Venda assim sendo eliminando a necessidade de criar uma Guia de Remessa separada.
* **Ignorar Regras de Preço**: Qualquer [Regra de Preço](/docs/user/manual/pt/contabilidade/regras-preço) activa será ignorada para este Perfil de POS.
* **Permitir Apagar**: Em POS Offline, os dados são guardados local. Selecionando esta caixa permitirá o Usuario em apagar as Facturas de Venda guardadas localmente em modo de Rascunho.
* **Permitir Usuario editar Preço**: O Perfil do POS do usuario irá permitir editar os 'Preços' dos Itens adicionados nas transações.
* **Permitir Usuario editar Descontos**: O Perfil do POS do usuario irá permitir editar os 'Descontos' dos Itens adicionados nas transações.
* **Permitir Imprimir Antes de Pagar**: Isto irá permitir o Usuuario do POS imprimir uma factura antes do pagamento ter sido feito.
* **Mostrar Itens em Stock**: A quantidade existente dos Itens apartir do Armazem selecionado será mostrado no POS do Usuário.

## 2. Funcionalidades

### 2.1 Aplicavel para Usuários
Por defeito, todos os Usuários de Venda podem aceder os Perfil POS criados no ERPNext. Contudos, se voçê quiser que somente alguns Usuarios pode aceder os Pefil POS, voçê pode adicionar eles a tabela. Once even one User is set in the POS Profile, other Users cannot use this POS Profile for retail transactions.

**Definindo o Perfil POS por defeito**: Ao selecionar a caixa de Defeito na tabela, o Perfil POS corrente torna-se o Perfil POS por defeito para aquele Usuario. Então, a proxima vez que o Uusuario entrar para o sistema, o Perfil POS será definido por defeito.

![Usuário POS](/docs/assets/img/pos-setting/pos-profile-default.png)

> Nota: Se voçê especificar um Usuario em particular, a configuração do POS será
aplicada para aquele Usuario. Se a opção do Usuario for deixada em branco, a definição será posta para todos usuarios.
Para entender como o POS funciona, visite a pagina [Ponto de Vendas](/docs/user/manual/pt/contabilidade/ponto-de-vendas).


### 2.2 Definindo Grupo de Itens e Grupo de Clientes
Ao definir uma Grupo de Item/Cliente no Perfil POS, o grupo será automaticamente selecionado quando fizer transações com o Perfil POS.

<img class="screenshot" alt="POS Setting" src="{{docs_base_url}}/assets/img/pos-setting/item_customer_group.png">

### 2.3 Configurações de Impressão

![Impressão POS](/docs/assets/img/pos-setting/pos-profile-print.png)

#### Formato de Impessão para Online
Voçê pode definir um Formato de Impressão pelo voçê decide o desenho do documento impresso. Para saber mais, visite a pagina [Formato de Impressão](/docs/user/manual/pt/configuração/imprimir/formato-impressão).

#### Cabeçalho de Carta
Voçê pode imprimir a sua Factura de Venda POS usando o Cabeçalho de Cartas da sua Empresa. Saiba mais [aqui](/docs/user/manual/pt/configurações/imprimir/cabeçalho-carta).


#### Imprimir Cabeçalhos
Cabeçalhos de Factura de Vendas POS opdem ser alterados ao imprimir o documento. Por exemplo, o cabeçalho poder ser 'Factura', ou 'Cobrança'. Voçê pode fazer isto selecionando **Imprimir Cabeçalhos**. Para criar um novo Imprimir Cabeçalhos vá para: Home > Configurações > Imprimir > Imprimir Cabeçalhos. Saiba mais [aqui](/docs/user/manual/pt/configurações/imprimir/imprimir-cabeçalhos).

#### Termos e Condições
Pode haver certos Termos e Condições no Item que esta a vender, estes podem ser aplicados aqui. Para saber mais sobre Termos e Condições, [clique aqui](/docs/user/manual/pt/configurações/imprimir/termos-e-condições).

### 2.4 Configurações do POS Offline
ERPNext é uma ferramente online que corre usando a Iternet. Contudo, voçê pode usar as funcionalidades do ERPNext Offline. Para fazer, primeiro deve activar nas configurações do POS o 'Usar POS Modo Offline'.

Quando online, a janela do POS irá mostrar 'Online', caso contrário, o sistema POS irá mostrar offline.

Depois os seguintes podem ser configurados no Perfil do POS:

* [Territorio](/docs/user/manual/pt/vendas/territorio)
* [Formato de Impressão](/docs/user/manual/pt/configurações/imprimir/formato-impressão)
* [Grupo de Cliente](/docs/user/manual/pt/CRM/grupo-cliente)

![Offline POS](/docs/assets/img/pos-setting/pos-profile-offline.png)

### 2.5 Contabilidade

* **Lista de Preços**: Uma [Lista de Preços](/docs/user/manual/pt/inventariio/lista-preços) guarda os [Preços dos Itens](/docs/user/manual/pt/inventario/preço-item). Definindo uma Lista de Preços aqui irá procurar os Preços dos Itens para o Perfil POS corrente apartir da Lista de Preços.
* **Moeda**: Por defeito, será de acordo a mmoeda por defeito da Empresa. Contudo, voçê pode trocar. No caso de trocar a moeda, lembre-se de mudar as contas tambem.
* **Impostos e Taxas**: Selecionando o [Modelo de Impostos e Taxas de Venda](/docs/user/manual/pt/vendas/modelo-impostos-taxas-vendas) ou [Modelo de Impostos e Taxas de Compra](/docs/user/manual/pt/compras/modelo-impostos-taxas-compra) aqui será aplicado automaticamente o imposto e taxa a transação POS.
* **Aplicar Desconto em**: Aqui voçê pode definir se o desconto é aplicado ao Total Geral (sem valor imposto) ou ao Total Liquido (depois do valor do imposto).
* **Categoria do Imposto**: Ao selecionar a [Categoria de Imposto](/docs/user/manual/pt/contabilidade/categoria-imposto) aqui, as Regras de Imposto associadas com a Categoria de Imposto serão aplicadas para cada transação feita neste Perfil POS.

As seguintes contas podem ser definidas no razão geral para actualizar de acordo:

* Conta para o Valor de Troco
* Conta Write Off
* Centro de Custo Write Off
* Conta de Recebimento
* Conta de Despesa

### 2.5 Dimensões Contabil
Dimensões Contabil permite marcar transações baseadas em Territorios, Branch, Ciente, etc. Isto ajuda a ver os extractos de contabilidade separados com base no criterio selecionado. Para saber mais, visite a pagina [Dimensões Contabil](/docs/user/manual/pt/contabilidade/dimensao-contabil).

> Nota: Centros de Custo são tratados como dimensão por defeito.

## 3. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
1. [Ponto de Vendas](/docs/user/manual/pt/contabilidade/ponto-de-vendas)
