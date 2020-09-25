# Log do Veiculo

**Log do Veiculo é usado para digitar as leituras do Odometer, Despesas de Combustivel e detalhes das despesas de Manutenção.**

Para aceder Log do Veiculo, vá para:

> Recursos Humanos > Gestão de Frota > Log do Veiculo


## 1. Pre-requisitos

Antes de criar o Log do Veiculo, é necessario criar os seguintes:

* [Veiculo](/docs/user/manual/pt/recursos-humanos/veiculo)


## 2. Como criar Log do Veiculo

1. Vá para a lista Log do Veiculo, clique em Novo.
1. Selecione Matricula e o Funcionario.
1. Digite as Leituras do Odometer como a Data e outras informações (leitura).
1. Digite os Detalhes de Reabastecimento [opcional] como Qtd de Combustivel, Preço, Fornecedor e Ref. da Factura.

    <img class="screenshot" alt="Vehicle Log" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log1.png">


1. Adicionalmente, os Detalhes dos Serviços do Veiculo tambem podem ser adicionados como mostra (opcional).

    <img class="screenshot" alt="Vehicle Log" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log2.png">

1. Salvar. Uma vez a informação salva, os valores do Modelo e Marca serão automaticamente inseridos.


	

## 3. Funcionalidades

Log do Veiculo no ERPNext permite automaticamente criar um [Relatorio de Despesas](/docs/user/manual/pt/recursos-humanos/relatorio-despesas) para as Despesa do Veiculo.

### 3.1 Criar Relatorio de Despesas contra as Despesas do Veiculo

Clique no botão Criar Relatorio de Despesas. Este botão irá aparecer somente no caso dos Logs de Veiculo forem submetidos.

<img class="screenshot" alt="Expense Claim Button" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log-expense-claim-button.png">

Quando fizer o clique em 'Criar Relatorio de Despesas',

  1. A Data, Funcionario, Total de Despesas serão inseridos no Relatorio de Despesas.
  2. A soma das Despesas do Combustivel e Despesas de Serviço são calculados e inserido no Valor do Relatorio de Despesas.
  3. Funcionario pode submeter o Relatorio de Despesas para mais processamento.

	<img class="screenshot" alt="Vehicle Log" src="{{docs_base_url}}/assets/img/human-resources/vehicle-log-expense-claim.png">

## 4. Topicos Relacionados

1. [Relatorio de Despesas](/docs/user/manual/pt/recursos-humanos/relatorio-despesas)



