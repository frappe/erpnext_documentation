<!-- add-breadcrumbs -->
# Dunning

**Um docmento para ser enviado como uma obrigação de pagamento de debito.**

Dunning é um documento para guardar e enviar como uma obrigação de pagamento de debito contra uma Factura de Venda não paga..

Para aceder a lista de Dunning, vá para:
> Home > Contabilidade > Dunning

## 1. Pre-requesitos
Antes de criar o Dunning, deve ter uma Factura de Venda pois será criada sobre a mesma.

* [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)

## 2. Como criar um Dunning
Um Dunning é criado contra uma Factura de Vendas.

Para criar manualmente, siga estes passos:

1. Vá para a lista de Dunning e click em Novo.
1. Selecione uma Factura de Venda caducada.
1. Defina o Tipo de Dunning no campo de dunning.
1. Defina a configuração de impressão para imprimir o modelo de Carta do Dunning.
1. A data de postagem e hora será automatica, voçê pode editar depois de fazer um click na caixa em baixo da Hora de Postagem para entrada de dias anteriores.
1. Salvar e Submeter.

 ![Exemplo Dunning](/docs/assets/img/accounts/dunning.gif)

### 2.1 O que é o Tipo de Dunning
O Tipo de Dunning guarda valores iniciais para dias vencidos, taxa dunning, taxa de xxx e blocos de texto para incluir. Por exemplo, um Tipo de Dunning `Primeira Notificação' não terá qualquer taxa, mas o Tipo de Dunning 'Segunda Notificação' terá uma taxa dunnig e cobrado uma percentagem sobre o valor em divida.

 ![Tipo de Dunning](/docs/assets/img/accounts/dunning-type.png)

### 2.2 Estados / Statuses

Estes são os Estados que são auto-atribuidos ao Dunning.

* **Rascunhos**: Um rascunho é salvo mas ainda não foi submetido.
* **Não Resolvido**: O Dunning não está resolvido quando submetido mas nenhum pagamento foi recebido.
* **Resolvido**: O Dunning está resolvido quando o valor pendente foi recebido.
* **Cancelado**: Um status cancelado é um documento Dunning cancelado.

## 3. Pagamento

Um Registo de Pagamento pode ser criado apartir de um Dunning. Será puxado em conjunto com os Detalhes da Factura de Venda pelo qual foi criado.
 
![Pagamento Dunning](/docs/assets/img/accounts/dunning-payment.png)

## 4. Topicos Relacionados
1. [Registo de Pagamento](/docs/user/manual/pt/contabilidade/registo-pagamento)
1. [Factura de Vendas](/docs/user/manual/pt/contabilidade/factura-vendas)
