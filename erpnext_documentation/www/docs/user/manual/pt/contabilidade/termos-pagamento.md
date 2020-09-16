<!-- add-breadcrumbs -->
# Termos de Pagamento

**Um Termos de Pagamento ajuda a definir o cronograma no qual os pagamentos serão feitos.**

Um Termos de Pagamento define uma laje especifica de pagamento. Por exemplo, 50% do pagamento ao enviar e 50% na entrega do item. Voçê pode salvar os seus Termos de Pagamento no ERPNext e incluir em todos os documentos nos ciclos de Vendas/Compras. O ERPNext irá fazer todas os registos do Razão Geral de acordo.

No ERPNext, os Termos de Pagamento somente define porções percentuais. O cronograma actual de pagamento pode ser facilmente aplicado usando o Modelo de Termos de Pagamento.

Voçê pode usar o Termos de Pagamento para os seguintes documentos:

- Factura de Vendas
- Facturas de Compra
- Ordem de Vendas
- Ordem de Compra
- Proformas

Para aceder aos Termos de Pagamento vá para:
> Home > Contabilidade > Mestre Contabil > Termos de Pagamento

Note que a introdução dos Termos de Pagamento remove os campos "Dias de Credito" e "Dias de Credito baseados em" na tabela Clientes/Fornecedor. Os Termos de Pagamento tem as mesmas informações e torna mais flexivel de usar.

![Termos de Pagamento]({{docs_base_url}}/assets/img/accounts/payment-terms.png)

## 1. Como criar um Termo de Pagamento

1. Vá para a lista de Termos de Pagamento e clique em Novo.
1. Digite o nome do Termo de Pagamento (eg: 50% após envio).
1. Digite a porção da Factura. Se voçê digiar 50, a porção será 50 porcento do valor da Factura.
1. Selecione o tipo de Data de Expiração.
1. Em baixo do Dias de Credito digite o nuimero de dias que o valor remanescente deve ser pago.
1. Salvar.

Os campos são explicados em baixo:

* **Nome do Termo de Pagamento:** O nome para este Termo de Pagamento.
* **Data de Expiração basead Em:** A base no qual a data de expiração para o Termo de Pagamento será calculado. Este é calculado x numero de dias apartir da **data de postagem** da factura/ordem. Exitem três opções:
 - **Dias depois da data da factura**: Data de expiração deve ser calculado em dias com referencia a data de postagem da factura. Por exemplo, se 7 for digitado no dia 20, a data de expiração será 27.
 - **Dias depois do fim do mês da factura**: Data de expiração deve ser calculada em dias com referencia ao ultimo dia do mês em que a factura foi criada. Por exemplo se 7 é digitado no mês corrente e o ultimo dia foi 30, a data de expiração será no dia 7 do proximo mês.
 - **Meses depois do fim do mês da factura**: Data de expiração deve ser calculada em meses com referencia ao ultimo dia do mês no qual a factura foi criada. Por exemplo, se 3 foi digitado no dia 20 de Janeiro, a data de expiração será no dia 20 de Março.
* **Porção da Factura:** A porção do valor total da factura no qual este Termo de Pagamento deve ser aplicado. Valor dado será visto como percentagem ex. 50 = 50% do Total Geral da Factura/Odens
* **Dias de Credito (opcional):** O numero de dias ou meses de credito permitido dependendo da opção escolhida no campo Data de Expiração Baseado Em. 0 significa que não tem credito.
* **Descrição:** (opcional) Uma pequena descrição dos Termos de Pagamento.

### 1.2 Termos de Pagamento em Documentos Convertidos
Quando estiver a converter ou copiar documente no ciclo de Vendas/Compras, os Termos de Pagamento anexados serão copiados. Ao criar a Ordem de Venda apartir de uma Proforma, a Data de Expiração nos Termos de Pagamento será de acordo a Data da Proforma. este precisa ser actuaizado.

Para facil uso, voçẽ pode definir o Modelo de Termos de Pagamento e simplesmente selecionar.

### 1.3 Adicionando Termos de Pagamento aos Documentos

Uma vez que tenha feito o Modelo de Termos de Pagamento, voçê pode usar nas transações de vendas e compras. Baseados no valor definidos nos Termos de Pagamento e valor de transação, o cronograma de pagamento será definido, com Datas de Expiração para cada laje de pagamento.

![Cronograma de Pagamento]({{docs_base_url}}/assets/img/accounts/payment-term-table.png)

Nota: O Cronograma de Pagamento pode ser mostrado na Impressão usando o [Construtor de Formato de Impressão](/docs/user/manual/configuração/imprimir/construtor-formato-impressão).

### 2. Topicos Relacionados
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
1. [Facturas de Compra](/docs/user/manual/pt/contabilidade/factura-compra)
