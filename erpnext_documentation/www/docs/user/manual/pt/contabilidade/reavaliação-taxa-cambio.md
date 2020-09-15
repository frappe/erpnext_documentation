<!-- add-breadcrumbs -->
# Reavaliação da Taxa de Cambio

No ERPNext, voçê pode lançamento contabilistico em varias moedas. Por exemplo, se voçê tiver uma conta bancária em moeda estrangeira, voçê pode fazer transações nesta moeda e o sistema irá mostrar o balanço do banco nesta mesma moeda.

O motivo do Reavaliação da Taxa de Cambio é para ajustar o balanço das contas do Razão Geral sobre qualquer alteração nas taxas de cambio da moeda. Isto é util quando voçê estiver a fechar as contas e quer actualizar as contas de GL da Empresa mostrando as contas das outras moedas feitas.

Para aceder a lista Reavaliação da Taxa de Cambio, vá para:
> Home > Contabilidade > Multi Moedas > Reavaliação da Taxa de Cambio

## 1. Como definir uma moeda numa conta

1. Para começar com contabilidade multi moedas, voçê de atribuir a moeda de contabilidade no registo de Contas.
1. Voçê pode definir a Moeda apartir do Plano de Contas enquanto estiver a criar a conta.

 <img class="screenshot" alt="Set Currency from Chart of Accounts" src="{{docs_base_url}}/assets/img/accounts/multi-currency/chart-of-accounts.png">
 
1. Voçê pode tambem atribuir/modificar a moeda para a conta existente ao abrir o registo de Contabilidade especifico.
1. Clique na Conta e em Editar.

 <img class="screenshot" alt="Modify Account Currency"  src="{{docs_base_url}}/assets/img/accounts/multi-currency/account-set-currency.png">

## 2. Como activar a Reavaliação da Taxa de Cambio

A funcionalidade Reavaliação da Taxa de Cambio é para lidar com a situação em que tem contas com diferentes moedas no Plano de Contas da Empresa.

1. Vá para: **Configurações > Empresa > *selecione a empresa***.
1. Defina o campo 'Conta de Ganho / Perda de Cambio Não Realizada' na tabela Empresa. Esta conta é para balancear a diferença do total de credito e total de debito.
 <img class="screenshot" alt="Field Set for Company"   src="{{docs_base_url}}/assets/img/accounts/field_set_company.png">
1. Vá para **Contabilidade > Multi Moedas > Reavaliação da Taxa de Cambio > Novo**.
1. Selecione a empresa.
1. Clique no botão 'Receber Entradas'. Irá procurar as contas que tem moedas diferentes apartir definição feita em 'Moeda Padrão' na Empresa.
1. Este irá procurar novas taxas de cambio automaticamente e se não foi definido na tabela Cambio de Moeda então irá procurar em 'Taxa de Cambio' definido no [Cambio de Moeda](/docs/user/manual/pt/contabilidade/taxa-cambio).
 <img class="screenshot" alt="Exchange Rate Revaluation"   src="{{docs_base_url}}/assets/img/accounts/exchange-rate-revaluation.png">

1. Ao Submeter o botão, **Criar Entrada de Diario** irá aparecer.
<img class="screenshot" alt="Exchange Rate Revaluation Submitting"    src="{{docs_base_url}}/assets/img/accounts/exchange-rate-revaluation-submit.png">

1. Fazendo o clique neste botão irá criar o Lançamento Contabilistico para a Reavaluação da Taxa de Cambio.
<img class="screenshot" alt="Journal Entry"   src="{{docs_base_url}}/assets/img/accounts/journal-entry-exchange.png">

1. Ao submeter o Lançamento Contabilistico, o razão geral será afectado como:
<img class="screenshot" alt="Journal Entry"   src="{{docs_base_url}}/assets/img/accounts/journal-entry-exchange-submit.png">

### 3. Topicos Relacionados
1. [Lançamento Contabilistico Inter Empresa](/docs/user/manual/pt/contabilidade/lançamento-contabilistico-inter-empresa)
1. [Facturas Inter Empresa](/docs/user/manual/pt/contabilidade/facturas-inter-empresa)
