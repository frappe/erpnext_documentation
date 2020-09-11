<!-- add-breadcrumbs -->
# Categoria de Imposto

**A Categoria de Imposto permite aplicar uma ou mais Regras de Imposto a transações com em varios critérios.**

Se voçê quiser aplicar diferentes tipo de impostos baseados na Categoria de Imposto, crie a Categoria de Impostos apartir:

> Home > Contabilidade > Impostos > Categoria de Imposto

## 1. Pre-requisitos
Antes de crar uma Categoria de Imposto, é aconselhavel criar o seguinte primeiro:

1. [Regra de Imposto](/docs/user/manual/pt/contabilidade/regra-imposto)

## 2. Como funciona a Categoria de Imposto
Criando uma Categoria de Imposto é simples, vá para a lista de Categoria de Imposto, Click em Novo e digite o nome.

- Uma categoria de Imposto pode estar ligado a um ou mais [Regras de Imposto](/docs/user/manual/pt/contabilidade/regra-imposto).
- Esta Categoria de Imposto pode ser atribuida a um Cliente, para quen o Clinte for selecionado, a Categoria de Imposto será procurada. Tambem é aplicado para Fornecedores.
- Irá procurar o Modelo de Imposto de Venda ligado a uma Regra de Imposto. Uma vez que as linhas na tabela de Imposto será preenchidas automaticamente.
- A Categoria de Imposto pode ser usado para agrupar Clientes a quem será atribuido um Imposto. Por exemplo, Governo, Sem Lucros, comercial, etc.

  <img class="screenshot" alt="Tax Category" src="{{docs_base_url}}/assets/img/accounts/tax-category.gif">

> Dica: Uma Categoria de Imposto pode ser atribuida a varias Regras de Imposto. Então pode criar varias combinações para aplicar impostos automaticamente as transações.

## 3. Atribuindo a Categoria de Imposto
Categoria de Impostos é automaticamente determinada numa transação pelo Endereço da Parte ou pela Parte Mestre (Cliente/Fornecedor). Voçê pode atribuir a Categoria de Imposto baseado em: 

1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Fornecedor](/docs/user/manual/pt/buying/fornecedor)
1. [Endereço](/docs/user/manual/pt/CRM/endereço) Cobranças ou Envios.
  Voçê pode selecionar Endereço de Cobrança ou Endereço de Envio modificando a opção 'Determinar Endereço de Categoria de Imposto apartir' nas configurações de Contabilidade. Categoria de Imposto é determinada pelo Endereço de Parte primeiro. Se o Endereço não for atribuido a qualquer Categoria de Imposto, então a Categoria de Imposto da Parte será usada.
      ![Endereço de Categoria do Imposto](/docs/assets/img/accounts/tax-cat-address.png)
1. [Item](/docs/user/manual/pt/inventario/item#316-imposto-de-item)
1. Voçê pode tambem manualmente selecionar a Categoria de Imposto durante uma transação.
  
## 4. Qual o efeito que uma Categoria de Imposto tem numa Transação?

* Modelos Especificos de Imposto de Item para aquela Categoria de Imposto são definidas automaticamente para itens.
* Voçê pode criar [Regras de Imposto]({{docs_base_url}}/user/manual/pt/contabilidade/regra-imposto) para automaticamente definir num Modelo de Impostos e Taxas de Vendas / Compras baseado em Categorias de Imposto diferentes em transações.

## 5. Topicos Relacionados
1. [Regras de Imposto](/docs/user/manual/pt/contabilidade/regra-imposto)
1. [Cliente](/docs/user/manual/pt/CRM/cliente)
1. [Fornecedor](/docs/user/manual/pt/compras/fornecedor)
1. [Endereço](/docs/user/manual/pt/CRM/endereço)
