<!-- add-breadcrumbs -->
# Termos e Conceitos

Antes de começar a implementação, vamos nos familiarizar com as terminologias usadas
e alguns conceitos basicos no ERPNext.

* * *

### Conceitos Basicos

#### Empresa

Este representa a Empresa para o qual o ERPNext foi configurado. Com esta Configurações,
voçê pode criar varias Empresa, cada representando uma entidade legal diferente.
A contabilidade de cada Empresa será diferente, mas todos partilham o mesmo
Cliente, Fornecedor e Produtos ou Serviços.

> Configurações > Empresa

#### Clientes

Representa um cliente. Um Cliente pode ser individual ou um empresa.
Voçê pode criar varios Contactos e Endereços para cada Cliente.

> Vendas > Clientes

#### Fornecedores

Representa o fornecedor de produtos ou serviços. Sua empresa de teleones é o 
seu Fornecedor, então é um fornecedor de material. Novamente, um Fornecedor pode ser
individual ou uma empresa e tem varios Contactos e Endereços.

> Compras > Fornecedores

#### Item

Um Produtos, sub-produto ou Serviço é comprado, vendido ou fabricado
e tem um identificador unico.

> Inventário > Item

#### Contabilidade

Uma Conta é um titulo em que transações de negócio e finaceiro são feitos
Por exemplo, "Despesas de Viagem" é uma conta, "Cliente Zoe", "Fornecedor Mae"
são contas. ERPNext cria contas para Clientes e para Fornecedores automaticamente.

> Contabilidade > Plano de Contas

#### Endereços

Um endereço representa detalhes de local de um Cliente ou Fornecedor. Estes podem ser
de diferentes locais tais como Empresa Mãe, Fabrica, Armazem, Loja etc.

> Vendas > Endereços

#### Contacto

Um contacto Individual pertençe a um Cliente ou Fornecedor ou de um 
independente. Um Contacto tem um nome e detalhes de contacto como email e numero de telefone.

> Vendas > Contacto

#### Comunicação

A lista de Comunicação com o Contacto ou Lead. Todos os emails envaidos apartir do 
sistema são adicionados a tabela de Comunicação.

> Suporte > Comunicação

#### Lista de Preços

Uma Lista de Preços é um lugar aonde lista de preços diferentes podem ser guardados. É um nome
que voçê da a um conjunto de Preços de Item guardados numa lista particular.

> Vendas > Lista de Preços


> Compras > Lista de Preços

* * *

### Contabilidade

#### Ano Fiscal

Representa um Ano Fiscal ou Ano Contabilistico. Voçê pode ter varios
Anos Fiscais. Cada Ano Fiscal tem uma data de inicio e de fim e as transações
somente podem ser guardadas dentro desse periodo. Quando "fecha" o ano fiscal,
os balanços são transferidos como balanços de "abertura" par ao proximo
ano fiscal.

> Configurações > Empresa > Ano Fiscal

#### Centro de Custo

Um Centro de Custo é como uma Conta, mas a diferença é que toda a 
estrutura representa o seu negocio melhor que as Contas.
Por exemplo, no seu Plano de Contas, voçê pode separar as despesas por tipo
(i.e., viagem, marketing, etc.). No seu Mapa de Centro de Custos, voçê pode separar por
linha de produto ou grupo de negocio (e.g., vendas online, vendas a retalho, etc.).

> Contabilidade > Mapa de Centros de Custo

#### Journal de Entrada

Um documento contem varias Contabilidades Gerais / General Ledger (GL) e a soma dos Debitos e Creditos
destas entradas são iguais. No ERPNext voçê pode actualizar os Pagamentos,
Develuções, etc., usando as entradas do Jornal.

> Contabilidade > Contabilidade Geral

#### Factura de Vendas

Uma bill enviada ao Cliente para entrega de Itens (serviços ou bens).

> Contabilidade > Factura de Vendas

#### Factura de Compras

Uma bill enviada pelo Fornecedor para a entrega de Itens (serviços ou bens).

> Contabilidade > Factura de Compras

