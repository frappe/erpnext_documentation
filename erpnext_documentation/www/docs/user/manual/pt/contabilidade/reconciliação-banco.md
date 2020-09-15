<!-- add-breadcrumbs -->
# Reconciliação Bancária

**Um registo de Reconciliação Bancária é usado para igualar os extractos de conta do ERPNext com os extractos de conta do seu banco.**

Se voçê estiver a receber pagamentos ou fazer pagamentos via cheque, os extractos do banco não vão accurately match as datas do registo, isto porque o banco normalmente leva tempo para "liquidar" estes pagamentos.

Tambem, voçê pode ter enviado um cheque ao seu Fornecedor e que poderá levar alguns dias ante que ele receba e depositado pelo Fornecdor. No ERPNext voçê pode sincronizar os extractos do banco e os seus Lançamentos Contabilisticos usando as datas de transação.

## 1. O que é um Extracto de Reconciliação Bancária?
O Relatorio da Reconciliação Bancária mostra a diferença entre o balanço do bano mostrado nos extractos do banco da empresa, enviados pelo banco contra o valor mostrado no Plano de Contas da Empresa.

É desta forma que um extracto de Reconciliação Bancária se parece:

<img class="screenshot" alt="Bank Reconciliation statement" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation-2.png"> 

No relatorio, verifique se o campo 'Balanço por Banco' é igual ao Extracto da Conta Bancária. Se o mesmo for igual, significa que a Data de Liquidação está correctamente actualizada para todos os seus registos de banco. Se não estiver certo, então os registos de banco para o qual a Data de Liquidação ainda não foi actualizada.

Para aceder a Reconciliação Bancária, vá para:
> Home > Contabilidade > Bancos e Pagamentos > Actualizar as Data de Transações Bancárias

## 2. Como Actualizar as Datas de Transações Bancárias

1. Vá para Actualizar as Datas de Transações Bancárias.
1. Selecione a sua Conta Bancária.
1. Selecione a Data apartir e fim.
1. Voçê pode esclher para incluir registo reconciliados e transações de POS.
1. Clique no botão **Obter Registos de Pagamento**.
1. Agora voçê irá ter todos os tipos registo do “Voucher do Banco”.
1. Em cada um dos registos, no lado mais a direita da coluna, actualize o campo "Data de Liquidação" e faça o clique no botão **Actualizar Data de Liquidação**.

Fazendo isto voçê poderá sincronizar os extractos do seu banco com os registo no sistema.

<img class="screenshot" alt="Bank Reconciliation" src="{{docs_base_url}}/assets/img/accounts/bank-reconciliation.png">
 
## 3. Ferramenta de Tipos de Reconciliação

No ERPNext tem duas ferramentas de reconciliação:

1. Uma ferramenta de reconciliação manual que permite definir a data de liquidação contra os registo de pagamento, pagamento de facturas de venda ou lançamentos contabilisticos
2. Uma ferramenta de reconciliação semi-automatica que permite limpar as transações bancárias contra os registo de pagamento, vendas, pagamento de facturas de compra, lançamentos contabilisticos ou reembolso de despesas.

### 3.1 Ferramenta de Reconciliação Bancária Manual

Para ver este relatorio, vá para **Contabilidade > Banoc e Pagamentos > Extracto de Reconciliação Bancária**. No relatorio, verifique se o campo 'Balanço por Banco' é igual ao Extracto da Conta Bancária. Se for igual, significa que a Data de Liquidação está correcta e correctamente actualizar para todos os registos de banco. Caso não, é porque a Data de Liquidaçáo ainda não foi actualizada nos registos de bancos.


### 3.2 Ferramenta de Reconciliação Bancária Semi-automatica

#### Carregar o Extracto do Banco

Voçê pode carrgar o Extracto do Banco em formato CSV ou XLS para o ERPNext usando a Ferramenta de Reconciliação Bancária.

1. Descarregue o Extracto Bancária da pagina do seu banco

 <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/sample_bank_statement.png">
 Tenha certeza de que voçê tem pelo menos a data, o debito/credito e a moeda em cada linho do extracto do seu banco.

1. Configura o formato de importação na tabela do Banco

 <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/bank_configuration.png">

 O seu ficheiro será lido e o ERPNext irá usar este mapeamento para enviar toda a informação para os campos correspondentes na tabela de Transação Bancária.

1. Carregue o seu ficheiro no ERPNext

 <img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/bank_transaction_upload.gif">


#### Sincronização da Conta Bancária

Voçê pode usar o Plaid (veja [Plaid Integrations page](/docs/user/manual/pt/integração_erpnext/plaid_integration)) para sincronicar automaticamente a sua conta bancária no ERPNext. Todas as suas transações bancarias serão automaticamente importadas para o ERPNext.

Uma vez todas as transações importadas no ERPNext, voçê pode reconciliar com os pagamentos existentes. Se encontrar um pagamento que parece ser igual a transação do banco, o ERPNext irá propor um pagamento correspondente.

Se o pagamento for igual, apenas clique em reconciliar para reconciliar com as suas transações bancárias.

<img class="screenshot" alt="Reconcile bank transactions" src="{{docs_base_url}}/assets/img/accounts/auto_reconciliation.gif">

Se O ERPNext não propor qualquer pagamento, voçê sempre pode selecionar os pagamentos correspondentes manualmente:

<img class="screenshot" alt="Reconcile bank transactions manually" src="{{docs_base_url}}/assets/img/accounts/manual_reconciliation.gif">

Voçê pode tambem criar um novo pagamento ou factura directamente apartir do dashboard de Reconciliação Bancária.

<img class="screenshot" alt="New payment entry" src="{{docs_base_url}}/assets/img/accounts/new_payment.gif">

### 4. Topicos Relacionados
1. [Reconciliação Bancária](/docs/user/manual/pt/contabilidade/reconciliação-banco)
1. [Garantia Bancária](/docs/user/manual/pt/contabilidade/garantia-bancária)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
