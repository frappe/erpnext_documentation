<!-- add-breadcrumbs -->
# Contabilidade Multi Moedas

**Fazer Transações em duas moedas diferentes é conhecido como Contabilidade Multi Moedas.**

No ERPNext, voçê pode criar Lançamento Contabilistico em varias moedas. Por exemplo, se voçê tem uma conta bancária em moeda estrangeira, voçê pode fazer transações nessa moeda e o sistema irá mostra os Balaço nessa mesma moeda.

Contas Bancárias em moeda estrangeiro podem ser para qualquer branches da sua propria empresa ou para conta de Devedores/Credores para Cliente/Fornecedores estrangeiros.

## 1. Configuração
### 1.1 Defina a moeda no Plano de Contas
Para começar com contas multi moedas, voçê precisa atribuir a moeda no registo de Contas. Voçê pode definir a moeda apartir do [Plano de Contas](/docs/user/manual/pt/contabilidade/plano-de-contas) quando estiver a criar a Conta.

<img class="screenshot" alt="Modify Account Currency" src="{{docs_base_url}}/assets/img/accounts/multi-currency/account-set-currency.png">


### 1.2 Nova conta com moeda diferente
Voçê pode atribuir/modificar a moeda abrindo o registo de Contas para Contas existentes.

<img class="screenshot" alt="Set Currency from Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/multi-currency/account-set-currency-1.png">

### 1.3 Moeda para Cliente/Fornecedor
Para Cliente/Fornecedor (Parte), voçê pode tambem definir a sua moeda de cobrança no registo. Caso a moeda da parte seja diferente da Moeda da Empresa, voçê deve mencionar a Conta default para Recebimentos/Pagamento nessa moeda.

<img class="screenshot" alt="Customer Accounting Currency"    src="{{docs_base_url}}/assets/img/accounts/multi-currency/customer-currency.png">

### 1.4 Depois da Configuração
Uma vez definida a Moeda nas contas necessárias e selecionada as contas necessarias no registo de Parte, voçê pode fazer a transação. Caso a conta da parte seja diferente da moeda da Empresa, o sistema não irá permitir fazer as transações com esta Parte.

Voçê precisa alterar a moeda para a moeda da parte na transação (Factura/Ordem de Vendas ou Compras). Se a moeda da parte é a mesma que a moeda da empresa, voçês pode fazer a transação para esta Parte em qualquer moeda. Mas os registo contabiliisticos (Entrada GL) seram sempre na Moeda da Conta da Parte..

> **Nota**: Tenha a certeza que a conta correcta com a moeda é definida no campo 'Debitar para' quando estiver a fazer facturas/pagamentos.

Voçê pode alterar a moeda da conta na Parte/Lançamento Contabilistico antes de fazer qualquer transação contra. Depois de fazer o Lançamento Contabilistico, o sistema não vai permitir alterar a moeda de ambos os registos Parte/Lançamento Contabilistico. Caso a configuração de multi-empresas, a moeda da conta da parte deve ser igual para todas as empresas. 

## 2. Taxa de Cambio
Quando estiver a lidar com varias moedas, o ERPNext tem uma pagina de Taxa de CAmbio para gerir os cambios. Permite salvar os cambios que precisa. Para saber mais, visite a pagina [Taxa de Cambio](/docs/user/manual/pt/contabilidade/taxa-cambio).

Para transação de moeda estrangeira, o ERPNext verifica a taxa de cambio:

1. Apartir da tabela Taxa de Cambio para qualquer registo (caso criado pelo Usuário).
1. Caso não tenha, o ERPNext irá tentar obter a taxa de cambio pelo mercado [Frankfurter](https://www.frankfurter.app).
1. Caso não tenha, então a taxa de cambio deverá ser inserida manualmente.

A taxa de cambio na tabela Taxa de Cambio mestre é procurada com base da opção 'Permitir Taxa de Cambio Fixa' estar activa ou não nas configurações de Contabilidade. Para saber mais, visite a pagina [Configurações de Contabilidade](/docs/user/manual/pt/contabilidade/configurações-contabilidade).

## 3. Transações

### 3.1 Factura de Venda

Em Facturas de Venda, a moeda de transação deve ser igual que a moeda do Cliente, se a moeda do Cliente for diferente que da Empresa. Caso contrário, voçê pode selecionar qualquer moeda na Factura de Vendas. Ao selecionar o Cliente, o sistema irá procurar a conta de Recebimentos do Cliente/Empresa. A moeda da conta de recebimento deve ser igual que a moeda da conta do Cliente.

Agora, em Factura, o valor Pago será digitado na moeda de transação, em vez da Moeda da Empresa. O valor Write Off tambem será digitado na moeda de transação.

O Valor em Falta e o Valor de Adiantamento será sempre calculado e mostrado na moeda do Cliente. O valor pago será reflectido no [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento):

<img class="screenshot" alt="Sales Invoice Outstanding"   src="{{docs_base_url}}/assets/img/accounts/multi-currency/paid-amount.png">

### 3.2 Factura de Compra

De igual mode, em Factura de Compra, Lançamento Contabilistico será baseado a moeda do Fornecedor. Valor em Falta e valor de Adiantament será mostrado na moeda do fornecedor. O valor Write off será digitado na moeda da transação.

### 3.3 Lançamento Contabilistico

No Lançamento Contabilistico, voçê pode fazer transações em moedas diferentes. Tem uma caixa 'Multi Moeda'. para activar em varias moedas. Somente quando 'Multi Moedas' está activo, que será possivel selecionar contas como moedas diferentes.

<img class="screenshot" alt="Journal Entry Exchange Rate" src="{{docs_base_url}}/assets/img/accounts/multi-currency/journal-entry-multi-currency.png">
 
Na tabela Contas, ao selecionar a conta de moeda estrangeira, o sistema irá mostrar a secção da Moeda e procurar a Conta da Moeda e a Taxa de Cambio automaticamente. Voçês pode modificar/alterar a Taxa de Cambio depois manual. Valor do Debito/Credito dever ser digitado na Conta da Moeda, o sistema vai calcular e mostrar o valor do Debito/Credito na Moeda da Empresa automaticamente.

<img class="screenshot" alt="Journal Entry in multi currency" src="{{docs_base_url}}/assets/img/accounts/multi-currency/journal-entry-row.png">

## 4. Relatorios

### 4.1 Razão Geral

No Razão Geral, o sistema mostra valores Debito/Credito na moeda da parte **se filtrar** pela Conta e essa Conta de Moeda diferente da Moeda da Empresa.

<img class="screenshot" alt="General Ledger Report"   src="{{docs_base_url}}/assets/img/accounts/multi-currency/general-ledger.png">

### 4.2 Contas de Recebimentos/Pagamentos

Nos relatorios de Contas de Recebimentos/Pagamentos, o sistema mostra todos os valores na moeda da Parte/Conta.

<img class="screenshot" alt="Accounts Receivable Report"  src="{{docs_base_url}}/assets/img/accounts/multi-currency/accounts-receivable.png">

### 5. Topicos Relacionados
1. [Re-evalução da Taxa de Cambio](/docs/user/manual/pt/contabilidade/reavaliação-taxa-cambio)
1. [Taxa de Cambio](/docs/user/manual/pt/contabilidade/taxa-de-cambio)
1. [Moeda](/docs/user/manual/pt/contabilidade/moeda)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Factura de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