#### Moeda

O ERPNext permite alocar transações em varias moedas. No entanto somente é usada uma moeda
para alocação no livro de contas. Enquanto que pode ter as suas Facturas com pagamentos
em moedas diferentes, o valor é convertido para  a moeda standard
usando a taxa de cambio especificada.

> Configurações > Moeda

* * *

### Vendas

#### Grupo de Clientes

Uma classificação de Clientes, normalmente baseada num segmento do mercado.

> Vendas > Configurações > Grupo de Clientes

#### Lead

Uma pessoa que poderá ser uma futura fonte do negócio. Um lider pode gerar
Oportunidades. (desde: “pode levar a uma venda”).

> CRM > Lead

#### Oportunidade

Uma potencial venda. (desde: “oportunidade para negócio”).

> CRM > Oportunidade

#### Proforma

Pedido do Cliente para preço de Item ou serviço.

> Vendas > Proforma

#### Ordem de Venda

Uma nota confirmando os termos de entrega e preço de um Item (produto ou serviço)
pelo Cliente. Entregas, Ordens de Trabalho e Facturas são feitas
com base nas Ordens de Venda.

> Vendas > Ordem de Venda

#### Território

Uma classificação geografica da area para gestão de vendas. Voçê pode definir objectivos
para os Territórios e cada venda fica ligada a um Território.

> Vendas > Configurações > Território

#### Parceiro de Vendas

Um terçeiro distribuidor / negociador / afiliado / agente de comissão que vende
produtos da empresa por uma comissão.

> Vendas > Configurações > Parceiro de Vendas

#### Vendedor

Alguem que ajuda o Cliente e fecha um negócio. Voçê pode definir objectivos para
o Vendedor e tag eles nas transações.

> Vendas > Configurações > Vendedor

* * *

### Compras

#### Ordem de Compra

Um contracto dado a um Fornecedor para entrega de itens especificos pelo 
custo, quantidade e datas e outros termos acordados.

> Compras > Ordem de Compra

#### Requisição de Material

Um pedido feito por um utilizador do sistema, ou gerado automaticamente pelo ERPNext baseado
num nivel de encomenda ou quantidade projectada no Plano de Produção para a compra 
de alguns Itens.

> Compras > Requisição de Material

* * *

### Stock (Inventário)

#### Armazem

Um Armazem logico no qual as entradas de stock são feitas.

> Stock > Armazem

#### Entrada de Stock

Material transferido de um Armazem, para um Armazem ou apartir de um outro Armazem para
outro.

> Stock > Entrada de Stock

#### Guia de Remessa

Uma lista de Itens com quantidades para shipment. Uma Guia de Remessa vai reduzir o
stock de Itens do Armazem de onde é retirado. Um Guia de Remessa é normalmente feita
contra uma Orde de Venda.

> Stock > Guia de Remessa

#### Recibo de Compra

Uma nota dizendo que um conjunto de Itens foram recebidos do Fornecedor,
normalmente apartir de uma Ordem de Compra.

> Stock > Recibo de Compra

#### Numero de Serie

Um unico numero dado particulamente a uma unidade de um Item.

> Stock > Numero de Serie

#### Lotes

Um numero dado a um grupo de unidades de um Item particular que pode ser comprado
ou fabricado em grupos.

> Stock > Lotes

#### Entrada de Stock Ledger

Uma tabela unificada de todos os movimentos de material apartir de um armazem para outro. Esta é
a tabela actualizada quando uma Entrada de Stock, Guia de Remessa, Recibo de Compra e 
Factura de Venda (POS) é feita.

#### Reconciliação de Stock

Actualizar a entrada de Stock de multiplos Itens apartir de uma folha (CSV).

> Stock > Reconciliação de Stock 

#### Inspecção de Qualidade

Uma nota é preparada para registar um certo parametro de Itens na altura da recepção
do Fornecedor, ou Entraga ao Cliente.

> Stock > Inspecção de Qualidade

#### Grupo de Itens

Uma classificação de Item.

> Stock > Configurações > Grupo de Itens

