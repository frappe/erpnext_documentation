<!-- add-breadcrumbs -->
# Registo de Adiantamento de Pagamento

**Pagamento feito pelo Cliente/Fornecedor antes da factura ser enviada é um Adiantamento de Pagamento.**

Normalmente, adiantamento de pagamento é feito no caso de valores grandes. Considere um Cliente - Jane D'souza que fez um ordem para um mobilia cara no valor de ₹24,000 Ela é lhe pedido para dar um adiantamento antes de XXXX começar o trabalho no seu pedido. Ela entrega ₹10,000 em dinheiro.

No ERPNext, um adiantamento de pagamento é criado usando o Registo de Pagamento. Caso exista uma Ordem de Venda, voçê pode criar directamente um Registo de Pagamento para o valor adiantado. Ou então, pode criar um Pagamento a parte para o cliente. Da mesma forma, voçê pode criar um Registo de Adiantamento de Pagamento para um Fornecedor, via Ordem de Pagamentos.

![RP apartir da OV](/docs/assets/img/accounts/advance-payment-1.png)

> Nota: Caso o pagamento não estiver ligado a uma Factura, é considerada como um adiantamento de pagamento. Os adiantamentos de pagamento são reflectidos nos Relatorios de Contas a Receber e Contas Pagar.

## 1. Pre-requisitos
Para criar um registo de adiantamento de pagamento, estes precisam ser criados primeiro:

* Parte (Cliente / Fornecedor)
* Conta de Pagamento (Conta Banco ou Dinheiro)

## 2. Como criar um Registo de Adiantamento de Pagamento
Uma vez a Ordem de Venda ou Ordem de Compra submetida, voçê irá encontrar uma opção para criar um Pagamento a favor. Pode criar tambem um novo Registo de Pagamento e manualmente selecionar os valores (como Parte e conta de pagamento). Aqui estão os passo spar criar um Adiantamento de Pagamento contra um Ordem de Venda.

1. Vá em Ordem de Vendas e click em **Criar > Pagamento**.
1. Definir/verificar as contas.
1. Salvar e Submeter.


Qualquer Registo de Pagamento que não estiver ligado a uma factura é considerada como um adiantamento de pagamento pelo sistema ERPNext.

Caso o Cliente entregou $5,000 em dinheiro como adiantamento, será registado como um
registo a credito contra a conta de Recebimentos do Cliente. Para balancear [pelo sistema de contas duplo], $5000 
é debitado contra a conta a dinheiro da Empresa.

### 2.2 Alocando o Adiantamento de Pagamento para um Factura

Quando criar uma factura, voçê pode verificar se existe um Adiantamento de Pagamento a favor esta Parte.

<img class="screenshot" alt="Advace Payment" src="{{docs_base_url}}/assets/img/accounts/advance-payment-3.png">

Ao fazer o click no botão **Obter Adiantamentos Recebidos**, irá buscar o Registo de Adiantamento de Pagamento encontrado para esta parte. Uma vez o Registo de Adiantamento de Pagamento encontrado, voçê pode alocar o Valor do avanço contra  a factura. A alocação irá reduzir o Valor em Falta desta factura de imediato..

Salvar e Submeter a Factura de Venda.

### 3. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Lançamento Contabilistico](/docs/user/manual/pt/contabilidade/lancamento-contabilistico)
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