* * *

### Gestão de Recusos Humanos

#### Funcionário

Registo de uma pessoa que está presente ou saiu, na lista de Funcionários da 
empresa.

> Recursos Humanos > Funcionário

#### Pedido de Licença

Um registo de um pedido de licença aprovado ou rejeitado.

> Recursos Humanos > Pedido de Licença

#### Tipo de Licença

Um tipo de licença (e.g., Doença, Maternidade, etc.).

> Recursos Humanos > Licença e Assiduidade > Tipo de Licença

#### Entrada da Folha de Pagamento

Uma ferramenta que ajuda na criação de varios Recibos de Salário para os Funcionários.

> Recursos Humanos > Entrada da Folha de Pagamento

#### Folha de Vencimento

Um registo mensal dos salários processados do Funcionário.

> Recursos Humanos > Folha de Vencimento

#### Estrutura Salarial

Um Modelo para indentificar todos os componentes de salário de um Funcionário (remunerações),
impostos e outras deduções de segurança social.

> Recursos Humanos > Folha de Pagamento > Estrutura Salarial

#### Avaliação

Um registo de avaliação de um Funcionário durante um periodo especifico baseado em
alguns parametros.

> Recursos Humanos > Avaliação

#### Modelo de Avaliação

Um Modelo para gravar os diferentes parametros da avaliação de um Funcionário(s) e
e peso para uma determinada tarefa.

> Recursos Humanos > Avaliação > Modelo de Avaliação

#### Assiduidade

Um registo indicando a presença ou ausencia de um Funcionário num dia particular.

> Recursos Humanos > Assiduidade

* * *

### Fabrico

#### Lista de Materiais (LDM)

A lista de Operações e Itens com as suas quantidades, que são necessários para
produzir outro Item. Uma Lista de Materiais (LDM) é usada para planificar compras e 
criar preço de custo dos produtos.

> Fabrico > LDM

#### Posto de Trabalho

Um lugar aonde a operação de LDM é feita. É util calcular o custo 
directo do produto.

> Fabriro > Posto de Trabalho

#### Ordem de Trabalho

Um documento assinalando a produção (fabrico) de um Item em particular com 
quantidades especificas.

> Fabrico > Ordem de Trabalho

#### Ferramenta de Produção

Uma ferramento par automatizar a criação da Ordem de Trabalho e pedidos de Compra baseados
numa Ordem de Venda aberta para um periodo especifico.

> Fabrico > Ferramenta de Produção

* * *

### Website

#### Blog Post

Um peuqnos artigo que aparece na secção "Blog" do website gerado
pelo modulo do ERPNext. Blog significa "Log de Pagina".

> Website > Blog Post

#### Web Page

Uma pagina web com un unico URL (endereço web) no website gerado pelo
ERPNext.

> Website > Web Page

* * *

### Configurações / Customização

#### Campo Personalizado

Um campo de usuario definido num formulário / tabela.

> Configurações > Customizar ERPNext > Campo Personalizado

#### Configurações Gerais

Esta secção é aonde voçê define varios parametros para o sistema.

> Configurações > Data > Configurações do ERPNext

#### Impressão de Cabeçalho

Um titulo que pode ser posto numa transação somente para imprimir. Por exemplo, voçê
quer imprimir uma Proforma com o titulo "Proposta" or "Factura Proforma".

> Configurações > Impressão > Cabeçalho de Carta

#### Termos e Condições

Texto com os seus termos de contracto. Em transações de Vendas/Compras pode haver a necessidade de alguns Termos e Condições baseados nos serviços ou bens que o Fornecedor emite para o Cliente. Voçê pode aplicar os Termos e Condições para as transações e ao imprimir aparece na Impressão. Para saber sobre os Termos e Condições, [click here](/docs/user/manual/en/setting-up/print/terms-and-conditions)


> Vendas > Configurações > Termos e Condições

#### Unidade de Medida (UDM)

Como é medida a quantidade para um Item. E.g., Kg, No., Pares, Pacote, etc.

> Stock > Configurações > UDM

{next}
